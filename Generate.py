#!/usr/bin/python  
#-*-  coding:GB2312  -*-
import re,string

def StringTolist(string):   
    tmp = []
    res = []
    for i in range(len(string)):
        if string[i] == '(':
            tmp.append(string[i])
            while string[i+1] != ')':
                i += 1
                tmp.append(string[i])
            if string[i+1] == ')':
                i += 1
                tmp.append(string[i])
            res.append(''.join(tmp))
            tmp =[]
        elif string[i] in ['+','^','*']:
            res.append(string[i])   
    return res     

class Stack(object):
    '''堆栈'''
    def __init__(self):
        self._stack = []
        
    def pop(self):
        return self._stack.pop()
    
    def push(self, x):
        self._stack.append(x)

    def is_null(self):
        if len(self._stack) == 0:
            return True
        return False

class Interpreter():
    def __init__(self,string):
        super().__init__()
        self.string = string
    def transfer(self):
        pass



class rpnInterpreter(Interpreter):
    def __init__(self,string):
        super().__init__(self)
        self.string = string
    def transfer(self): # to generate the reverse polish notation
        pro = dict(zip('^*+#', [3,2,1,0]))
        out = []
        s = Stack()
        s.push('#')
        for i in range(len(self.string)):
            if self.string[i] == '(':            
                s.push(self.string[i])
                if self.string[i+1] != "(":
                    out.append('(')
            elif self.string[i] == ')':          
                t = s.pop()
                if self.string[i-1] != ")":
                    out.append(')')
                while t != '(':
                    out.append(t)
                    t = s.pop()
            elif self.string[i] in '^*+':     
                while True:
                    t = s.pop()
                    if t == '(':    
                        s.push(t)
                        break
                    if pro[self.string[i]] <= pro[t]:
                        out.append(t)
                    else:
                        s.push(t)
                        break
                s.push(self.string[i])
            else:                  
                out.append(self.string[i])
            
        while not s.is_null():
            out.append(s.pop())     
        return ''.join(out[:-1])
        
class SQLInterpreter(Interpreter):
    def __init__(self,string,tableName):
        super().__init__(self)
        self.string = string
        self.tableName = tableName

    def transfer(self):
        final = []
        res = StringTolist(self.string)
        basesql = "select * from " + self.tableName +" " +"where "
        for i in range(len(res)):
            if res[i] in ['+','^','*']:
                if res[i] == '^':
                    tmp = final.pop()
                    final.append('('+res[i]+" "+tmp+')')
                elif res[i] == '+' or res[i] == '*':
                    tmp = final.pop()
                    tmp2 = final.pop()
                    final.append('('+tmp2 +" "+ res[i] +" "+ tmp+')')
            else:
                final.append(res[i])
        final_str = final[0].replace("==","=")
        final_str = final_str.replace("^","NOT")
        final_str = final_str.replace("+","OR")
        final_str = final_str.replace("*","AND")
        return basesql + final_str[1:-1]
    


