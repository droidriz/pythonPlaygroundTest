def calculator_function(operand1,operand2,operator):
    if(operator.lower()=='add'):
        return operand1+operand2
    elif(operator.lower()=='subtract'):
        if(operand1>operand2):
            return operand1-operand2
        return operand2-operand1
    else:
        return "ERROR: Invalid Operator"


print(calculator_function(2,4,"Divide"))
