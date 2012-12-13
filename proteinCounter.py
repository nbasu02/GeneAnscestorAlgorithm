class ProteinCounter(object):
	def __init__(self):
		self.reset()
		
	def reset(self):
		self.numProteins = {'A':0,
		 'R':0,
		 'N':0,
		 'D':0, 
		 'C':0,
		 'E':0, 
		 'Q':0, 
		 'G':0, 
		 'H':0, 
		 'I':0, 
		 'L':0,
		 'K':0, 
		 'M':0, 
		 'F':0, 
		 'P':0, 
		 'S':0, 
		 'T':0, 
		 'W':0, 
		 'Y':0, 
		 'V':0, 
		 '-':0}
		 
	def toString(self):
		outputString = ""
		for key, value in self.numProteins.items():
			if value != 0:
				outputString += key + ": " + str(value) + " "
				
		return outputString

class ConvergenceCounter(object):
	def __init__(self):
		self.convergences = {}
		
	def setConvergences(self, differentGenes):	
		self.differentGenes = differentGenes
		for i in differentGenes:	
			self.convergences[str(i)] = self.numProteins = {'A':0,
		 'R':0,
		 'N':0,
		 'D':0, 
		 'C':0,
		 'E':0, 
		 'Q':0, 
		 'G':0, 
		 'H':0, 
		 'I':0, 
		 'L':0,
		 'K':0, 
		 'M':0, 
		 'F':0, 
		 'P':0, 
		 'S':0, 
		 'T':0, 
		 'W':0, 
		 'Y':0, 
		 'V':0, 
		 '-':0,
		 'X':0}
		 
	def newConvergence(self, index, aminoAcid):
		self.convergences[str(index)][aminoAcid] += 1
	
	def toString(self):
		outputString = ""
		for i in self.differentGenes:
			outputString += "Index " + str(i) + ": "
			for key, value in self.convergences[str(i)].items():
				if value != 0:
					outputString += key + ": " + str(value) + " "
			outputString += "\n"
		
		return outputString
	
	def toCsv(self):
		outputString = "Index"
		for key, value in self.convergences[str(self.differentGenes[0])].items():
			outputString += "," + key
		outputString += "\n"
		for i in self.differentGenes:
			outputString += str(i)
			for key, value in self.convergences[str(i)].items():
				outputString += "," + str(value) + " "
			outputString += "\n"
		
		open('aminoacidtable.csv', 'w').write(outputString)
