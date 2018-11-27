import re
def IsInteger(s):
	c=re.compile('?=[\d]')
	d=re.match(c,s)
	if d:
		return True
	return False
def IsFloat(s):
	a=re.compile('?=[\d+.\d+]')
	d=re.match(c,s)
	if d:
		return True
	return False
def HasVowel(s):
	c=re.compile('.*(?=[aeiouAEIOU]).*')
	d=re.match(c,s)
	if d:
		return True
	return False
def IsHex(s):
	c=re.compile('.*(?=[0-9,a-f]).*')
	d=re.match(c,s)
	if d:
		return True
	return False
def IsDate(s):
	c=re.compile('.*(?=[\d\d-\d\d-\d\d\d\d]).*')
	d=re.match(c,s)
	if d:
                                 return True
                return False
def IsValidPassword(s):
        c=re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{8,16})')
        d=re.match(c,s)
        if d:
                return True
        return False
def IsValidEmail(s):
        c=re.compile('^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$')
        d=re.match(c,s)
        if d:
                return True
        return False

st=raw_input("Enter the string: ")
print "Contains Intiger : ",IsInteger(st)
print "Contains Float : ",IsFloat(st)
print "Contains Vowels : ",HasVowel(st)
print "Contains Hex : ",IsHex(st)
print "Strong Password : ",IsValidPassword(st)
print "Valid Email : ",IsValidEmail(st)
