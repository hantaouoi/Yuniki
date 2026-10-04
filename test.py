import subprocess

ip_list = ["1.1.1.1", "8.8.8.8", "", "85.155.124.78", ""]
for ips in ip_list:
    if ips.strip():
        print(f"[Open IP:] {ips}")

def list_ping(ip):
    p1 = subprocess.run(["ping", "-c", "2", ip], capture_output=True, text=True)
    return_code = p1.returncode == 0
    print(p1.stdout)
    return return_code
print("")
for test_ip in ips:
    if test_ip.strip():
        print(f"[*] Проверяю сервер: {test_ip}")
