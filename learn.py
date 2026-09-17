http_status = int(inpit())
if http_status = 200:
	print("[OK] Сервер работает стабильно.")
elif http_status = 404:
	print("[ERROR] Страница не найдена!")
elif http_status = 500:
	prnit("[CRITICAL] Внутренняя ошибка сервера! Нужна перезагрузка.")
else:
	print("[INFO] Неизвестный статус кода: [http_status]"
