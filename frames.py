import imageio
from upload import sendImages 
import binascii
from pydub import AudioSegment
from splice import splice

filename = 'Basket.m4v'
vid = imageio.get_reader(filename,  'ffmpeg')
length =  vid.get_length()
fps = vid.get_meta_data()['fps']
images = []
for num in range(0, length, int(5*fps)):
    images.append(imageio.core.util.asarray(vid.get_data(num)))

images_bytes = []
for i in range(len(images)):
    file_name = "temp/" + str(i) 
    images_bytes.append(imageio.imwrite(imageio.RETURN_BYTES, images[i], "jpg"))


base64 = []
for image in images_bytes:
	base64.append(binascii.b2a_base64(image))

r = sendImages(base64)

print('--'*48)
# the below is a list of n maps of labeled concepts and probabilities
# for m images.
concept_counts = {}
for image in r['outputs']:
	concepts = (image['data']['concepts'])
	word = ''
	value = 0.0
	for concept in concepts:
		#print(concept['id'], concept['value'])
		if concept['value'] > value:
			value = concept['value']
			word = concept['id']
	concept_counts[word] = concept_counts.get(word, 0) + 1
	#print (concept_counts[word])
print concept_counts

def argmax(concept_counts):
	return max(concept_counts.iterkeys(), key=(lambda key: concept_counts[key]))

if(argmax(concept_counts) == 'action'):
	song = AudioSegment.from_mp3("songs/Action1.mp3")
elif(argmax(concept_counts) == 'happy'):
	song = AudioSegment.from_mp3("songs/Happy1.mp3")
elif(argmax(concept_counts) == 'sad'):
	song = AudioSegment.from_mp3("songs/Sad2.mp3")
elif(argmax(concept_counts) == 'calm'):
	song = AudioSegment.from_mp3("songs/Calm1.mp3")

vidLen = int(length/fps)
songLen = int(song.duration_seconds)
vidSong = song

while(songLen < vidLen):
	vidSong += song
	songLen = int(vidSong.duration_seconds)

if(songLen >= vidLen):
	vidSong = vidSong[:vidLen*1000]

vidSong.export('temp.mp3', format="mp3")
splice(filename, "temp.mp3", 'output.mp4')

