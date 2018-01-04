#!/usr/bin/env python3
# -*- coding: utf-8 -*-


var = 0
while var < 10:
	num = input(str(var)+"Enter a number:")
	var += 1
	if num == "fuck":
		print ("请注意语言文明")
		break
else:
	print ("超过限制！")