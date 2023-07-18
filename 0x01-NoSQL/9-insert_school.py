#!/usr/bin/env python3
"""
Function to insert a new document in a collection in MongoDB
"""


def insert_school(mongo_collection, **kwargs):
    """
    Returns the _id of new document inserted in a collection
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
