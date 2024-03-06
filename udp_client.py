import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if __name__ == "__main__":
    print("Este programa pode converter reais em três moedas: dolar | euro | bitcoin")
    
    user_input = input("\nDigite a moeda que deseja saber quanto você tem e o valor \n(exemplo: dolar,10):\n")

    try:
        client_socket.sendto(user_input.encode(), ('localhost', 12345))

        data, server = client_socket.recvfrom(4096)
        print(f"Valor da Conversão: {data.decode()}")
        
    finally:
        client_socket.close()