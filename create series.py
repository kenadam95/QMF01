import os

portfolio = ['AGG','ASM','CCL','CIG','CLG','CRE','D2D','DRH','DTA','DXG','FDC','FIR','FLC','HAR','HDC','HPX','HQC','HTN','ITC','KBC','KDH','KOS','LDG','LEC','LHG','NBB','NLG','NTL','NVL','NVT','PDR','PTL','QCG','SCR','SGR','SJS','SZL','TDC','TDH','TEG','TIX','TN1','VHM','VIC','VPH','VPI','VRE']

for i in range(len(portfolio)):
	x = portfolio[i]
	print('series r',x,' = l',x,' - f',x)
