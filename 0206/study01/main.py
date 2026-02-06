from fastapi import FastAPI
from kafka import KafkaProducer
from settings import settings

pd = KafkaProducer(bootstrap_servers='localhost:9092')

pd.send('test', b'Hello2')
pd.flush()

app = FastAPI()

@app.get("/")
def read_root():
    return {"status":"Producer"}