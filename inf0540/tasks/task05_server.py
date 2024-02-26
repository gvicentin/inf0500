#!/usr/bin/env python3
#
# Usage: task05_server.py -p PORT [-tcp|-udp]
#
# Example (using TCP)
# $ task05_server.py -p 3000 -tcp
#
# Example (using UDP)
# $ task05_server.py -p 3000 -udp
# ------------------------------------------------------------------------------
import argparse
import socket
import dns.resolver as res


def resolve_dns(host):
    result = []
    for r in res.resolve(host):
        result.append(r.to_text())
    return result


def tcp_server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", port))
    s.listen()
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        host = data.decode()
        result = resolve_dns(host)
        print(f"Received data: {host}")
        print(f"Sending result: {result}")
        conn.sendall(str.encode(" ".join(result)))


def udp_server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("0.0.0.0", port))
    while True:
        data, addr = s.recvfrom(1024)
        if not data:
            break
        host = data.decode()
        result = resolve_dns(host)
        print(f"Received: {host}, from {addr}")
        print(f"Sending result: {result}")
        s.sendto(str.encode(" ".join(result)), addr)
        return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Task05 Client")
    parser.add_argument('-p', '--port', type=int, help='Server port number', required=True)
    parser.add_argument('-tcp', action='store_true', help='Use TCP protocol')
    parser.add_argument('-udp', action='store_true', help='Use UDP protocol')

    args = parser.parse_args()

    if args.udp:
        print("UDP server")
        udp_server(args.port)
    else:
        print("TCP server")
        tcp_server(args.port)
