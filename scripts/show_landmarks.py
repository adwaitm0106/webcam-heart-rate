"""Draw face landmarks on frame 0, zoomed in, so we can pick indices for skin regions."""
import sys
from pathlib import Path

import cv2

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from face import get_landmarks, make_landmarker
from ubfc import iter_frames, subject_paths

video, _ = subject_paths(1)
frame = next(iter_frames(video))
pts = get_landmarks(make_landmarker(), frame, 0)
print("landmarks:", pts.shape)

# crop around the face and blow it up 6x so the numbers are readable
x0, y0 = pts.min(axis=0).astype(int) - 15
x1, y1 = pts.max(axis=0).astype(int) + 15
scale = 6
crop = cv2.resize(frame[y0:y1, x0:x1], None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

for i, (x, y) in enumerate(pts):
    p = (int((x - x0) * scale), int((y - y0) * scale))
    cv2.circle(crop, p, 2, (0, 255, 0), -1)
    if i % 4 == 0:
        cv2.putText(crop, str(i), (p[0] + 3, p[1] - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
cv2.imwrite(str(ROOT / "outputs" / "landmarks_frame0.png"), crop)
print("saved", crop.shape)
