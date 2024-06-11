# user_routes.py

from flask import Blueprint, jsonify, request
from persistence.data_manager import DataManager
from models.user import User

# Function to create the user_bp blueprint
def create_user_bp():
    user_bp = Blueprint('user_bp', __name__)

    data_manager = DataManager()

    @user_bp.route('/users', methods=['GET'])
    def get_users():
        users = data_manager.get_all('User')
        if users:
            return jsonify([user.to_dict() for user in users]), 200
        else:
            return jsonify({"error": "No users found"}), 404

    @user_bp.route('/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        user = data_manager.get(user_id, 'User')
        if user:
            return jsonify(user.to_dict()), 200
        else:
            return jsonify({"error": "User not found"}), 404

    @user_bp.route('/users', methods=['POST'])
    def create_user():
        data = request.json
        if not data or 'email' not in data or 'first_name' not in data or 'last_name' not in data:
            return jsonify({"error": "Email, first name, and last name are required"}), 400

        new_user = User(email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
        saved_user = data_manager.save(new_user)
        return jsonify(saved_user.to_dict()), 201

    @user_bp.route('/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        existing_user = data_manager.get(user_id, 'User')
        if not existing_user:
            return jsonify({"error": "User not found"}), 404

        # Update user attributes
        for key, value in data.items():
            setattr(existing_user, key, value)

        if data_manager.update(existing_user):
            return jsonify(existing_user.to_dict()), 200
        else:
            return jsonify({"error": "Failed to update user"}), 500

    @user_bp.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        if data_manager.delete(user_id, 'User'):
            return '', 204
        else:
            return jsonify({"error": "User not found"}), 404

    return user_bp
