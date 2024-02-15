#!/usr/bin/env python3
#
# Usage: task04.py DOMAIN
#
# Example:
# $ ./task04.py ic.unicamp.br
# E-mail server taquaral.ic.unicamp.br., has ICMP: True
# E-mail server mx2.unicamp.br., has ICMP: True
# ------------------------------------------------------------------------------
import os
import sys
import dns.resolver as dns_res

def get_email_servers(domain):
    es = []
    res_out = dns_res.resolve(domain, "MX")
    for res in res_out:
        es.append(res.to_text().split(" ")[1])
    return es


def has_icmp(host):
    ping_code = os.system(f"ping -c 1 {host} >/dev/null")
    return ping_code == 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} DOMAIN")
        exit(1)

    es = get_email_servers(sys.argv[1])
    for server in es:
        icmp = has_icmp(server)
        print(f"E-mail server {server}, has ICMP: {icmp}")
