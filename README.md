class Taximetar:
    def __init__(self, start_rate, rate_per_km):
        self.start_rate = start_rate  # poÄetna cijena voÅ¾nje
        self.rate_per_km = rate_per_km  # cijena po kilometru

    def get_total_cost(self):
        km = int(input('Please enter the km: '))  # unos kilometraÅ¾e
        total = km * self.rate_per_km  # izraÄun ukupne cijene voÅ¾nje
        rounded_total = round(total, 0)  # zaokruÅ¾ivanje na cijeli broj
        return rounded_total


taximetar = Taximetar(5, 2.1)  # stvaranje instance objekta Taximetar s poÄetnom cijenom od 5 i cijenom po kilometru od 2.1
total_cost = taximetar.get_total_cost()  # dobivanje ukupnih troÅ¡kova voÅ¾nje
print('Your expenses are', total_cost)  # ispis ukupnih troÅ¡kova voÅ¾nje
