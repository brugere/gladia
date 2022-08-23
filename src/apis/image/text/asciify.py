from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

inputs = [
    {
        "type": "image",
        "name": "image",
        "example": "http://files.gladia.io/test/test.png",
        "placeholder": "image url to convert to ascii if no file upload",
    }
]

output = {"name": "asciified_image", "type": "str", "example": "asciified_image"}

router = APIRouter()

TaskRouter(router=router, input=inputs, output=output, default_model="ramesh-aditya")
