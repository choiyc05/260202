# 260202

  ## Docker Hub 에서 이미지 다운로드 CLI
```bash
- `docker` : 도커 명령어
- `pull` : 받다
- `ubuntu` : 이미지 이름
- `:` : 이미지 이름과 태그 구분자
- `24.04` : 태그 이름
```

  ## Docker 이미지 확인
```bash
docker image
```

  ## 명령어 확인
```bash
 docker exec -it (ubt) /bin/bash : 실행
 ls -l usr/bin : 명령어 보기
 ls -l
 ls -la : 숨어있는 명령어 포함
 whoami : 
 su (사용자명) : 사용자 변경
 su : root로 돌아가기 (비밀번호 요구 할 수 있음)
 exit : 돌아가기
 useradd -m -s /bin/bash -c "(이름설명)" (이름) : 사용자 생성
 apt install (설치파일)
 docker pull (설치할이미지)
 docker stop (컨테이너이름) : 정지
 docker ps : 켜진 컨테이너 목록
 docker ps -a : 전체 컨터네이너
 docker rm (컨테이너이름) : 컨테이너 삭제
 docker run -d -it -p 80:5173 --name nd node:24.13.0 : 포트 포워딩/매핑 / 80:외측, 5173:내측
 mkdir (폴더명) : 폴더 생성
 apt update : 업데이트부터 할 것 /
 apt install vim : vi설치
```

  ## vi
```bash
vi (파일명.sh) : 새로 만들기
i : 작성모드, 현재 커서 위치부터 입력
```

  ## redis
    백에서 사용하는 캐시를 이용하여 데이터 저장 (쿠키랑 유사한 느낌)
```py
uv add redis

import redis

client = redis.Redis(
        host="localhost",
        port=6379,
        db=0
)

@app.get("/set")
def setRedis():
    client.setex("fastapi:100", 60*60*24, "abcdefg")
    return {"status": True}

@app.get("/get")
def getRedis():
    result = client.get("fastapi:100")
    return {"result": result}

@app.get("/del")
def delRedis():
    client.delete("fastapi:100")
    return {"status": True}
```

```bash
docker exec -it redis redis-cli  
127.0.0.1:6379> ping
PONG
127.0.0.1:6379> keys *
(empty array)
# docs에서 set execute
127.0.0.1:6379> keys *
1) "fastapi:100"
127.0.0.1:6379> set fastapi:200 12345
OK
127.0.0.1:6379> keys *
1) "fastapi:200"
2) "fastapi:100"
127.0.0.1:6379> GET fastapi:100
"abcdefg"
127.0.0.1:6379> get fastapi:200
"12345"
```



