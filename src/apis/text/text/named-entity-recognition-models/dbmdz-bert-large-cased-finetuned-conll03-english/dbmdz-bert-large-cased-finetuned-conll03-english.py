import json
import os
from typing import Dict, List, Union

from gladia_api_utils.triton_helper import (
    TritonClient,
    check_if_model_needs_to_be_preloaded,
    data_processing,
)


def predict(text: str) -> Dict[str, Union[List[Dict[str, Union[str, float]]], str]]:
    """
    Apply NER on the given task and return each token within the sentence associated to its label.

    **Labels**:\n
    O : Outside of a named entity\n
    B-MISC : Beginning of a miscellaneous entity right after another miscellaneous entity\n
    I-MISC : Miscellaneous entity\n
    B-PER : Beginning of a person's name right after another person's name\n
    I-PER : Person's name\n
    B-ORG : Beginning of an organisation right after another organisation\n
    I-ORG : Organisation\n
    B-LOC : Beginning of a location right after another location\n
    I-LOC : Location\n

    :param text: sentence to search the named entities in
    :return: entities founded in the string
    """

    MODEL_NAME = "named-entity-recognition_dbmdz_bert-large-cased-finetuned-conll03-english_tensorrt_inference"
    MODEL_SUB_PARTS = [
        "named-entity-recognition_dbmdz_bert-large-cased-finetuned-conll03-english_tensorrt_model",
    ]

    client = TritonClient(
        model_name=MODEL_NAME,
        sub_parts=MODEL_SUB_PARTS,
        output_name="output",
        preload_model=check_if_model_needs_to_be_preloaded(MODEL_NAME),
    )

    np_output = data_processing.text_to_numpy(text)

    client.set_input(name="TEXT", shape=np_output.shape, datatype="BYTES")

    prediction_raw = client(np_output)
    prediction_decode = prediction_raw[0].decode("utf8")
    prediction = json.loads(prediction_decode)[0]

    return {"prediction": prediction, "prediction_raw": prediction_raw}
