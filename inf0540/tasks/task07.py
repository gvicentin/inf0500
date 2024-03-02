#!/usr/bin/env python3
#
# Usage: task07.py LOG_FILEPATH
#
# ------------------------------------------------------------------------------
import re
import sys


def retrieve_user(logentry):
    pattern = r"[Accepted|Failed] password for ([\w]+)"
    match = re.search(pattern, logentry)
    return match.group(1)


def retrieve_ip(logentry):
    pattern = r"([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})\\.([0-9]{1,3})"
    match = re.search(pattern, logentry)
    return match.group(1)


def login_has_failed(logentry):
    return "Failed password" in logentry

    
def login_has_succeeded(logentry):
    return "Accepted password" in logentry


def register_attempt(user, ip, has_failed):
    if not has_failed:
        print(f"Success attempt: user: {user}, ip: {ip}")


def parse_logs(logfile):
    login_attemps = {}
    total_failures = 0
    total_success = 0

    for logentry in logfile:
        if login_has_failed(logentry):
            total_failures += 1
        elif login_has_succeeded(logentry):
            total_success += 1
            user = retrieve_user(logentry)
            ip = retrieve_ip(logentry)
            register_attemp(user, ip, False)

    print(f"Total Failures: {total_failures}")
    print(f"Total Success: {total_success}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} LOG_FILEPATH")
        exit(1)

    logfile = open(sys.argv[1], "r")
    parse_logs(logfile)
