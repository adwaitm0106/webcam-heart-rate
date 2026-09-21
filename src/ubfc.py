"""Loading one UBFC-rPPG (DATASET_2) subject: the video and the pulse sensor file."""
from pathlib import Path

import cv2
import numpy as np

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "ubfc" / "DATASET_2"


def iter_frames(video_path):
    """Yield frames one at a time (each is a 480x640x3 BGR array). Returns nothing else."""
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise FileNotFoundError(f"can't open {video_path}")
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            yield frame
    finally:
        cap.release()


def get_fps(video_path):
    cap = cv2.VideoCapture(str(video_path))
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()
    return fps


def load_ground_truth(gt_path):
    """Row 0 = pulse wave, row 1 = heart rate (BPM), row 2 = time in seconds."""
    ppg, hr, t = np.loadtxt(gt_path)
    return {"ppg": ppg, "hr": hr, "time": t}


def subject_paths(n):
    folder = DATA_DIR / f"subject{n}"
    return folder / "vid.avi", folder / "ground_truth.txt"
