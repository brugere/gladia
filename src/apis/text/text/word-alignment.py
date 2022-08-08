from fastapi import APIRouter
from gladia_api_utils.submodules import TaskRouter

router = APIRouter()

inputs = [
    {
        "type": "text",
        "name": "input_string_language_1",
        "default": "Sentence from first language",
        "placeholder": "Insert the Sentence from first language",
    },
    {
        "type": "text",
        "name": "input_string_language_2",
        "default": "来自 第一 语言的 句子",
        "placeholder": "Insert the Sentence from second language",
    },
]

output = {"name": "word_aligment", "type": "dict", "example": "word_aligment"}

TaskRouter(
    router=router,
    input=inputs,
    output=output,
    default_model="bert-base-multilingual-cased",
)
