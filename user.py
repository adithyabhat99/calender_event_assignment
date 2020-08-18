from app import *
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from database import db_session
from models import User
import datetime


@app.route("/api/user", methods=["POST"])
def create_user():
    data = request.get_json()
    if data is None or "name" not in data or "email" not in data or "password" not in data:
        return jsonify({"success": False, "message": "Send name,email and password"}), 400
    try:
        name = data["name"]
        email = data["email"]
        password_hash = generate_password_hash(
            data['password'], method='sha256')
        user = User(name, email, password_hash)
        db_session.add(user)
        db_session.commit()
        token = jwt.encode({"id": str(user.id), "name": user.name, "exp": datetime.datetime.now(
        )+datetime.timedelta(days=10)}, "secret key")
        return jsonify({"success": True, "message": "user created", "Token": token.decode("UTF-8")}), 200
    except:
        return jsonify({"success": False, "message": "send unique email. error occured"}), 500


@app.route("/api/user/auth", methods=["POST"])
def authenticate():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({"success": False, "message": "email and password required in authorization header"}), 400
    try:
        user = User.query.filter_by(email=auth.username).first()
        if user is None:
            return jsonify({"success": False, "message": "user does not exist"}), 400
        password_hash = user.password_hash
        if check_password_hash(password_hash, auth.password):
            token = jwt.encode({"id": str(user.id), "name": user.name, "exp": datetime.datetime.now(
            )+datetime.timedelta(days=10)}, "secret key")
            return jsonify({"success": True, "message": "authentication successful", "Token": token.decode("UTF-8")}), 200
        else:
            return jsonify({"success": False, "message": "wrong password"}), 401
    except:
        return jsonify({"success": False, "message": "error occured"}), 500


@app.route("/api/user", methods=["PUT"])
@token_required
def update_user(userid):
    data = request.get_json()
    if data is None:
        return jsonify({"success": False, "message": "Send either name,email or password"}), 400
    user = User.query.filter_by(id=userid).first()
    if user is None:
        jsonify({"success": False, "message": "user does not exist"}), 400
    if "email" in data:
        user.email = data["email"]
    if "name" in data:
        user.name = data["name"]
    if "password" in data:
        user.password_hash = generate_password_hash(
            data["password"], method='sha256')
    db_session.commit()
    return jsonify({"success": True, "message": "user update successful"}), 200


@app.route("/api/user")
@token_required
def get_user(userid):
    try:
        user = User.query.filter_by(id=userid).first()
        if user is None:
            jsonify({"success": False, "message": "user does not exist"}), 400
        return jsonify({"success": True, "message": "user exists", "data": {"name": user.name, "email": user.email}}), 200
    except:
        return jsonify({"success": False, "message": "error occured"}), 500
