from matplotlib import pyplot as p
pro_na=["intel","amd","snapdragon","tensor"]
use=[200,100,250,50]
p.bar(pro_na,use,color='blue',width=0.2)
p.xlabel("processors"),p.ylabel("noof users")
p.title("processors users in a community")
p.show()