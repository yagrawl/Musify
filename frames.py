import imageio
from upload import sendImages 
import binascii
from pydub import AudioSegment
from splice import splice
import sys
def analyze(infile, outfile): 
	filename =  
	vid = imageio.get_reader(filename,  'ffmpeg')
	length =  vid.get_length()
	fps = vid.get_meta_data()['fps']
	images = []
	for num in range(0, length, int(5*fps)):
		try:
			frame = vid.get_data(num)
			images.append(imageio.core.util.asarray(frame))
		except RuntimeError:
		print('bad frame')


	images_bytes = []
	for i in range(len(images)):
		file_name = "temp/" + str(i) 
		images_bytes.append(imageio.imwrite(imageio.RETURN_BYTES, images[i], "jpg"))


	base64 = []
	for image in images_bytes:
		base64.append(binascii.b2a_base64(image))
	rs = []
	for i in range(0,len(base64), 128):
		if len(base64) - i < 128:
			rs += sendImages(base64[i:])
		else:
			rs += sendImages(base64[i:i+128])

	print('--'*48)
	# the below is a list of n maps of labeled concepts and probabilities
	# for m images.
	word_counts = {}
	concept_counts = {}
	for r in rs:
		for image in r['outputs']:
			concepts = (image['data']['concepts'])
			word = ''
			value = 0.0
			for concept in concepts:
				#print(concept['id'], concept['value'])
				if concept['value'] > value:
					value = concept['value']
					word = concept['id']
				word_counts[concept['id']] = word_counts.get(concept['id'], 0) + concept['value']
			concept_counts[word] = concept_counts.get(word, 0) + 1
			#print (concept_counts[word])
	print concept_counts




	def argmax(concept_counts):
		return max(concept_counts.iterkeys(), key=(lambda key: concept_counts[key]))
	mx = argmax(concept_counts)
	#from word counts, determine if we want double words
	if(mx == 'action'):
		songf = ("songs/AA.mp3")
	elif(mx == 'happy'):
		songf = ("songs/HH.mp3")
	elif(mx == 'sad'):
		songf = ("songs/SS.mp3")
	elif(mx == 'calm'):
		songf = ("songs/CC.mp3")
	other = ''
	if(mx == 'sad' or mx == 'happy'):
		ratio = word_counts['calm']/word_counts['action']
		if ratio > 2:
			songf[6] = 'C'
		elif 1/ratio > 2:
			songf[6] = 'A'
	else:
		ratio = word_counts['sad']/word_counts['happy']
		if ratio > 2:
			songf[7] = 'S'
		elif 1/ratio > 2:
			songf[7] = 'H'
			
	print(songf)
	song = AudioSegment.from_mp3(songf)

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

def main():
	analyze(sys.argv[1], sys.argv[2])
if __name__ == '__main__':
	main()