#!/usr/bin/env python3
#
# Usage: task07.py LOG_FILEPATH [USER]
#
# Example:
# $ task07.py secure-ssh.log
# LOGIN               FAILURES SUCCESS  
# teste                   49         0
# invalid              15218         0
# root                  4724         0
# wesley                   5         0
# bruno                   11         0
# jefferson                4         0
# lee                      7         0
# postgres               233         0
# hadoop                  71         0
# zabbix                  39         0
# carlos                  15         0
# mysql                  107         0
# celia                    3         0
# operator                20         0
# sandro                   7         0
# conta10                  1         5
# ftp                     42         0
# nginx                   14         0
# conta16                  1         9
# conta28                  0         1
# backuppc                 3         0
# raXX6561                 0         1
# apache                   6         0
# leandro                  3         0
# joao                     6         0
# raXX1882                 0        12
# eduardo                  2         0
# jose                     8         0
# william                 11         2
# raXX9781                 2         1
# adm                      5         0
# conta36                  1        12
# conta01                  7        17
# conta24                  0         5
# conta06                  3        12
# christian                9         0
# ceph                     5         0
# conta20                  0        12
# mail                     6         0
# paulo                    4         0
# conta33                  0         2
# deluge                   5         0
# luciano                  2         0
# beatriz                  2         0
# lucas                   12         0
# bin                     11         0
# daemon                   3         0
# cecilia                  3         0
# games                    2         0
# silvia                   3         0
# arthur                   3         0
# openvpn                  6         0
# andre                    4         3
# leonardo                 3         0
# danielk                  3         2
# raXX0217                 0         1
# natalia                  3         0
# raXX2466                 0         3
# raXX5431                 0         1
# conta05                  1         3
# raXX5643                 3         0
# nobody                   2         0
# sshd                     1         0
# isaac                    4         0
# conta29                  0         1
# raXX4864                 0         1
# mosquitto                1         0
# mauricio                 1         0
# conta31                  0         1
# conta25                  0         1
# raXX2883                 0         1
# raXX5974                 1         2
#
# Example:
# $ task07.py secure-ssh.log william
# Number of failures: 11
# Failed IPs: ['103.84.71.58', '112.161.42.192', '218.75.121.74', '82.65.143.234', '118.89.241.214', '103.16.202.187', '138.197.171.79', '193.227.16.160', '83.234.50.32', '129.146.171.142', '109.207.69.219']
# 
# Number of succeess: 2
# Success IPs: ['143.106.7.154', '143.106.16.163']
# ------------------------------------------------------------------------------
import re
import sys


def retrieve_user(logentry):
    pattern = r"[Accepted|Failed] password for ([\w]+)"
    match = re.search(pattern, logentry)
    return match.group(1)


def retrieve_ip(logentry):
    pattern = r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})"
    match = re.search(pattern, logentry)
    return match.group(1)


def login_has_failed(logentry):
    return "Failed password" in logentry

    
def login_has_succeeded(logentry):
    return "Accepted password" in logentry


def register_ip(ip_list, ip):
    """
    Prevent inserting repeated IPs.
    """
    if ip in ip_list:
        return
    ip_list.append(ip)


def register_attempt(login_attempts, user, ip, has_failed):
    """
    Prevent inserting repeated login.
    This function will register counting and IP for each login user.
    """
    if user not in login_attempts:
        login_attempts[user] = {
            "failed": 0,
            "failed_ips": [],
            "succeeded": 0,
            "succeeded_ips": []
        }

    if  has_failed:
        login_attempts[user]["failed"] += 1
        register_ip(login_attempts[user]["failed_ips"], ip)
    else:
        login_attempts[user]["succeeded"] += 1
        register_ip(login_attempts[user]["succeeded_ips"], ip)


def parse_logs(logfile):
    login_attempts = {}

    for logentry in logfile:
        if login_has_failed(logentry):
            user = retrieve_user(logentry)
            ip = retrieve_ip(logentry)
            register_attempt(login_attempts, user, ip, True)
        elif login_has_succeeded(logentry):
            user = retrieve_user(logentry)
            ip = retrieve_ip(logentry)
            register_attempt(login_attempts, user, ip, False)

    return login_attempts


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} LOG_FILEPATH")
        exit(1)

    try:
        logfile = open(sys.argv[1], "r")
        login_attempts = parse_logs(logfile)

        if len(sys.argv) < 3:
            # Print all login attemps with count of failures and success
            print("{:20}{:5} {:9}".format("LOGIN", "FAILURES", "SUCCESS"))
            for login, ldata in login_attempts.items():
                print(f"{login:20} {ldata['failed']:5} {ldata['succeeded']:9}")
        else:
            # Filter specific user
            user = sys.argv[2]
            if user not in login_attempts:
                print(f"Could not find login attempt for user: {user}")
                exit(1)
            
            user_ldata = login_attempts[user]
            print(f"Number of failures: {user_ldata['failed']}")
            print(f"Failed IPs: {user_ldata['failed_ips']}")
            print("")
            print(f"Number of succeess: {user_ldata['succeeded']}")
            print(f"Success IPs: {user_ldata['succeeded_ips']}")
    except Exception as e:
        print(f"Failed to read log file {sys.argv[1]}")
        print(e)
        exit(1)
