from flask import Blueprint, request, jsonify
from .models import users

main = Blueprint("main", __name__)


from flask import render_template

@main.route("/")
def home():
    return render_template("index.html")
# Healthcheck
@main.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


#  READ ALL
@main.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


#  READ ONE
@main.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


#  CREATE
@main.route("/users", methods=["POST"])
def create_user():
    data = request.json

    new_user = {
        "id": len(users) + 1,
        "name": data.get("name")
    }

    users.append(new_user)
    return jsonify(new_user), 201


#  UPDATE
@main.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json

    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            return jsonify(user), 200

    return jsonify({"error": "User not found"}), 404


#  DELETE
@main.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "Deleted"}), 200

    return jsonify({"error": "User not found"}), 404