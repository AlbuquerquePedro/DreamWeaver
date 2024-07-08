from flask import Blueprint, request, jsonify
from .dream_controller import create_dream, get_dream, update_dream, delete_dream, analyze_dream

dream_bp = Blueprint('dream_bp', __name__)

@dream_bp.route('/dreams', methods=['POST'])
def dream_create():
    data = request.get_json()
    result = create_dream(data)
    return jsonify(result), 201

@dream_bp.route('/dreams/<int:dream_id>', methods=['GET'])
def dream_retrieve(dream_id):
    result = get_dream(dream_id)
    if result:
        return jsonify(result), 200
    return jsonify({"error": "Dream not found"}), 404

@dream_bp.route('/dreams/<int:dream_id>', methods=['PUT'])
def dream_update(dream_id):
    data = request.get_json()
    result = update_dream(dream_id, data)
    if result:
        return jsonify(result), 200
    return jsonify({"error": "Dream not found"}), 404

@dream_bp.route('/dreams/<int:dream_id>', methods=['DELETE'])
def dream_delete(dream_id):
    result = delete_dream(dream_id)
    if result:
        return jsonify({"message": "Dream deleted"}), 200
    return jsonify({"error": "Dream not found"}), 404

@dream_bp.route('/dreams/<int:dream_id>/analysis', methods=['GET'])
def dream_analysis(dream_id):
    result = analyze_dream(dream_id)
    if result:
        return jsonify(result), 200
    return jsonify({"error": "Analysis not found"}), 404