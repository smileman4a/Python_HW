from address import Address


class Mailing:
    def __init__(
        self, to_address: Address, from_address: Address, cost: int, track: str
    ):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        to_address = self.to_address
        from_address = self.from_address
        cost = self.cost
        track = self.track
        return f"Отправление {track} из {from_address} в {to_address}. Стоимость {cost} рублей."
