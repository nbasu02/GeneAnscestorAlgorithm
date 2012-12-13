from random import random 
from proteinsort import *

#Input is sorted list of proteins
def survivingGenes(proteinList):
	divide(proteinList)
	minScore = proteinList[0].score
	maxScore = proteinList[-1].score
	scoreRange = maxScore-minScore
	if scoreRange != 0:
		
		for protein in proteinList:
			chanceOfSurvival = float(protein.score - minScore)/scoreRange
			if random() > chanceOfSurvival: #lhs in range [0, 1), rhs [0, 1]
				proteinList.remove(protein) #Will remove by pointer
				
	while len(proteinList) >= 100:
		del proteinList[0]
