# Face-Hair-Segmentation-Dataset
[Official webpage](http://www.cs.ubbcluj.ro/~dadi/face-hair-segm-database.html)

The purpose of this dataset is to provide segmentation masks (labeled with face, hair and background pixels) for more than 3500 unconstrained, "in-the-wild" face images. The input images are taken from the CelebA . We do not own the input images so you have to contact the authors to obtain permission to use the corresponding input images. 

The segemntation masks correspond to the aligned and cropped png images from the CelebA dataset. Each mask is a bmp file with the same basename as its corresponding input image (for example, the segmentation mask 000567.bmp corresponds to the image 000567.png).

The segmentation masks contain only the following pixels 0 (background pixel), 128 (face area pixel) or 255 (hair area pixel).

The database contains the following files:

- Segmentation masks: bmp images corresponding to a subset of the CelebA dataset images.
- Scripts (python): useful scripts to view the segmentation and to select the corresponding input images from the CelebA dataset. 

## Terms and conditions
The database is made public  only for non-commercial purposes.
This database contains the corresponding segmentation masks (hair, face and skin pixels) for a subset of the images from CelebA dataset. We do not own the corresponding input images for the segmentation masks. You have to contact CelebA authors to obtain permission to also use the corresponding input images 
You agree not to further copy, publish or distribute any of the segmentation masks included in this database

## Citation 

If you use these data please cite the following work: 

Borza, Diana, Tudor Ileni, and Adrian Darabant. "A Deep Learning Approach to Hair Segmentation and Color Extraction from Facial Images." International Conference on Advanced Concepts for Intelligent Vision Systems. Springer, Cham, 2018.

### Bibtex format:

@inproceedings{borza2018deep,
  title={A Deep Learning Approach to Hair Segmentation and Color Extraction from Facial Images},
  author={Borza, Diana and Ileni, Tudor and Darabant, Adrian},
  booktitle={International Conference on Advanced Concepts for Intelligent Vision Systems},
  pages={438--449},
  year={2018},
  organization={Springer}
}
