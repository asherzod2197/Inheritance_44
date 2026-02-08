# 44. Restoran menyusi

class MenuItem:
    def __init__(self, name, price):
        self.name = name           # taom nomi
        self.price = price         # narx ($)

    def get_price(self):
        """Taomning narxi"""
        return self.price

    def __str__(self):
        return f"{self.name:16} | {self.price:6.2f}$"


# -----------------------------------------------
# Voris sinflar (chiroyli chiqish + emoji)
# -----------------------------------------------

class HotMenuItem(MenuItem):
    def __str__(self):
        return f"🍲 {self.name:14} → {self.price:6.2f}$"


class ColdMenuItem(MenuItem):
    def __str__(self):
        return f"🥗 {self.name:14} → {self.price:6.2f}$"


# Qo‘shimcha misollar uchun (foydali bo‘lishi mumkin)
class DessertMenuItem(MenuItem):
    def __str__(self):
        return f"🍰 {self.name:14} → {self.price:6.2f}$"


class DrinkMenuItem(MenuItem):
    def __str__(self):
        return f"🥤 {self.name:14} → {self.price:6.2f}$"


# --------------------------------------------------
# Menyu narxlarini chiqarish
# --------------------------------------------------

def show_menu_prices(items):
    print("\n" + "═" * 55)
    print("       RESTORAN MENYUSI — NARX RO‘YXATI       ".center(55))
    print("═" * 55)
    print("Taom nomi                  Narxi ($)")
    print("─" * 55)

    total = 0

    for item in items:
        print(item)
        total += item.get_price()

    print("─" * 55)
    print(f"JAMI (barcha taomlar):              {total:8.2f}$")
    print("═" * 55 + "\n")


# Test ma'lumotlari
menyu = [
    HotMenuItem("Sho‘rva (qovurilgan go‘shtli)", 9.50),
    ColdMenuItem("Sezar salati (tovuq bilan)", 7.80),
    HotMenuItem("Lag‘mon", 8.90),
    ColdMenuItem("Olivye salati", 6.50),
    DessertMenuItem("Medovik tort", 5.50),
    DrinkMenuItem("Cola 0.5L", 2.50),
    HotMenuItem("Palov", 11.00),
]

show_menu_prices(menyu)


# Sizning misol qiymatlaringiz bilan:
print("\nSizning misol menyuingiz:\n")
misol_menyu = [
    HotMenuItem("Sho‘rva", 8),
    ColdMenuItem("Salat", 5),
]

show_menu_prices(misol_menyu)
