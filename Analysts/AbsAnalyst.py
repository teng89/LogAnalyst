import re
import Queue

class AbsAnalyst(object):
	"""docstring for AbsAnalyst"""
	LOGTIME_REGEXP = re.compile("(?P<log_time>\w{4}-\w{2}-\w{2} \w{2}:\w{2}:\w{2})")
	
	def __init__(self):
		raise NotImplemented

	def isMatch(self, line):
		raise NotImplemented

	def doStatistic(self):
		raise NotImplemented

	def doAnalyse(self):
		raise NotImplemented