import socket
import os
from datetime import datetime

hosts_number = int(os.getenv("HOSTS_NUMBER", 81))
server_list = []
for i in range(0, hosts_number + 1):
    server_list.append(f"host-{i}")

while True:
    for host_name in server_list:
        now = datetime.now().strftime("%H:%M:%S.%f")
        try:
            s = socket.create_connection((host_name, 22), timeout=1)
            print(f"{now} create_connection {host_name} opened")
        except socket.timeout as sock_timeout:
            print(f"create_connection {host_name} timeout")
        except socket.error as sock_error:
            print(f"create_connection {host_name} error")
        else:
            # s.shutdown(socket.SHUT_RDWR) # remove immediately
            # print(f"{now} closing connection {host_name} now closed")
            s.close()
