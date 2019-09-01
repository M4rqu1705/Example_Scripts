#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def simplify(expression, variables):

    # Initially parse expression to work with a standarized input
    expression = str(expression).strip()
    expression = ''.join(expression.split(' '))

    # Identify which operations are to be done
    group_parenthesis = re.compile(r'(?:\(([^\[\]\{\}\(\)]+)\)|\[([^\[\]\{\}\(\)]+)\]|\{([^\[\]\{\}\(\)]+)\})')
    add_substract = re.compile(r'\+|\-')
    multiply_coefficient = re.compile(r'(\d+)([A-Za-z](?:(?:\^|\*\*)([A-Za-z])?(?(3)[A-Za-z]+|\d+))?)')
    multiply_divide = re.compile(r'(?<=[^\*])\*(?=[^\*])|\/')
    exponentiate = re.compile(r'(?:\^|\*\*)')

    operations = {
            "parenthesis" : bool(group_parenthesis.search(expression)),
            "addition_substraction" : bool(add_substract.search(expression)),
            "coefficient_multiplication": bool(multiply_coefficient.search(expression)),
            "multiplication_division" : bool(multiply_divide.search(expression)),
            "exponent" : bool(exponentiate.search(expression))
            }

    #  print("Expression: {}".format(expression))
    #  print(operations)

    # Work with parenthesis first. The're the most important
    if operations["parenthesis"]:
        print("Began evaluating parenthesis in {}".format(expression))
        # Identify every parenthesis inside expression
        parenthesis_groups = group_parenthesis.finditer(expression)
        parenthesis_groups = [parenthesis_group.groups() for parenthesis_group in parenthesis_groups]
        parenthesis_groups = [y for x in parenthesis_groups for y in x]
        while parenthesis_groups.count(None) > 0:
            parenthesis_groups.remove(None)

        for i in range(len(parenthesis_groups)):
            start = expression.find(parenthesis_groups[i])
            end = start + len(parenthesis_groups[i])
            start-=1; end+=1
            expression = expression[:start] + "<item>{}</item>".format(str(i)) + expression[end:]

        for i in range(len(parenthesis_groups)):
            temp = str(simplify(parenthesis_groups[i], variables))
            expression = expression.replace("<item>{}</item>".format(str(i)), temp)

        output = str(simplify(expression, variables))

        return eval(output)

    # Decompose and process expression into polynomial terms
    elif operations["addition_substraction"]:
        print("Began adding/subtracting {}".format(expression))
        # Divide expression into list of terms
        terms = add_substract.sub(',', expression).split(',')
        # Get operators of matches
        operators = add_substract.finditer(expression)
        operators = [operator.group(0) for operator in operators]

        # Substitute variable values for factors
        for i in range(len(terms)):
            if str(terms[i]) in variables.keys():
                terms[i] = str(variables[terms[i]])

        # Recompose expression
        output = ""
        for i in range(len(operators)):
            output += str(simplify(terms[i], variables)) + str(operators[i])
        output += str(simplify(terms[-1], variables))

        # Return evaluated form
        return eval(output)

    # Decompose and process expression into mutiplications and divisions, if possible
    elif operations["multiplication_division"]:
        print("Began multiplying/dividing {}".format(expression))
        # Divide expression into multiplication and division factors
        factors = multiply_divide.sub(',', expression).split(',')
        # Get operators of matches
        operators = multiply_divide.finditer(expression)
        operators = [operator.group(0) for operator in operators]

        # Substitute variable values for factors
        for i in range(len(factors)):
            if str(factors[i]) in variables.keys():
                factors[i] = str(variables[factors[i]])

        # Recompose expression
        output = ""
        for i in range(len(operators)):
            output += str(simplify(factors[i], variables)) + str(operators[i])
        output += str(simplify(factors[-1], variables))

        # Return for further simplification
        return eval(output)

    # Decompose and process terms into multiplications of coefficients and variables
    elif operations["coefficient_multiplication"]:
        print("Began finding coefficients for {}".format(expression))
        # Get operators of matches
        instances = multiply_coefficient.finditer(expression)
        instances = [instance.groups() for instance in instances]
        instances = [instance for group in instances for instance in group]
        while instances.count(None) > 0:
            instances.remove(None)

        # Substitute variable values for factors
        for i in range(len(instances)):
            if str(instances[i]) in variables.keys():
                instances[i] = str(variables[instances[i]])

        simplified_instances = [str(simplify(instance, variables)) for instance in instances]

        # Recompose expression in terms of multiplications        
        output = ""
        for i in range(len(simplified_instances)-1):
            output += simplified_instances[i] + "*"
        output += simplified_instances[-1]

        return eval(output)

    # Simplify exponents
    elif operations["exponent"]:
        print("Began exponentiating {}".format(expression))
        # Divide expression into base and exponent
        base, exponent = exponentiate.sub(',', expression).split(',')

        # Substitute variable values for factors
        if str(base) in variables.keys():
            base = str(variables[base])

        # Return simplified exponent
        output = "{}**{}".format(base, exponent)
        return eval(output)

    # If no operations left to do, simply return the number
    else:
        return expression

if __name__ == "__main__":
    print(simplify("3x^3+2x^2+x-1", {"x":2, "z":3}))
