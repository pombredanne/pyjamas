from UnitTest import UnitTest
import time
from write import write, writebr

class A(object):

    def __init__(self, x):
        self.x = x

    def getX(self):
        return self.x

def fib(n):
    if n<3:
        return 1
    return fib(n-2)+fib(n-1)

int0 = 0
int1 = 1
int2 = 2
int3 = 3
int10 = 10
int100 = 100

def fibc(n):
    if n<int3:
        return int1
    return fibc(n-int2)+fibc(n-int1)

class LoopTest(UnitTest):

    def testLoop1(self):
        t1 = t0 = time.time()
        n = 1000
        a = A(1)
        m = 0;
        while t1 - t0 == 0:
            m += 1
            for i in range(n):
                x = a.getX()
            t1 = time.time()
        dt = t1 - t0
        writebr("Loop1: %.2f/sec" % (n*m/dt))

    def testLoop2(self):
        t1 = t0 = time.time()
        n = 100
        m = 0
        while t1 - t0 == 0:
            m += 1
            for i in range(n):
                fib(10)
            t1 = time.time()
        dt = t1 - t0
        writebr("Loop2: %.2f/sec" % (n*m/dt))

    def testLoop3(self):
        t1 = t0 = time.time()
        n = 100
        m = 0
        while t1 - t0 == 0:
            m += 1
            for i in range(n):
                fibc(int10)
            t1 = time.time()
        dt = t1 - t0
        writebr("Loop3: %.2f/sec" % (n*m/dt))

if __name__ == '__main__':
    l = LoopTest()
    l.run()
