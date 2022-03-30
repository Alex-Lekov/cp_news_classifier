########################## IMPORT ###############################
from typing import Dict
import yaml
from model import Model
from itertools import compress

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


########################## FUNC ###############################
def load_config(config_name: str = "config.yaml") -> Dict:
    """Load Config file

    Args:
        config_name (str, optional): file name. Defaults to "config.yaml".

    Returns:
        Dict: config
    """
    with open(config_name, "r") as stream:
        try:
            config = yaml.safe_load(stream)
            print(config)
        except yaml.YAMLError as exc:
            print(exc)
    return config


app = FastAPI()

class InputDoc(BaseModel):
    text: str


class LabeledDoc(InputDoc):
    label: list


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict", response_model=LabeledDoc, status_code=200)
def predict(doc: InputDoc):
    """
    Help from https://testdriven.io/blog/fastapi-machine-learning/
    """
    text = doc.text
    text_tegs = list(compress(model_config["TEGS"], (model.predict_proba(text) > 0.5)[0]))
    print(f"Labeles: {text_tegs}")

    return {"text": text, "label": text_tegs}


########################## MAIN ###############################

if __name__ == "__main__":
    model_config = load_config("config.yaml")
    model = Model(max_length=model_config["MAX_LENGTH"])
    uvicorn.run(app, host="0.0.0.0", port=8008)


