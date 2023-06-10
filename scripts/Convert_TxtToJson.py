import os
import json
# import cv2
from skimage import io, filters

# def compute_sharpness(img_file):
#     print(img_file)
#     img = cv2.imread(img_file)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     return cv2.Laplacian(gray, cv2.CV_64F).var()
# 0000_color.png
txt_dir = "/tmp/BundleTrack/ycbineoat/YCBInEOAT/poses"
img_dir = "/home/sathrij/instant-ngp/data/nerf/bleach/images"
scene_1_dir = "/home/sathrij/BundleTrack/YCBInEOAT/bleach0/rgb"

txt_files = [f for f in os.listdir(txt_dir) if f.endswith(".txt")]

txt_files = sorted(txt_files, key=lambda x: int(os.path.splitext(x)[0]))

frames = []
# [ WARN:0@0.003] global loadsave.cpp:244 findDecoder imread_('/BundleTrack/NOCS/real_test/scene_1/0000_color.png'): can't open/read file: check file path/integrity

for txt_file in txt_files:
    img_file = f"{img_dir}/{txt_file.split('.')[0]}.png"
    with open(os.path.join(txt_dir, txt_file)) as f:
        transform_matrix = [[float(x) for x in line.split()] for line in f]
        transform_matrix[-1] = [0.0, 0.0, 0.0, 1.0]
    scene_1_img = txt_file.split('.')[0] + '.png'
    img = io.imread(os.path.join(scene_1_dir, scene_1_img))

    # Compute the Laplacian of the image
    laplacian = filters.laplace(img)

    # Compute the variance of the Laplacian to get an estimate of sharpness
    sharpness = laplacian.var()
    # sharpness = compute_sharpness(os.path.join(scene_1_dir, scene_1_img))

    frames.append({
        "file_path": img_file,
        "sharpness": sharpness,  # replace with actual sharpness value if available
        "transform_matrix": transform_matrix
    })

# Put the camera intrinsinsic parameters here
cam_K = {
    "camera_angle_x": 1.572103430310901,
    "camera_angle_y": 1.0442314293090673,
    "fl_x": 319.5820007324218750,
    "fl_y": 417.1186828613281250,
    "k1": 0,
    "k2": 0,
    "p1": 0,
    "p2": 0,
    "cx": 320.2149847676955687,
    "cy": 244.3486680871046701,
    "w": 640.0,
    "h": 480.0,
    "aabb_scale": 4
 }


with open("frames.json", "w") as f:
    json.dump({"frames": frames}, f, indent=2)
