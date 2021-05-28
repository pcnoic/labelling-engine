from firebase_admin import firestore

####################
# Firestore Wrapper#
####################

class FirestoreWrapper:
    
    def get_collection(client, collection):
        col_ref = client.collection(collection)
        docs = col_ref.stream()
        data = []
        for doc in docs:
            data.append(doc.to_dict())
            
        return data 
        
    def get_collection_with_limit(client, collection, limit):
        col_ref = client.collection(collection)
        docs = col_ref.limit(limit).stream()
        data = []
        for doc in docs:
            data.append(doc.to_dict())        
        
        return data
    