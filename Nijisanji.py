class Nijisanji:

    def __init__(self,name,color,department):
        self.__name = name
        self.__color = color
        self.__department = department

    def _showData(self):
        print(f'Department : {self.__department} \nName : {self.__name} \nColor : {self.__color}')