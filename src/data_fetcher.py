from src.database_manager import DatabaseManager

class DataFetcher:
    def __init__(self):
        self.db = DatabaseManager()

    def get_booster_pack(self, chosen_pack):
        """Fetch the pack_set_name for the given booster pack ID."""
        query = "SELECT pack_set_name FROM pack_sets WHERE pack_id = %s;"
        result = self.db.fetch_one(query, (chosen_pack,))
        return result[0] if result else None

    def get_pack_contents(self, pack_set_name, slot):
        """Fetch cards and their probabilities for a given pack set and slot."""
        query = "SELECT card_id, probability FROM pack_contents WHERE pack_set_name = %s AND slot = %s;"
        return self.db.fetch_all(query, (pack_set_name, slot))
