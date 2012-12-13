def divide(proteinList):
	if len(proteinList) <= 1:
		return proteinList
	else:
		left = divide(proteinList[0:len(proteinList)/2])
		right = divide(proteinList[len(proteinList)/2:])
	
	return conquer(left, right)
		
def conquer(left, right):
	leftIndex = 0
	rightIndex = 0
	returnList = []
	for i in range(len(left)+len(right)):
		if leftIndex == len(left):
			returnList.append(right[rightIndex])
			rightIndex += 1
		elif rightIndex == len(right):
			returnList.append(left[leftIndex])
			leftIndex += 1
		
		elif left[leftIndex].score <= right[rightIndex].score:
			returnList.append(left[leftIndex])
			leftIndex += 1
			
		else:
			returnList.append(right[rightIndex])
			rightIndex += 1
	
	return returnList
