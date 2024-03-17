#!/bin/env python3

import re
import sys
from neo4j import GraphDatabase

NEO4J_URI = 'neo4j://localhost:7687'
NEO4J_DRIVER = GraphDatabase.driver(NEO4J_URI, auth=("neo4j", "admin@admin"),
                                    max_connection_lifetime=1000)


def create_router_if_not_exist(nsession, gateway_ip):
    query = f"MATCH (r:Router {{ip: '{gateway_ip}'}}) RETURN r;"
    res = nsession.run(query)
    if (len(res.value()) == 0):
        query = f"CREATE (r:Router {{ip: '{gateway_ip}'}});"
        nsession.run(query)


def create_route_if_not_exist(nsession, dest_ip):
    query = (
        "MATCH p=(o:Router {ip: 'origin'})-[r:ROUTE]->(d:Router "
        f"{{ip: '{dest_ip}'}}) RETURN p;"
    )
    res = nsession.run(query)
    if (len(res.value()) == 0):
        query = (
            f"MATCH (o:Router {{ip: 'origin'}}) MATCH (d:Router {{ip: '{dest_ip}'}})"
            "CREATE (o)-[route:ROUTE]->(d) RETURN ID (route);"
        )
        nsession.run(query)


def create_cidr_if_not_exist(nsession, dest_cidr):
    query = f"MATCH (c:Cidr {{cidr: '{dest_cidr}'}}) RETURN c;"
    res = nsession.run(query)
    if (len(res.value()) == 0):
        query = f"CREATE (c:Cidr {{cidr: '{dest_cidr}'}});"
        nsession.run(query)


def create_cidr_route_if_not_exist(nsession, src_ip, dest_cidr):
    query = (
        "MATCH p=(o:Router {ip: 'src_ip'})-[r:ROUTE]->(c:Cidr "
        f"{{cidr: '{dest_cidr}'}}) RETURN p;"
    )
    res = nsession.run(query)
    if (len(res.value()) == 0):
        query = (
            f"MATCH (o:Router {{ip: '{src_ip}'}}) MATCH (c:Cidr {{cidr: "
            f"'{dest_cidr}'}}) CREATE (o)-[route:ROUTE]->(c) RETURN ID (route);"
        )
        nsession.run(query)


def parse_routes(rfile, nsession):
    pattern = (
        r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/[0-9]{1,2})"
        r"\s+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})"
    )
    for route in rfile:
        match = re.search(pattern, route)
        if match:
            cidr = match.group(1)
            gateway = match.group(2)
            create_router_if_not_exist(nsession, gateway)
            create_route_if_not_exist(nsession, gateway)
            create_cidr_if_not_exist(nsession, cidr)
            create_cidr_route_if_not_exist(nsession, gateway, cidr)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} ROUTES_FILEPATH")
        exit(1)

    try:
        rfile = open(sys.argv[1], "r")
        nsession = NEO4J_DRIVER.session()

        # create origin and other routes
        query = "CREATE(r:Router {ip: 'origin'});"
        nsession.run(query)
        parse_routes(rfile, nsession)

    except Exception as e:
        print(f"Failed to read log file {sys.argv[1]}")
        print(e)
        exit(1)
