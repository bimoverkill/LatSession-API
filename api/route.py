from flask import request
from . import app, db
from .models import Account
from hashlib import sha256

from random import randint

@app.route("/", methods=["GET"])
def main():
    return {"Hello" : "World"}


@app.route("/user/register/", methods=["POST"])
def register():
    uname = str(request.form.get("username"))
    password = str(request.form.get("password")).encode("utf-8")
    is_seller = int(request.form.get("is_seller"))

    try:
        db.session.add(Account(
            username=uname, 
            password=sha256(password).hexdigest(),
            is_seller=True if is_seller == 1 else False
        ))
        db.session.commit()
        return {
            "message": "registrasi berhasil",
            "content": {
                "registration_status": 1
            }
        }
    except Exception:
        return {
            "message": "Registrasi Gagal",
            "content": {
                "registration_status": 0
            }
        }

