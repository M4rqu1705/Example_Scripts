default_minimum = 1
default_maximum = 40

product1 = {
        "code": 1243,
        "name": "Oak end table",
        "price": 190,
        "cost": 130,
        "minimum": 20,
        "maximum": 40,
        "sr labor": 0.5,
        "jr labor": 1.3,
        "machine hours": 0.4,
        "oak feet": 2.8,
        "cherry feet": 0
        }
product1["profit"] = product1["price"] - product1["cost"]
product2 = {
        "code": 2243,
        "name": "Cherry end table",
        "price": 203,
        "cost": 146,
        "minimum": default_minimum,
        "maximum": 30,
        "sr labor": 0.7,
        "jr labor": 1.2,
        "machine hours": 0.4,
        "oak feet": 0,
        "cherry feet": 2.8
        }
product2["profit"] = product2["price"] - product2["cost"]
product3 = {
        "code": 1456,
        "name": "Oak rocking chair",
        "price": 371,
        "cost": 277,
        "minimum": 5,
        "maximum": 20,
        "sr labor": 2.1,
        "jr labor": 2.9,
        "machine hours": 1.2,
        "oak feet": 5.2,
        "cherry feet": 0
        }
product3["profit"] = product3["price"] - product3["cost"]
product4 = {
        "code": 2456,
        "name": "Cherry rocking chair",
        "price": 407,
        "cost": 308,
        "minimum": 5,
        "maximum": 15,
        "sr labor": 2.5,
        "jr labor": 2.7,
        "machine hours": 1.2,
        "oak feet": 0,
        "cherry feet": 5.2
        }
product4["profit"] = product4["price"] - product4["cost"]
product5 = {
        "code": 1372,
        "name": "Oak coffee table",
        "price": 238,
        "cost": 167,
        "minimum": 10,
        "maximum": 30,
        "sr labor": 1.3,
        "jr labor": 1.7,
        "machine hours": 0.6,
        "oak feet": 3.2,
        "cherry feet": 0
        }
product5["profit"] = product5["price"] - product5["cost"]
product6 = {
        "code": 2372,
        "name": "Cherry coffee table",
        "price": 259,
        "cost": 185,
        "minimum": default_minimum,
        "maximum": 10,
        "sr labor": 1.5,
        "jr labor": 1.5,
        "machine hours": 0.6,
        "oak feet": 0,
        "cherry feet": 3.2
        }
product6["profit"] = product6["price"] - product6["cost"]
product7 = {
        "code": 1531,
        "name": "Oak dining table",
        "price": 837,
        "cost": 648,
        "minimum": 5,
        "maximum": default_maximum,
        "sr labor": 1.9,
        "jr labor": 3.2,
        "machine hours": 1.7,
        "oak feet": 15.6,
        "cherry feet": 0
        }
product7["profit"] = product7["price"] - product7["cost"]
product8 = {
        "code": 2531,
        "name": "Cherry dining table",
        "price": 964,
        "cost": 724,
        "minimum": default_minimum,
        "maximum": 10,
        "sr labor": 2.1,
        "jr labor": 2.8,
        "machine hours": 1.6,
        "oak feet": 0,
        "cherry feet": 15.6
        }
product8["profit"] = product8["price"] - product8["cost"]
product9 = {
        "code": 1635,
        "name": "Oak desk",
        "price": 1084,
        "cost": 841,
        "minimum": 5,
        "maximum": 15,
        "sr labor": 4.3,
        "jr labor": 5.8,
        "machine hours": 3.2,
        "oak feet": 18.2,
        "cherry feet": 0
        }
product9["profit"] = product9["price"] - product9["cost"]
product10 = {
        "code": 2635,
        "name": "Cherry desk",
        "price": 1214,
        "cost": 938,
        "minimum": 5,
        "maximum": default_maximum,
        "sr labor": 4.5,
        "jr labor": 5.6,
        "machine hours": 3.5,
        "oak feet": 0,
        "cherry feet": 18.2
        }
