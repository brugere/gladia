import re
from typing import Dict

import cv2
import numpy as np
import pytesseract
from gladia_api_utils.io import _open


def predict(image: bytes, source_language: str) -> Dict[str, str]:
    """
    Call the tesseract ocr and return the text detected in the image

    :param image: image to provide to the ocr
    :param source_language: [UNUSED] language of the text to be searched
    :return: characters found in the image
    """

    del source_language

    image = _open(image)

    np_image = np.array(image)

    gray_image = cv2.cvtColor(np_image, cv2.COLOR_BGR2GRAY)

    gray_thresh = cv2.threshold(
        src=gray_image, thresh=0, maxval=255, type=cv2.THRESH_BINARY | cv2.THRESH_OTSU
    )[1]

    text = pytesseract.image_to_string(gray_thresh)

    out = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]", "", text)

    result = out.strip()

    return {"prediction": result, "prediction_raw": text}
