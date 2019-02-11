import face_recognition

image = face_recognition.load_image_file("image/obama.jpg")
# image2 = face_recognition.load_image_file("image/obama2.jpg")
image2 = face_recognition.load_image_file("image/trump.jpg")


barack_encoding = face_recognition.face_encodings(image)[0]
image2_encoding = face_recognition.face_encodings(image2)[0]

results = face_recognition.compare_faces([barack_encoding], image2_encoding)
print(results)

