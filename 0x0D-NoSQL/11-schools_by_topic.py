#!/usr/bin/env python3
""" Where can I learn Python?"""

def schools_by_topic(mongo_collection, topic):
    """ function that returns the list of school 
    having a specific topic: """
    documents = mongo_collection.find({"topics": topic})
    list_docs = [d for d in documents]
    return list_docs