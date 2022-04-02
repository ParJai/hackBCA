

### Define variables ###
board = [3, 4, 5]
#stones = [0, 1, 3, 5, 7]
player = 1

def removeStone(stones, row):
    stones[row].pop(-1)

### Game loop ##
# while sum(stones) != 0:
# 	pile = 0
# 	num_stones = 0
# 	### Print out piles and take (correct) input ###
# 	for i in range(1, len(stones)):
# 		print(f'Pile {i}: {stones[i]}')
# 	print(f'\nPlayer {player}:')
# 	while pile < 1 or pile > len(stones) - 1 or stones[pile] <= 0:
# 		pile = int(input('From which pile would you like to take? '))
# 	while not 0 < num_stones <= stones[pile]:
# 		num_stones = int(input('How many stones would you like to take? '))
# 	stones[pile] -= num_stones

# 	### Check if lose ###
# 	if sum(stones) != 0:
# 		player = 3 - player
# 		print('\n')

# ### Return win results ###
# print(f'\nYou took the last stone! Player {player} loses.')
