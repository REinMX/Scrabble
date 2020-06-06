# Listas separadas de letras y puntos por letra
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Definicion de diccionario con letras y valores, se agrega valor cero en caso de estar vacia
letters_to_points = {key:value for key, value in zip(letters, points)}
letters_to_points[" "] = 0

# Funcion para sacar puntos por palabra 
def score_word(word):
  point_total = 0
  for i in word:
    point_total += letters_to_points.get(i, 0)
  return point_total

# Prueba de funcion score_word
brownie_points = score_word("BROWNIE")
print(brownie_points)

# Ejemplo de juego entre jugadores
player_to_words = {'player1' : ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd' : ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con' : ['ERASER', 'BELLY', 'HUSKY'], 'Prod Reader' : ['ZAP', 'COMA', 'PERIOD']}

# Funcion para jugar mas palabras por jugador
def play_word(player ,word):
  lst = player_to_words.get(player)
  lst.append(word)
  player_to_words[player] = lst

# Prueba de funcion play_word
play_word('player1', 'ACCOUNT')

# Funcion para recalcular los puntos cada vez que se juega una palabra

# Loop para obtener puntos totales por jugador
player_to_points = {}
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

# Impresion de resultados
print(player_to_words)
print(player_to_points)







# If you want extended practice, try to implement some of these ideas with the Python you’ve learned:
# update_point_totals() — turn your nested loops into a function that you can call any time a word is played
# make your letter_to_points dictionary able to handle lowercase inputs as well