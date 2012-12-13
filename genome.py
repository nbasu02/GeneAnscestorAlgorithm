from random import randint
from mutation import Mutation
from proteinsort import *

class Gene(object):
	def __init__(self, proteinString):
		self.proteinString = proteinString
		self.mutations = [] #List of all mutations that occurred
		self.score = 0
		
	#remainingProteins is the list of indices where all proteins have not
	#yet converged
	def mutate(self, remainingProteins):
		for i in remainingProteins:
			willItChange = randint(0, 99)
			if willItChange == 0:
				mutation = Mutation(self.proteinString[i])
				self.proteinString = self.proteinString[0:i] + mutation.getProtein() + self.proteinString[i+1:]
				
				self.mutations.append(mutation)

	#Because assignments appear to be pointer-based instead of value
	def replicate(self):
		newGenome = Gene(self.proteinString)
		for mutation in self.mutations:
			newGenome.mutations.append(mutation)
		
		return newGenome
	
	def resetScore(self):
		self.score = 0
	
	#Input is a pointer to the dictionary in ProteinCounter and a protein
	#Used to more quickly add up scores of each gene. O(n) instead of O(n^2)
	def setDictAndKey(self, counterDict, key):
		self.counterDict = counterDict
		self.key = key
	
	def addScore(self):
		self.score += self.counterDict[self.key]
