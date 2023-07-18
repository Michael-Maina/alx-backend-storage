#!/usr/bin/env python3
"""
Function to find documents in a collection in MongoDB
"""


def schools_by_topic(mongo_collection, topics):
    """
    Returns a list of school documents having a specific topic
    """
    return mongo_collection.find({"topics": topics})
