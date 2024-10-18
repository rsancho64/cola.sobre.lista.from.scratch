#! /usr/bin/python3

class cola:

    __data = []
    __maxSize = None  

    def __init__(self, size = 10):
        self.__maxSize = size

    # def len(self) -> int: 
    #     return len(self.__data)

    def __len__(self):
        return len(self.__data)

    def __str__(self) -> str:
        answ = "<"
        # answ += f"{self.len()} de {self.__maxSize}, {self.__data}"
        answ += f"{len(self)} de {self.__maxSize}, {self.__data}"
        if self.esVacia(): answ += "VACIA"
        if self.esLlena(): answ += "LLENA"
        answ += ">"
        return answ

    def esVacia(self) -> bool:
        return len(self) == 0

    def esLlena(self) -> bool:
        return len(self) == self.__maxSize
    
    def enqueue(self, something):
        if not self.esLlena():
            self.__data.append(something)
        else:
            raise OverflowError (f'queue: ya estoy llena')

    def dequeue(self) -> object:
        if len(self) == 0:
            raise ValueError (f'queue: esta vacia')
        else:
            item = self.__data[0]
            self.__data = self.__data[1:]
            return item

if __name__ == "__main__":

    c = cola(4)
    print(c)

    try:
        c.enqueue(11)
        print(c)

        c.enqueue(22)
        print(c)    

        c.enqueue(33)
        print(c)

        c.enqueue(44)
        print(c)

        # c.enqueue(55)
        # print(c)

        item = c.dequeue()
        print(item, c)

        item = c.dequeue()
        print(item, c)

        item = c.dequeue()
        print(item, c)

        item = c.dequeue()
        print(item, c)

        item = c.dequeue()
        print(item, c)

        print("FINAL DEL TRY")

    except OverflowError:
        print("no entro, estaba llena")
    except ValueError:
        print("nada sale, estaba vacia")

