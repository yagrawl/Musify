import matplotlib.pyplot as plt
import imageio
filename = 'IDShots.mp4'
vid = imageio.get_reader(filename,  'ffmpeg')
length =  vid.get_length()
fps = vid.get_meta_data()['fps']
for num in range(0, length, int(10*fps)):
    image = vid.get_data(num)
    fig = plt.figure()
    plt.imshow(image)
plt.show()