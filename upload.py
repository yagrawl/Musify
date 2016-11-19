from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as CImage
import requests

def sendImages(rawArray):
	payload = {'client_id':'gRuqdodmCNn8v8dNM-52YJVsqJF40JYaFxCBqhkW', 'client_secret':'EitsVNoFsVlG6zwur3HBxZ65TzP9aEvGVfuyX-58', 'grant_type':'client_credentials'}
	#r = requests.post("https://api.clarifai.com/v1/token/", data=payload)
#print(r.text)

	app = ClarifaiApp(app_id=payload['client_id'], app_secret=payload['client_secret'])
	model = app.models.get('Classify')
	#image = app.inputs.create_image_from_filename(argv[1])
	#image = app.inputs.create_image_from_url(url='https://samples.clarifai.com/puppy.jpeg',allow_duplicate_url=True)
	images = []
	for im in rawArray:
		images.append(CImage(base64=im))
	return model.predict(images)
			
						
