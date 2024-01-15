#!/usr/bin/env python3
import re
import sys
import subprocess


def find_num_routes(ttl):
    known_ttls = {
        "Linux": 64,
        "Microsoft": 128,
        "Equipment": 255
    }

    os = ""
    min_hops = 256
    for key, val in known_ttls.items():
        hops = val - ttl
        if hops > 0 and hops < min_hops:
            min_hops = hops
            os = key

    return (os, min_hops)


if __name__ == "__main__":
    ip = sys.argv[1]

    ping_sub = subprocess.run(["ping", "-c", "1", ip], capture_output=True)
    ping_out = ping_sub.stdout.decode("ascii")
    if ping_sub.returncode != 0:
        print(f"Falha ao executar: ping {ip}")
        exit(1)
    
    ttl_pattern = re.compile(r'ttl=([0-9]+)')
    match = ttl_pattern.search(ping_out)

    if match:
        ttl_value = match.group(1)
        print(f"TTL: {ttl_value}")

        (os, hops) = find_num_routes(int(ttl_value))
        print(f"Sistema: {os}, numero de saltos: {hops}") 
    else:
        print("Falha ao extrair TTL")
        exit(1)
