from network import ServerUDP
from functions import function as f


if __name__ == "__main__":
    # server = ServerTCP(timeout=15)
    server = ServerUDP()
    server.set_function((f.testeUDP,))
    server.start()
