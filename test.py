from matplotlib import pyplot as plt
import numpy as np

class DRAW_GRAPH():

    def __init__(self,p):
        self.n=20
        self.p=p
        self.data=[]
        self.x=[]

    def cal_binomial(self):
        for i in range(4):
            a=[]
            b=[]
            for i in range(self.n+1):
                n=self.n
                p=self.p
                nCi=self.factorial(n)/(self.factorial(i)*self.factorial(n-i))
                px= nCi * p**i * (1-p)**(n-i)
                a.append(px)
                b.append(i+1)
            self.data.append(list(a))
            self.x.append(list(b))
            self.n=self.n+10
        self.n=20
    def factorial(self, n):
        if n>1:
            return n * self.factorial(n-1)
        else:
            return 1

    def draw_graph(self):
        fig, ax=plt.subplots()
        plt.grid(linestyle = '--')
        plt.title("p=1/6")
        ax.plot(self.x[0], self.data[0],marker='o',markersize=3,label='n=20')
        ax.plot(self.x[1], self.data[1],marker='o',markersize=3,label='n=30')
        ax.plot(self.x[2], self.data[2],marker='o',markersize=3,label='n=40')
        ax.plot(self.x[3], self.data[3],marker='o',markersize=3,label='n=50')

        ax.legend()
        plt.show()

p=1/6
a=DRAW_GRAPH(p)
a.cal_binomial()
a.draw_graph()
