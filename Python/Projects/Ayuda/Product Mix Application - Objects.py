class Product:
    def __init__(self, productCode, description, unitPrice, unitCost, minUnits,
            maxUnits, srLabor, jrLabor, machineHR, oakFt, cherryFt):
        self.unitPrice = unitPrice
        self.unitCost = unitCost
        self.minUnits = minUnits
        self.maxUnits = maxUnits
        self.srLabor = srLabor
        self.jrLabor = jrLabor
        self.machineHR = machineHR
        self.oakFt = oakFt
        self.cherryFt = cherryFt
        self.productCode = productCode
        self.description = description

    def getCode(self):
        return self.productCode

    def getDescription(self):
        return self.description

    def getPrice(self):
        return self.unitPrice

    def getCost(self):
        return self.unitCost

    def getMinUnits(self):
        return self.minUnits

    def getMaxUnits(self):
        return self.maxUnits

    def getJrLabor(self):
        return self.jrLabor

    def getSrLabor(self):
        return self.srLabor

    def getMachineHR(self):
        return self.machineHR

    def getOakFt(self):
        return self.oakFt

    def getCherryFt(self):
        return self.cherryFt

    def getProfitPerUnit(self):
        #profit per unit = revenue per unit - cost per unit
        return self.getPrice() - self.getCost()

    def getConsumptionPerUnit(self):
        consumption = []
#1)SrLaborHours
        consumption.append(self.getSrLabor())
#2)JrLaborHours
        consumption.append(self.getJrLabor())
#3)MachineHrs
        consumption.append(self.getMachineHR())
#4)OakFt
        consumption.append(self.getOakFt())
#5)CherryFt
        consumption.append(self.getCherryFt())

        return consumption


#prepare products
minProducts = 1 #logically you want at least 1 piece if you are ordering it
maxProducts = 35 #determined by dividing 638 / 18.2 to calculate max amount of cherry ft in "cherry desk"

p1 = Product(1243, "Oak end table", 190, 130, 20, 40, 0.5, 1.3, 0.4, 2.8, 0)
p2 = Product(2243, "Cherry end table", 203, 146, minProducts, 30, 0.7, 1.2, 0.4, 0, 2.8)
p3 = Product(1456, "Oak rocking chair", 371, 277, 5, 20, 2.1, 2.9, 1.2, 5.2, 0)
p4 = Product(2456, "Cherry rocking chair", 407, 308, 5, 15, 2.5, 2.7, 1.2, 0, 5.2)
p5 = Product(1372, "Oak coffee table", 238, 167, 10, 30, 1.3, 1.7, 0.6, 3.2, 0)
p6 = Product(2372, "Cherry coffee table", 259, 185, minProducts, 10, 1.5, 1.5, 0.6, 0, 3.2)
p7 = Product(1531, "Oak dining table", 837, 648, 5, maxProducts, 1.9, 3.2, 1.7, 15.6, 0)
p8 = Product(2531, "Cherry dining table", 964, 724, minProducts, 10, 2.1, 2.8, 1.6, 0, 15.6)
p9 = Product(1635, "Oak desk", 1084, 841, 5, 15, 4.3, 5.8, 3.2, 18.2, 0)
p10 = Product(2635, "Cherry desk", 1214, 938, 5, maxProducts, 4.5, 5.6, 3.5, 0, 18.2)
p11 = Product(1367, "Oak bookshelves", 401, 315, 15, 30, 1.8, 2.5, 2.1, 6.2, 0)
p12 = Product(2367, "Cherry bookshelves", 455, 349, minProducts, 40, 1.9, 2.5, 2.2, 0, 6.2)

#data con resources cost
srLaborCost = 20
jrLaborCost = 12
machineHrsCost = 15
oakFtCost = 35
cherryFtCost = 40

#data on resources availability
availableResources = [263, 450, 225, 488, 638]
#srLabor, jrLabor, machineHrs, Oakft, cherryft

#============== Generating combination functions ==============
combination = []
combinations = []
def combinationsHelper(l, depth):
    global combination
    global combinations
    for el in l[-depth]:
        combination[-depth] = el
        if(depth == 1):
            combinations.append(combination[:])
        else:
            combinationsHelper(l, depth-1)
            combinations.append(combination[:])
def generateCombinations(l, depth):
    global combination
    global combinations
    combination = [0]*depth
    combinations = []
    combinationsHelper(l[:], depth)

#========== Brute-force to find optimal combination ===========
def findOptimalCombination(products):
    optimalCombination = {"Profit": 0, "Product Quantities": [], "Resources Used": [10000]*5}

    possibilities = []
    for product in products:
        possible = list(range(product.getMaxUnits(), product.getMinUnits()-1, -1))
        possibilities.append(possible)
    generateCombinations(possibilities, len(possibilities))


    if not isinstance(combinations[0], list):
        for i in range(len(combinations)):
            combinations[i] = [combinations[i]]

    for combination in combinations:

        units = combination[:]

        #calculate how many of each resource is consumed
        #sum(resource * unit) for every resource
        consumedResources = []
        for resource in range(5):
            consumedResources.append(sum([product.getConsumptionPerUnit()[resource] * units[i] for i, product in enumerate(products)]))

        #if any of the consumed resources for the hypothetical situation exceeds thoe available, continue to next loop
        if any([consumedResources[i] > availableResources[i] for i in range(5)]):
            continue

        #calculate profit for selling every product
        profit = sum([product.getProfitPerUnit() * units[i] for i, product in enumerate(products)])

        #since profit is linearly decreasing as function continues, take the first profit that fits the criteria 
        if optimalCombination["Profit"] < profit:
            optimalCombination["Profit"] = profit
            optimalCombination["Product Quantities"] = units[:]
            break

    return optimalCombination


def main():
    user = "0"
    mapping = {
            str(p1.getCode()): p1,
            str(p2.getCode()): p2,
            str(p3.getCode()): p3,
            str(p4.getCode()): p4,
            str(p5.getCode()): p5,
            str(p6.getCode()): p6,
            str(p7.getCode()): p7,
            str(p8.getCode()): p8,
            str(p9.getCode()): p9,
            str(p10.getCode()): p10,
            str(p11.getCode()): p11,
            str(p12.getCode()): p12,
            }

    #make sure entered elements are unique
    products = set()

    exitWhile = ["exit", "quit", "done", "finished"]
    while user not in exitWhile:

        print("Please Select the products for the mix\n")
        print("Insert the product code and press enter for each product\n"
                "Write 'done' or 'finished' to proceed to look for best combination\n"
                "Write 'exit' or 'quit' to exit program")
        for key in mapping:
            print(f"{key} - {mapping[key].getDescription()}")

        #check user input
        user = input().strip().lower()
        if user in exitWhile:
            continue
        elif mapping.get(user, None) is None:
            print("Please enter a valid number!")
            continue
        else:
            products.add(mapping[user])

    products = list(products)

    if user.strip().lower() in ["exit", "quit"]:
        exit()
    else:
        if len(products) < 1:
            print("You did not select any product. Please try again")
            exit()
        elif len(products) >= 1:
            optimalCombination = findOptimalCombination(products)
            print("The best combination of products is:")
            for i, quantity in enumerate(optimalCombination["Product Quantities"]):
                print(f"- ({quantity}) {products[i].getDescription()}")
            print(f"Profit: ${optimalCombination['Profit']}")

if __name__ == "__main__":
    main()
