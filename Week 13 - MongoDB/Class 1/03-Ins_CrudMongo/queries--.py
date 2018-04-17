# Update, Delete and Drop in MongoDB
# -/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-


# We insert two countries in Africa

# Show how to update data
# using db.[COLLECTION_NAME].update()

# Note that the above will only update the first entry it matches.

# To update multiple entries, you can add {multi:true}
# All countries listed as being in Africa will now show Antarctica as their continent

# Alternatively, we can use this syntax to update more than one record

# Ask the class what they think will happen when you run this command,
# even though a capital doesn't exist

# Answer: it will add the capital field to the document

# And show the field can now be updated with the same command


# Show how to push to an array with $push

# The upsert option updates a document if one exists; it otherwise creates a new document

# Show how to delete an entry with db.[COLLECTION_NAME].remove()

# Show how to empty a collection with db.[COLLECTION_NAME].remove()

# Show how to drop a collection with db.[COLLECTION_NAME].drop()

# Show how to drop a database
