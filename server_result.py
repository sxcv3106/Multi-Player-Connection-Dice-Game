class result:
    
    def __init__(self):                             #初始化
        self.poli = []
        self.nali = []
        self.reli = []
    
    def inp(self, port):                            #加port
        self.poli.append(port)
        self.nali.append("player")
        self.reli.append(0)
    
    def inn(self, port, name):                      #加名字
        try:
            i = self.poli.index(port)
            self.nali[i] = name
        except ValueError:
            print("port didn't come in!")

    def inr(self, port, res):                       #加結果
        try:
            i = self.poli.index(port)
            #print("here",res)
            res = int(res)
            #print("here2",res)
            self.reli[i] = res
            #print("here3")
        except ValueError:
            print("port didn't come in!")
    
    def rtnum(self):                                #回傳玩家數量
        return len(self.poli)
    
    def clnum(self):                                #回傳骰了的玩家數量
        count = 0
        for i in range(0, len(self.reli)):
            if (self.reli[i] != 0):
                count += 1    
        return count
    
    def delply(self, name):
        try:
            i = self.nali.index(name)
            self.poli.pop(i)
            self.nali.pop(i)
            self.reli.pop(i)
        except ValueError:
            print("port didn't come in!")
    
    def setzero(self):
        for i in range(0, len(self.reli)):
            self.reli[i] = 0
    
    def findmax(self):                              #找出贏家
        max_value = max(self.reli)
        max_index = self.reli.index(max_value)
        winname = self.nali[max_index]
        if (max_value == 13):
            s = "r1: "+winname+" won! "+"He/She has leopard."
        else: 
            s = "r1: "+winname+" won! "+"He/She has "+str(max_value)+" points."
        return s
    
    def ifres(ss):                                  #找出結果
        subss = ""
        b = False
        index_s = ss.find("c1: ")
        if (index_s >= 0):
            b = True
            subss = ss[index_s+4:]
        return b, subss    