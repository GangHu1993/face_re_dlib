import face_recognition
import cv2
import os
data_dir = './templetes'

face_dict = []
face_coding = []
for guy in os.listdir(data_dir):
	face_dict.append(guy.split('_')[0])
	img = face_recognition.load_image_file(data_dir+'/'+guy)
	face_coding.append(face_recognition.face_encodings(img)[0])


# Load a sample picture and learn how to recognize it.
#obama_image = face_recognition.load_image_file("45.jpg")
#obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

class Face_recon:
	def __init__(self):
		print ('init_____________________')
		self.frame_counter = 0
		self.predict = []
		self.bounding_boxex = []
		self.res = []

	def face_rec(self, frame):
		self.res = []
		#print (face_dict)
		# Resize frame of video to 1/4 size for faster face recognition processing
		small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
		# Find all the faces and face encodings in the current frame of video
		face_locations = face_recognition.face_locations(small_frame)
		face_encodings = face_recognition.face_encodings(small_frame, face_locations)
		face_names = []
		i = 0
		for face_encoding in face_encodings:
			res_dic = {}
			print ('for')
    		# See if the face is a match for the known face(s)
    			results = face_recognition.compare_faces(face_coding, face_encoding)
	    		name = 'Unknown'
    			for index in range(len(results)):
    				if (results[index] != 0):
    					name = face_dict[index]
	    		res_dic [name]= (face_locations[i][3]*2,face_locations[i][0]*2,face_locations[i][1]*2,face_locations[i][2]*2)
	    		self.res.append(res_dic)
			i = i+1
		print (self.res)
		return self.res
