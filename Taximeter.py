class Taximetar:
    def __init__(self, start_rate, rate_per_km):
        self.start_rate = start_rate  # početna cijena vožnje
        self.rate_per_km = rate_per_km  # cijena po kilometru

    def get_total_cost(self):
        km = int(input('Please enter the km: '))  # unos kilometraže
        total = km * self.rate_per_km  # izračun ukupne cijene vožnje
        rounded_total = round(total, 0)  # zaokruživanje na cijeli broj
        return rounded_total


taximetar = Taximetar(5, 2.1)  # stvaranje instance objekta Taximetar s početnom cijenom od 5 i cijenom po kilometru od 2.1
total_cost = taximetar.get_total_cost()  # dobivanje ukupnih troškova vožnje
print('Your expenses are', total_cost)  # ispis ukupnih troškova vožnje