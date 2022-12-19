a=open("i").read();print([i+14for i in range(len(a))if len({*a[i:i+14]})>13][0])
