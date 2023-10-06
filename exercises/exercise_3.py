# Exercise 3: Write a function to find the greatest common divisor (GCD) of two numbers.

def gcd(a, b):
    # Your code here
    def prime(pi,pb,pc,pg):
  
        if isinstance(pb,int)==True:
                while pi <= pb and pb>0 :
                    if pb%pi == 0:
                        pc = pb/pi
                        pg.append(pc)
                        pi +=1
                    else:
                        pi+=1 
    ii = 1
    ab = a
    c=0
    ag = []
        
    iii = 1
    bb = b
    cb =0
    bg = []
    wtc = 0
    prime(ii,ab,c,ag)
    prime(iii,bb,cb,bg)    
    d = 0
    if len(bg) >= len(ag):
        wtc = len(bg)
        wtl = len(ag)
        wtg = bg
        wtgl = ag
    else:
        wtc = len(ag)
        wtl = len(bg)
        wtg = ag
        wtgl = bg
    s = wtl-1
    mmm = 0
    for i in range(wtc-1,-1,-1):
        for s in range(wtl-1,-1,-1):
            if wtg[i] == wtgl[s]:
                mmm = wtg[i]
    print(mmm)
    return(mmm)
   

# Unit tests
import unittest

class TestExercise3(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(gcd(56, 98), 14)
        self.assertEqual(gcd(54, 24), 6)

if __name__ == '__main__':
    unittest.main()
