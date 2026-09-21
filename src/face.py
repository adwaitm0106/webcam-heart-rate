"""Face landmark detection with MediaPipe FaceLandmarker (Tasks API)."""
from pathlib import Path

import cv2
import mediapipe as mp
import numpy as np
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "face_landmarker.task"


def make_landmarker():
    options = vision.FaceLandmarkerOptions(
        base_options=mp_python.BaseOptions(model_asset_path=str(MODEL_PATH)),
        running_mode=vision.RunningMode.VIDEO,
        num_faces=1,
    )
    return vision.FaceLandmarker.create_from_options(options)


def get_landmarks(landmarker, frame_bgr, timestamp_ms):
    """Return a (478, 2) array of landmark positions in PIXELS, or None if no face."""
    h, w = frame_bgr.shape[:2]
    rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    result = landmarker.detect_for_video(image, int(timestamp_ms))
    if not result.face_landmarks:
        return None
    pts = result.face_landmarks[0]
    return np.array([[p.x * w, p.y * h] for p in pts])
