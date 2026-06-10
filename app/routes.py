from flask import Blueprint, request, jsonify
from .models import User
from .database import db

main = Blueprint("main", __name__)


from flask import render_template

@main.route("/")
def home():
    return render_template("index.html")
# Healthcheck
@main.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Estoy ok"}), 200




#  READ ALL
@main.route("/users", methods=["GET"])
def get_users():

    users = User.query.all()

    return jsonify(
        [user.to_dict() for user in users]
    ), 200


#  READ ONE
@main.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):

    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user.to_dict()), 200


# CREATE
@main.route("/users", methods=["POST"])
def create_user():

    data = request.json

    new_user = User(
        name=data.get("name")
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify(
        new_user.to_dict()
    ), 201
#  UPDATE
@main.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):

    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.json

    user.name = data.get("name", user.name)

    db.session.commit()

    return jsonify(user.to_dict()), 200

#  DELETE
@main.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "Deleted"}), 200