import cv2
import os
import pickle
import numpy as np
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
Image_dir = os.path.join(BASE_DIR, "Lib", 'Images')
face_cascade = cv2.CascadeClassifier('Lib/cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0;
label_ids = dict()  

x_train = list()
y_labels = list()

for root, dirs, files in os.walk(Image_dir):
    for file in files:
        if file.endswith('jpg'):
            path = os.path.join(root, file)
            label = os.path.basename(root).lower()            
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1

            id_ = label_ids[label]
            # print(label_ids)
            pil_image = Image.open(path).convert('L')  # Converts to Grayscale
            size = (550, 550)
            final_image = pil_image.resize(size, Image.ANTIALIAS)
            image_array = np.array(final_image, 'uint8')
            # print(image_array)

            faces = face_cascade.detectMultiScale(
                image_array,
                scaleFactor=2,
                minNeighbors=5,
                minSize=(35, 35)
            )

            for (x, y, w, h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)


with open('labels.pickle', "wb") as f:
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("Trainer.yml")
print("Training is Done!")