
'''3. Write a program that will simulate user score in a game.
Create a list with 5 player's names. After that simulate 100 games for each player.
As a result of the game create a list with player's name and his score (0-1000 range).'''
import random
import csv

players = ["Player_1", "Player_2", "Player_3", "Player_4", "Player_5"]
# Записуємо рандомні результати для кожного гравця в 100 іграх
game_results = []
for player in players:
    for i in range(100):
        score = random.randint(0, 1000)
        game_results.append((player, score))

# Створюємо файл і аписуємо в нього усі результати
with open("game_results.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Player name", " Score"])
    writer.writerows(game_results)

'''4. Write a script that reads the data from previous CSV file and creates a new file called high_scores.csv
where each row contains the player name and their highest score.
Final score should sorted by descending of highest score'''
# Читаємо файл з результатами
with open("game_results.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        player_name = row[0]
        score = int(row[1])
        game_results.append((player_name, score))

# Шукаємо найвищий результат для кожного гравця
high_scores = {}
for player_name, score in game_results:
    if player_name not in high_scores or score > high_scores[player_name]:
        high_scores[player_name] = score

# Сортуємо у спадаючому порядку по набраних очках
sorted_high_scores = sorted(high_scores.items(), key=lambda x: x[1], reverse=True)

# Записуємо найкращі результати у файл
with open("high_scores.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Player name", " Highest Score"])
    writer.writerows(sorted_high_scores)
