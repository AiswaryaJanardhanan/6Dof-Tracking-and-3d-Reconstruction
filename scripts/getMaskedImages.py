import cv2
import os
import numpy as np

def merge_mask_with_image(image_path, mask_path, output_path):
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    # Convert the mask to a binary mask with values of 0 or 255
    mask = np.where(mask > 0, 255, 0).astype(np.uint8)

    # Resize mask to match the image size if needed
    if image.shape[:2] != mask.shape[:2]:
        mask = cv2.resize(mask, (image.shape[1], image.shape[0]))
    # cv2.imwrite(output_path + 'temp_orig.jpg', image)
    # cv2.imwrite(output_path + 'temp_mask.jpg', mask)
    # Apply the mask to the image
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    # Save the masked image
    cv2.imwrite(output_path, masked_image)


def merge_images_in_folder(rbg_folder, mask_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    rgb_files = [f for f in os.listdir(rbg_folder) if f.endswith('.jpg') or f.endswith('.png')]
    mask_files = [f for f in os.listdir(mask_folder) if f.endswith('.jpg') or f.endswith('.png')]


    # Merge each image with its corresponding mask
    for image_file in rgb_files:
        image_path = os.path.join(rbg_folder, image_file)
        mask_path = os.path.join(mask_folder, image_file)
        output_path = os.path.join(output_folder, image_file)
        merge_mask_with_image(image_path, mask_path, output_path)



rbg_folder = '/home/sathrij/BundleTrack/YCBInEOAT/bleach0/rgb/'

mask_folder = '/home/sathrij/BundleTrack/YCBInEOAT/bleach0/gt_mask/'

output_folder = '/home/sathrij/instant-ngp/data/nerf/bleach/images/'


# Merge the images with their masks
merge_images_in_folder(rbg_folder, mask_folder, output_folder)