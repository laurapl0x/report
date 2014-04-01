'''
python 2.6
Created on 31 Mar 2014
@version: 1.0.0
@author: darrendaly
'''

from report import Report
import Analyse_data

report = Report()

for section in report.sections:
    print 'the average value for ' + section + ': ' + str(Analyse_data.calculateAverages(section, report))

print ' '

for section in report.sections:
    print 'the maximum value for ' + section + ': ' + str(Analyse_data.findMaxs(section, report))
    
print ' '  
  
for section in report.sections:
    print 'the minimum value for ' + section + ': ' + str(Analyse_data.findMins(section, report))
    
print ' '

print 'at ' + str(Analyse_data.checkAveragePercentage('Empty Responses', 'Total DSP Requests', report, 5, 20)) + '%'

print ' '

Analyse_data.getPointPercentage('Empty Responses', 'Total DSP Requests', report, 1, 10, 30)
Analyse_data.getPointPercentage('Empty Responses', 'Total DSP Requests', report, 50, 10, 30)
Analyse_data.getPointPercentage('Empty Responses', 'Total DSP Requests', report, 144, 10, 30)


