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

sendImages(base64)
