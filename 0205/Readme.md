# 0205

  ## Docker
Docker는 **독립적**인 컨테이너를 이용해 애플리케이션을 개발 → 빌드 → 테스트 → 배포하는 전체 사이클을 지원하는 오픈 플랫폼입니다. 
    docker의 구성 요소 세 가지
    Container, Volumes, Network

- 설치된 docker 버전 확인
```bash
docker -v
```
- 설치된 docker image 목록 확인
```bash
docker image
```
- docker image 삭제
```bash
rmi nginx:latest
```
- nginx : 정적 파일을 웹에 서비스해주는 이미지
```bash
docker pull nginx:1.28
```
- docker container, network, volume 확인
```bash
docker container ls
docker network ls
docker volume ls
```
- docker user-defined bridge 만들기 /삭제
```bash
docker network create my-net
docker network rm my-net
```
- 컨테이너 생성
```bash
docker run --network=my-net -d -p 80:80 --name web nginx:1.28
```
| 옵션 | 설명 | 비유 |
| :--- | :--- | :--- |
| **`-d`** | 컨테이너를 **백그라운드**에서 실행 (터미널 점유 X) | "보이지 않는 곳에서 계속 일해!" |
| **`-p`** | **호스트와 컨테이너의 포트 연결** (예: `-p 80:8080`) | "밖에서 80번으로 오면 안의 8080번으로 연결해줘" |
| **`-v`** | **호스트와 컨테이너의 디렉토리 연결** (데이터 보존) | "내 컴퓨터 폴더랑 컨테이너 폴더를 공유하자" |
| **`-it`** | 컨테이너 내부로 **대화형 터미널 입력** 가능하게 설정 | "컨테이너 안으로 들어가서 직접 명령할게" |
| **`--name`** | 컨테이너에 **고유한 이름** 부여 | "ID 대신 'my-web'이라는 이름으로 부를게" |
예시 : docker run -d -p 80:80 -v ./index.html:/usr/share/nginx/html/index.html --name web nginx:1.28
-> 
- 컨테이너 실행
```bash
docker exec -it (컨테이너이름) /bin/bash
```
- curl : **"Client URL"**의 약자로, 터미널(CLI) 환경에서 서버와 데이터를 주고받을 때 사용
```bash
curl http://localhost:80/
```
- ifconfig (ip확인)
```bash
apt update
apt install net-tools
ifconfig
```
- 실행 중인 컨테이너 확인
```bash
docker ps
```
- 컨테이너 삭제
```bash
docker rm (컨테이너ID)
docker rm -f (컨테이너ID)
```
- ping-pong 알아보기
```bash
apt install -y iputils-ping
ping (ip주소 or 컨테이너name도 가능)
```
- nginx 화면 경로
```bash
/usr/share/nginx/html/index.html
```
- nginx html교체
/study01/nginx/에 index.html 만들고 교체
```bash
docker run -d -p 80:80 -v ./index.html:/usr/share/nginx/html/index.html --name web nginx:1.28
```

- 포트 포워딩
```
80:80
앞의 외부 포트는 동일하면 안 됨
뒤의 내부 포트는 동일할 수 있음
```

  ## Dockerfile 설명
```
FROM        : 기본 대상 이미지를 정의하는 속성
MAINTAINER  : 작성자의 정보를 기록하는 속성
RUN         : FROM의 기반 이미지 위에서 실행될 명령어 정의
COPY        : 도커 컨테이너의 경로로 파일을 복사할 때 사용하는 속성
COPY 로컬:컨테이너
COPY ./index.html:/usr/share/nginx/html/index.html
ENV         : 도커 컨테이너의 환경변수를 정의하는 속성
EXPOSE      : 연결할 포트 번호 정의
ENTRYPOINT  : 도커 컨테이너 생성 후 실행될 명령어 (1회 실행)
CMD         : 실행 시, 해당 속성으로 컨테이너 켜기.
```
- 이미지 생성
```bash
dockerfile 있는 곳에 터미널을 열고
docker build -t web:0.0.1 .
```
- 이미지 삭제
```bash
docker rmi [이미지이름]
```

