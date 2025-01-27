from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

router = APIRouter()

inputs = [
    {
        "type": "string",
        "name": "text",
        "example": "Лорем ипсум долор сит амет",
        "placeholder": "Insert the text to transliterate here",
    },
    {
        "type": "string",
        "name": "language",
        "example": "ru",
        "placeholder": "Insert the language code here",
    },
]

output = {
    "name": "transliterated_text",
    "type": "string",
    "example": "transliterated_text",
}

TaskRouter(router=router, input=inputs, output=output, default_model="transliterate")
