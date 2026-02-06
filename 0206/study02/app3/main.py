from fastapi import FastAPI
from settings import settings
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from starlette.responses import JSONResponse
from typing import List

class EmailSchema(BaseModel):
    email: List[EmailStr]
    msg: str

conf = ConnectionConfig(
    MAIL_USERNAME = settings.mail_username,
    MAIL_PASSWORD = settings.mail_password,
    MAIL_FROM = settings.mail_from,
    MAIL_PORT = settings.mail_port,
    MAIL_SERVER = settings.mail_server,
    MAIL_FROM_NAME= settings.mail_from_name,
    MAIL_STARTTLS = settings.mail_starttls,
    MAIL_SSL_TLS = settings.mail_ssl_tls,
    USE_CREDENTIALS = settings.use_credentials,
    VALIDATE_CERTS = settings.validate_certs
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg":"Email Service"}

@app.post("/email")
async def simple_send(model: EmailSchema) -> JSONResponse:
    html = f"""
    <h1>안녕</h1>
    <p>{model.msg}</p>
    """

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=model.dict().get("email"),
        # recipients=[model.email],
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})