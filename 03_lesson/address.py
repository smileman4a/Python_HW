class Address:
    def __init__(
        self, zip_code: int, city: str, street: str, house_n: int, room_n: int
    ):
        self.zip_code = zip_code
        self.city = city
        self.street = street
        self.house_n = house_n
        self.room_n = room_n

    def __str__(self):
        zip_code = self.zip_code
        city = self.city
        street = self.street
        house_n = self.house_n
        room_n = self.room_n
        return f"{zip_code}, {city}, {street}, {house_n} - {room_n}"
