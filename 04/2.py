import re;print(sum(1-eval(re.sub('(\d+).?'*4,r'\4<\1>\3or \2<\3>\1',l))for l in open('i')))
