import socketserver


class ClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(f"[+] Connection from {self.client_address}")
        while True:
            data = self.request.recv(1024).strip()
            if not data:
                break
            print(f"Received from {self.client_address}: {data.decode()}")
            self.request.sendall(b"Message received\n")


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999
    with socketserver.ThreadingTCPServer((HOST, PORT), ClientHandler) as server:
        print(f"Server started on {HOST}:{PORT}")
        server.serve_forever()
