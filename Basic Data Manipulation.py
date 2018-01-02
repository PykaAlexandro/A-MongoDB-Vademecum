from pymongo import MongoClient 
client = MongoClient('localhost:27017')
db = client.examples
#importing the databases in the folder examples as db via the client at 27017

Genova = {"name" : "Genova",
          "state" : "Italy",
          "region" : "Liguria",
          "province" : "Genova",
          "position" : "seaside",
          "population" : 600000}
#creating the Genova document

db.cities.insert(Genova)
#inserting the document into the database cities

Liguria = { "Genova" : {"name" : "Genova",
                      "state" : "Italy",
                      "region" : "Liguria",
                      "province" : "Genova",
                      "position" : "seaside",
                      "population" : 594733},
            "Imperia" : {"name" : "Imperia",
                      "state" : "Italy",
                      "region" : "Liguria",
                      "province" : "Imperia",
                      "position" : "seaside",
                      "population" : 42241}
            }
#creating the Liguria document
            
for a in Liguria:
    db.cities.insert(a)
#to insert the document
    
num_cities = db.cities.find().count()
print(num_cities)
#to know the number of cities

for a in db.cities.find():
    print(a)
#printing out all of the cities database
    
def update():
    city = db.cities.find_one({"name" : "Genova"})
    city["climate"] = "Mediterranean"
    db.cities.save(city)
#to update a document with a new field
    
db.cities.update({"name" : "Genova"}, {"$set" : {"climate" : "Mediterranean"}})
#with the update method and the set operator (unset would delete the field)
    
db.cities.update({"position" : "seaside"}, {"$set" : {"climate" : "Mediterranean"}}, multi = True)
#to perform a mass update for a certain criteria

db.cities.remove()
#if we want to remove all the documents from the collection

db.cities.drop()
#a more efficient way to remove all the collection and all the data associated with it

db.cities.remove({"name" : "Genova"})
#to remove a document matching the chosen criteria

db.cities.remove({"name" : {"$exists" : 0}})
#to remove multiple documents (the ones with a specific field missing)