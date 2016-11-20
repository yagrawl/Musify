Theme Song Generator is an application that classifies video clips in order to provide backgroud music which matches the mood and intensity of the video.

In order to run the code in this GitHub, the proper syntax is:
	python frames.py \<video-file\> \<output-file\> or python frames.py -u \<url-to-video\> \<output-file\> 
	
This code is meant to be used as server backend and requires a lot of dependencies to use. These dependencies are as follows:
python2.7(although a port to 3.5 would likely be simple)
python libraries:
imageio
binascii
pydub
pafy
clarifai(and a trained agent with credentials)
nonpython libraries:
ffmpeg

