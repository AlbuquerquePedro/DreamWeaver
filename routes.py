from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest
from .dream_controller import create_dream, get_dream, update_dream, delete_dream, analyze_dream

dream_bp = Blueprint('dream_bp', __name__)

@dream_bp.route('/dreams', methods=['POST'])
def dream_create():
    """Create a new dream and store it."""
    try:
        data = request.get_json()
        if data is None:
            raise BadRequest("No input data provided or Content-Type header is not application/json.")

        result = create_dream(data)
        return jsonify(result), 201
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Failed to create dream: " + str(e)}), 500

@dream_bp.route('/dreams/<int:dream_id>', methods=['GET'])
def dream_retrieve(dream_id):
    """Retrieve a dream by its ID."""
    try:
        result = get_dream(dream_id)
        if result:
            return jsonify(result), 200
        else:
            return jsonify({"error": "Dream not found"}), 404
    except Exception as e:
        return jsonify({"error": "Failed to retrieve dream: " + str(e)}), 500

@dream_bp.route('/dreams/<int:dream_id>', methods=['PUT'])
def dream_update(dream_id):
    """Update an existing dream by its ID."""
    try:
        data = request.get_json()
        if data is None:
            raise BadRequest("No input data provided or Content-Type header is not application/json.")

        result = update_dream(dream_id, data)
        if result:
            return jsonify(result), 200
        else:
            return jsonify({"error": "Dream not found"}), 404
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Failed to update dream: " + str(e)}), 500

@dream_bp.route('/dreams/<int:dream_id>', methods=['DELETE'])
def dream_delete(dream_id):
    """Delete a dream by its ID."""
    try:
        result = delete_dream(dream_id)
        if result:
            return jsonify({"message": "Dream deleted"}), 200
        else:
            return jsonify({"error": "Dream not found"}), 404
    except Exception as e:
        return jsonify({"error": "Failed to delete dream: " + str(e)}), 500

@dream_bp.route('/dreams/<int:dream_id>/analysis', methods=['GET'])
def dream_analysis(dream_id):
    """Perform analysis on a specified dream."""
    try:
        result = analyze_dream(dream_id)
        if result:
            return jsonify(result), 200
        else:
            return jsonify({"error": "Analysis not found"}), 404
    except Exception as e:
        return jsonify({"error": "Failed to perform analysis: " + str(e)}), 500