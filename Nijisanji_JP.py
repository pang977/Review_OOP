from Nijisanji import Nijisanji


class Nijisanji_JP(Nijisanji):
    __department = "Nijisanji JP"
    def __init__(self,name,color,wave,YnJP):
        super().__init__(name,color,self.__department)
        self.__wave = wave
        self.__YnJP = YnJP
    
    def _showData(self):
        super()._showData()
        print(f'Wave : {self.__wave} \nJP : {self.__YnJP}')