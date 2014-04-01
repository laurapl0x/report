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

'''    
print Analyse_data.calculateAverages('SLA timeout', report)
print Analyse_data.calculateAverages('Empty Responses', report)
print Analyse_data.calculateAverages('Bid Response', report)
print Analyse_data.calculateAverages('Error Responses', report)
print Analyse_data.calculateAverages('Internal Errors', report)
print Analyse_data.calculateAverages('Total DSP Requests', report)
print Analyse_data.calculateAverages('Unmatched requests', report)
'''
print ' '

for section in report.sections:
    print 'the maximum value for ' + section + ': ' + str(Analyse_data.findMaxs(section, report))
    
'''
print Analyse_data.findMaxs('SLA timeout', report)
print Analyse_data.findMaxs('Empty Responses', report)
print Analyse_data.findMaxs('Bid Response', report)
print Analyse_data.findMaxs('Error Responses', report)
print Analyse_data.findMaxs('Internal Errors', report)
print Analyse_data.findMaxs('Total DSP Requests', report)
print Analyse_data.findMaxs('Unmatched requests', report)
'''
print ' '    
for section in report.sections:
    print 'the minimum value for ' + section + ': ' + str(Analyse_data.findMins(section, report))
    
'''
print Analyse_data.findMins('SLA timeout', report)
print Analyse_data.findMins('Empty Responses', report)
print Analyse_data.findMins('Bid Response', report)
print Analyse_data.findMins('Error Responses', report)
print Analyse_data.findMins('Internal Errors', report)
print Analyse_data.findMins('Total DSP Requests', report)
print Analyse_data.findMins('Unmatched requests', report)
'''
print ' '

print "SLA timeout is " + str(Analyse_data.getPercentage('SLA timeout', 'Error Responses', report)) + "% of Error Responses"

