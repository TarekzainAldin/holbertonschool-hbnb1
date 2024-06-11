from flask import Blueprint, jsonify, request
from persistence.amenity_data_manager import AmenityDataManager

amenity_bp = Blueprint('amenity_bp', __name__)
amenity_manager = AmenityDataManager()

@amenity_bp.route('/amenities', methods=['POST'])
def create_amenity():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    name = data['name']
    # Check if the amenity name is unique
    if amenity_manager.get_by_name(name):
        return jsonify({"error": "Amenity with this name already exists"}), 409

    amenity = amenity_manager.save({'name': name})
    return jsonify(amenity), 201

@amenity_bp.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = amenity_manager.get_all()
    return jsonify(amenities), 200

@amenity_bp.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = amenity_manager.get(amenity_id)
    if amenity:
        return jsonify(amenity), 200
    else:
        return jsonify({"error": "Amenity not found"}), 404

@amenity_bp.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    name = data['name']
    amenity = amenity_manager.get(amenity_id)
    if amenity:
        # Check if the new name conflicts with existing amenities
        if amenity_manager.get_by_name(name) and amenity_manager.get_by_name(name)['id'] != amenity_id:
            return jsonify({"error": "Amenity with this name already exists"}), 409

        amenity['name'] = name
        amenity_manager.update(amenity)
        return jsonify(amenity), 200
    else:
        return jsonify({"error": "Amenity not found"}), 404

@amenity_bp.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    deleted = amenity_manager.delete(amenity_id)
    if deleted:
        return '', 204
    else:
        return jsonify({"error": "Amenity not found"}), 404
