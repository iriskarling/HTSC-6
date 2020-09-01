#!/usr/bin/python  
#-*-  coding:GB2312  -*-
class Condition(object):
    def __init__(self,leftExpression,rightExpression,Expression):
        self.leftExpression = leftExpression
        self.rightExpression = rightExpression
        self.Expression = Expression

    def getSQL(self):
        pass

class AndCondition(Condition):
    def __init__(self, leftExpression,rightExpression):
        super().__init__(leftExpression,rightExpression)
        self.leftExpression = leftExpression
        self.rightExpression = rightExpression

    def getSQL(self):
        return self.leftExpression + ' AND ' + self.rightExpression

class OrCondition(Condition):
    def __init__(self, leftExpression,rightExpression):
        super().__init__(leftExpression,rightExpression)
        self.leftExpression = leftExpression
        self.rightExpression = rightExpression
    def getSQL(self):
        return self.leftExpression + ' OR ' + self.rightExpression

class NotCondition(Condition):
    def __init__(self, Expression):
        super().__init__(Expression)
        self.Expression = Expression

    def getSQL(self):
        return ' NOT ' + self.Expression

