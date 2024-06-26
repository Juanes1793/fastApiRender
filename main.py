
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from PIL import Image
import requests
from io import BytesIO
import os

app = FastAPI()

class StringRequest(BaseModel):
    image_url: str

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL") 

@app.post("/convert_image")
async def convert_image(request: StringRequest):
    url_image = request.image_url
    response = requests.get(url_image)
    img = Image.open(BytesIO(response.content))
    grayscale_image = img.convert('L')

    # Save the grayscale image to a BytesIO object
    img_byte_arr = BytesIO()
    grayscale_image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    # Send the image to Discord
    payload = {
        "content": "Here is your converted image:"
    }
    files = {
        "file": ("grayscale_image.png", img_byte_arr, "image/png")
    }
    discord_response = requests.post(DISCORD_WEBHOOK_URL, data=payload, files=files)

    # Check if the request was successful
    if discord_response.status_code == 204:
        message = "Image successfully sent to Discord."
    else:
        message = "Failed to send image to Discord."

    return {"message": message}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
