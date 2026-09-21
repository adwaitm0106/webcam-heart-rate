"""Skin regions + pixel averaging. This part is mine to write (Step 1 [ME])."""
import cv2
import numpy as np

# TODO: pick landmark indices (see outputs/landmarks_frame0.png).
# Each list is the corners of one region, in order around its edge.
FOREHEAD = []
LEFT_CHEEK = []
RIGHT_CHEEK = []


def region_mask(shape, pts, indices):
    """Return a mask (same height/width as the frame): 255 inside the region, 0 outside.

    hint: cv2.fillConvexPoly on an all-zeros uint8 array
    """
    raise NotImplementedError


def mean_rgb(frame_bgr, mask):
    """Average the pixels where mask is on. Return (r, g, b).

    hint: frame_bgr[mask > 0] gives an (n_pixels, 3) array. Watch out: it's BGR.
    """
    raise NotImplementedError
