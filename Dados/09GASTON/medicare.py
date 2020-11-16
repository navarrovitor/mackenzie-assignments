import matplotlib.pyplot as plt
from pylab import plot, show, legend

anos = [2010, 2011, 2012, 2013, 2014]
florida = [110970, 112400, 111630, 109790, 109430]
eua = [95830, 97190, 96860, 95410, 95880]


plot(anos, florida, anos, eua)
plt.title("Reembolso de benefício saúde na Florida vs EUA")
plt.ylabel("Reembolso por inscrito")
plt.legend(["Florida", "EUA"])
show()