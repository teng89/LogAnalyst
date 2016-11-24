# encoding=utf-8
"""
StartTime for catch eslworking restart in logfile 
"""
import re
from AbsAnalyst import AbsAnalyst


class StartTime(AbsAnalyst):
	"""docstring for StartTime"""
	ENTRY_REGEXP =  re.compile("ESL system starting")
	ANALIZY_REGEXP =  re.compile("(\w\.\w.\w\_rc\w[\_sp\w]*)")

	def __init__(self):
		self.collect=[]
		self.current_line = None

	def isMatch(self, line):
		self.current_line = line
		return re.search(self.ENTRY_REGEXP,line)

	def doStatistic(self):
		print "系统重启时间"
		print self.collect 

	def doAnalyse(self):
		_t = re.findall(self.LOGTIME_REGEXP, self.current_line)
		_p = re.findall(self.ANALIZY_REGEXP, self.current_line)
		self.collect.append([_t, _p])
