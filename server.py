import socket

#precisamos dizer ao nosso SO que desejamos criar um socket com determinadas características (TCP, IPv4)
HOST = "127.0.0.1"
PORT = 5000

#AF_INET para endereços de rede IPv4
#SOCK_STREAM protoclo TCP na camada de transporte
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criando socket

server.bind((HOST, PORT)) #ligar IP + porta
server.listen(1) #servidor começa a escutar conexões (por enquanto apenas com 1 cliente)

print("Servidor aguardando...")

'''
conn, addr = server.accept() #cliente conecta
print("Cliente conectado:", addr)

conn.send(b"Conectado ao servidor!\n") #enviando mensagem para o cliente (precisa ser bytes, por isso o b"")

while True:
    data = conn.recv(1024) #recebendo dados do cliente (máximo de 1024 bytes)
    if not data:
        break #se o cliente desconectar, saímos do loop
    print("Recebido do cliente:", data.decode()) #decodificando bytes para string e imprimindo

'''