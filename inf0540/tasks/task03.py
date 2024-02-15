#!/usr/bin/env python3
#
# Usage: task03.py URL
# ------------------------------------------------------------------------------
import sys
import httplib2
import subprocess
from urllib.parse import urlparse

def get_server_and_status(url):
    http = httplib2.Http()
    http_output = http.request(url)
    return (http_output[0]["server"], http_output[0]["status"])


def get_origin_country(url):
    parsed_uri = urlparse(url)
    fqdn = parsed_uri.netloc

    geoip = subprocess.run(["geoiplookup", fqdn], capture_output=True)
    geoip_out = geoip.stdout.decode("ascii")
    return geoip_out.split(':')[1].strip()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} URL")
        exit(1)

    url = sys.argv[1]
    (server, status) = get_server_and_status(url)
    origin_country = get_origin_country(url)

    print(f"Server system: {server}")
    print(f"HTTP status: {status}")
    print(f"Origin country: {origin_country}")
