triplets = []
last_result = 100

def are_coprime(a,b):

    # Check if numbers are both even
    if a%2==0 and b%2==0:
        return False

    # Check if a and b have common factors with uneven numbers
    for c in range(3, min(a,b), 2):
        if a%c==0 and b%c==0:
            return False

    return True

def are_factors(a,b):
    # Check each triplet
    for triplet in triplets:
        # Check each triplet's factors and compare them to the current factors
        if (triplet[0]==a or triplet[1]==a) and (triplet[0]==b or triplet[1]==b):
            return True

    return False


if __name__ == "__main__":
    for a in range(2,last_result+1):
        for b in range(2, last_result+1):

            # c = sqrt(a^2 + b^2)
            result = (a**2 + b**2)**0.5

            if int(result) == result and are_coprime(a,b) and not are_factors(a,b):
                triplets.append([int(a),int(b),int(result)])

def third_element(e):
    return e[2]

# Sort triplets by their "c"
triplets.sort(key=third_element)

# Print each triplet nicely in an numbered manner
counter = 0
for triplet in triplets:
    if triplet[2] < last_result:
        counter+=1
        print("{}) ".format(counter), end='')
        print(triplet)
