Python 3.3.2 (v3.3.2:d047928ae3f6, May 16 2013, 00:06:53) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
from forms import VoteForm
import config
import pydocumentdb.document_client as document_client
	

#Need a function specifically oriented toward making the call.
#This is *not* async, which will need to change.
#Ideally, after this is complete, we'd send the confirmation to the UI that the upload completed.
def makeMetadata(date, url)

	client = document_client.DocumentClient(config.DOCUMENTDB_HOST, {'masterKey': config.DOCUMENTDB_KEY});
	
	db = next((data for data in client.ReadDatabases() if data['id'] == config.DOCUMENTDB_DATABASE));
	
	coll = next((coll for coll in client.ReadCollections(db['_self']) if coll['id'] == config.DOCUMENTDB_COLLECTION));

	document = client.CreateDocument(coll['_self'],
			{   "photo_url": url,
				"photo_id": date,
				"user_id": user,
				"file_name": originalFilename,
				"tag": tags,
			});
			
	#this is not the intended end result.
	return;
