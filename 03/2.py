print(sum((10+sum({*l}&{*k}&{*m}))%58 for k,l,m in zip(*[iter(open("i","rb"))]*3)))
