#-*- coding:utf-8 -*-

while True:
	print u'请输入1-100之间的数字：',
	num = raw_input("")
	try:
		if 1< int(num) <100:
			print num
			break
		else:
			print u"输入错误，请核对后重新输入"
	except:
		print u"输入错误，请检查输入是否为数字"
