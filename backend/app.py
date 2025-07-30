import re
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from textwrap import dedent
from agno.agent import Agent, RunResponse
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List, Optional, Union

load_dotenv()

class FormField(BaseModel):
    name: str = Field(description="The name/identifier of the field")
    label: str = Field(description="The display label for the field")
    type: str = Field(description="The type of the field (text, email, textarea, select, multiselect, date)")
    required: bool = Field(description="Whether the field is required")
    placeholder: Optional[str] = Field(default=None, description="Optional placeholder text")
    options: Optional[List[str]] = Field(default=None, description="Options for select/multiselect fields")

class FormComponent(BaseModel):
    type: str = Field(description="The type of the component")
    fields: List[FormField] = Field(description="The fields of the component")
    submitText: str = Field(description="The text of the submit button")


# New agent specifically for UI component generation
ui_component_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    description=dedent("""\
        You are a UI Component Generator, an expert at creating dynamic form components based on user requirements.
        Your specialty is understanding user requests and generating appropriate form fields with proper validation
        and user experience considerations.

        Your approach is:
        - Understanding user intent quickly
        - Generating appropriate field types
        - Creating user-friendly labels and placeholders
        - Following best practices for form design
        - Providing helpful validation and options\
    """),
    instructions=dedent("""\
        You are a UI Component Generator that creates dynamic form components based on user requests. 
        When a user asks for specific input fields, you should:

        1. **Analyze the Request**: Understand what fields the user needs
        2. **Choose Appropriate Types**: Select the right field types (text, email, date, select, etc.)
        3. **Create User-Friendly Labels**: Make labels clear and descriptive
        4. **Add Helpful Placeholders**: Provide example text where appropriate
        5. **Include Validation**: Set required fields and add options for select fields
        6. **Generate Component**: Return a properly formatted component

        Examples of user requests you can handle:
        - "I need name, email, and phone fields"
        - "Create a form with date picker and dropdown"
        - "I want fields for address, city, and zip code"
        - "Generate a form with multiple choice options"

        Always respond with a brief explanation followed by the component code.\
    """),
    expected_output=dedent("""\
    Your response should follow this exact format:

    [Brief explanation of the form you're creating]

    ```component
    {
      "type": "form",
      "fields": [
        {
          "name": "field_name",
          "label": "Field Label",
          "type": "text|email|textarea|select|multiselect|date",
          "required": true|false,
          "placeholder": "Optional placeholder text",
          "options": ["option1", "option2"] // for select/multiselect
        }
      ],
      "submitText": "Submit"
    }
    ```
                           
                

    Available field types:
    - "text" for single line text
    - "email" for email addresses
    - "textarea" for longer text
    - "number" for phone numbers
    - "select" for dropdown selection
    - "multiselect" for multiple selections
    - "date" for date picker

    Always include the component code after your explanation text.
    Make forms user-friendly with clear labels and helpful placeholders.\
    """),
    markdown=True,
    show_tool_calls=False,
    add_datetime_to_instructions=False,
)


app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/ui-test")
async def generate_ui_component(request: dict):
    try:
        user_message = request.get("message", "")
        response = await ui_component_agent.arun(user_message)
        print("response", response.content)
        
        # Parse the response to extract text content and component
        content = str(response.content) if response.content else ""
        component = None
        
        # Try to extract component from the response content
        # Look for component block in the response
        component_match = re.search(r'```component\s*\n(.*?)\n```', content, re.DOTALL)
        if component_match:
            try:
                component_json = component_match.group(1).strip()
                component = json.loads(component_json)
                # Remove the component block from the content
                content = re.sub(r'```component\s*\n.*?\n```', '', content, flags=re.DOTALL).strip()
            except json.JSONDecodeError as e:
                print(f"Failed to parse component JSON: {e}")
        
        # If no component found, try to find JSON object in the content
        if not component:
            json_match = re.search(r'\{[\s\S]*?"type"[\s\S]*?"fields"[\s\S]*?\}', content)
            if json_match:
                try:
                    component = json.loads(json_match.group(0))
                    # Remove the JSON from content
                    content = re.sub(r'\{[\s\S]*?"type"[\s\S]*?"fields"[\s\S]*?\}', '', content).strip()
                except json.JSONDecodeError as e:
                    print(f"Failed to parse JSON object: {e}")
        
        return {
            "content": content,
            "component": component
        }
    except Exception as e:
        return {"error": str(e)}

@app.post("/ui")
async def get_ui_component(request: dict):
    try:
        trigger = request.get("trigger", "default")
        
        # Return dummy Next.js component code with input fields
        component_code = {
            "type": "form",
            "fields": [
                {
                    "name": "fullName",
                    "label": "Full Name",
                    "type": "text",
                    "required": True,
                    "placeholder": "Enter your full name"
                },
                {
                    "name": "email",
                    "label": "Email Address",
                    "type": "email",
                    "required": True,
                    "placeholder": "your.email@example.com"
                },
                {
                    "name": "phone",
                    "label": "Phone Number",
                    "type": "text",
                    "required": False,
                    "placeholder": "+1 (555) 123-4567"
                },
                {
                    "name": "summary",
                    "label": "Professional Summary",
                    "type": "textarea",
                    "required": True,
                    "placeholder": "Brief description of your professional background and career objectives..."
                },
                {
                    "name": "experience",
                    "label": "Years of Experience",
                    "type": "select",
                    "required": True,
                    "options": ["0-1 years", "1-3 years", "3-5 years", "5-10 years", "10+ years"]
                },
                {
                    "name": "skills",
                    "label": "Technical Skills",
                    "type": "multiselect",
                    "required": True,
                    "options": ["JavaScript", "React", "Node.js", "Python", "Java", "SQL", "AWS", "Docker", "Kubernetes", "Git"]
                }
            ],
            "submitText": "Create Resume"
        }
        
        # Different messages based on trigger
        if trigger == "chat":
            content = "Perfect! I've loaded the resume form for you. Please fill out the information below and I'll help you create a professional resume."
        else:
            content = "Welcome to ResumeGPT! Let's create your professional resume. Please fill out the form below with your information."
        
        return {
            "content": content,
            "component": component_code
        }
    except Exception as e:
        return {"error": str(e)}