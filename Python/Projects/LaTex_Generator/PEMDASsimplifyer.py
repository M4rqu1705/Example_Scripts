#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def simplify(expression, variables, procedure=None):
    if procedure == None:
        procedure = []

    # Initially parse expression to work with a standarized input
    expression = str(expression).strip()
    expression = ''.join(expression.split(' '))

    # Identify which operations are to be done
    substitute_variable = re.compile(r'[A-Za-z]')
    group_parenthesis = re.compile(r'(?:\(([^\[\]\{\}\(\)]+)\)|\[([^\[\]\{\}\(\)]+)\]|\{([^\[\]\{\}\(\)]+)\})')
    exponentiate = re.compile(r'(\w+)(?:\^)(\w+)')
    multiply_divide = re.compile(r'(?<=[^\*])\*(?=[^\*])|\/')
    multiply_coefficient = re.compile(r'(\d+)([A-Za-z](?:(?:\^|\*\*)([A-Za-z])?(?(3)[A-Za-z]+|\d+))?)')
    add_substract = re.compile(r'\+|\-')

    operations = {
            "substitution" : bool(substitute_variable.search(expression)),
            "parenthesis" : bool(group_parenthesis.search(expression)),
            "addition_substraction" : bool(add_substract.search(expression)),
            "coefficient_multiplication": bool(multiply_coefficient.search(expression)),
            "multiplication_division" : bool(multiply_divide.search(expression)),
            "exponent" : bool(exponentiate.search(expression))
            }

    #  print("Expression: {}".format(expression))
    #  print(operations)

    # Substitute variable letters for their actual values inside parens
    if operations["substitution"]:
        print("Began substituting variables in {}".format(expression))

        i, expression_length = 0, len(expression)
        while i < expression_length-1:
            character = str(expression[i])
            # If character is valid letter and is in keys
            if substitute_variable.match(character) and character in variables.keys():
                value = str(variables[character])
                # Insert value with surrounding parenthesis
                expression = expression[:i] + "({})".format(value) + expression[i+1:]
                # Increase working index and final index
                expression_length += 2 + len(value); i += 2 + len(value)
            i+=1

        procedure.append(expression)

        return simplify(expression, variables, procedure)

    # Work with parenthesis first. The're the most important
    elif operations["parenthesis"]:
        print("Began evaluating parenthesis in {}".format(expression))
        # Identify every parenthesis inside expression
        matches = group_parenthesis.findall(expression)
        matches = [y for x in matches for y in x]   # Flatten 2d list
        matches = list(filter(None, matches))       # Remove Nones from list

        # Substitute matches with simplified matches
        for i in range(len(matches)):
            start = expression.find(matches[i])
            end = start + len(matches[i])
            start-=1; end+=1
            temp = str(simplify(matches[i], variables, procedure))
            expression = expression[:start] + temp + expression[end:]

        procedure.append(expression)

        return simplify(expression, variables, procedure)

    # Decompose and process expression into polynomial terms
    elif operations["addition_substraction"]:
        print("Began adding/subtracting {}".format(expression))
        # Divide expression into list of terms
        terms = add_substract.sub(',', expression).split(',')
        # Get operators of matches
        operators = add_substract.findall(expression)

        # Recompose expression
        output = ""
        for i in range(len(operators)):
            output += str(simplify(terms[i], variables, procedure)) + str(operators[i])
        output += str(simplify(terms[-1], variables, procedure))

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
            output += str(simplify(factors[i], variables, procedure)) + str(operators[i])
        output += str(simplify(factors[-1], variables, procedure))

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
        # Evaluate base and exponent based on regex captures
        base, exponent = exponentiate.findall(expression)[0]

        # Substitute variable values for factors
        if str(base) in variables.keys():
            base = str(variables[base])

        # Return simplified exponent
        output = "{}**{}".format(base, exponent)
        return eval(output)

    # If no operations left to do, simply return the number
    else:
        #  print(procedure)
        return expression

if __name__ == "__main__":
    print(simplify("{(1+2)*2}*[2+4*(2+5)]", {"x":1, "z":5}))
