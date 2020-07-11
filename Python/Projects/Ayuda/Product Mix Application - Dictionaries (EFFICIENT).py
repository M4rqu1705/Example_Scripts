products = [
        {
            "code": 1243,
            "description": "Oak end table",
            "unit price": 190,
            "unit cost": 130,
            "min units": 20,
            "max units": 40,
            "labor hours": {
                "senior": 0.5,
                "junior": 1.3,
                "machine": 0.4,
                },
            "feet":{
                "oak": 2.8,
                "cherry": 0,
                }
            },
        {
            "code": 2243,
            "description": "Cherry end table",
            "unit price": 203,
            "unit cost": 146,
            "min units": 1,
            "max units": 30,
            "labor hours": {
                "senior": 0.7,
                "junior": 1.2,
                "machine": 0.4,
                },
            "feet":{
                "oak": 0,
                "cherry": 2.8,
                }
            },
        {
            "code": 1456,
            "description": "Oak rocking chair",
            "unit price": 371,
            "unit cost": 277,
            "min units": 5,
            "max units": 20,
            "labor hours": {
                "senior": 2.1,
                "junior": 2.9,
                "machine": 1.2,
                },
            "feet":{
                "oak": 5.2,
                "cherry": 0,
                }
            },
        {
                "code": 2456,
                "description": "Cherry rocking chair",
                "unit price": 407,
                "unit cost": 308,
                "min units": 5,
                "max units": 15,
                "labor hours": {
                    "senior": 2.5,
                    "junior": 2.7,
                    "machine": 1.2,
                    },
                "feet":{
                    "oak": 0,
                    "cherry": 5.2,
                    }
                },
        {
                "code": 1372,
                "description": "Oak coffee table",
                "unit price": 238,
                "unit cost": 167,
                "min units": 10,
                "max units": 30,
                "labor hours": {
                    "senior": 1.3,
                    "junior": 1.7,
                    "machine": 0.6,
                    },
                "feet":{
                    "oak": 3.2,
                    "cherry": 0,
                    }
                },
        {
                "code": 2372,
                "description": "Cherry coffee table",
                "unit price": 259,
                "unit cost": 185,
                "min units": 1,
                "max units": 10,
                "labor hours": {
                    "senior": 1.5,
                    "junior": 1.5,
                    "machine": 0.6,
                    },
                "feet":{
                    "oak": 0,
                    "cherry": 3.2,
                    }
                },
        {
                "code": 1531,
                "description": "Oak dining table",
                "unit price": 837,
                "unit cost": 648,
                "min units": 5,
                "max units": 10E4,
                "labor hours": {
                    "senior": 1.9,
                    "junior": 3.2,
                    "machine": 1.7,
                    },
                "feet":{
                    "oak": 15.6,
                    "cherry": 0,
                    }
                },
        {
                "code": 2531,
                "description": "Cherry dining table",
                "unit price": 964,
                "unit cost": 724,
                "min units": 1,
                "max units": 10,
                "labor hours": {
                    "senior": 2.1,
                    "junior": 2.8,
                    "machine": 1.6,
                    },
                "feet":{
                    "oak": 0,
                    "cherry": 15.6,
                    }
                },
        {
                "code": 1635,
                "description": "Oak desk",
                "unit price": 1084,
                "unit cost": 841,
                "min units": 5,
                "max units": 15,
                "labor hours": {
                    "senior": 4.3,
                    "junior": 5.8,
                    "machine": 3.2,
                    },
                "feet":{
                    "oak": 18.2,
                    "cherry": 0,
                    }
                },
        {
                "code": 2635,
                "description": "Cherry desk",
                "unit price": 1214,
                "unit cost": 938,
                "min units": 5,
                "max units": 10E4,
                "labor hours": {
                    "senior": 4.5,
                    "junior": 5.6,
                    "machine": 3.5,
                    },
                "feet":{
                    "oak": 0,
                    "cherry": 18.2,
                    }
                },
        {
                "code": 1367,
                "description": "Oak bookshelves",
                "unit price": 401,
                "unit cost": 315,
                "min units": 15,
                "max units": 30,
                "labor hours": {
                    "senior": 1.8,
                    "junior": 2.5,
                    "machine": 2.1,
                    },
                "feet":{
                    "oak": 6.2,
                    "cherry": 0,
                    }
                },
        {
                "code": 2367,
                "description": "Cherry bookshelves",
                "unit price": 455,
                "unit cost": 349,
                "min units": 1,
                "max units": 40,
                "labor hours": {
                    "senior": 1.9,
                    "junior": 2.5,
                    "machine": 2.2,
                    },
                "feet":{
                    "oak": 0,
                    "cherry": 6.2,
                    }
                },
        ]

