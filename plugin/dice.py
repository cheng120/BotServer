from argparse import Namespace


from random import randint


class Dice:
    base_num = 0
    def __init__(self,number) -> None:
        self.base_num = number #初始化 面数
        pass
    
    def GetNumber(self) :
        print(self.base_num)
        res = randint(1,self.base_num)
        return res
    