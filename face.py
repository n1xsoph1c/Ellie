# import cv2
# import sys
# import os
# import pickle

# def check_img():
#     face_cascade = cv2.CascadeClassifier(
#     'cascades/data/haarcascade_frontalface_alt2.xml')
#     recognizer = cv2.face.LBPHFaceRecognizer_create()
#     recognizer.read("Trainer.yml")

#     labels = {"person_name": 1}
#     with open('labels.pickle', "rb") as f:
#         og_labels = pickle.load(f)
#         labels = {v: k for k, v in og_labels.items()}

#     video_capture = cv2.VideoCapture(0)

#     while True:
#         # Capture Frame by Frame
#         returnValue, frame = video_capture.read()

#         # Convert RGB to GrayScale
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # Detect Faces from haarcascade
#         faces = face_cascade.detectMultiScale(
#             gray,
#             scaleFactor=1.4,
#             minNeighbors=5,
#             minSize=(30, 30)
#         )

#         # Draw Rectangle around faces

#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (150, 150, 0), 4)

#             # Region of Intreset
#             roi_gray = gray[y:y+h, x:x+w]

#             # Try to Recognize the face
#             id_, conf = recognizer.predict(roi_gray)
#             print(id_, conf)

#             if conf >= 25 and conf <= 100:
#                 font = cv2.FONT_HERSHEY_SIMPLEX
#                 name = labels.get(id_)
#                 color = (255, 255, 255)
#                 stroke = 2

#                 cv2.putText(frame, name,  (x, y), font, 2, color, stroke, cv2.LINE_AA)

#         cv2.imshow('Video', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # When everything is done, release the capture
#     video_capture.release()
#     cv2.destroyAllWindows()

# check_img()