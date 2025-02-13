class Country:
    def __init__(self, name, pop, area=None, language=None):
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__language = language

    def print_info(self):
        if self.__area == None:
            print(f"I {self.__name} bor det {self.__population} miljoner invånare")
        else:
            print(f"I {self.__name} bor det {self.__population} miljoner invånare. Arean är {self.__area} m2")

        if self.__language is not None:
            print(f"Språken i landet är: {','.join(self.__language)}")

    def add_language(self, language: list):
        self.__language = language


se = Country("Sverige", 10.5, 500)
se.add_language(['svenska', 'finska'])

no = Country("Norge", 5.5)

se.print_info()
