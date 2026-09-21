"""Skin regions + pixel averaging."""
import cv2
import numpy as np

# landmark numbers around each patch (picked from outputs/landmarks_frame0.png)
FOREHEAD = [67, 297, 299, 105]
LEFT_CHEEK = [100, 203, 187, 123]   # left side of the picture
RIGHT_CHEEK = [329, 330, 411, 266]  # right side of the picture
REGIONS = [FOREHEAD, LEFT_CHEEK, RIGHT_CHEEK]


def region_mask(shape, pts, indices):
    """Black image, region painted white (255)."""
    corners = pts[indices].astype(np.int32)
    mask = np.zeros(shape, dtype=np.uint8)
    cv2.fillConvexPoly(mask, corners, 255)
    return mask


def skin_mask(shape, pts):
    """All 3 regions in one mask."""
    mask = np.zeros(shape, dtype=np.uint8)
    for region in REGIONS:
        mask = np.maximum(mask, region_mask(shape, pts, region))
    return mask


def mean_rgb(frame_bgr, mask):
    """Average color of the masked pixels. Returns (r, g, b)."""
    pixels = frame_bgr[mask > 0]
    b, g, r = pixels.mean(axis=0)
    return r, g, b
