from collections import OrderedDict

FACIAL_LANDMARKS_68_IDS = OrderedDict([
    ("mouth", (48, 68)),
    ("right_eyebrow", (17, 22)),
    ("left_eyebrow", (22, 27)),
    ("right_eye", (36, 42)),
    ("left_eye", (42, 48)),
    ("nose", (27, 36)),
    ("jaw", (0, 17)),
])

IMAGE_RESIZE_WIDTH = 500
VIDEO_RESIZE_WIDTH = 1200
ROI_RESIZE_WIDTH = 250

EAR_THRESHOLD = 0.3
EAR_GAP_FRAMES = 3

BLINKS_THRESHOLD = 15
# 0.6s in 24fps/s
EYE_OPEN_THRESHOLD = 15
