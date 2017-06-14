# Aufgabenzettel 8, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 39

######################################################################################################################
#                                           Aufgabe 39a: arithmetische Operationen                                   #
######################################################################################################################
class Ausdruck:
    def __init__(self,operator,op1=None,op2=None):
        self.operator=operator
        self.operand1=op1
        self.operand2=op2

    def __str__(self):
        print("(",self.operand1.__str__(),self.operator.__str__(),self.operand2.__str__(),")")


a=Ausdruck('*',Ausdruck('+',3,'x'),Ausdruck('/',6,2))
print(a)