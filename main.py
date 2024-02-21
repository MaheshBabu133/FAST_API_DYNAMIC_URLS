from fastapi import FastAPI
app = FastAPI()


@app.get("/phase/{id}")
def Sample(id:int):
    return {"value": id}



@app.get("/friend/{id}/friend")
def Sample2(id):
    return f"Mahesh {id} Sonu"

