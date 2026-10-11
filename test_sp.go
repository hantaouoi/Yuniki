package main

import (
	"fmt"
	"os/exec"
	"time"
)

func main() {
	// Твой IP для проверки
	serverIP := "1.1.1.1"

	// ANSI-коды цветов для терминала Arch
	cyan := "\033[1;36m"
	// green := "\033[1;32m"
	// red := "\033[1;31m"
	reset := "\033[0m"

	fmt.Printf("%s[YUNIKI Go]%s Запуск проверки...\n", cyan, reset)
	fmt.Println("---------------------------------")

	// Аналог subprocess.run в Python. Запускаем: ping -c 2 -q 1.1.1.1
	cmd := exec.Command("ping", "-c", "2", "-q", serverIP)

	// Замеряем время выполнения (SRE фишка)
	startTime := time.Now()

	// Выполняем команду
	err := cmd.Run()
	duration := time.Since(startTime)

	// Подсвечиваем IP
	highlightedIP := fmt.Sprintf("%s%s%s", cyan, serverIP, reset)

	// Если ошибок нет (err == nil), значит сервер ответил (ONLINE)
	if err == nil {
		fmt.Printf("🟢 [ONLINE]  -> %s | Время: %v\n", highlightedIP, duration)
	} else {
		fmt.Printf("🔴 [OFFLINE] -> %s | Сервер лежит!\n", highlightedIP)
	}

	fmt.Println("---------------------------------")
}
