import subprocess
SERVER_IP = ("85.155.124.78", "1.1.1.1", "8.8.8.8")

def ping_server():
    p1 = subprocess.run(["top","-b","-n1"], capture_output=True, text=True)
    return_code = p1.returncode == 0
    print(p1.stdout)
    return return_code
ping_server()
# for test_ip in SERVER_IP:
#     print(f"[*] Проверка сервера: {test_ip}")
#     is_online = ping_server(test_ip)