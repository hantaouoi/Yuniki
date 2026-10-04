use std::process::Command;

fn main() {
    // 1. Создаем список серверов для проверки
    let servers = vec!["google.com", "github.com", "yandex.ru", "1.1.1.1"];

    println!("=== НАЧАЛО МОНИТОРИНГА СЕРВЕРОВ ===");

    for server in servers {
        println!("Пингую {}...", server);

        // 2. Вызываем системную команду ping.
        // Флаг "-c 1" означает "отправить только 1 пакет" (на Mac/Linux)
        let status = Command::new("ping").arg("-c").arg("1").arg(server).status(); // Получаем статус выполнения (успешно/ошибка)

        // 3. Проверяем результат
        match status {
            Ok(s) if s.success() => {
                println!("✅ Сервер {} ДОСТУПЕН\n", server);
            }
            _ => {
                println!("❌ Сервер {} НЕ ОТВЕЧАЕТ или ошибка сети\n", server);
            }
        }
    }

    println!("=== МОНИТОРИНГ ЗАВЕРШЕН ===");
}
