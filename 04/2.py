import re;print(sum(eval(re.sub('(\d+).?'*4,r'\3<=\2>=\1<=\4',l))for l in open('i')))
