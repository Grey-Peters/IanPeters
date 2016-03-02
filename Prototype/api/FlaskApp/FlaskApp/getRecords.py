def getRecords(user, lastID, direction, tags)

	dir = ">";
	order = "ASC";

	if direction == True:
		dir = "<";
		order = "DESC";
	
	tagString = "[\""+'", "'.join(tags)+"\"]";
	
	queryString = 'SELECT TOP 20 '+collectionName+'.user_id, '+collectionName+'.photo_id, '+collectionName+'.file_name, '+collectionName+'.photo_url, '+collectionName+'.tags FROM '+collectionName+' where '+collectionName+'.user_id = ".'+user+'" and '+collectionName+'.tags = '+tagString+' ORDER BY '+collectionName+'.photo_id '+order+';';
	
	itterResult =  QueryDocuments(collection_link, queryString);
	
	sorted(itterResult, key="photo_id");
	
	jsnOb = flask.jsonify(**itterResult);
	
	if(direction == True){
		return sorted(jsnOb, key="photo_id")
	}
	return jsnOb;