import math
import matplotlib.pyplot as ppl


x = [i / 10 for i in range(-50, 50)]

y = [2 * i + math.sin(i)**2 + 3 for i in x]

ppl.plot(x, y, label=r'$2x + \sin^2(x) + 3$')
ppl.title("hello,po!")
ppl.xlabel('x')
ppl.ylabel('y')
ppl.legend()
ppl.grid(True)
ppl.savefig("po.pdf")
ppl.show()

