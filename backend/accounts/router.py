from fastapi import APIRouter, Cookie, Response
from fastapi.responses import JSONResponse
from firebase_admin import auth
from starlette.responses import RedirectResponse
from accounts import schemas
from service.firebase_session import firebase_app
from utils.main import FireBase

app = APIRouter()


@app.post('/createUser', response_model=schemas.User)
async def create_user(data: schemas.User, response: Response):
    try:
        user_data = auth.create_user(**data.__dict__, app=firebase_app)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})
    uid = user_data._data["localId"]
    custom_token = auth.create_custom_token(uid, app=firebase_app)
    id_token = FireBase().get_id_token(custom_token)["idToken"]
    response.set_cookie(key="session_cookie",
                        value=auth.create_session_cookie(id_token, 172800), expires=172800)
    response.set_cookie(key="uid", value=uid, expires=172800)
    return data


@app.get("/logout")
async def logout(uid: str = Cookie(...)):
    response = RedirectResponse(url="/")
    if uid:
        response.delete_cookie("session_cookie")
        response.delete_cookie("uid")
    return response


@app.post('/loginCheck')
async def check_user(uid: str = Cookie(...), session_cookie: str = Cookie(...)):
    data = FireBase().verify_session_cookie(session_cookie)
    if data.get("uid") == uid:
        return {
            "uid": uid,
            "session_cookie": session_cookie,
            "data": data
        }
    return {"message": "login required"}
