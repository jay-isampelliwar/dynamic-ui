# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from dotenv import load_dotenv
# from openai_client import OpenAIClient
# from constants.tool_call_schema import FunctionWrapper, SchemaType, Function, Parameters, ParameterProperty, PropertyType
# from typing import Dict, List, Any

# app = FastAPI()

# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # Frontend URL
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# load_dotenv()

# class ChatRequest(BaseModel):
#     user_prompt: str

# class FormSchemaRequest(BaseModel):
#     form_type: str

# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}

# @app.post("/weather")
# async def get_weather(request: ChatRequest):
#     system_prompt = "You are a helpful assistant that can use the get_weather tool to get the weather for a given location with the latitude and longitude."
#     tools = [
#         FunctionWrapper(
#             type=SchemaType.FUNCTION,
#             function=Function(
#                 name="get_weather",
#                 description="Get the weather for a given location with the latitude and longitude",
#                 parameters=Parameters(
#                     type="object", 
#                     properties={
#                         "latitude": ParameterProperty(type=PropertyType.NUMBER), 
#                         "longitude": ParameterProperty(type=PropertyType.NUMBER)
#                         }, 
#                     required=["latitude", "longitude"], 
#                     additionalProperties=False
#                     ),
#                 strict=True
#             )
#         )
#     ]
#     client = OpenAIClient(system_prompt, tools)
#     response_content = client.generate(request.user_prompt)
#     return {"content": response_content}

# @app.post("/form-schema")
# async def get_form_schema(request: FormSchemaRequest):
#     """
#     Returns dynamic form schema based on form type.
#     This endpoint provides JSON configuration for rendering dynamic forms in the frontend.
#     """
#     form_schemas = {
#         "user_registration": {
#             "title": "User Registration",
#             "description": "Create a new account",
#             "fields": [
#                 {
#                     "name": "firstName",
#                     "label": "First Name",
#                     "type": "text",
#                     "required": True,
#                     "placeholder": "Enter your first name",
#                     "validation": {
#                         "minLength": 2,
#                         "maxLength": 50
#                     }
#                 },
#                 {
#                     "name": "lastName",
#                     "label": "Last Name",
#                     "type": "text",
#                     "required": True,
#                     "placeholder": "Enter your last name",
#                     "validation": {
#                         "minLength": 2,
#                         "maxLength": 50
#                     }
#                 },
#                 {
#                     "name": "email",
#                     "label": "Email Address",
#                     "type": "email",
#                     "required": True,
#                     "placeholder": "Enter your email address",
#                     "validation": {
#                         "pattern": "^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$"
#                     }
#                 },
#                 {
#                     "name": "password",
#                     "label": "Password",
#                     "type": "password",
#                     "required": True,
#                     "placeholder": "Enter your password",
#                     "validation": {
#                         "minLength": 8,
#                         "pattern": "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)[a-zA-Z\\d@$!%*?&]{8,}$"
#                     }
#                 },
#                 {
#                     "name": "confirmPassword",
#                     "label": "Confirm Password",
#                     "type": "password",
#                     "required": True,
#                     "placeholder": "Confirm your password"
#                 },
#                 {
#                     "name": "agreeToTerms",
#                     "label": "I agree to the Terms and Conditions",
#                     "type": "checkbox",
#                     "required": True
#                 }
#             ],
#             "submitButton": {
#                 "text": "Create Account",
#                 "type": "submit"
#             }
#         },
#         "contact_form": {
#             "title": "Contact Us",
#             "description": "Send us a message",
#             "fields": [
#                 {
#                     "name": "name",
#                     "label": "Full Name",
#                     "type": "text",
#                     "required": True,
#                     "placeholder": "Enter your full name"
#                 },
#                 {
#                     "name": "email",
#                     "label": "Email Address",
#                     "type": "email",
#                     "required": True,
#                     "placeholder": "Enter your email address"
#                 },
#                 {
#                     "name": "subject",
#                     "label": "Subject",
#                     "type": "select",
#                     "required": True,
#                     "options": [
#                         {"value": "general", "label": "General Inquiry"},
#                         {"value": "support", "label": "Technical Support"},
#                         {"value": "billing", "label": "Billing Question"},
#                         {"value": "feedback", "label": "Feedback"}
#                     ]
#                 },
#                 {
#                     "name": "message",
#                     "label": "Message",
#                     "type": "textarea",
#                     "required": True,
#                     "placeholder": "Enter your message",
#                     "rows": 5,
#                     "validation": {
#                         "minLength": 10,
#                         "maxLength": 1000
#                     }
#                 },
#                 {
#                     "name": "priority",
#                     "label": "Priority",
#                     "type": "radio",
#                     "required": True,
#                     "options": [
#                         {"value": "low", "label": "Low"},
#                         {"value": "medium", "label": "Medium"},
#                         {"value": "high", "label": "High"}
#                     ]
#                 }
#             ],
#             "submitButton": {
#                 "text": "Send Message",
#                 "type": "submit"
#             }
#         },
#         "settings_form": {
#             "title": "User Settings",
#             "description": "Update your account settings",
#             "fields": [
#                 {
#                     "name": "displayName",
#                     "label": "Display Name",
#                     "type": "text",
#                     "required": False,
#                     "placeholder": "Enter display name"
#                 },
#                 {
#                     "name": "timezone",
#                     "label": "Timezone",
#                     "type": "select",
#                     "required": True,
#                     "options": [
#                         {"value": "utc", "label": "UTC"},
#                         {"value": "est", "label": "Eastern Time"},
#                         {"value": "pst", "label": "Pacific Time"},
#                         {"value": "gmt", "label": "GMT"}
#                     ]
#                 },
#                 {
#                     "name": "notifications",
#                     "label": "Notification Preferences",
#                     "type": "checkbox-group",
#                     "required": False,
#                     "options": [
#                         {"value": "email", "label": "Email Notifications"},
#                         {"value": "push", "label": "Push Notifications"},
#                         {"value": "sms", "label": "SMS Notifications"}
#                     ]
#                 },
#                 {
#                     "name": "theme",
#                     "label": "Theme",
#                     "type": "radio",
#                     "required": True,
#                     "options": [
#                         {"value": "light", "label": "Light"},
#                         {"value": "dark", "label": "Dark"},
#                         {"value": "auto", "label": "Auto"}
#                     ]
#                 },
#                 {
#                     "name": "bio",
#                     "label": "Bio",
#                     "type": "textarea",
#                     "required": False,
#                     "placeholder": "Tell us about yourself",
#                     "rows": 3,
#                     "validation": {
#                         "maxLength": 500
#                     }
#                 }
#             ],
#             "submitButton": {
#                 "text": "Save Settings",
#                 "type": "submit"
#             }
#         }
#     }
    
#     form_type = request.form_type.lower()
    
#     if form_type not in form_schemas:
#         return {
#             "error": "Form type not found",
#             "available_forms": list(form_schemas.keys())
#         }
    
#     return {
#         "success": True,
#         "form": form_schemas[form_type],
#         "metadata": {
#             "generated_at": "2024-01-01T00:00:00Z",
#             "version": "1.0.0"
#         }
#     }

# @app.get("/form-schema/{form_type}")
# async def get_form_schema_by_type(form_type: str):
#     """
#     Alternative GET endpoint to retrieve form schema by type.
#     """
#     request = FormSchemaRequest(form_type=form_type)
#     return await get_form_schema(request)



