from flask import Blueprint, jsonify, request
from models.country import Country
from persistence.country_data_manager import CountryDataManager

country_city_bp = Blueprint('country_city_bp', __name__)

country_manager = CountryDataManager()

@country_city_bp.route('/countries', methods=['GET'])
def get_countries():
    countries = country_manager.get_all()
    if countries:
        return jsonify([country.to_dict() for country in countries]), 200
    else:
        return jsonify({"error": "No countries found"}), 404

@country_city_bp.route('/countries/<country_code>', methods=['GET'])
def get_country(country_code):
    country = country_manager.get(country_code)
    if country:
        return jsonify(country.to_dict()), 200
    else:
        return jsonify({"error": "Country not found"}), 404

@country_city_bp.route('/countries', methods=['POST'])
def create_country():
    data = request.json
    if not data or 'name' not in data or 'code' not in data:
        return jsonify({"error": "Name and code are required"}), 400

    new_country = Country(name=data['name'], code=data['code'])
    saved_country = country_manager.save(new_country)
    return jsonify(saved_country.to_dict()), 201

@country_city_bp.route('/countries/<country_code>', methods=['PUT'])
def update_country(country_code):
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    updated_country = country_manager.update(country_code, data['name'])
    if updated_country:
        return jsonify(updated_country.to_dict()), 200
    else:
        return jsonify({"error": "Country not found"}), 404

@country_city_bp.route('/countries/<country_code>', methods=['DELETE'])
def delete_country(country_code):
    deleted = country_manager.delete(country_code)
    if deleted:
        return '', 204
    else:
        return jsonify({"error": "Country not found"}), 404