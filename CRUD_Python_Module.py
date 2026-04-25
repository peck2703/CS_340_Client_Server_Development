# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, USER, PASS): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'SNHU1234' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
    def get_next_rec_number(self):
        #Get current count of documents
        current_count = self.collection.count_documents({})
        
        #Increment and return the new count
        return current_count + 1
    
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            data['rec_num'] = self.get_next_rec_number()
            
            self.collection.insert_one(data)  # data should be dictionary 
            return True
        else: 
            raise Exception("Nothing to save, because data parameter is empty")
            return False

    # Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            #return all records but leave out _id, as it is not needed for display
            cursor = self.collection.find(query, {"_id": False})
            
            #Return a list of objects
            return list(cursor)
        else:
            #list is empty, return an empty list
            return []
    def update(self, query, data):
        if query is not None:
            #update all records that match the given query
            result = self.collection.update_many(query, {"$set": data})
            
            #output the number of rows that were modified
            print(f"Rows modified: {result.modified_count}")
            
            return result.modified_count
        else:
            #nothing is updated
            return 0
            
    def delete(self, query):
        if query is not None:
            #perform a delete_many of all records in query
            result = self.collection.delete_many(query)
            
            #output the number of rows that were removed
            print(f"Rows Deleted: {result.deleted_count}")
            
            #return the list of deleted records
            return result.deleted_count
        else:
            print("No query provided. Zero records deleted.")
            return result.deleted_count
            
            