class quadrati:
    #attributi
    #self.variabile    variabile come un altra            self.nomevariabile
    #self._variabile  variabile sicura self._nomevariabile
    #self.__variabile variabile sicura che cambia nome  --->self._nomeclasse__nomevariabile
    
    def __init__(self,l):
        self.__lato=l

    #metodi    
    def perimetro(self):
        p=self.__lato *4
        return p

    def area(self):
        a= self.__lato **2
        return a
  

q1= quadrati(9)


print(q1.perimetro())
print(q1.area())


q2= quadrati(20)
print(q2.perimetro())
print(q2.area())
