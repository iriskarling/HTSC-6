#!/usr/bin/python  
#-*-  coding:GB2312  -*-
from Generate import Interpreter,rpnInterpreter,SQLInterpreter
def transferOp(string):
    string = string.replace(" ","")
    string = string.replace('AND','*')
    string = string.replace('OR','+')
    string = string.replace("NOT",'^')
    return string

if __name__ == "__main__":
    string = "(companyName == \"HTSC\") OR ((AGE >30) AND ( SEX != \"MALE\"))"
    teststring = "(A = a)+((B>20)*(C!=A))"
    teststring = "^(A=A)*^((b=a)+(a-c))"
    
    teststring = "(companyName == \'HTSC\') OR ((AGE >30) AND ( SEX != \'MALE\'))"
    teststring ="NOT(CompanyName =\"Htsc\")AND NOT((Age = 30 )AND(SEX = \'Man\'))"
    teststring = teststring.replace(" ","")
    transfer_res = transferOp(teststring)
    RPN = rpnInterpreter(transfer_res)
    res = RPN.transfer()
    print(res)
    SQL = SQLInterpreter(res,"Customer")
    final_res = SQL.transfer()
    print(final_res)