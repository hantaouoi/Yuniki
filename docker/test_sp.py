import subprocess
SERVER_IP = ("85.155.124.78", "1.1.1.1", "8.8.8.8")

def ping_server(ip):
    p1 = subprocess.run(["ping", "-c", "2", ip], capture_output=True, text=True)
    return_code = p1.returncode == 0
    print(p1.stdout)
    return return_code

for test_ip in SERVER_IP:
    print(f"[*] Проверяю сервер: {test_ip}")
    is_online = ping_server(test_ip)