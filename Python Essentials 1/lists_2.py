board = [["EMPTY" for i in range(8)] for j in range(8)]
board[0][0] = "ROOK"
board[0][7] = "ROOK"
board[7][0] = "ROOK"
board[7][7] = "ROOK"
board[4][2] = "KNIGHT"
board[3][4] = "PAWN"

for row in range(8):
    print(board[row])
    
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#
 
total = 0.0
 
for day in temps:
    total += day[11]
 
average = total / 31
 
print("Temperatura promedio al mediodía:", average)

# Temperatura más alta durante todo el mes
highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("La temperatura más alta fue:", highest)

# Cuenta los días en que la temperatura al mediodía fue de al menos 20 ℃
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#

hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "fueron los días calurosos.")

