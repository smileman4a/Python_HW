from smartphone import Smartphone

catalog = []
catalog += [Smartphone("Xiaomi", "17T Pro", "+79123456789")]
catalog += [Smartphone("Samsung", "A16", "+79789456123")]
catalog += [Smartphone("Apple", "X", "+79147258369")]
catalog += [Smartphone("Huawei", "Mate 80 Pro", "+79159159159")]
catalog += [Smartphone("OPPO", "Find N3", "+79321654987")]
for phone in catalog:
    print(phone)
