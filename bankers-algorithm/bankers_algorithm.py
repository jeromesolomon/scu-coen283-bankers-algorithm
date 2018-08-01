"""
Gabriel Jerome Solomon
Bankers Algorithm, Homework programming question implementation

Question from Professor Elkady

Program a simulation of the banker’s algorithm. Your program should cycle 
through each of the bank clients asking for a request and evaluating whether it 
is safe or unsafe. Output a log of requests and decisions to a file.

"""

# types of resources available
gResourceTypes = ["printer", "network storage", "scanner"]

def print_welcome():
    """
    prints welcome
    """
    print("\n")
    print("------------------------------------------")
    print("\t\tBanker's Algorithm Simulation")
    print("\t\tJerome Solomon")
    print("\t\tCOEN 283 Operating Systems")
    print("\t\tHomework Assignment 4")
    print("\t\tProfessor Amr Elkady")
    print("------------------------------------------")
    print("\n")


def get_number_resources():
    """"
    get initial information from user on number of resources
    """
    resources = []
    # get the number of resources for each resource type
    for e in enumerate(gResourceTypes):
        n = input("Enter number of resource #" + str(e[0]) + " <" + e[1] + "> :")
        resources.append(int(n))

    return resources


def predict_maximum_resources(numClient, totalResources):
    """"
    predicts maximum resource by setting them to a random value between 0 to max available
    """

    import random

    maxResources = []
    for i in range(0, numClient):

        row = []
        for r in totalResources:
            randMax = random.randint(0, r)
            row.append(randMax)

        maxResources.append(row)

    return maxResources

def initialize_current_allocations(numClient, totalResources):
    """"
    initialize current allocations to 0
    """

    allocations = []
    for i in range(0, numClient):

        row = []
        for r in totalResources:
            row.append(0)

        allocations.append(row)

    return allocations

def get_client_request(c):
    """"
    get client resource request
    """

    request = []

    print("Request for client #" + str(c) + ":")


    for r in gResourceTypes:
        userRequest = input("\tEnter the number of <" + r + "> :")
        request.append(userRequest)

    return request


#
# main routine
#
# E, C, R, and A structures


print_welcome()

# intialize the data structures and get user input

numClient = int(input("Enter the number of clients:"))

E_TotalResources = get_number_resources()
print("gE_TotalResources = " + str(E_TotalResources))

R_MaximumRequest = predict_maximum_resources(numClient, E_TotalResources)

C_CurrentAllocations = initialize_current_allocations(numClient, E_TotalResources)

# all resources are initially available
A_AvailableResources = E_TotalResources

request = []

userQuit = False

while not userQuit:

    print()
    client = input("[Enter the client number or 'q' to quit:]")
    print()

    validClient = False

    if client == "q":
        userQuit = True
    else:
        # check the client number
        if int(client) >= 0 and int(client) < numClient:
            validClient = True
        else:
            print("Error: Invalid client number.")
            validClient = False

    if (not userQuit) and validClient:
        #print_available_resources(A_AvailableResources)

        request = get_client_request(client)

        # is the request safe or unsafe

        # if the request is safe service it

        # save request and if it is safe or unsafe into a txt file
        # with matrices printed nicely for debugging results


print("E_TotalResources = " + str(E_TotalResources))
print("A_AvailableResources = " + str(A_AvailableResources))
print("C_CurrentAllocations = " + str(C_CurrentAllocations))
print("R_MaximumRequest = " + str(R_MaximumRequest))




