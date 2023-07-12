# b.	Alpha-Beta pruning

import math
# Returns optimal value for current player
#(Initially called for root and maximizer)
def minimax(depth, nodeIndex, maximizingPlayer,
			values, alpha, beta):

	# Terminating condition. i.e
	# leaf node is reached
	if depth == treeDepth:
		return values[nodeIndex]

	if maximizingPlayer:

		best = -math.inf

		# Recur for left and right children
		for i in range(0, 2):

			val = minimax(depth + 1, nodeIndex * 2 + i,
						False, values, alpha, beta)
			best = max(best, val)
			alpha = max(alpha, best)

			# Alpha Beta Pruning
			if beta <= alpha:
				break

		return best

	else:
		best = math.inf

		# Recur for left and
		# right children
		for i in range(0, 2):

			val = minimax(depth + 1, nodeIndex * 2 + i,
							True, values, alpha, beta)
			best = min(best, val)
			beta = min(beta, best)

			# Alpha Beta Pruning
			if beta <= alpha:
				break

		return best

# Driver Code

scores= list(map(int,input('Enter utility scores: ').split()))
k=int(input('Enter initial turn, 1 for max or 0 for min: '))
treeDepth = math.log(len(scores), 2)
print("The optimal value is :", minimax(0, 0, k, scores, -math.inf, math.inf))

#3 5 6 9 1 2 0 -1


#MINIMAX ALGORITHM
import math

def minimax (curDepth, nodeIndex,
			maxTurn, scores,
			targetDepth):

	# base case : targetDepth reached
	if (curDepth == targetDepth):
		return scores[nodeIndex]

	if (maxTurn):
		return max(minimax(curDepth + 1, nodeIndex * 2,
					False, scores, targetDepth),
				minimax(curDepth + 1, nodeIndex * 2 + 1,
					False, scores, targetDepth))

	else:
		return min(minimax(curDepth + 1, nodeIndex * 2,
					True, scores, targetDepth),
				minimax(curDepth + 1, nodeIndex * 2 + 1,
					True, scores, targetDepth))

# Driver code
scores = [3, 5, 2, 9, 12, 5, 23, 23]

treeDepth = math.log(len(scores), 2)

print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))


