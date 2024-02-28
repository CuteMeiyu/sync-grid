# https://ai.baidu.com/ai-doc/OCR/Al1zvpylt

import base64
import io

import requests
from PIL import Image


URL = "https://aip.baidubce.com/rest/2.0/ocr/v1/table"


def parse_result(result: dict):
    grid = [""] * 25
    valid_count = 0
    for cell in result["body"]:
        index = cell["row_start"] * 5 + cell["col_start"]
        if index >= 25 or index < 0:
            continue
        valid_count += 1
        grid[index] = cell["words"].replace("\n", "")
    return grid, valid_count / 25


def ocr(image: Image.Image):
    image_byte_array = io.BytesIO()
    image.save(image_byte_array, format="PNG")
    image64 = base64.b64encode(image_byte_array.getvalue())

    with open("ocr/baidu/access_token", "r") as f:
        access_token = f.read().strip()
    params = {"image": image64}
    request_url = URL + "?access_token=" + access_token
    headers = {"content-type": "application/x-www-form-urlencoded"}
    response = requests.post(request_url, data=params, headers=headers)
    response = response.json()
    print(response)
    max_score = 0
    best_result = None
    for result in response["tables_result"]:
        try:
            grid, score = parse_result(result)
            if score > max_score:
                max_score = score
                best_result = grid
        except:
            continue
    if max_score == 0:
        print("No result")
    else:
        print("Score:", max_score)
        print("Result:", best_result)
    return best_result
