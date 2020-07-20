# canQueenAttack(qX, qY, oX, oY) [15 pts]
# Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine 
# whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and 
# diagonally.

def canqueenattack(qR, qC, oR, oC):
	# Your code goes here
	kill = False
	r = qR
	c = qC
	while(r < 8 and c < 8):

		r +=1
		c +=1
		if(r == oR and c == oC):
			kill = True
	if(qR == oR or qC == oC):
		kill = True
	return kill

print(canqueenattack(1, 1, 1, 2))