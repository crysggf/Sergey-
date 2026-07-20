from smartphone import Smartphone

catalog = [
    Smartphone("Iphone", "17_Pro", "+7(987)1673434"),
    Smartphone("Siemens", "A70", "98765656"),
    Smartphone("Samsung", "Galaxy", "876545"),
    Smartphone("Nokia", "6300", "23456789"),
    Smartphone("Motorola", "1265", "35789087788")]


for smartphone in catalog:
    print(f"{smartphone.brand} {smartphone.model}- {smartphone.number}")
