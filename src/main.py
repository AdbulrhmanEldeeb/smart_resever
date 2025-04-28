from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal
from config import AppConfig

app = FastAPI(
    title=AppConfig.PROJECT_NAME,
    description=AppConfig.PROJECT_DESCRIPTION,
    version=AppConfig.PROJECT_VERSION
)
# Define the expected data model
class Destination(BaseModel):
    lat: float = Field(..., description="Latitude of the destination")
    lng: float = Field(..., description="Longitude of the destination")

class MoveRequest(BaseModel):
    destination: Destination
    drive_mode: Literal["Normal", "Sport", "Eco"]
@app.get("/")
async def health_check():
    return {
        "health_check":"healthy",
        "version":AppConfig.PROJECT_VERSION
            }
@app.post("/move")
async def move(request: MoveRequest):
    # Access the data safely thanks to pydantic validation
    lat = request.destination.lat
    lng = request.destination.lng
    drive_mode = request.drive_mode

    # Logging received data (for now)
    print(f"Received Destination: Latitude={lat}, Longitude={lng}")
    print(f"Received Drive Mode: {drive_mode}")

    # TODO: Here you can add the real robot movement logic based on drive_mode

    return {
        "message": "Destination and drive mode received successfully!",
        "destination": {"lat": lat, "lng": lng},
        "drive_mode": drive_mode
    }
