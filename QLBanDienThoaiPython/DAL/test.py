class test:
    abc = None

    def __init__(self):
        global abc
        abc = "Tran Van Dong"
    
    def getAbc(self):
        global abc
        return abc

t1 = test()
name = t1.getAbc()
print(name)
