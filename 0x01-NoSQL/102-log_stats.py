#!/usr/bin/env python3
"""
Function to count documents fitting certain criteria in a collection in MongoDB
"""
from pymongo import MongoClient
from bson.son import SON


def main():
    """
    Prints count values of documents fitting certain criteria
    """
    client = MongoClient("mongodb://localhost:27017")
    nginx = client.logs.nginx

    total = nginx.count_documents({})
    get = nginx.count_documents({"method": "GET"})
    post = nginx.count_documents({"method": "POST"})
    put = nginx.count_documents({"method": "PUT"})
    patch = nginx.count_documents({"method": "PATCH"})
    delete = nginx.count_documents({"method": "DELETE"})
    status = nginx.count_documents({"method": "GET", "path": "/status"})

    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": SON([("count", -1)])}
    ]

    print("""\
{} logs
Methods:
\tmethod GET: {}
\tmethod POST: {}
\tmethod PUT: {}
\tmethod PATCH: {}
\tmethod DELETE: {}
{} status check\
"""
          .format(total, get, post, put, patch, delete, status))

    ips = list(nginx.aggregate(pipeline))
    print("IPs:")
    for i in range(10):
        print("\t{}: {}"
              .format(ips[i].get('_id'), ips[i].get('count')))


if __name__ == '__main__':
    main()
