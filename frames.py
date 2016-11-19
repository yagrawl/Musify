import imageio
from upload import sendImages 
import binascii

filename = 'IDShots.mp4'
vid = imageio.get_reader(filename,  'ffmpeg')
length =  vid.get_length()
fps = vid.get_meta_data()['fps']
images = []
for num in range(0, length, int(10*fps)):
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
	print (concept_counts[word])
print concept_counts
			
