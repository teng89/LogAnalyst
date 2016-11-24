# encoding=utf-8
import sys
import Analysts
############BUGGLY AUTOLOAD PARA ###############
Analystslist = []
for x in Analysts.__dict__:
	kls = getattr(Analysts, x, None) 
	if kls and type(kls) == type(type) \
		and issubclass(kls, Analysts.AbsAnalyst.AbsAnalyst):
		Analystslist.append(kls())
############BUGGLY AUTOLOAD PARA ###############

def main(fp):
	with open(fp,"r") as logfile:
		for line in logfile:
			for Analyst in Analystslist:
				try:
					if Analyst.isMatch(line):
						Analyst.doAnalyse()
				except Exception as e:
					print e
	for x in Analystslist:
		x.doStatistic()
if __name__ == '__main__':
	main(sys.argv[1])



