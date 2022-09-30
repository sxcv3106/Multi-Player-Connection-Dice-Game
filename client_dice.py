import random

class dice:

    def __init__(self):                     #初始化
        self.count = [0, 0, 0, 0, 0, 0]
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
    
    def throw(self):                        #骰骰子
        self.a = random.randint(1,6)
        self.b = random.randint(1,6)
        self.c = random.randint(1,6)
        self.d = random.randint(1,6)
        for i in range(1, 7):
            if (self.a == i):
                self.count[i-1] += 1
            if (self.b == i):
                self.count[i-1] += 1
            if (self.c == i):
                self.count[i-1] += 1
            if (self.d == i):
                self.count[i-1] += 1
    def setcount(self):                     #歸零
        self.count = [0, 0, 0, 0, 0, 0]
        
    def ifone(self):                        #判斷豹子
        bl = False
        for i in range(1, 7):
            if (self.count[i-1] == 4):
                bl = True
        return bl   
    
    def ifredo(self):                       #判斷是否重骰
        one = 0
        for i in range(1, 7):
            if (self.count[i-1] == 1):
                one += 1
        if (one == 4):
            return True
        return False
    
    def cal(self):                          #計算大小
        one = 0
        two = 0
        three = 0
        th1 = 0
        th2 = 0
        for i in range(1, 7):
            if (self.count[i-1] == 1):
                th1 = i
                one += 1
            if (self.count[i-1] == 2):
                th2 = i
                two += 1
            if (self.count[i-1] == 3):
                th2 = i
                three += 1
        if (three == 1):
            return th1+th2
        elif (one == 2):
            for i in range(1, 7):
                if (self.count[i-1] == 1):
                    th2 = i
                    break
            return th1+th2
        else:
            return th2*2    
        
class clistr:
    
    def dicetostring(di):                   #判斷結果
        if (not dice.ifredo(di)):
            if (dice.ifone(di)):
                return True,"c1: 13"
            else:
                return True,"c1: "+str(dice.cal(di))
        return False, "redo"
    
    def talk(account, line):                #聊天
        return account+": "+line
        
    def isres(ss):                          #是否為結果
        sub = ""
        e = False
        index_ss = ss.find("r1: ")
        if (index_ss >= 0):
            e = True
            sub = ss[index_ss+4:]
        return e, sub
            
