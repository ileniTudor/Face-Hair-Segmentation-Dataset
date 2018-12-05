import os
import sys
import shutil
from utils_segmentation import find_corresponding_images


def copy_segmented_images(masks_dir, input_images_dir, output_dir, input_ext ='.png'):
    """
    Copies the subset of the images from input_images_dir which contain segmenentations in masks_dir to output_dir.
    :param masks_dir: path to the folder which contains the segmentation masks
    :param input_images_dir: path to the folder which contains the input images
    :param output_dir: path to the folder where to copy the input images
    :param input_ext: the extension of the input images (by default png)
    :return None
    """
    image_pairs = find_corresponding_images(masks_dir, input_images_dir, input_ext)

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    num_images = len(image_pairs)
    print(num_images)
    images_text_filepath = os.path.join(output_dir, 'segmentations.txt')
    images_text_file = open(images_text_filepath, 'w')
    for idx, pair in enumerate(image_pairs):
        img_path, _ = pair
        basename = os.path.basename(img_path)
        shutil.copy(img_path, output_dir)

        sys.stdout.write('\r>>Copying image %s (%d/%d) ' % (basename, idx, num_images))
        sys.stdout.flush()
        images_text_file.write('%s\n' %basename)
    images_text_file.close()


def display_help():
    print('Usage: copy_segmentations.py [masks_dir] [images_dir] [output_dir].  \n'
          'Args:\n\tmasks_dir - path to the directory where the segmentation masks are stored.\n'
                '\timages_dir - path to the directory where in corresponding images are stored.\n'
                '\toutput_dir - path to the folder where to copy the input images which contain hair-face segmentations'
                )


def parse_command_line():
    if len(sys.argv) < 3:
        display_help()
        exit(-1)

    masks_dir = sys.argv[1]
    images_dir = sys.argv[2]
    output_dir = sys.argv[3]
    return masks_dir, images_dir, output_dir


if __name__ == '__main__':
    m_dir, i_dir, o_dir = parse_command_line()
    copy_segmented_images(m_dir, i_dir, o_dir)

