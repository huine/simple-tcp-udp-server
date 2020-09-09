from network import ClientUDP

if __name__ == "__main__":
    client = ClientUDP()
    client.send(['teste', 'de', 'udp'])
    print(client.receive())