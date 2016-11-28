# encoding=utf-8
import re
from AbsAnalyst import AbsAnalyst
from collections import Counter

class UpdateProcess(AbsAnalyst):
	"""docstring for UpdateProcess"""
	UPDATE_ENTRY = re.compile("esl_update|sales_updata_buf|UPDATA_ACK,|ERROR_ACK")
	UPDATE_ACK =  re.compile("\'status\': \'(\S*)\', \'apid\': \'(\S*)\', \'eslid\': \'(\w{2}-\w{2}-\w{2}-\w{2})\'")
	SALES_UPDATA_BUF = re.compile("\'eslid\': \'(\w{2}-\w{2}-\w{2}-\w{2})\', \'template\': \'(\S*)\'")
	ESL_UPDATA = re.compile("\'eslid\': \'(\w{2}-\w{2}-\w{2}-\w{2})\'")

	def __init__(self):
		self.__esl_event__ = {}

	def isMatch(self, line):
		self.current_line = line
		return re.findall(self.UPDATE_ENTRY, line)

	def doStatistic(self):
		with open("eslevent.txt","w+") as f:
			for eslid in self.__esl_event__:
				f.write("\n================================\nTask Eslid:%s, \t\t\t(time), \t\t\t(status\\template\\errorid), \t\t\t(apid\\trigger\\errormsg),"%(eslid))
				f.writelines(self.__esl_event__[eslid])

	def doAnalyse(self):
		_t = re.findall(self.LOGTIME_REGEXP, self.current_line)
	
		# _sales = re.findall(self.SALES_UPDATA_BUF,	self.current_line)
		# if  _sales:
		# 	for eslid, template in _sales:
		# 		if eslid not in self.__esl_event__:
		# 			self.__esl_event__[eslid] = []
		# 		self.__esl_event__[eslid].append("\nUPDATA,\t\t%s,\t\t%s,"%(_t[0], template))
		# 	return

		_ack = re.findall(self.UPDATE_ACK, self.current_line)
		if _ack:
			for status, apid, eslid in _ack:
				if eslid not in self.__esl_event__:
					self.__esl_event__[eslid] = []
				self.__esl_event__[eslid].append("\nACK,\t\t%30s,\t\t%30s,\t\t%30s,"%(_t[0], status, apid))
			return
	
		if "_updat" in self.current_line:
			obj = eval(self.current_line.split(";")[4])
			for x in obj:
				eslid = x.get("eslid",None)
				template = x.get("template","UNKOWN")
				trigger = x.get("_trigger","Normal")
				if eslid: 
					if eslid not in  self.__esl_event__:
						self.__esl_event__[eslid] = []
					self.__esl_event__[eslid].append("\nUPDATA,\t\t%30s,\t\t%30s,\t\t%30s,"%(_t[0], template,trigger))
			return

		if "ERROR_ACK" in self.current_line:
			obj = eval(self.current_line.split(";")[4])
			for x in obj:
				eslid = x.get("eslid",None)
				errormsg = x.get("errmsg","UNKOWN")
				errorid = x.get("errid","UNKOWN")
				if not eslid:
					print "\nno esl for process :",self.current_line
				else:
					if eslid not in  self.__esl_event__:
						self.__esl_event__[eslid] = []
					self.__esl_event__[eslid].append("\nERROR,\t\t%30s,\t\t%30s,\t\t%30s,"%(_t[0], errorid, errormsg))
			return

		print "\nmissing process :",self.current_line