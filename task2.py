environment = input()

if environment == "prod":
    print("ВНИМАНИЕ: Выкатываем код на боевой сервер! Требуется подтверждение админа.")
elif environment == "stage" or environment == "test":
    print(f"Запуск автоматических тестов для окружения {environment}.")
else:
    print("Ошибка: Окружение не существует. Деплой отменен.")
