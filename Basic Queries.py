from pymongo import MongoClient 
client = MongoClient('localhost:27017')
db = client.examples
#importing the databases in the folder examples as db via the client at 27017

def single_argument_query():
    query = db.cities.find({"region" : "Liguria"})
    for a in query:
        print(a)
#to return all the cities of Liguria
        
db.cities.find_one({"region" : "Liguria"})
#here it returns the first instance that satisfies the query
        
def multiple_argument_query():
    query = db.cities.find({"region" : "Liguria", "position" : "seaside"})
    for a in query:
        print(a)
#for returning all the regional cities with access to the sea
        
def projection_query():
    query = {"region" : "Liguria", "position" : "seaside"}
    projection = {"_id" : 0, "name" : 1}
    autos = db.autos.find(query, projection)
    for a in autos:
        print(a)
#if we want to return just the name of the city and not all the fields

def num_operator_query():
    query = {"population" : {"$gt" : 200000, "$let" : 600000}}
    cities = db.cities.find(query)
    num_cities = 0
    for c in cities:
        print(c)
        num_cities += 1
    print('\nNumber of Cities Matching: %d\n' %num_cities )     
#querying for mid-sized cities, returning a list and the total count
    
def char_operator_query():
    query = {"name" : {"$gt" : "D", "$let" : "G"}}
    cities = db.cities.find(query)
    num_cities = 0
    for c in cities:
        print(c)
        num_cities += 1
    print('\nNumber of Cities Matching: %d\n' %num_cities )     
#querying for cities' name starting with specific letters, returning a list and the total count
    
def ne_operator_query():
    query = {"state" : {"$ne" : "Italy"}}
    cities = db.cities.find(query)
    num_cities = 0
    for c in cities:
        print(c)
        num_cities += 1
    print('\nNumber of Cities Matching: %d\n' %num_cities )     
#querying for non Italian cities, returning a list and the total count
    
db.cities.find({"province" : {"$exists" : 1}})
#to list the cities that have a province field

db.cities.find({"province" : {"$regex" : "[Li]"}})
#to find cities with the province's name starting with Li

db.cities.find({"state" : {"$in" : ["Germany", "United Kingdom", "Japan"]}})
#if we want to look for cities matching any values in a scalar array of choice

db.cities.find({"province" : {"$regex" : "[Li]"}, "state" : {"$in" : ["Germany", "United Kingdom", "Japan"]}})
#using a composite query

db.cities.find({"position" : {"$all" : ["seaside", "hillside"]}})
#here the cities must match either condition

db.cities.find({"population.unemployed" : {"$gt" : 0.05}}).count()
#♣in case of subfields, returning the total count