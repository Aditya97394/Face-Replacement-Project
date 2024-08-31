import numpy as np
import cv2
from PIL import Image


source_img = cv2.imread('Images/src1.jpg') 
target_img = cv2.imread('Images/tar1.jpg')  


source_img_gray = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)
target_img_gray = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


source_faces = face_cascade.detectMultiScale(source_img_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


target_faces = face_cascade.detectMultiScale(target_img_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


if len(source_faces) == 0 or len(target_faces) == 0:
    raise ValueError("No faces detected in one or both images.")


(x_s, y_s, w_s, h_s) = source_faces[0]
(x_t, y_t, w_t, h_t) = target_faces[0]


source_face = source_img[y_s:y_s+h_s, x_s:x_s+w_s]


resized_source_face = cv2.resize(source_face, (w_t, h_t))


mask = 255 * np.ones(resized_source_face.shape, resized_source_face.dtype)


center = (x_t + w_t // 2, y_t + h_t // 2)


output = cv2.seamlessClone(resized_source_face, target_img, mask, center, cv2.NORMAL_CLONE)


final_image = Image.fromarray(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))


final_image.save('final_output.png')
final_image.show()
