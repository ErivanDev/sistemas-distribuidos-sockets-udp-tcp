import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

if __name__ == "__main__":
    print("Este programa pode converter reais em três moedas: dolar | euro | bitcoin")
    
    user_input = input("\nDigite a moeda que deseja saber quanto você tem e o valor \n(exemplo: dolar,10):\n")

    try:
        client_socket.sendall(user_input.encode())

        data = client_socket.recv(1024)
        print(f"Valor da Conversão: {data.decode()}")

    finally:
        client_socket.close()