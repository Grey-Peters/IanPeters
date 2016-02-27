def getRecords(user, lastID, direction, tags)

	var dir = ">";
	order = "ASCENDING";

	if direction == "back":
		dir = "<";
		order = "DESCENDING";

	var queryString = "Select TOP 20 file_name, photo_url, photo_id, tags from ".DBname." Where photo_id".dir.lastID." and tags = ".tags." ORDER BY ".order";";
	
	itterResult =  QueryDocuments(collection_link, queryString);