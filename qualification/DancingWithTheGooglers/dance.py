#!/usr/bin/python

from itertools import combinations_with_replacement

def best_score(total_score, is_surprising=False):
	""" Given a total score, find the 'best' 3 judge score.
	'Best' is having the highest individual score, if 'is_surprising' is
	True we will look for scores that are separated by 2 points which normally isn't allowed. 
	"""

	# Get all 3 digit combos from "best" to "worst" breaking on the best to short circuit
	for combo in combinations_with_replacement(range(10,-1,-1), 3):
		score1 = combo[0]
		score2 = combo[1]
		score3 = combo[2]
		if score1+score2+score3 == total_score:
			# If the score is the right total, make sure it is valid
			diff_limit = 1  	# Maximum score difference
			if is_surprising:
				diff_limit = 2
			
			if abs(score1-score2) > diff_limit or abs(score1-score3) > diff_limit or abs(score2-score3) > diff_limit:
				continue
			else:
				# We have a valid score!
				return combo
	
	return None


if __name__ == "__main__":
	import sys
	f = sys.stdin
	T = int(f.readline())

	for i in xrange(T):
		score_data = f.readline().split(' ')

		N = int(score_data[0])	# Number of googlers
		S = int(score_data[1]) 	# Number of surprising scores
		p = int(score_data[2])	# Best possible score
		scores = [int(x) for x in score_data[3:]]

		count = 0
		surprising_used = 0

		# For each googlers score....
		for total_score in scores:
			# Get the 'best' score and the 'best surprising' score
			best = best_score(total_score)
			surprising = best_score(total_score, is_surprising=True)

			if best[0] >= p:	# The 'best' score without needing a surprise is good enough!
				count += 1
			elif surprising[0] >= p and surprising_used < S: # See if their surprising score hits the threshold (and there is a surprising score left!)
				count += 1
				surprising_used += 1
			else:	# neither score was high enough (or we ran out of surprising scores)
				pass	
		
		print "Case #%s: %s" % (i+1, count)
		

			
