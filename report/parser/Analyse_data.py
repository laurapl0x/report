'''
python 2.6
Created on 29 Mar 2014
@version: 1.0.0
@author: darrendaly
'''
import time

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

def checkAveragePercentage(section, section1, report, min_limit=None, max_limit=None):
    '''check the percentage of section out of section1'''
    percent = getPercentage(section, section1, report)
    checkLimits(section, section1, percent, min_limit, max_limit)
    return percent
    
def getPointPercentage(section, section1, report, point=0, min_limit=None, max_limit=None):
    '''checks the levels of percentages for a point, taking point in as index 0 but displaying back as index 1'''
    if point > report.size:
        print 'The point was out of range, so we changed it to the last point instead'
        point = report.size - 1
    elif point != 0:
        point = point - 1
    value = report.sections[section][point][0]
    value2 = report.sections[section1][point][0]
    percent = value / value2 * 100
    print 'The percentage for point ' + str(point + 1) + ' out of ' + str(section) + ' and ' + str(section1) + ' is: ' + str(percent) + '% at ' + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(report.sections[section][point][1]))
    checkLimits(section, section1, percent, min_limit, max_limit)
    return percent

def checkLimits(section, section1, percent=None, min_limit=None, max_limit=None):
    '''Checks if the percentage is within, below or exceeding the normal limits'''
    if percent > max_limit:
        print 'The average percentage of ' + str(section) + ' out of ' + str(section1) + ' is exceeding the normal range'
    elif percent < min_limit:
        print 'The average percentage of ' + str(section) + ' out of ' + str(section1) + ' is below the normal range'
    else:
        print 'The average percentage of ' + str(section) + ' out of ' + str(section1) + ' is within the normal range'



