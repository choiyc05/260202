from fastapi import FastAPI, Request, Response, Cookie
import redis
import uuid
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

# docker run -d -p 6379:6379 --name redis redis:8.4.0
# docker exec -it redis redis-cli

app = FastAPI()

client = redis.Redis(
        # host="localhost",
        host="192.168.0.250",
        port=6379,
        db=0
)
print(type(client))

SECRET_KEY = "super-tired-so-i-want-twelve-hours-deep-sleep"

def set_token(no: int, name: str):
    try:
        iat = datetime.now(timezone.utc) + (timedelta(hours=7))
        exp = iat + (timedelta(minutes=60))
        data = {
            "name": name,
            "secret" : SECRET_KEY,
            "iss": "team2", 
            "sub": str(no), 
            "iat": iat,
            "exp": exp
        }
        token = jwt.encode(data, SECRET_KEY, algorithm="HS256")
        return token
    except JWTError as e:
        print(f"error: {e}")
    return None


@app.get("/set")
def setRedis(response: Response, no: int, name: str):
    id = uuid.uuid4().hex
    token = set_token(no,name)
    client.setex(f"2team:{id}", 60*60*24, token)
    response.set_cookie(
        key="data",
        value=id,
        max_age=60 * 60,        # 1시간 (초)
        expires=60 * 60,        # max_age와 유사 (초)
        path="/",
        domain="localhost",
        secure=True,            # HTTPS에서만 전송
        httponly=True,          # JS 접근 차단 (⭐ 보안 중요)
        samesite="lax",         # 'lax' | 'strict' | 'none'
      )
    return {"status": True, "id": id}

@app.get("/get")
def getRedis(request: Request):
    id = request.cookies.get("data")
    result = client.get(f"2team:{id}")
    return {"result": result}

@app.get("/del")
def delRedis(request: Request, response: Response):
    id = request.cookies.get("data")
    client.delete(f"2team:{id}")
    response.delete_cookie(key="data")
    return {"status": True}

@app.get("/")
def read_root():
    return {"status": True}

@app.get("/dell")
def delRedis(id):
    client.delete(f"2team:{id}")
    return {"status": True}