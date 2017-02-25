from socket import *


def new_server_socket():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind (('0.0.0.0', 1337))
    s.listen(2)
    return s

def send_data(first_user, second_user):
    (first_socket, first_addr) = first_user
    (second_socket, second_addr) = second_user
    # 1 means that he should be the one that start the conversation
    # 2 means that he should be the one that wait for the conversation
    first_socket.send(str(second_addr[0]) + ' ' + str(second_addr[1]) + ' 1')
    second_socket.send(str(first_addr[0]) + ' ' + str(first_addr[1]) + ' 2')
    
def close_all(sockets):
    for i in sockets:
        i.close()

def main():
    s = new_server_socket()
    first_user = s.accept()
    second_user = s.accept()
    send_data(first_user, second_user)
    close_all([s,first_socket,second_socket])

main()
