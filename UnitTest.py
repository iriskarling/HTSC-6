from Generate import Interpreter,rpnInterpreter,SQLInterpreter
import pytest

def transferOp(string):
    string = string.replace(" ","")
    string = string.replace('AND','*')
    string = string.replace('OR','+')
    string = string.replace("NOT",'^')
    return string

def test_Case1():
    teststring = "NOT(CompanyName =\'Htsc\')AND NOT((Age = 30 )AND(SEX = \'Man\'))"
    teststring = teststring.replace(" ","")
    transfer_res = transferOp(teststring)
    RPN = rpnInterpreter(transfer_res)
    res = RPN.transfer()
    SQL = SQLInterpreter(res,"Customer")
    final_res = SQL.transfer()
    assert final_res == "select * from Customer where (NOT (CompanyName='Htsc')) AND (NOT ((Age=30) AND (SEX='Man')))"
    
    

def test_Case2():
    teststring = "(companyName == \'HTSC\') OR ((AGE >30) AND ( SEX != \'MALE\'))"
    teststring = teststring.replace(" ","")
    transfer_res = transferOp(teststring)
    RPN = rpnInterpreter(transfer_res)
    res = RPN.transfer()
    SQL = SQLInterpreter(res,"Customer")
    final_res = SQL.transfer()
    assert final_res == "select * from Customer where (companyName='HTSC') OR ((AGE>30) AND (SEX!='MALE'))"
    
    

def test_Case3():
    teststring = "(companyName == \'HTSC\') AND ((AGE >30) OR ( SEX != \'FEMALE\'))"
    teststring = teststring.replace(" ","")
    transfer_res = transferOp(teststring)
    RPN = rpnInterpreter(transfer_res)
    res = RPN.transfer()
    SQL = SQLInterpreter(res,"Customer")
    final_res = SQL.transfer()
    assert final_res == "select * from Customer where (companyName='HTSC') AND ((AGE>30) OR (SEX!='FEMALE'))"
    
    

    

if __name__ == "__main__":
    
    pytest.main(["UnitTest.py"])
    
    