"""
Gabriel Jerome Solomon
Bankers Algorithm, Homework programming question implementation

Question from Professor Elkady

Program a simulation of the banker’s algorithm. Your program should cycle 
through each of the bank clients asking for a request and evaluating whether it 
is safe or unsafe. Output a log of requests and decisions to a file.

"""

import sys

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
    """
    get initial information from user on number of resources
    """
    resources = []
    # get the number of resources for each resource type
    for e in enumerate(gResourceTypes):
        n = input("Enter number of resources for resource #" + str(e[0]) + " <" + e[1] + "> :")
        resources.append(int(n))

    return resources


def predict_maximum_resources(numClient, totalResources):
    """
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
    """
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
    """
    get client resource request
    """

    request = []

    print("Request for client #" + str(c) + ":")


    for r in gResourceTypes:
        userRequest = input("\tEnter the number of <" + r + "> resources you are requesting :")
        request.append(userRequest)

    return request


def print_resource_vector(v):
    """
    print a resource vector
    """
    for i in range(0, len(v)):
        print("\t" + gResourceTypes[i] + " = " + str(v[i]))


def print_status(numClient, E_TotalResources, R_MaximumRequest, C_CurrentAllocations, A_AvailableResources):
    """
    prints the bankers algorithm data structures
    """

    print("-------------")
    print("System Status")
    print("-------------")

    print("E Total Resources: " + str(E_TotalResources))
    for i in range(0, len(E_TotalResources)):
        print("\t" + gResourceTypes[i] + " = " + str(E_TotalResources[i]))

    print("A Available Resources: " + str(A_AvailableResources))
    for i in range(0, len(A_AvailableResources)):
        print("\t" + gResourceTypes[i] + " = " + str(A_AvailableResources[i]))

    print("Current Allocation:")
    for c in range(0, numClient):
        sys.stdout.write("\t" + "Client #" + str(c))
        for r in range(0, len(gResourceTypes)):
            sys.stdout.write(" " + gResourceTypes[r] + " = ")
            sys.stdout.write(str(C_CurrentAllocations[c][r]))
        sys.stdout.write("\n")

    print("Maximum Requests")
    for c in range(0, numClient):
        sys.stdout.write("\t" + "Client #" + str(c))
        for r in range(0, len(gResourceTypes)):
            sys.stdout.write(" " + gResourceTypes[r] + " = ")
            sys.stdout.write(str(R_MaximumRequest[c][r]))
        sys.stdout.write("\n")


def is_request_safe(request,E_TotalResources, R_MaximumRequest, C_CurrentAllocations, A_AvailableResources):
    """
    determine if the request is safe or unsafe
    """

    safe = False

    return safe


#
# main routine
#
# E, C, R, and A structures


print_welcome()

# intialize the data structures and get user input

numClient = int(input("Enter the number of clients:"))
print()

E_TotalResources = get_number_resources()
print()

R_MaximumRequest = predict_maximum_resources(numClient, E_TotalResources)

C_CurrentAllocations = initialize_current_allocations(numClient, E_TotalResources)

# all resources are initially available
A_AvailableResources = E_TotalResources



# print the initial status
print_status(numClient, E_TotalResources, R_MaximumRequest, C_CurrentAllocations, A_AvailableResources)

#
# loop until user quits and ask for resource requests
#
request = []

userQuit = False

while not userQuit:

    print()
    client = input("[Enter the client number 0-" + str(numClient-1) + " to request resources or 'q' to quit:]")
    print()

    validClient = False

    if client == "q":
        userQuit = True
    else:
        # check the client number
        if 0 <= int(client) < numClient:
            validClient = True
        else:
            print("Error: Invalid client number.")
            validClient = False

    if (not userQuit) and validClient:
        #print_available_resources(A_AvailableResources)

        request = get_client_request(client)

        # print("Request = " + str(request))

        # check if the request is safe
        safe = is_request_safe(request,E_TotalResources, R_MaximumRequest, C_CurrentAllocations, A_AvailableResources)

        print("Request for:")
        print_resource_vector(request)
        if safe:
            print(" is SAFE.")
        else:
            print(" is UNSAFE.")

        
        # if the request is safe
        # execute_the_request(request,E_TotalResources, R_MaximumRequest, C_CurrentAllocations, A_AvailableResources)

        # save request and if it is safe or unsafe into a txt file
        # save matrices printed nicely for debugging results


# print the final status
print_status(numClient, E_TotalResources, R_MaximumRequest, C_CurrentAllocations, A_AvailableResources)




