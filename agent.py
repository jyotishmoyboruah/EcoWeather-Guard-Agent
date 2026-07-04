import os
from google import genai
from google.genai import types
from weather_tools import get_real_time_weather

def run_eco_weather_analysis(lat: float, lon: float) -> str:
    raw_weather_json = get_real_time_weather(lat, lon)
    if "❌" in raw_weather_json:
        return raw_weather_json
        
    client = genai.Client()
    model_id = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
    
    system_instruction = (
        "You are the EcoWeather Guard Agent, a lightweight cloud-native expert system specialized "
        "in translating raw regional weather parameters into localized, high-value agricultural "
        "and community action warnings under the Agents for Good framework."
    )
    
    analysis_prompt = f"""
    Analyze the following real-time coordinate weather data block and compile an operational advisory report 
    covering all 5 specialized ecological dimensions. 
    
    Raw Target Data Block:
    {{raw_weather_json}}
    
    Your report MUST be clearly split into these 5 markdown sections:
    ### 1. 🌪️ AeroForecast Module
    ### 2. ❄️ EcoFrost Guard Module
    ### 3. 🌱 HydroCrops Sowing Window
    ### 4. 🚨 MonsoonAlert Risk Level
    ### 5. 🐄 ThermaHerd Index (THI)
    """
    
    response = client.models.generate_content(
        model=model_id,
        contents=analysis_prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.3
        )
    )
    return response.text
