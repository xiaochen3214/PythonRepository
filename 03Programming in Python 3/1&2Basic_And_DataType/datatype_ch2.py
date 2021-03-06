#!/usr/local/bin/python3
# coding:utf-8

z = -80 + 20j
print(z)
print(z.real,z.imag)

import decimal
a = decimal.Decimal(1233)
b = decimal.Decimal(2344)
print( a + b )

print(23/1.05)
print(decimal.Decimal(23) / decimal.Decimal("1.05"))

text = """ test test "test" test1
		test2\
		test3 test"""
print(text)

a = "single 'quotes' are fine;\"doubles\" must be escaped."
b = 'single \'quotes\' must be secaped;"doubles" are fine.'
print(a,'\n#',b)


import re
def test_whether_is_phone(phonestring):
	phonePattern = re.compile(r"^((?:[0\d+[]])?\s*\d+(?:-\d+)?)$")
	# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
	match = phonePattern.match(phonestring)	 
	if match:
	    # 使用Match获得分组信息
	    print(match.group())
	else:
		print('not matched')

test_whether_is_phone('13911634999')
test_whether_is_phone('1391163test')

t = "This is not the best way to join two long strings" +\
  " together "
s = ("this is the nice way to"
	" join two long strings")
print(t)
print(s)

#unicode
#打出欧元符号 在osx：http://www.macgg.com/archives/6490.html
euros = "€\N{euro sign}\u20AC\U000020AC"
print(euros)
print(ord(euros[0]))
print(ord(euros[1]))
print(hex(ord(euros[0])))
print(hex(ord(euros[1])))

s = "test:" + chr(8364)+chr(0x20ac)
print('s=',s)
print(ascii(s))

#compare string
from unicodedata import normalize

print( normalize('NFD', u'\u00C7'),end = ""  )
print( normalize('NFC', u'C\u0327') ,end = "")
print( normalize('NFKD', u'C\u0327') ,end = "")
print()
s = 'Spicy Jalapeño'
print(ord(s[13]))
print( ord(normalize('NFKD', s)[13] ))




treatises =['abc','def','gh']
print("".join(treatises))
print("-<>-".join(treatises))

record = "Leo Tolstory*123*1910-01-10*2015-01-22"
fields = record.split("*")
print(fields)
born = fields[2].split("-")

died = fields[3].split("-")
print(born,died)
print("lived about",int(died[0]) - int(born[0]),"years")

#http://stackoverflow.com/questions/10329290/python-3-x-using-string-maketrans-in-order-to-create-a-unicode-character-tran
intab = "abcde"
outtab = "12345"
trantab = str.maketrans(intab,outtab)
str = "this is a test of trans"
print(str)
print(str.translate(trantab))

print("The movel '{0}' was published in {1}".format("Hard Times",1854));
x = "three"
s = "{0} {1} {2}"
s = s.format("The",x,"tops")
print(s)
print("{who} turned {age} this year.".format(who="She",age=88))
print("The {who} was {0} last week".format(12, who = "boy"))
stock = ["paper","envelopes","notepads"]
print("We have {0[1]} and {0[2]} in stock".format(stock))

d = dict(animal="elephant",weight=12000)
print("The {0[animal]} weighs {0[weight]}kg.".format(d))

import math,sys
print("math.i=={0.pi} sys.maxunicode=={1.maxunicode}".format(math,sys))
print("从python3.1开始 可以忽略字段名:{} {} {}".format("Python","can","count"))

#another way
element = "Silver"
number = 47
print("Element {number} is {element}".format(**locals()))
print("The {animal} weighs {weight}kg. ---@^@".format(**d))

#ascii
print("{0} {0!s} {0!a}".format(decimal.Decimal("10.2")))
s = "The sword of truth"
print("{0}".format(s))
print("{0:30}".format(s))
print("{0:>30}".format(s))
print("{0:^30}".format(s))
print("{0:-^30}".format(s))
print("{0:<30}".format(s))
print("{0:.10}".format(s))

print("{0:0=12}".format(1234))
print("{0:0=12}".format(-1234))
print("{0:012}".format(1234))
print("{0:012}".format(-1234))

#符号实例
print("[{0: }][{1: }]".format(123,-456))
print("[{0:+}][{1:+}]".format(123,-456))
print("[{0:-}][{1:-}]".format(123,-456))

print("{0:b} | {0:o} | {0:X}".format(64))
print("{0:#b} | {0:#o} | {0:#X}".format(64))
print("{0:,} | {0:*>13,}".format(int(2.3943e6)))

print("{:*>20}{:*<20}".format('locale',''))
import locale
# “”时候python自动确定，以c为默认场所
locale.setlocale(locale.LC_ALL, "")

x,y = (1234567890, 12345.6789)
locale.setlocale(locale.LC_ALL, "C")
c ="{0:n} {1:n}".format(x,y)
print(c)
locale.setlocale(locale.LC_ALL,"en_US.UTF-8")
en = "{0:n} {1:n}".format(x,y)
print(en)
locale.setlocale(locale.LC_ALL,"de_DE.UTF-8")
de = "{0:n} {1:n}".format(x,y)
print(de)

amount = (10 ** 3) * math.pi
print("[{0:12.2e}][{0:12.2f}]".format(amount))
print("[{0:*>12.2e}] [{0:*>12.2f}]".format(amount))
print("{:,.6f}".format(decimal.Decimal("123.123412341234")))
print("{:,.4f}".format(3.21321e2-4.5678956789e3j))



# import pdb
# pdb.set_trace()
import unicodedata
def print_unicode_table(word):
	print("decimal hex chr {0:^40}".format("name"))
	print("--- --- {0:-<40}".format(""))

	code = ord(" ")
	end = sys.maxunicode

	while code < end:
		c = chr(code)
		name = unicodedata.name(c,"*** unknown ***")
		if word is None or word in name.lower():
			# print('{0:^3c} '.format(code))
			try:
				print("{0:7} {0:5X} {0:^3c} {1}".format(code,name.title()))
			except:
				print("Error in print_unicode_table")
		code += 1

word = None
if len(sys.argv) >1:
	if sys.argv[1] in ("-h","--help"):
		print("usage:{0}[string]".format(sys.argv[0]))
		word = 0
	else:
		word = sys.argv[1].lower()
if word !=0:
	print_unicode_table(word)






