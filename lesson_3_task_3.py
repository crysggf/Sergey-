from address import Address
from mailing import Mailing 


from_address = Address(
    index="63933",
    city="Хабаровск",
    street="Ленина",
    house="34",
    apartment="156"
)

to_address = Address(
    index="427765",
    city="Тверь",
    street="Орджоникидже",
    house="45",
    apartment="458"
)

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=780.67,
    track="J56738LFC75848"
)
print(mailing)
