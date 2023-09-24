from typing import Annotated
from Caesar_cipher import encrypt, decrypt, generate_html_response, crack

from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def homepage():
    return generate_html_response()


@app.get("/encrypt/")
def encryption(msg: str, key: Annotated[int, Query(title="key for enncryption", ge=1, le=25)]):
    new_msg = encrypt(msg, key)
    return {"msg": msg, "new_msg": new_msg}


@app.get("/decrypt/")
def decryption(msg: str, key: Annotated[int, Query(title="key for enncryption", ge=1, le=26)]):
    new_msg = decrypt(msg, key)
    return {"msg": msg, "new_msg": new_msg}


@app.get("/crack/")
def cracking(msg: str):
    lst = crack(msg)
    for idx, messege in enumerate(lst):
        print(f"Index: {idx}--{messege}")
