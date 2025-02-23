CREATE DATABASE booster_simulation;
USE booster_simulation;

DROP TABLE IF EXISTS pack_contents;
DROP TABLE IF EXISTS booster_packs;
DROP TABLE IF EXISTS cards;

CREATE TABLE booster_packs(
	pack_id INT AUTO_INCREMENT PRIMARY KEY,
    pack_name VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE cards(
	card_id INT AUTO_INCREMENT PRIMARY KEY,
    card_name VARCHAR(255) NOT NULL
);

CREATE TABLE pack_contents(
	pack_id INT,
    card_id INT,
    slot INT CHECK (slot BETWEEN 1 AND 4),
    probability FLOAT NOT NULL CHECK(probability BETWEEN 0 AND 1),
    FOREIGN KEY (pack_id) REFERENCES booster_packs(pack_id),
    FOREIGN KEY (card_id) REFERENCES cards(card_id),
    PRIMARY KEY (pack_id, card_id, slot)
);