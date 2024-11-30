import uvicorn
from fastapi import FastAPI
from app.api import user 


def create_app():

    app = FastAPI(
        title='MTS Hack Change',
        debug=True
    )
    return app


app = create_app()
app.include_router(user.router, tags=['User'], prefix='')


@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)