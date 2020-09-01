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
    teststring = "(companyName == \"HTSC\") OR ((AGE >30) AND ( SEX != \"MALE\"))"
    teststring = "NOT(companyName == \'HTSC\')"
    teststring = teststring.replace(" ","")
    transfer_res = transferOp(teststring)
    RPN = rpnInterpreter(transfer_res)
    res = RPN.transfer()
    print("the result of RPN:",res)
    SQL = SQLInterpreter(res,"Customer")
    final_res = SQL.transfer()
    print("sql result:",final_res)