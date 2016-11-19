import matplotlib.pyplot as plt
import imageio
filename = 'IDShots.mp4'
vid = imageio.get_reader(filename,  'ffmpeg')
length =  vid.get_length()
print vid.get_meta_data().fps
# for num in range(0, length, 5*30):
#     image = vid.get_data(num)
#     fig = plt.figure()
#     #fig.suptitle('image #{}'.format(num), fontsize=20)
#     plt.imshow(image)
# plt.show()