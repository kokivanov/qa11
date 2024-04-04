import socket

# Параметри хоста і порту
host = '192.168.0.5'
port = 12345

# Створення сокету
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Прив'язка сокету до адреси хоста і порту
server_socket.bind((host, port))

# Встановлення максимальної кількості одночасних з'єднань
server_socket.listen(5)
print(f"Сервер слухає на {host}:{port}")

try:
    while True:
        # Очікування на підключення
        client_socket, address = server_socket.accept()
        print(f"Підключення від {address} було успішно встановлено.")

        # Відправлення повідомлення клієнту
        client_socket.send("Hello, Client!".encode())

        # Закриття підключення
        client_socket.close()

except KeyboardInterrupt:
    # Закриття сокету сервера при виході
    server_socket.close()
    print("\nСервер зупинено.")
