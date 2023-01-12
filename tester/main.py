from test import Tester
import config as cfg
from fastapi import FastAPI

if cfg.ACCESS_TOKEN == "":
    print('Set Access token in "config.py" for dropbox')

app = FastAPI()
tester = Tester(cfg.ACCESS_TOKEN, 'smile.png')

@app.get("/")
def read_root():
    return {"Status": 200}

@app.post("/image")
def upload_file():
    return tester.upload()


@app.get("/image/metadata")
def file_get_metadata():
    return tester.get_metadata()


@app.delete("/del")
def delete_file():
    return tester.delete()