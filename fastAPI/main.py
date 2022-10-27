from fastapi import FastAPI
import uvicorn
#from typing import Optional
from enum import Enum
from typing import Union

from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


class ModelName(str, Enum):
    marinet = "marinet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.marinet:
        return {"model_name": model_name, "message": "Bloup bloup bloup"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "m": m}
    return {"item_id": item_id}
 #Union et none vont permettre de rendre le contenu optionel
 
@app.get("/testboo/{testboo_id}")
async def read_item(testboo_id: str, m: Union[str, None] = None, short: bool = False):
    testboo = {"testboo_id": testboo_id}
    if m:
        testboo.update({"m": m})
    if not short:
        testboo.update(
            {"description": "Cette description est très dense ..."}
        )
    return testboo
#avec le booléen

#######################

#http://127.0.0.1:8000/items/foo?short=1

#http://127.0.0.1:8000/items/foo?short=True

#http://127.0.0.1:8000/items/foo?short=true

#http://127.0.0.1:8000/items/foo?short=on

#http://127.0.0.1:8000/items/foo?short=yes

#######################

@app.get("/etdeun/{etdeun_id}/etdedeux/{etdedeux_id}")
async def lisons_les_deux(
    etdeun_id: int, etdedeux_id: str, q: Union[str, None] = None, short: bool = False
):
    etdedeux = {"etdedeux_id": etdedeux_id, "owner_id": etdeun_id}
    if q:
        etdedeux.update({"q": q})
    if not short:
        etdedeux.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return etdedeux


# class Coord(BaseModel):
#    lat : float
#    lon : float
#    zoom : Optional[int]
    
#@app.post("/position/{priority}")
#async def make_position(priority:int, coord: Coord):
    # db write completed
#    return {"priority":priority,"new_coord": coord.dict()}


#fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

#@app.get("/items/")
#async def read_item(skip: int = 0, limit: int = 10):
#    return fake_items_db[skip : skip + limit]


#from fastapi import FastAPI
#app = FastAPI()
#@app.get("/files/{file_path:path}")
#async def read_file(file_path: str):
#    return {"file_path": file_path}
###Disons que vous avez une fonction de chemin liée au chemin /files/{file_path}.
###Mais que file_path lui-même doit contenir un chemin, comme home/johndoe/myfile.txt par exemple.
###Donc, l'URL pour ce fichier pourrait être : /files/home/johndoe/myfile.txt.



#@app.get("/component/{component_id}") #path parameter
#async def get_component(component_id: int):
#    return {"component_id" : component_id}
 
#@app.get("/component/")
#async def read_component(number: int, text: Optional[str]):
#    return {"number" : number, "text": text}
#http://127.0.0.1:8000/component/?number=6&text=camarche

#if __name__ == "__main__":
#   uvicorn.run(app, host="127.0.0.1", port=8000)