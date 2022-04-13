from Nijisanji import Nijisanji

class Nijisanji_EN(Nijisanji):

    __department = "Nijisanji EN"
    def __init__(self,name,color,group):
        super().__init__(name,color,self.__department)
        self.__group = group 
    
    def _showData(self):
        super()._showData()
        print(f'Group : {self.__group}')