from Nijisanji import Nijisanji

class Nijisanji_KR(Nijisanji):
    __department = "Nijisanji KR"
    def __init__(self,name,color,wave):
        super().__init__(name,color,self.__department)
        self.__wave = wave

    def _showData(self):
        super()._showData()
        print(f'Wave : {self.__wave}')