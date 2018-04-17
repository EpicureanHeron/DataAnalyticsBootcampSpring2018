# Query 1 - Creating dbs, inserting data and finding data
# -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-

# Start up a new database by switching to it.
# NOTE: The db does not exist until you create a collection.

# Show the current db by running db.

# Show current databases in existence

# Insert data into the travel_db database with this command.
# NOTE: This will create the collection automatically,
# ALSO, TAKE NOTE: the contents of the insert are basically a JS object,
# and include an array.

# As a class, come up with 3-5 more countries and
# insert them into the db using the same syntax as above.



# Observe where the data was entered in the MongoDB instance (in mongod)

# Find all data in a Collection with db.[COLLECTION_NAME].find()
# NOTE: the MongoDB _id was created automatically.
# This id is specific for each doc in the collection.

# Adding .pretty() makes the data more readable.

# Find specific data by matching a field.

# Try a few queries with the examples we came up with as a class.
# Also, pick something that will find more than one entry
# so we can see how it will return all matches.

# Find specific data by matching an _id.
# By id:

# Example: db.destinations.find({_id: ObjectId("5416fe1d94bcf86cd785439036")})
