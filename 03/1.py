print(sum((sum({*l[:len(l)//2]}&{*l[len(l)//2:]})+20)%58 for l in open("i","rb")))
