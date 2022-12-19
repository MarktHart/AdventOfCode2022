a=open('i').read();print([i+4for i in range(len(a))if len({*a[i:i+4]})>3][0])
