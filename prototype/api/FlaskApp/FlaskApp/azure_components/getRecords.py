import pydocumentdb.document_client as document_client
from static.app_keys import db_client, db_client_key, db_name, db_collection

def getRecords(user, lastID, direction, tags):

    dir = ">";
    order = "ASC";

    if direction == True:
        dir = "<";
        order = "DESC";

    tagString = "[\""+'", "'.join(tags)+"\"]";
    client = document_client.DocumentClient(db_client, {'masterKey': db_client_key});
    #Not sure we need this. Client may be it.
    #db = next((data for data in client.ReadDatabases() if data['id'] == db_name));
    #coll = next((coll for coll in client.ReadCollections(db['_self']) if coll['id'] == db_collection));
    
    queryString = 'SELECT TOP 20 '+ db_collection +'.user_id, '+ db_collection +'.photo_id, '+ \
                    db_collection +'.file_name, '+ db_collection +'.photo_url, '+ db_collection + \
                    '.tags FROM '+ db_collection +' WHERE '+ db_collection +'.user_id = "' \
                    + user + '" AND ' + db_collection + '.photo_id ' + dir + ' ' + lastID

    if len(tags) > 0:
        for taG in tags:
            #queryString += ' AND '
            queryString += ' AND ARRAY_CONTAINS(' + db_collection + '.tags ,"' + taG + '")'

    queryString += ' ORDER BY '+ db_collection +'.photo_id '+ order
    
    print(queryString)

    itterResult =  client.QueryCollections(db_client, queryString);

    print(itterResult._client)

#    for e in itterResult:
#        print(e)

    #print(itterResult);
    #sorted(itterResult, key="photo_id");
    #jsnOb = flask.jsonify(**itterResult);

    #if(direction == True):
        #return sorted(jsnOb, key="photo_id")
    #print(itterResult)
    #return itterResult

def main():
    fun = getRecords('testuser2','00000000', False, ["blah", "blah2", "blah3"])
    #fun2 = list(fun)
    #print(fun.next(fun))
    #for k in fun:
        #print(k)
# call main
if __name__ == "__main__":
    main()
