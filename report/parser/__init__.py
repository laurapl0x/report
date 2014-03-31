'''
python 2.6
Created on 31 Mar 2014
@version: 1.0.0
@author: darrendaly
'''

from report import Report
import Analyse_data

report = Report()
report.printSection('SLA timeout')

Analyse_data.calculateAverages('SLA timeout', report)
Analyse_data.calculateAverages('Empty Responses', report)
Analyse_data.calculateAverages('Bid Response', report)
Analyse_data.calculateAverages('Error Responses', report)
Analyse_data.calculateAverages('Internal Errors', report)
Analyse_data.calculateAverages('Total DSP Requests', report)
Analyse_data.calculateAverages('Unmatched requests', report)
print ' '
Analyse_data.findMaxs('SLA timeout', report)
Analyse_data.findMaxs('Empty Responses', report)
Analyse_data.findMaxs('Bid Response', report)
Analyse_data.findMaxs('Error Responses', report)
Analyse_data.findMaxs('Internal Errors', report)
Analyse_data.findMaxs('Total DSP Requests', report)
Analyse_data.findMaxs('Unmatched requests', report)
print ' '
Analyse_data.findMins('SLA timeout', report)
Analyse_data.findMins('Empty Responses', report)
Analyse_data.findMins('Bid Response', report)
Analyse_data.findMins('Error Responses', report)
Analyse_data.findMins('Internal Errors', report)
Analyse_data.findMins('Total DSP Requests', report)
Analyse_data.findMins('Unmatched requests', report)


