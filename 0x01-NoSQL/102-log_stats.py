#!/usr/bin/env python3
"""
Function to count documents fitting certain criteria in a collection in MongoDB
"""
from pymongo import MongoClient


def main():
    """
    Prints count values of documents fitting certain criteria
    """
    client = MongoClient("mongodb://localhost:27017")
    nginx = client.logs.nginx

    total = nginx.count_documents({})
    print("{} logs".format(total))

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("Methods:")
    for method in methods:
        count = nginx.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status = nginx.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status))

    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    ips = list(nginx.aggregate(pipeline))
    print("IPs:")
    for ip in ips:
        print("\t{}: {}"
              .format(ip.get('_id'), ip.get('count')))


if __name__ == '__main__':
    main()
