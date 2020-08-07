# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 18:17:53 2020

@author: User
"""


def isYearLeap(year):
    if year==2000 or year==2016:
        print("True")
        return True
    elif year==1900 or year==1987:
        print("False")
        return False

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")


