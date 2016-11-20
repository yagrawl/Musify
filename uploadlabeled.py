from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as CImage
import requests

payload = {'client_id':'IPrJFqHURndkFxHoJmlSantt4WXPEh2lwTkWTxO_', 'client_secret':'b3kT3CsZgGB5YYROAJ7qgsR696tY255tCFj6hicF', 'grant_type':'client_credentials'}
#r = requests.post("https://api.clarifai.com/v1/token/", data=payload)
#print(r.text)
app = ClarifaiApp(app_id=payload['client_id'], app_secret=payload['client_secret'], quiet=True)
images = []
for i in range(83):
	try:
		with open('pics/action' + str(i), 'r') as f:
			a = 1
		f = 'pics/action' + str(i)
		images.append(CImage(filename=f, concepts=['action']))
	except IOError:
		continue 
			
app.inputs.bulk_create_images(images)
			
						
