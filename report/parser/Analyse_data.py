'''
python 2.6
Created on 29 Mar 2014
@version: 1.0.0
@author: darrendaly
'''

def calculateAverages(section, report):
    '''Calculates the average value of occurrences in the specified section'''
    total = getTotal(section, report)
    avg = total / report.size
    return avg

def getTotal(section, report):
    '''Calculates and returns the total value of occurrences in the specified section'''
    total = 0
    for counter in range(report.size):
        total += report.sections[section][counter][0]
    return total

def findMins(section, report):
    '''find the minimum value in the specified section'''
    for counter in range(report.size):
        value = report.sections[section][counter][0]
        if counter == 0:
            minimum = value
        elif minimum > value:
            minimum = value
    return minimum
            
def findMaxs(section, report):
    '''find the maximum value in the specified section'''
    for counter in range(report.size):
        value = report.sections[section][counter][0]
        if counter == 0:
            maximum = value
        elif maximum < value:
            maximum = value
    return maximum
          
def getPercentage(section, section1, report):
    '''returns the percentage of one section compared with another section'''
    total1 = getTotal(section, report)
    total2 = getTotal(section1, report)
    return ((total1 / total2) * 100)


    
    