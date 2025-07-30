from pydantic import BaseModel, Field

class WeatherModel(BaseModel):
    temperature: str = Field(description="The temperature in degrees Celsius")
    # city: str = Field(description="The city of the weather")
    # country: str = Field(description="The country of the weather")

