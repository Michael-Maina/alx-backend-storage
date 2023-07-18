#!/usr/bin/env python3
"""
Function to update a document in a collection in MongoDB
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name
    """
    name_to_update = {"name": name}
    new_topics = {"$set": {"topics": topics}}
    mongo_collection.update_one(name_to_update, new_topics)
