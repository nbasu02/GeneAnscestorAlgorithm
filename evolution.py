import sys
from proteinCounter import *
from genome import Gene
from survival import survivingGenes
import sys

def populate(genes, remainingGenes):
	numberOfCopies = 33
	for gene in range(len(genes)):
		for i in range(numberOfCopies):
			newgene = genes[i].replicate()
			newgene.mutate(remainingGenes)
			genes.append(newgene)
			
	return genes


if (len(sys.argv)) != 2:
	print "Requires one input argument"
	exit()

inputfile = open(sys.argv[1], 'r')
geneInputs = inputfile.read().strip().split('\n')
convergenceCounter = ConvergenceCounter()

trials = 100
generations = 1000

for trial in range(trials):
	genes = []
	for value in geneInputs:
		genes.append(Gene(value))

	geneIndices = range(len(genes[0].proteinString))
	proteinCount = ProteinCounter()
	originalDifferences = []

	for generation in range(generations):
		toBeRemoved = []
		proteinCount.reset()
		
		#After pruning out the same proteins in each, we create a population
		if generation == 1:
			populate(genes, geneIndices)
		elif generation > 1:
			pass
		
		for i in range(len(genes)):
			genes[i].resetScore()
		
		for i in geneIndices:
			proteinCount.reset()
			for j in range(len(genes)):
				proteinCount.numProteins[genes[j].proteinString[i]] += 1
				genes[j].setDictAndKey(proteinCount.numProteins, genes[j].proteinString[i])
			
			#Comes out true if every gene has the same ith protein
			if proteinCount.numProteins[genes[-1].proteinString[i]] == len(genes):
				if generation > 0:
					convergenceCounter.newConvergence(i, genes[-1].proteinString[i])
				toBeRemoved.append(i)
			#Each gene's score is determined by the sum of each protein's
			#category score in proteinCounter (i.e. if 50 have an A protein
			#each score is upped by 50)
			else:
				for i in range(len(genes)):
					genes[i].addScore()
		
		#If each gene is constant throughout all protein strings present, remove
		for i in toBeRemoved:
			geneIndices.remove(i)

		if generation == 0:
			differentGenesFile = open('differenceIndices.txt', 'w')
			for i in geneIndices:
				differentGenesFile.write(str(i) + ": ")
				originalDifferences.append(i)
				proteinCount.reset()
				for gene in genes:
					proteinCount.numProteins[gene.proteinString[i]] += 1
				
				differentGenesFile.write(proteinCount.toString() + "\n")
				
			if trial == 0:
				convergenceCounter.setConvergences(originalDifferences)
			
			print originalDifferences
		else:
			survivingGenes(genes) #Removes unfit individuals by pointer
			for i in range(len(genes)):
				gene = genes[i].replicate()
				gene.mutate(geneIndices)
				genes.append(gene)

	print geneIndices
	for i in geneIndices:
		convergenceCounter.newConvergence(i, 'X')

open('geneconvergencefile.txt', 'w').write(convergenceCounter.toString())
convergenceCounter.toCsv()
