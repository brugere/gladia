from gladia_api_utils.io import _open
from gladia_api_utils.TorchvisionModelHelper import TorchvisionModel
from typing import Dict, List, Union
from importlib_metadata import version


def predict(image: bytes, top_k: int = 1) -> Dict[str, Union[List[Dict[str, Union[str, float]]], Dict[str, float]]]:
    img = _open(image)

    model = TorchvisionModel(
        model_name="regnet_y_3_2gf",
        weights="RegNet_Y_3_2GF_Weights",
        weights_version="IMAGENET1K_V2",
    )
    output = model(img, top_k)

    return { "prediction": output["prediction"], "prediction_raw": output["prediction_raw"] }
