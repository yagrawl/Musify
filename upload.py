from clarifai.rest import ClarifaiApp
import requests

def sendImages(rawArray):
	payload = {'client_id':'HayIsw2teQjYnJt-JnUA2v9Ue4B1qePMufhj6_m6', 'client_secret':'bON_Lt_z6pS5mOA4E4deBs0zq71Xn324VxW8lq1E', 'grant_type':'client_credentials'}
	#r = requests.post("https://api.clarifai.com/v1/token/", data=payload)
#print(r.text)

	app = ClarifaiApp(app_id=payload['client_id'], app_secret=payload['client_secret'])
	model = app.models.get('Classify')
	#image = app.inputs.create_image_from_filename(argv[1])
	#image = app.inputs.create_image_from_url(url='https://samples.clarifai.com/puppy.jpeg',allow_duplicate_url=True)
	for im in rawArray():
		image = app.inputs.create_image_from_bytes(im ,allow_duplicate_url=True)
	r = model.predict([image])
	print('--'*48)
	# the below is a list of n maps of labeled concepts and probabilities
	# for m images.
	for image in r['outputs']:
		concepts = (image['data']['concepts'])
		for concept in concepts:
			print(concept['id'], concept['value'])
