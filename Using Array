class Array:
    def __init__(self, dtype, size):
        self.__dtype = dtype
        self.__size = size
        self.array = [None]*self.__size

    def shift(self):
        
        for index in range(self.__size -1, 0, -1):
            if self.array[index] is not None and self.array[index-1] is None:
                self.array[index-1] = self.array[index]
                self.array[index] = None

    def add(self, value, index):
        if isinstance(value, self.__dtype):
            if None in self.array[index:]:
                for posn in range(self.__size - 1, index ,-1 ):
                    if self.array[posn] is None and self.array[posn-1] is not None:
                       self.array[posn] = self.array[posn - 1]
                       
                       self.array[posn-1] = None
                self.array[index] = value
            else:
                raise Exception("No space")
        self.shift()           

    def delete(self, index):
        self.array[index] = None
        self.shift()

    def reverse(self):
        for each in range(self.__size // 2):
            temporary = self.array[each]
            self.array[each] = self.array[self.__size - 1]
            self.array[self.__size - 1] = temporary
            self.__size -= 1

    def printout(self):
        return self.array

       
        


class PythonStack(Array):
    def __init__(self, datatype, size):
        super().__init__(datatype, size)
        self.__top = -1 

    def push(self, element):
            self.add(element, self.__top + 1)
            self.__top +=1

    def pops(self):
        self.delete(self.__top)
        self.__top -= 1

    def showtop(self):
        return self.array[self.__top]

    def size(self):
        if self.isEmpty() is False:
            count = 0
            for key in self.array:
                if key is not None:
                    count += 1
                else:
                    break
            return count
        else:
            return 0

    def isEmpty(self):
        if self.array[0] is None:
            return True
        else:
            return False

    def isFull(self):
        if self.size - 1 == self.__top:
            return True
        return False

    def printout(self):
        return self.array

from cgitb import html
from logging import raiseExceptions


class Html(PythonStack):
    def __init__(self, files):
        with open(files, "r") as self.refer:
            self.refline = self.refer.readlines()
        super().__init__(str, len(self.refline) * 5)
        

    def handler(self):
        self.open_tag = ""
        self.close_tag = ""
        for line in range (len(self.refline)):
            for value in range(0, len(self.refline[line])):
                
                if (self.refline[line][value] == '<') and (self.refline[line][value + 1] != '/'):
                    if ('<'  in self.open_tag):
                        raise Exception("Error at line "+ str(line +1) + " unepected '<' for openning tag "+ self.open_tag)
                    
                    elif len(self.open_tag) == 0:
                        self.open_tag += self.refline[line][value]
                    else:
                        pass
                if (self.refline[line][value] == '<' and self.refline[line][value + 1] == '/'):
                    if '<' in self.close_tag:
                        raise Exception("Error at line "+ str(line+1) + " unespected '<' for closing tag "+self.close_tag)
                    else:
                        self.close_tag += self.refline[line][value]
                if self.refline[line][value] not in "<>/":
                    if self.refline[line][value] == " ":
                        if len(self.open_tag) > 1:
                            self.open_tag += '>'
                            self.push(self.open_tag)
                            self.open_tag = ""
                    
                    elif len(self.close_tag)>=2 :
                        
                        self.close_tag += self.refline[line][value]
                        
                    elif len(self.open_tag) >= 1 and ((value + 1) < len(self.refline[line])):
                        self.open_tag += self.refline[line][value]
                    
                        
                    elif len(self.open_tag) >= 1 and self.refline[line][value +1] == '<':
                        raise Exception("Errors at line"+ str(line + 1) + "unexpected '<'")
                    
                elif self.refline[line][value] == '>' :
                    
                    if len(self.close_tag) > 2 :
                        self.close_tag += self.refline[line][value]
                        if super().size() == 0:
                            raise Exception("Error at line " + str(line + 1) + " cannot open with closing tag " + self.close_tag)
                        
                        checker = ""
                        for character in super().showtop():
                            if character != " " or character != '>':
                                checker += character
                            elif character == " " or character == '>':
                                break
                        
                        if checker[1:len(checker)-1] == self.close_tag[2:len(self.close_tag) - 1]:
                            
                            self.pops()
                            
                            self.close_tag = ""
                            continue
                        raise Exception("Error at line "+ str(line+1) +" "+ super().showtop()+" cannot be closed with " + self.close_tag)
                    elif  len(self.open_tag) > 1 and self.open_tag[0] == '<':
                        self.open_tag += self.refline[line][value]
                
                        
                        self.push(self.open_tag)
                        self.open_tag = ""
                        continue
                    
                elif self.refline[line][value] == '/':
                    
                    if len(self.close_tag) ==1 and self.close_tag[0] == '<':
                        self.close_tag += '/'
                    else:
                        pass
    def validator(self):
        if super().size() == 0:
            return "your code is neat"
        else:
            return "it aint good end-tags required for " + super().showtop()
                    
                    
    def Print(self):
        return super().printout()

trial = Html("givintry.html")
trial.handler()
print(trial.validator())
