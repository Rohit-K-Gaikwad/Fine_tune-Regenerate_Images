from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os

# Load environment variables from .env file

# Initialize FastAPI app
app = FastAPI()

# Replicate API base URL and your token from environment variables
REPLICATE_API_URL = "https://api.replicate.com/v1/predictions"
REPLICATE_API_TOKEN = "" # enter your secrete key

# Pydantic models for request validation
class ImageGenerationRequest(BaseModel):
    prompt: str
    width: int = 512
    height: int = 512
    num_images: int = 1

# Utility function to interact with Replicate API for image generation
def generate_images_via_replicate(prompt: str, width: int, height: int, num_images: int):
    headers = {
        "Authorization": f"Token {REPLICATE_API_TOKEN}",
        "Content-Type": "application/json",
    }

    # Define the input payload
    body = {
        "version": "cc376d7a1a520e7f2745ff1a64f0dbfa58ffdcbd5cc31940c7a0536e87ba4cbe",  # Example stable diffusion model version ID
        "input": {
            "prompt": prompt,
            "image_dimensions": f"{width}x{height}",  # Alternative format
            "num_outputs": num_images
        }
    }

    # Send request to Replicate API
    response = requests.post(REPLICATE_API_URL, json=body, headers=headers)

    # Log the raw response for debugging
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")

    # Handle the case where image generation fails
    if response.status_code != 200:
        try:
            error_message = response.json().get("detail", "Unknown error occurred.")
        except Exception:
            error_message = response.text
        raise HTTPException(status_code=response.status_code, detail=f"Image generation failed: {error_message}")

    return response.json()

# FastAPI route to generate images
@app.post("/generate-images/")
async def generate_images(request: ImageGenerationRequest):
    try:
        # Generate images by sending a request to the Replicate API
        result = generate_images_via_replicate(
            request.prompt, request.width, request.height, request.num_images
        )
        return {"generated_images": result}
    except Exception as e:
        # Capture and return errors to the client
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
