# class City(BaseModel):
#     name: str = Field(description="The name of the city")
#     country: str = Field(description="The country of the city")
#     population: int = Field(description="The population of the city")
#     area: float = Field(description="The area of the city")
#     currency: str = Field(description="The currency of the city")
#     language: str = Field(description="The language of the city")



#         def generate_with_structured_output(self, user_prompt: str) -> City:
#         """
#         Generate structured output using OpenAI's beta parse functionality.
        
#         MISTAKES THAT WERE FIXED:
#         1. Return type was 'str' but should be 'City' since we're returning a parsed City object
#         2. Trying to return response.choices[0].message.parsed directly - this returns a City object, not a string
#         3. The system message was about weather tools, but this method is for generating City objects
#         4. Need to handle the case where parsing fails and return a proper error
#         """
#         try:
#             messages = [
#                 # MISTAKE: This system message was about weather tools, but we're generating City objects
#                 # FIXED: Changed to be specific about generating city information
#                 {"role": "system", "content": "You are a helpful assistant that generates city information. Generate accurate city data based on the user's request."},
#                 {"role": "user", "content": user_prompt}
#             ]

#             response = self.client.beta.chat.completions.parse(
#                 # MISTAKE: gpt-3.5-turbo doesn't support structured outputs with response_format
#                 # FIXED: Using gpt-4o-mini which supports structured outputs
#                 model="gpt-4o-mini",
#                 messages=messages,
#                 response_format=City,
#             )

#             # MISTAKE: This was printing the parsed object but then trying to return it as a string
#             # FIXED: Return the parsed City object directly
#             parsed_city = response.choices[0].message.parsed
#             print(f"Generated city: {parsed_city}")
#             return parsed_city

#         except Exception as e:
#             print(f"Error in structured output generation: {e}")
#             # MISTAKE: Returning error as string when method should return City object
#             # FIXED: Raise the exception instead of returning error string
#             raise e
    


#     @app.post("/city")
# async def get_city(user_prompt: str):
#     client = OpenAIClient()
#     return client.generate_with_structured_output(user_prompt)