import os
import cv2
import numpy as np
from typing import Tuple
def find_files(directory: str = ".", prefix: str="") -> Tuple[str, str, str]:
    files = os.listdir(directory)

    r = []
    g = []
    b = []

    for filename in files:
        full_filename = os.path.join(directory, filename)
        if filename.startswith(prefix):
            without_suffix = ".".join(filename.split(".")[:-1])
            parts = without_suffix.split("_")



            if parts[-1].lower().startswith("r"):
                r.append(full_filename)

            if parts[-1].lower().startswith("g"):
                g.append(full_filename)

            if parts[-1].lower().startswith("b"):
                b.append(full_filename)

    lens = [len(r), len(g), len(b)]

    if any([l == 0 for l in lens]):
        raise FileNotFoundError("Missing one of *_r*.*, *_g*.*, or *_b*.*")

    elif any([l > 1 for l in lens]):
        raise FileExistsError("Found more files with that pattern than expected")

    return r[0], g[0], b[0
    ]
def load_rgb_files(directory: str = ".", prefix: str="") -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    r, g, b = find_files(directory, prefix)

    return cv2.imread(r), cv2.imread(g), cv2.imread(b)