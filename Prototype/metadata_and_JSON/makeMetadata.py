Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:06:53) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>
import pydocumentdb.document_client as document_client
import verify_oauth
import datetiem
from datetime import timedelta
	

#Need a function specifically oriented toward making the call.
#This is *not* async, which will need to change.
#Ideally, after this is complete, we'd send the confirmation to the UI that the upload completed.
def makeMetadata(user, originalFilename, tags, time, url, token, secret,)

	if verify_oauth(token, secret).status_code != 200:
		return returnList["Could not verify oAuth credentials"];

	epoc = datetime.datetime(2016, 2, 23, 3, 0, 00, 000000));
	val = (time - epoc).total_seconds()*1000000;
		
	client = document_client.DocumentClient(DOCUMENTDB_HOST, {'masterKey': DOCUMENTDB_KEY});
	
	#Not sure we need this. Client may be it.
	#db = next((data for data in client.ReadDatabases() if data['id'] == config.DOCUMENTDB_DATABASE));
	
	coll = next((coll for coll in client.ReadCollections(db['_self']) if coll['id'] == config.DOCUMENTDB_COLLECTION));

	#create document. Tags is an array, as passed.
	document = client.CreateDocument(coll['_self'],
			{   "user_id": user,
				"file_name": originalFilename,
				"photo_url": url,
				"photo_id": val,
				"tags": tags,
			});
	
	returnlist = [];	
	
	if uploaded:
		return returnList["Success", "File has been uploaded and added successfully."]
	else:
		return returnList["Failed to upload metadata to Azure DocumentDB"]
