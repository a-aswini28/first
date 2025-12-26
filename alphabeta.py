Class Alpha:
  def fun1(self):
print("i am an alpha")
Class Beta(alpha):
  def fun2(self):
print("i am an beta")
Class gamma(beta):
pass
g=gamma()
g.fun1()
g.fun2()
print(dir gamma)

