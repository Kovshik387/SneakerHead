class Sneaker:

    def __init__(self, id_item, brand, model, size, coloring, count):
        self.id_item = id_item
        self.brand = brand
        self.model = model
        self.size = size
        self.coloring = coloring
        self.count = count

    def decrement_count(self):
        self.count -= 1

    def display_info(self):
        return f'{self.id_item} {self.brand} {self.model} {self.coloring} {self.size} {self.count}'


def search_in_sneakers(text):
    for item in sneakers:
        if item.size == text or item.brand == text or item.coloring == text or item.model == text:
            search_sneakers.append(item)


def refresh_sneak(self):
    self.sneakers = [position_1, position_4, position_5, position_2, position_3, position_6]


position_1 = Sneaker(1, "Adidas", "Ozweego", 10, "Черный", 52)
position_2 = Sneaker(2, "Adidas", "Ozweego", 12, "Серый", 12)
position_3 = Sneaker(3, "Adidas", "Yung-1", 9, "Белый", 9)
position_4 = Sneaker(4, "Nike", "Monarhc-IV", 11, "Белый", 3)
position_5 = Sneaker(5, "Nike", "Force-1", 8, "Розовый", 20)
position_6 = Sneaker(6, "Nike", "Force-5", 8, "Белый>", 1)
sneakers = [position_1, position_4, position_5, position_2, position_3, position_6]
search_sneakers = []
buy_sneakers = []
