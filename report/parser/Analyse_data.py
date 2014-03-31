'''
python 2.6
Created on 29 Mar 2014
@version: 1.0.0
@author: darrendaly
'''

def calculateAverages(section, report):
    '''Calculates the average value of occurrences in the specified section'''
    total = 0
    for counter in range(report.size):
        total += report.sections[section][counter][0]
        avg = total / report.size
    print section + " average value is: " + str(avg) + " and the total value is: " + str(total)
  
def findMins(section, report):
    '''find the minimum value in the specified section'''
    for counter in range(report.size):
        value = report.sections[section][counter][0]
        if counter == 0:
            minimum = value
        elif minimum > value:
            minimum = value
    print section + " minimum value = " + str(minimum)
            
def findMaxs(section, report):
    '''find the maximum value in the specified section'''
    for counter in range(report.size):
        value = report.sections[section][counter][0]
        if counter == 0:
            maximum = value
        elif maximum < value:
            maximum = value
    print section + " maximum value = " + str(maximum)
          
                    