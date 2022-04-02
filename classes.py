
class Grandpa:
    """Class represents grandad"""
    def speakes(self, line):
        print(f"{line}")
    def smokes(self):
        print("'Smokes pipe'")
    def walks(self):
        print("'Walks'")
    def sleeps(self):
        print("'Sleeps'")

class Dad(grandpa):
    """Class represents dad"""
    def works(self):
        print("'Works'")

class Son(dad):
    """Class represents son"""
    def plays_playstation(self):
        print("'plays_playetation'")

class grandson(son):
    """Class represents grandson"""
    def enters_matrix(self):
        print("'enters_matrix'")


grandpa = Grandpa()
dad = Dad()
son = Son()
grandson = Grandson()

dad.sleeps()
son.walks()
grandpa.smokes()
grandson.enters_matrix()
