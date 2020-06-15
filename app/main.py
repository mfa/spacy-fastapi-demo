from typing import List

import spacy
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
nlp = spacy.load("de_core_news_sm")


@app.get("/")
async def hello():
    return {"message": "Hello World"}


class Sentence(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": "Maria sieht Hans und Franz mit dem Fernglas auf dem Hügel.",
            }
        }


class ParseItem(BaseModel):
    word: str
    pos: str
    tag: str


@app.post("/pos/")
async def pos(sentence: Sentence) -> List[ParseItem]:
    doc = nlp(sentence.text)
    return [{"word": w.text, "pos": w.pos_, "tag": w.tag_} for w in doc]
