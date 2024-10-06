from flask import Blueprint, jsonify, request
from mongoengine import Q
from models.overlay import Overlay

overlay_routes = Blueprint('overlay_routes', __name__)

@overlay_routes.route('/overlays', methods=['GET'])
def get_overlays():
    overlays = Overlay.objects()
    return jsonify([overlay.to_json() for overlay in overlays])

@overlay_routes.route('/overlays', methods=['POST'])
def create_overlay():
    data = request.get_json()
    overlay = Overlay(**data).save()
    return jsonify(overlay.to_json())

@overlay_routes.route('/overlays/<id>', methods=['GET'])
def get_overlay(id):
    overlay = Overlay.objects.get(id=id)
    return jsonify(overlay.to_json())

@overlay_routes.route('/overlays/<id>', methods=['PUT'])
def update_overlay(id):
    overlay = Overlay.objects.get(id=id)
    data = request.get_json()
    overlay.update(**data)
    return jsonify(overlay.to_json())

@overlay_routes.route('/overlays/<id>', methods=['DELETE'])
def delete_overlay(id):
    overlay = Overlay.objects.get(id=id)
    overlay.delete()
    return jsonify({'message': 'Overlay deleted'})