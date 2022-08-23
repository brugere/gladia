import numpy as np
from gladia_api_utils.io import _open


def predict(image: bytes, source_language: str) -> dict:
    """
    Call the EasyOcr package and return the text detected in the image by the ocr

    :param image: image to provide to the ocr
    :param source_language: language of the text to be searched
    :return: characters found in the image
    """

    import easyocr

    image = _open(image)
    image = np.array(image)
    reader = easyocr.Reader([source_language], gpu=True)
    text = reader.readtext(image, detail=False)
    plain_text = '\n'.join(text)

    return {"prediction": plain_text, "prediction_raw": text}
