import socket
import dns.resolver as res

HOST = "0.0.0.0"
PORT = 3000

def resolve_dns(host):
    result = []
    for r in res.resolve(host):
        result.append(r.to_text())
    return result


if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
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
