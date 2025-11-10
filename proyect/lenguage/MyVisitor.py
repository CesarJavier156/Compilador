from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser

class MyViisitor(GrammarVisitor):
    def __init__(self):
        self.memory = {}

#Defnimos las assignacion
def visitAssign(self,ctx):
    name=ctx.ID().getText()
    value=self.visit(ctx.expr())
    self.memory[name]=value

#Definimos la impression
def visitPrint(self,ctx):
    value=self.visito(ctx.expr())
    print(value)