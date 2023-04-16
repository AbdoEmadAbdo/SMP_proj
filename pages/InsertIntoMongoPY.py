# first : pip install pymongo , -m pip install "pymongo[srv]"

from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost' ,27017)
client = MongoClient('mongodb://localhost:27017')
db = client.FTKP_DB
Login = db.Login  # Login is the Collection     The Document is {email}  
email = { "name":"Python AEA" ,"Content":"this is the Connection" ,"eng": "Abdo"}
result = Login.insert_one(email)   # as a result    put  {email}  inside the collection

print('User Login email: {0}'.format(result.inserted_id))

#After Run:
#? We will see the FTKP_DB db.  is Added to our MongoDb and comtaining Document Login    , Login  contain  the  {email}  which we added

