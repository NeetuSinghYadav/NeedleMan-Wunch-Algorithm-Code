import numpy as np


seq1='ATAATTCA'
seq2='ATGGCTA'


m = len(seq1)
n = len(seq2) 
score_mat = np.zeros((m+1, n+1), dtype=int)

match=1
gap= mismatch= -1
score_mat[0][0] = 0

for i in range(0,m+1):
	score_mat[i][0] = i * gap 
for j in range(0,n+1):
	score_mat[0][j] = j * gap 

#print score_mat


def Align(x,y):
	if x==y:
		return match
	elif x!= y:
		return mismatch	
	elif x == '-' or y == '-':
		return gap	

def NeedlemanWunchScoring(seq1, seq2, n, m):
	#fill the other entries of the matrix
	for i in range(1, m+1):
		for j in range(1, n+1):
			match  = score_mat[i-1][j-1] + Align(seq1[i-1], seq2[j-1])
			delete = score_mat[i-1][j]   +  gap
			insert = score_mat[i][j-1]   +  gap
			score_mat[i][j] = max(match, delete, insert)
			#print seq1[i-1], seq2[j-1], score_mat[i-1][j-1]
	return score_mat		


Final_mat=NeedlemanWunchScoring(seq1, seq2, n, m)

print "seq1=", seq1 +"\n" + "seq2=", seq2

print '\n\nscore matrix \n'

print Final_mat

