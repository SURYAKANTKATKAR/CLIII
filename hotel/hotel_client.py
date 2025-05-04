import Pyro5.api

def main():
    uri = input("Enter URI from server (e.g. PYRO:obj_xxxxxx@localhost:xxxxx):\n")
    hotel = Pyro5.api.Proxy(uri)

    while True:
        print("\n1. Book Room\n2. Cancel Booking\n3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter guest name: ")
            print(hotel.book_room(name))
        elif choice == "2":
            name = input("Enter guest name: ")
            print(hotel.cancel_booking(name))
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
