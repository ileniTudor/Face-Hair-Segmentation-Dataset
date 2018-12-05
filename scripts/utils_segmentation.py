import os
import sys
import glob
import shutil


def find_corresponding_images(masks_dir, input_images_dir, input_ext='.png'):
    """
    :param masks_dir: path to the folder which contains the segmentation masks
    :param input_images_dir: path to the folder which contains the input images
    :param input_ext: the extension of the input images (by default png)
    :return a list of tuples (image-mask), where each element is a mapping between the path of the input image
            and the path of the corresponding segmentation mask
    """
    if not os.path.exists(masks_dir) or not os.path.isdir(masks_dir):
        raise ValueError('The path for the masks directory %s does not exist or is not a folder' % masks_dir)
    if not os.path.exists(input_images_dir) or not os.path.isdir(input_images_dir):
        raise ValueError('The path for the input images directory %s does not exist or is not a folder' % input_images_dir)

    # find the segmentation masks (bmp) images in the masks directory
    mask_files = glob.glob(os.path.join(masks_dir, "*.bmp"))
    print('Found %d segmentation masks ' % len(mask_files))

    num_images = len(mask_files)

    image_tuples = []
    for idx, mask_path in enumerate(mask_files):
        basename = os.path.basename(mask_path)
        sys.stdout.write('\r>> Searching image for  segmentation mask %s (%d/%d) ' % (basename, idx, num_images))
        sys.stdout.flush()
        img_path = os.path.join(input_images_dir, basename.replace('.bmp', input_ext))
        if os.path.exists(img_path):
            image_tuples.append((img_path, mask_path))
        else:
            sys.stdout.write('\r>> Error! Could not find input image for segmentation %s' % basename)
            sys.stdout.flush()

    return image_tuples



