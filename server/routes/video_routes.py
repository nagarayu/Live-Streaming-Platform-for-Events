from flask import Blueprint, jsonify, request
import cv2

video_routes = Blueprint('video_routes', __name__)

@video_routes.route('/video', methods=['POST'])
def play_video():
    rtsp_url = request.get_json()['rtsp_url']
    cap = cv2.VideoCapture(rtsp_url)
    if not cap.isOpened():
        return jsonify({'message': 'Failed to open video stream'})
    return jsonify({'message': 'Video stream started'})