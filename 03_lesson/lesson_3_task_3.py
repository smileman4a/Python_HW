from address import Address
from mailing import Mailing

from_address = Address(427620, "Galzov", "F.Vasil'eva str.", 19, 1)
to_address = Address(113213, "Moscow", "Krasnaya ploshad'", 1, 1)

mail = Mailing(to_address, from_address, 1313, "1243124AE")

print(mail)
