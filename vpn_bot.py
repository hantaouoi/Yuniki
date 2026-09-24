import os
import time
import subprocess
import requests

# ==================== НАСТРОЙКИ ====================
# 1. Вставь сюда токен, который тебе дал @BotFather
TOKEN = "8900895010:AAEnNW4mIGzIv3AQqKkgbSM-cn1bzkLK8RI"

# 2. Вставь сюда свой цифровой ID из @userinfobot
CHAT_ID = "5057125017"

# 3. IP-адрес твоего VPN-сервера Hysteria 2 (без порта)
SERVER_IP = "85.155.124.78"  

# 4. Как часто проверять сервер (в секундах)
CHECK_INTERVAL = 30         
# ===================================================

def send_telegram_message(text):
    """Отправляет сообщение в твой Telegram."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("[+] Сообщение отправлено в Telegram.")
        else:
            print(f"[-] Ошибка Telegram API: {response.text}")
    except Exception as e:
        print(f"[-] Ошибка сети при отправке: {e}")

def ping_server(ip):
    """Проверяет, пингуется ли твой VPN-сервер."""
    # Отправляем 2 пакета пинга. stdout убирает лишний мусор из консоли.
    result = subprocess.run(["ping", "-c", "2", ip], stdout=subprocess.DEVNULL)
    return result.returncode == 0

def get_free_mem():
    """Считывает данные о памяти напрямую из ядра Linux."""
    try:
        with open("/proc/meminfo", "r") as f:
            lines = f.readlines()
        
        total_kb = int(lines[0].split()[1])
        free_kb = int(lines[1].split()[1])
        available_kb = int(lines[2].split()[1])
        
        total_mb = total_kb // 1024
        available_mb = available_kb // 1024
        used_mb = total_mb - available_mb
        
        return f"RAM total: {total_mb}MB | used: {used_mb}MB | free: {available_mb}MB"
    except Exception:
        return "RAM telemetry: status unknown"



if __name__ == "__main__":
    # Сбор телеметрии памяти
    mem_status = get_free_mem()
    
    # Сборка финального лога (обрати внимание на 'f' в начале)
    start_log = f"`[INFO] vpn_monitor daemon started.\n[SYS] {mem_status}\n[NET] Hysteria 2 tracking active.`"
    send_telegram_message(start_log)
    
    was_online = True
    try:
        while True:
            is_online = ping_server("85.155.124.78")

            print(f"[*] Проверил сервер. Результат онлайна: {is_online}")
            
            # Если сервер только что упал
            if not is_online and was_online:
                print(f"[-] CRITICAL: Host {SERVER_IP} down.")
                
                send_telegram_message(f"`[CRITICAL] Service connection failed. Host {SERVER_IP} is unreachable. State shifted to OFFLINE.`")
                
                was_online = False
                
            # Если сервер лежал, но снова поднялся
            elif is_online and not was_online:
                print(f"[+] NOTICE: Host {SERVER_IP} up.")
 
                send_telegram_message(f"`[NOTICE] Service connection restored. Host {SERVER_IP} is responding to ping. State shifted to ONLINE.`")

                was_online = True
            
            # Спим перед следующей проверкой
            time.sleep(CHECK_INTERVAL)
            
    except KeyboardInterrupt:
        print("\n[*] Скрипт остановлен пользователем.")

