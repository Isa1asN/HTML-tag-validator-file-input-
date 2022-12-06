class LinkedList:
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
class PythonStack:
    def __init__(self, datatype, size):
        self.head=None
        self.length=0
        
    def push(self,data):
        new_LinkedList = LinkedList(data)
        new_LinkedList.next = self.head
        self.head = new_LinkedList
        self.length += 1
        
    def pops (self):
        if self.length==0:
            return None
        item = self.head
        self.head = self.head.next
        self.length -= 1
        item.next = None
        return item.data
    
    def showtop(self):
        if self.length == 0:
            return None
        return self.head.data
    
    def isEmpty(self):
        return self.length==0
    
    def size(self):
        return self.length
    

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
        
