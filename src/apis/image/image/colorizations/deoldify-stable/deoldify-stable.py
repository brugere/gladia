import os

from PIL import Image
from pathlib import Path

from gladia_api_utils.io import _open
from gladia_api_utils.model_management import download_models


urls = {
    "deoldify-stable": {
        "url": "https://huggingface.co/databuzzword/deoldify-stable",
        "output_path": "models",
    }
}

models_path = download_models(urls)

current_model_path = os.path.join(models_path["deoldify-stable"]["output_path"])


def predict(image: bytes) -> Image:
    """
    Call the model to return the image colorized

    :param image: image to colorize
    :return: colorized image
    """

    from deoldify import device
    from deoldify import visualize
    from deoldify.device_id import DeviceId

    device.set(device=DeviceId.GPU0)

    render_factor = 30

    image = _open(image)

    image_colorizer = visualize.get_image_colorizer(
        root_folder=Path(current_model_path).parent,
        render_factor=render_factor,
        artistic=False,
    )

    result = image_colorizer.get_transformed_image(
        path=image, render_factor=render_factor
    )

    return result
