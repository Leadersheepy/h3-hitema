from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/component/{component_id}") #path parameter
async def get_component(component_id: int):
    return {"component_id" : component_id}
 
@app.get("/component/")
async def read_component(number: int, text: str):
    return {"number" : number, "text": text}

#http://127.0.0.1:8000/component/?number=6&text=camarche

#if __name__ == "__main__":
#   uvicorn.run(app, host="127.0.0.1", port=8000)