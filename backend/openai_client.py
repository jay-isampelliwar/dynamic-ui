from os import getenv
from typing import List
from openai import OpenAI
from tools.weather import get_weather
from model.weather_model import WeatherModel
import json
from pydantic import BaseModel, Field
from constants.tool_call_schema import FunctionWrapper

class OpenAIClient:
    def __init__(self, system_prompt: str, tools: List[FunctionWrapper]):
        self.client = OpenAI(api_key=getenv("OPENAI_API_KEY"))
        self.system_prompt = system_prompt
        self.tools = tools

    def generate(self, user_prompt: str) -> str:
        try:
            tools = [
                tool.to_json() for tool in self.tools
            ]

            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_prompt}
            ]

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                tools=tools,
            )
        except Exception as e:
            print(f"Error in initial API call: {e}")
            return "I apologize, but I encountered an error while connecting to the AI service. Please try again."

        def call_function(name, args):
            if name == "get_weather":
                return get_weather(**args)

        tool_calls = response.choices[0].message.tool_calls
        if tool_calls:
            for tool_call in tool_calls:
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                messages.append(response.choices[0].message)
                result = call_function(name, args)
                messages.append(
                    {"role": "tool", "tool_call_id": tool_call.id, "content": json.dumps(result)}
                )


        try:
            completion_2 = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                tools=tools,
            )

            return completion_2.choices[0].message.content
        except Exception as e:
            print(f"Error in second completion: {e}")
            # If second completion fails, return the first response content
            first_response_content = response.choices[0].message.content
            if first_response_content:
                return first_response_content
            else:
                return "I apologize, but I encountered an error while processing your request. Please try again."
        