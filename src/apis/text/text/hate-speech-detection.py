from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

router = APIRouter()

inputs = [
    {
        "type": "string",
        "name": "text",
        "example": "I hate you piece of shit",
        "placeholder": "Insert the text to classify as hate or not",
    }
]

output = {"name": "classified_text", "type": "string", "example": "offensive"}

TaskRouter(
    router=router,
    input=inputs,
    output=output,
    default_model="byt5-base-tweet-hate-detection",
)
