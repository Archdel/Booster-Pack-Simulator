from src.database_manager import DatabaseManager

def main():
    db = DatabaseManager()

    query = "SELECT * FROM booster_packs;"
    packs = db.fetch_all(query)

    print("Available Booster Packs:")
    for pack in packs:
        print(pack)

    db.close_connection()

if __name__ == "__main__":
    main()
