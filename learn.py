http_status = int(input())
if http_status == 200:
	print("[OK] Сервер работает стабильно.")
elif http_status == 404:
	print("[ERROR] Страница не найдена!")
elif http_status == 500:
	print("[CRITICAL] Внутренняя ошибка сервера! Нужна перезагрузка.")
else:
	print(f"[INFO] Неизвестный статус кода: {http_status}")
