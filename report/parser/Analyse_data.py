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

def checkAveragePercentage(section, section1, report, min_limit, max_limit):
    '''check the percentage of section out of section1'''
    total = getPercentage(section, section1, report)
    if total > max_limit:
        print 'The average percentage of ' + str(section) + ' out of ' + str(section1) + ' is exceeding the normal range'
    elif total < min_limit:
        print 'The average percentage of ' + str(section) + ' out of ' + str(section1) + ' is below the normal range'
    else:
        print 'The average percentage of ' + str(section) + ' out of ' + str(section1) + ' is within the normal range'
    return total
    
def getPointPercentage(section, section1, report, point=0):
    '''checks the levels of percentages for a point, taking point in as index 0 but displaying back as index 1'''
    if point != 0:
        point = point - 1
    value = report.sections[section][point][0]
    value2 = report.sections[section1][point][0]
    print 'The percentage for point ' + str(point) + ' out of ' + str(section) + ' and ' + str(section1) + ' is: ' + str(value / value2 * 100) + '% at ' + time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime(report.sections[section][point][0]))
    return ((value / value2) * 100)




