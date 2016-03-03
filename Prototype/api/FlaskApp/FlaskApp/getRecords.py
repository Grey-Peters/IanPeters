import pydocumentdb.document_client as document_client
from static.app_keys import db_client, db_client_key, db_name, db_collection

#helper method 
def extract_val(json):
	return int(json['photo_id'])

def getRecords(user, lastID, direction, tags)
	try:
		dir = ">";
		order = "ASC";

		if direction == True:
			dir = "<";
			order = "DESC";
		
		tagString = "[\""+'", "'.join(tags)+"\"]";
		
		client = document_client.DocumentClient(db_client, {'masterKey': db_client_key});

		db = next((data for data in client.ReadDatabases() if data['id'] == db_name));
		coll = next((coll for coll in client.ReadCollections(db['_self']) if coll['id'] == db_collection));
		
		queryString = 'SELECT TOP 20 '+db_collection+'.user_id, '+db_collection+'.photo_id, '+db_collection+'.file_name, '+db_collection+'.photo_url, '+db_collection+'.tags FROM '+db_collection+' where '+db_collection+'.user_id = "'+user+'" and '+db_collection+'.tags = '+tagString+' and '+db_collection+'.photo_id'+dir+lastID+' ORDER BY '+db_collection+'.photo_id '+order+';';
		
		itterResult =  QueryDocuments(coll, queryString);
		
		jsnOb = flask.jsonify(**itterResult);
		
		if(direction == True){
			return sorted(jsnOb, key=extract_val(jsnOb), reverse=True);
		}
		return jsnOb;
	except Exception:
        return "error";