import Queue

class AbsAnalysier(object):
	"""docstring for AbsAnalysier"""
	
	def __init__(self, regexp="*"):
		super(AbsAnalysier, self).__init__()
		self.entry_regexp = regexp
		self.data_queue = Queue.Queue()

	def isMatch(regexp=""):
		raise NotImplemented

	def statistics(**keyagrs):
		raise NotImplemented

