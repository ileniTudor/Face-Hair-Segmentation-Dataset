import cv2
import sys
import numpy as np
from utils_segmentation import find_corresponding_images

g_label_face = 128
g_label_hair = 255

g_hair_color_display = (0, 0, 255)
g_skin_color_display = (0, 255, 0)


def overlay_mask_with_color(img, seg_mask, color):
    color_img = np.zeros(img.shape, img.dtype)
    color_img[:, :] = color

    color_mask = cv2.bitwise_and(color_img, color_img, mask=seg_mask)
    display_image = cv2.addWeighted(color_mask, 0.3, img, 0.7, 0)
    return display_image


def overlay_segmentation(img, mask):
    """ Overlays the hair-face segmentation over the input image
    :param img: input bgr-image containing the color image
    :param mask: input greyscale image containing the segmentation mask
                (0 - background pixel,
                1 - skin pixel,
                2 - hair pixel)
    :return: a "pretty" view of the segmentation (the segmentation mask: mask is super-imposed over the input image: img)
    """
    hair_mask = np.zeros(mask.shape, dtype=np.uint8)
    hair_mask[mask == g_label_hair] = 255
    segmentation_color = overlay_mask_with_color(img, hair_mask, g_hair_color_display)

    skin_mask = np.zeros(mask.shape, dtype=np.uint8)
    skin_mask[mask == g_label_face] = 255
    segmentation_color = overlay_mask_with_color(segmentation_color, skin_mask, g_skin_color_display)

    return segmentation_color


def view_segmentations(masks_dir, input_images_dir):
    """ 'Pretty' display the segmentation images. Use the keys to navigate through the images:
        - press 'p' key for previous image
        - press 'r' key to restart
    :param masks_dir: path to the directory where the segemntation masks are stored
    :param input_images_dir: path to the directory where the input images corresponding to the segemntations are stored
    :return: None
    """
    image_pairs = find_corresponding_images(masks_dir, input_images_dir)

    cv2.namedWindow('segmentation', cv2.WINDOW_NORMAL)

    idx = 0
    num_images = len(image_pairs)

    while idx < num_images:
        img_path, mask_path = image_pairs[idx]
        mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.imread(img_path)

        seg_display = overlay_segmentation(img, mask)
        cv2.imshow('segmentation', seg_display)
        key = cv2.waitKey(0)

        if key == ord('p'):
            # previous image
            if idx > 0:
                idx -= 1
        elif key == ord('r'):
            # reset
            idx = 0
        else:
            idx += 1


def display_help():
    print('Usage: view_segmentations.py [masks_dir] [images_dir].  \n'
          'Args:\n\tmasks_dir - path to the directory where the segmentation masks are stored.\n'
                '\timages_dir - path to the directory where in corresponding images are stored.'
                'Can be the same as masks_dir.  \nUse the keys to navigate through the images:'
                ' press p for previous image, press r key to restart and any other key for next image.')


def parse_command_line():
    if len(sys.argv) < 2:
        display_help()
        exit(-1)

    masks_dir = sys.argv[1]
    images_dir = sys.argv[2]
    return masks_dir, images_dir


if __name__ == '__main__':
    m_dir, i_dir = parse_command_line()
    view_segmentations(m_dir, i_dir)
