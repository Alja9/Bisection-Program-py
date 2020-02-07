iterasi = 0
a = 0.0
b = 1.0
def pers(x):
       return x**3 - 2*(x**2) + 6*x - 4.0
print("Iterasi\t\ta\t\tb\t\tNilai Tengah")
print("-"*60)
while((b-a) >= 0.01):
       c = (a+b)/2
       print("%d\t\t%f\t%f\t%f" % (iterasi, a, b, c))
       if(pers(c)==0.0):
              break
       if(pers(c)*pers(a)<0):
              b = c
       else:
              a = c
       iterasi+=1
print("DONE")
