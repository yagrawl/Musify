import matplotlib.pyplot as plt
import imageio
from upload import sendImages 

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


sendImages(images_bytes)