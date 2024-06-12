from flask import Blueprint, jsonify, request
from persistence.place_data_manager import PlaceDataManager

place_bp = Blueprint('places', __name__, url_prefix='/api/v1/places')
place_manager = PlaceDataManager()

@place_bp.route('/', methods=['POST'])
def create_place():
    data = request.json
    try:
        new_place = place_manager.save(data)
        return jsonify(new_place), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@place_bp.route('/', methods=['GET'])
def get_all_places():
    all_places = place_manager.get_all()
    return jsonify(all_places)

@place_bp.route('/<int:place_id>', methods=['GET'])
def get_place(place_id):
    place = place_manager.get(place_id)
    if place:
        return jsonify(place)
    else:
        return jsonify({'error': 'Place not found'}), 404

@place_bp.route('/<int:place_id>', methods=['PUT'])
def update_place(place_id):
    data = request.json
    data['id'] = place_id
    try:
        if place_manager.update(data):
            return jsonify(data)
        else:
            return jsonify({'error': 'Place not found'}), 404
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@place_bp.route('/<int:place_id>', methods=['DELETE'])
def delete_place(place_id):
    if place_manager.delete(place_id):
        return '', 204
    else:
        return jsonify({'error': 'Place not found'}), 404
