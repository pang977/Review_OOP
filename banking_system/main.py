class User:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_detail(self):
        print("Personal Detail")
        return f"\n Account Name : {self.name} \n Age : {self.age} \n Gender : {self.gender}"
