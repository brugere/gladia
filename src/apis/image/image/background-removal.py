from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

inputs = [
    {
        "type": "image",
        "name": "image",
        "example": "http://files.gladia.io/examples/image/image/background-removal/owl2.png",
        "examples": [
            "http://files.gladia.io/examples/image/image/background-removal/owl2.gif",
            "http://files.gladia.io/examples/image/image/background-removal/owl2.jpg",
            "http://files.gladia.io/examples/image/image/background-removal/owl2.png",
        ],
        "placeholder": "Image to remove the background from",
    }
]

output = {"name": "cleaned_image", "type": "image", "example": "a.png"}

router = APIRouter()

TaskRouter(router=router, input=inputs, output=output, default_model="mobilenet")
