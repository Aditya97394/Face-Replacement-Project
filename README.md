# Face Swap Using OpenCV and Seamless Cloning

This project demonstrates a simple face swap technique using OpenCV's face detection and seamless cloning functionalities. The goal is to detect faces in two images and blend the face from the source image onto the target image in a realistic manner.

## Features

- **Face Detection**: Utilizes OpenCV's Haar cascades to detect faces in both the source and target images.
- **Seamless Cloning**: Uses OpenCV's `seamlessClone` function to blend the source face into the target image, ensuring a smooth and realistic appearance.
- **Image Processing**: Converts images to grayscale for face detection and performs resizing to match face dimensions.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- PIL (Pillow)


