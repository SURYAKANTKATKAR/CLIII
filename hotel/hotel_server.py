import Pyro5.server
from hotel_service import HotelService

def main():
    daemon = Pyro5.server.Daemon()  # Start Pyro5 server
    uri = daemon.register(HotelService)
    print("HotelService is ready.")
    print("URI:", uri)  # Share this with the client
    daemon.requestLoop()

if __name__ == "__main__":
    main()
