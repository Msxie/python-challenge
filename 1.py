message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
code = 'map'
def yiwei(mes):
	for item in mes:
		if item == 'y':
			item = 'a'
		elif item == 'z':
			item  = 'b'
		else:
			item = chr(ord(item)+2)
		print item,
yiwei(message)
print ''
yiwei(code)