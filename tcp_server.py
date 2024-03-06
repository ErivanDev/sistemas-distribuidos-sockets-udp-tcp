import random

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', 12345))
server_socket.listen(1)

curr_map = {
    "dolar": random.uniform(4,6),
    "euro": random.uniform(5,7),
    "bitcoin": random.uniform(200000,400000)
}

def generate_random_price(currency):
    random_value = curr_map[currency]
    return random_value

def convert_to_dolar(value, currency):
    price = generate_random_price(currency)
    value = value * price
    return round(value, 2)

if __name__ == "__main__":
    print("Aguardando por conexões...")

    while True:
        connection, client_address = server_socket.accept()

        try:
            print(f"Conexão de {client_address}")

            data = connection.recv(1024)
            print(f"Recebido: {data.decode()}")

            (currency, amount) = data.decode().split(sep=",")
            result = convert_to_dolar(float(amount), currency)

            if data:
                connection.sendall(str(result).encode())
            else:
                print("Não foram recebidos dados do cliente")
                break

        finally:
            connection.close()