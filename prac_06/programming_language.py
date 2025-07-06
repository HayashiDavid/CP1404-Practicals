class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection=bool, year=0):
        """Function classes"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self. year= year

    def __str__(self):
        """ Return the string"""
        return f"{self.name}, {self.typing} typing, Reflection = {self.reflection}, First appeared in {self.year}"

    def __is_dynamic(self):
        """ Check whether it is dynamic or not"""
        if self.typing == "Dynamic":
            return True
        else:
            return False
