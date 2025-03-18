import random
from collections import defaultdict
from src.data_fetcher import DataFetcher

class PackSimulator:
    def __init__(self, chosen_pack):
        self.fetcher = DataFetcher()
        self.booster_pack = self.fetcher.get_booster_pack(chosen_pack)

    def select_card(self, slot):
        results = self.fetcher.get_pack_contents(self.booster_pack, slot)
        if not results:
            return None 
        
        cards, probabilities = zip(*results)  
        return random.choices(cards, probabilities)[0]  

    def generate_god_pack(self):
        return [self.select_card(slot=4) for _ in range(5)]

    def open_pack(self):
        if random.randint(1, 10000) <= 5:  
            return self.generate_god_pack()

        pack = [self.select_card(slot=1) for _ in range(3)]
        pack.append(self.select_card(slot=2))
        pack.append(self.select_card(slot=3))
        return pack

    def monte_carlo_simulation(self, target_card, num_simulations=10000):
        pack_counts = []
        card_pulls = defaultdict(int)  
        for _ in range(num_simulations):
            packs_opened = 0
            found = False

            while not found:
                packs_opened += 1
                pack = self.open_pack()

                if target_card in pack:
                    found = True
                    card_pulls[target_card] += 1

            pack_counts.append(packs_opened)

        avg_packs_needed = sum(pack_counts) / num_simulations

        return {
            "Total Simulations": num_simulations,
            "Average Packs Needed": avg_packs_needed,
            "Total Copies Pulled": card_pulls[target_card]
        }
