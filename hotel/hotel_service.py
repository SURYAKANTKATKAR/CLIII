import Pyro5.api

@Pyro5.api.expose
class HotelService:
    def __init__(self):
        self.booked_rooms = set()

    def book_room(self, guest_name):
        if guest_name in self.booked_rooms:
            return f"Booking failed: {guest_name} already has a room."
        self.booked_rooms.add(guest_name)
        return f"Room successfully booked for {guest_name}"

    def cancel_booking(self, guest_name):
        if guest_name in self.booked_rooms:
            self.booked_rooms.remove(guest_name)
            return f"Booking cancelled for {guest_name}"
        return f"No booking found for {guest_name}"
