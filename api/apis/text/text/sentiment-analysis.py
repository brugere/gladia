from fastapi import APIRouter
from ai_api_utils.submodules import TaskRouter

router = APIRouter()

input = [
    {
        "type": "text",
        "name": "text",
        "default": "I like you. I love you",
        "placeholder": "I like you. I love you",
        "tooltip": "Insert the text to anlayse sentiment from",
    },
]

output = [
    {
        "type": list,
        "name": "results",
    }
]

TaskRouter(router=router, input=input, output=output, default_model="distilbert-base-uncased-finetuned-sst-2-english")