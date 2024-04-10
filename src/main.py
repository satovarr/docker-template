from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host='redis', port=6379)

import debugpy
debugpy.listen(("0.0.0.0", 5678))
# debugpy.wait_for_client()

@app.get("/")
def read_root():
    return {"Hello": "There"}

@app.get("/hits")
def read_hits():
    r.incr('hits')
    print("hits: ", r.get('hits'))
    return {"Hello": r.get('hits')}