from random import randint

aminoacids = ['A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L',
'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', '-']

class Mutation(object):
	def __init__(self, mutatedFrom):
		newAminoAcid = randint(0, 20)
		while mutatedFrom == aminoacids[newAminoAcid]:
			newAminoAcid = randint(0, 20)
		
		self.mutatedGene = aminoacids[newAminoAcid]
		
	def getProtein(self):
		return self.mutatedGene