resources = {
        "availability": {
            "labor hours": {
                "senior": 263,
                "junior": 450,
                "machine": 225,
                },
            "feet":{
                "oak": 488,
                "cherry": 638,
                }
            },
        "unit cost":{
            "labor hours": {
                "senior": 20,
                "junior": 12,
                "machine": 15,
                },
            "feet":{
                "oak": 35,
                "cherry": 40,
                }
            }
        }


# ======== START HELPER FUNCTIONS ========
def print_products():
    '''
    Helper function to debug any problems with the products array
    '''
    global products

    print("| {: ^12s} | {: ^30s} | {: ^10s} | {: ^9s} | {: ^9s} | {: ^9s} | {: ^10s} | {: ^10s} | {: ^10s} | {: ^5s} | {: ^8s} |".format(
        "Product Code",
        "Description",
        "Unit Price",
        "Unit Cost",
        "Min Units",
        "Max Units",
        "SrLaborHrs",
        "JrLaborHrs",
        "MachineHrs",
        "OakFt",
        "CherryFt"))

    for product in products:
        print("| {: ^12d} | {: ^30s} | {: ^10d} | {: ^9d} | {: ^9d} | {: ^9.0f} | {: ^10.2f} | {: ^10.2f} | {: ^10.2f} | {: ^5.2f} | {: ^8.2f} |".format(
            product["code"],
            product["description"],
            product["unit price"],
            product["unit cost"],
            product["min units"],
            product["max units"],
            product["labor hours"]["senior"],
            product["labor hours"]["junior"],
            product["labor hours"]["machine"],
            product["feet"]["oak"],
            product["feet"]["cherry"]))

def print_product_codes():
    global products

    for product in products:
        print("({}) - {}".format(product["code"], product["description"]))

def print_resources():
    '''
    Helper function to debug any problems with the resources dictionary
    '''
    global resources

    print("| {: ^30s} | {: ^12s} | {: ^12s} |".format(
        "Resource",
        "Unit Cost",
        "Availability"))

    print("| {: ^30s} | {: ^12d} | {: ^12d} |".format("SrLaborHours", resources["unit cost"]["labor hours"]["senior"], resources["availability"]["labor hours"]["senior"]))
    print("| {: ^30s} | {: ^12d} | {: ^12d} |".format("JrLaborHours", resources["unit cost"]["labor hours"]["junior"], resources["availability"]["labor hours"]["junior"]))
    print("| {: ^30s} | {: ^12d} | {: ^12d} |".format("MachineHrs", resources["unit cost"]["labor hours"]["machine"], resources["availability"]["labor hours"]["machine"]))
    print("| {: ^30s} | {: ^12d} | {: ^12d} |".format("OakFt", resources["unit cost"]["feet"]["oak"], resources["availability"]["feet"]["oak"]))
    print("| {: ^30s} | {: ^12d} | {: ^12d} |".format("CherryFt", resources["unit cost"]["feet"]["cherry"], resources["availability"]["feet"]["cherry"]))

def print_consumption(products):
    resources_consumed = {
            "availability": {
                "labor hours": {
                    "senior": 0,
                    "junior": 0,
                    "machine": 0,
                    },
                "feet":{
                    "oak": 0,
                    "cherry": 0,
                    }
                },
            }

    for product in products:
        resources_consumed["availability"]["labor hours"]["senior"] += product["quantity"] * product["labor hours"]["senior"]
        resources_consumed["availability"]["labor hours"]["junior"] += product["quantity"] * product["labor hours"]["junior"]
        resources_consumed["availability"]["labor hours"]["machine"] += product["quantity"] * product["labor hours"]["machine"]
        resources_consumed["availability"]["feet"]["oak"] += product["quantity"] * product["feet"]["oak"]
        resources_consumed["availability"]["feet"]["cherry"] += product["quantity"] * product["feet"]["cherry"]

    print("Consumed {} senior, {} junior, and {} machine hours, and {} oak feet and {} cherry feet".format(
        resources_consumed["availability"]["labor hours"]["senior"],
        resources_consumed["availability"]["labor hours"]["junior"],
        resources_consumed["availability"]["labor hours"]["machine"],
        resources_consumed["availability"]["feet"]["oak"],
        resources_consumed["availability"]["feet"]["cherry"],
        ))
