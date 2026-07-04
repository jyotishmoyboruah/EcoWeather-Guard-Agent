import httpx
import json

def get_real_time_weather(lat: float, lon: float) -> str:
    """
    Queries the free Open-Meteo API to retrieve critical micro-climate parameters
    for a specific coordinate point without requiring authentication tokens.
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m", "relative_humidity_2m", "surface_pressure", "wind_speed_10m", "precipitation"],
        "timezone": "auto"
    }
    try:
        response = httpx.get(url, params=params, timeout=10.0)
        if response.status_code == 200:
            data = response.json()
            current_metrics = data.get("current", {})
            return json.dumps({
                "latitude": lat,
                "longitude": lon,
                "temperature_celsius": current_metrics.get("temperature_2m"),
                "relative_humidity_percentage": current_metrics.get("relative_humidity_2m"),
                "surface_pressure_hpa": current_metrics.get("surface_pressure"),
                "wind_speed_kmh": current_metrics.get("wind_speed_10m"),
                "precipitation_mm": current_metrics.get("precipitation"),
                "timezone": data.get("timezone")
            }, indent=2)
        return f"❌ API Connection Error: {response.status_code}"
    except Exception as e:
        return f"❌ Execution Exception: {str(e)}"