product10["profit"] = product10["price"] - product10["cost"]
product11 = {
        "code": 1367,
        "name": "Oak bookshelves",
        "price": 401,
        "cost": 315,
        "minimum": 15,
        "maximum": 30,
        "sr labor": 1.8,
        "jr labor": 2.5,
        "machine hours": 2.1,
        "oak feet": 6.2,
        "cherry feet": 0
        }
product11["profit"] = product11["price"] - product11["cost"]
product12 = {
        "code": 2367,
        "name": "Cherry bookshelves",
        "price": 455,
        "cost": 349,
        "minimum": default_minimum,
        "maximum": 40,
        "sr labor": 1.9,
        "jr labor": 2.5,
        "machine hours": 2.2,
        "oak feet": 0,
        "cherry feet": 6.2
        }
product12["profit"] = product12["price"] - product12["cost"]


def consumption_per_unit(prod):
    return [
            prod["sr labor"],
            prod["jr labor"],
            prod["machine hours"],
            prod["oak feet"],
            prod["cherry feet"]
            ]


#srLabor, jrLabor, machineHrs, Oakft, cherryft
resource_costs = [20, 12, 15, 35, 40]
resource_availability = [263, 450, 225, 488, 638]


c = []
combos = []
def combo_aux(l, depth):
    global c
    global combos
    for e in l[-depth]:
        c[-depth] = e
        if(depth == 1):
            combos.append(c[:])
        else:
            combo_aux(l, depth-1)
def create_combinations(l, depth):
    global c
    global combos
    c = [0]*depth
    combos = []
    combo_aux(l[:], depth)


def findOptimalCombination(prods):
    optimal = {"profit": 0, "quantities": []}

    pos = []
    for prod in prods:
        p = list(range(prod["maximum"], prod["minimum"]-1, -1))
        pos.append(p)
    create_combinations(pos, len(pos))


    if not isinstance(combos[0], list):
        for i in range(len(combos)):
            combos[i] = [combos[i]]

    for combination in combos:
        resources_consumed = []
        for resource in range(5):
            resources_consumed.append(sum([consumption_per_unit(products[i])[resource] * combination[i] for i in range(len(products))]))

        if any([resources_consumed[i] > resource_availability[i] for i in range(5)]):
            continue

        profit = sum([products[i]["profit"] * combination[i] for i in range(len(products))])

        if profit > 0:
            optimal["profit"] = profit
            optimal["quantities"] = combination[:]
            return optimal


summary = [
        [str(product1["code"]), product1["name"], product1],
        [str(product2["code"]), product2["name"], product2],
        [str(product3["code"]), product3["name"], product3],
        [str(product4["code"]), product4["name"], product4],
        [str(product5["code"]), product5["name"], product5],
        [str(product6["code"]), product6["name"], product6],
        [str(product7["code"]), product7["name"], product7],
        [str(product8["code"]), product8["name"], product8],
        [str(product9["code"]), product9["name"], product9],
        [str(product10["code"]), product10["name"], product10],
        [str(product11["code"]), product11["name"], product11],
        [str(product12["code"]), product12["name"], product12]
        ]

_in = "13"
products = []
while _in not in ["exit", "done"]:

    print("Select products for mix by entering product code and 'enter'")
    print("Write 'done' to search for best combination and 'exit' to exit program")

    for prod in summary:
        print(str(prod[0]) + ": " + str(prod[1]))

    _in = input().lower().strip()
    if _in in ["exit", "done"]:
        break
    elif not any([_in == summary[n][0] for n in range(len(summary))]):
        print("Enter the code for a valid product!")
        continue
    else:
        prod = ""
        for n in range(len(summary)):
            if summary[n][0] == _in:
                prod = summary[n][2]
                break
        if prod != "" and prod not in products:
            products.append(prod)

if _in == "exit":
    exit()
else:
    if len(products) < 1:
        print("Please select a product")
        exit()
    elif len(products) >= 1:
        optimal = findOptimalCombination(products)
        print()
        print("-"*80)
        print("Most profitable product combination")
        for i in range(len(optimal["quantities"])):
            print(str(optimal["quantities"][i]), products[i]["name"])
        print("Profit: $" + str(optimal['profit']))