# ======== END HELPER FUNCTIONS ========


def get_product(code):
    global products

    #Convert to integer
    try:
        code = int(code)
    except Exception:
        return False

    for product in products:
        if code == product["code"]:
            return product

    return False

def request_input():
    requested_products = []
    products_found = []

    print_product_codes()
    input_message = "Enter the code for the furniture you want: "
    code = input(input_message)

    if code in products_found:
        print("You already entered this code. ")
    else:
        found_product = get_product(code)

        if found_product:
            requested_products.append(found_product)
            products_found.append(code)
        else:
            print("Please enter a correct code!")
    print()

    while code != "" or code == "exit":
        print_product_codes()
        input_message = "Enter the code for the furniture you want: "
        code = input(input_message)

        if code in products_found:
            print("You already entered this code. ")
        else:
            found_product = get_product(code)

            if found_product:
                requested_products.append(found_product)
                products_found.append(code)
            else:
                print("Please enter a correct code!")
        print()


    return requested_products

def find_optimal(requested_products):
    global resources
    total_profit = 0
    combinations = []

    #Set minimal quantities for each product and "consume" those resources
    for i in range(len(requested_products)):
        quantity = requested_products[i]["min units"] 
        requested_products[i]["quantity"] = quantity

        resources["availability"]["labor hours"]["senior"] -= quantity * requested_products[i]["labor hours"]["senior"]
        resources["availability"]["labor hours"]["junior"] -= quantity * requested_products[i]["labor hours"]["junior"]
        resources["availability"]["labor hours"]["machine"] -= quantity * requested_products[i]["labor hours"]["machine"]
        resources["availability"]["feet"]["oak"] -= quantity * requested_products[i]["feet"]["oak"]
        resources["availability"]["feet"]["cherry"] -= quantity * requested_products[i]["feet"]["cherry"]

    #Find highest-profit product
    for i in range(len(requested_products)):
        requested_products[i]["profit"] = requested_products[i]["unit price"] - requested_products[i]["unit cost"]

    requested_products.sort(key=lambda x: x["profit"], reverse=True)

    #Increment quantities from highest-profit product to least-profit product
    for i in range(len(requested_products)):
        #Iterate from highest quantity to least quantity
        for units in range(int(requested_products[i]["max units"]), int(requested_products[i]["min units"]), -1):
            #Check if meets criteria for leftover resources

            #Take into account the min units already "consumed"
            quantity = units - requested_products[i]["quantity"]
            
            enough = [
                quantity * requested_products[i]["labor hours"]["senior"] <= resources["availability"]["labor hours"]["senior"],
                quantity * requested_products[i]["labor hours"]["junior"] <= resources["availability"]["labor hours"]["junior"],
                quantity * requested_products[i]["labor hours"]["machine"] <= resources["availability"]["labor hours"]["machine"],
                quantity * requested_products[i]["feet"]["oak"] <= resources["availability"]["feet"]["oak"],
                quantity * requested_products[i]["feet"]["cherry"] <= resources["availability"]["feet"]["cherry"]
            ]

            #If there is enough of all resources ...
            if all(enough):
                #Update the current product's quantity
                requested_products[i]["quantity"] += quantity

                #"Consume" the resources
                resources["availability"]["labor hours"]["senior"] -= quantity * requested_products[i]["labor hours"]["senior"]
                resources["availability"]["labor hours"]["junior"] -= quantity * requested_products[i]["labor hours"]["junior"]
                resources["availability"]["labor hours"]["machine"] -= quantity * requested_products[i]["labor hours"]["machine"]
                resources["availability"]["feet"]["oak"] -= quantity * requested_products[i]["feet"]["oak"]
                resources["availability"]["feet"]["cherry"] -= quantity * requested_products[i]["feet"]["cherry"]

                #Break to continue with next product
                break


    #Calculate profit and set up combinations
    for product in requested_products:
        profit = product["unit price"] - product["unit cost"]
        total_profit += product["quantity"] * profit

        combinations.append({
            "code": product["code"],
            "description": product["description"],
            "quantity": product["quantity"],
            "labor hours": product["labor hours"],
            "feet": product["feet"]
            })

    print("Profit = {}".format(total_profit))

    return combinations

def display_results(combinations):
    print("In order to maximize profits you should produce:")
    for product in combinations:
        print("  - ({}) {} (Code {})".format(product["quantity"], product["description"], product["code"]))


#Call functions
requested_products = request_input()
combinations = find_optimal(requested_products)
display_results(combinations)
print_consumption(combinations)
