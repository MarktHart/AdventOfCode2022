import re;print(sum(eval(re.sub('(\d+).?'*4,r'\3<=\1<=\2<=\4or \1<=\3<=\4<=\2',l))for l in open('i')))
