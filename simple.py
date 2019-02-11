import face_recognition
from PIL import Image

image = face_recognition.load_image_file("image/crowd2.jpg")
face_locations = face_recognition.face_locations(image)

print("found {}".format(len(face_locations)))
i=0

for face_location in face_locations:
	top,right,bottom,left = face_location
	print("Top: {},Left: {}, Bottom: {},Right: {}".format(top,left,bottom,right))

	face_image = image[top:bottom, left:right]
	pil_image = Image.fromarray(face_image)
	pil_image.save("face-{}.jpg".format(i))
	i = i+1
