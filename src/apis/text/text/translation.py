from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

router = APIRouter()

inputs = [
    {
        "type": "text",
        "name": "input_string",
        "default": "Text to translate",
        "placeholder": "Insert the text to translate here",
    },
    {
        "type": "text",
        "name": "source_language",
        "default": "en",
        "placeholder": "Use the ISO 2 letters representation for source language",
    },
    {
        "type": "text",
        "name": "target_language",
        "default": "fr",
        "placeholder": "Use the ISO 2 letters representation for target language",
    },
]

output = {"name": "translated_text", "type": "str", "example": "translated_text"}

TaskRouter(router=router, input=inputs, output=output, default_model="Helsinki-NLP")
