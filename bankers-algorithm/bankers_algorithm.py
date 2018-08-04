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
    resourceList = []
    # get the number of resources for each resource type
    for resource in range(0, len(gResourceTypes)):
        n = input("Enter number of total resources for <" + gResourceTypes[resource] + "> :")
        resourceList.append(int(n))

    return resourceList


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


def get_client_request(client, R_MaximumRequest, C_CurrentAllocations):
    """
    get client resource request
    """

    request = []

    print("Request for client #" + str(client) + ":")

    r = 0
    for resource in gResourceTypes:
        maxResourceRequest = R_MaximumRequest[client][r] - C_CurrentAllocations[client][r]

        validInput = False
        userRequest = 0

        while not validInput:
            userRequestStr = input("\tEnter the number of <" + resource + "> resources you are requesting (from 0-" +
                                    str(maxResourceRequest) + ") :")
            userRequest = int(userRequestStr)
            if 0 <= userRequest <= maxResourceRequest:
                validInput = True
            else:
                print ("ERROR: Client requested too many resources.  Must be in range from 0-" + str(maxResourceRequest) + ".")

        request.append(int(userRequest))

        r = r + 1

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

    print("------------------------------------------")
    print("System Status")
    print("------------------------------------------")

    print("E Total Resources: " + str(E_TotalResources))
    print_resource_vector(E_TotalResources)

    print("A Available Resources: " + str(A_AvailableResources))
    print_resource_vector(A_AvailableResources)

    print("Current Allocation:")
    for client in range(0, numClient):
        sys.stdout.write("\t" + "Client #" + str(client) + " [")
        for resource in range(0, len(gResourceTypes)):
            sys.stdout.write(" " + gResourceTypes[resource] + " = ")
            sys.stdout.write(str(C_CurrentAllocations[client][resource]))
        sys.stdout.write("]")
        sys.stdout.write("\n")

    print("Maximum Requests")
    for client in range(0, numClient):
        sys.stdout.write("\t" + "Client #" + str(client) + " [")
        for resource in range(0, len(gResourceTypes)):
            sys.stdout.write(" " + gResourceTypes[resource] + " = ")
            sys.stdout.write(str(R_MaximumRequest[client][resource]))
        sys.stdout.write("]")
        sys.stdout.write("\n")

    print("------------------------------------------")


def is_request_satisfied_by_available(request, A_AvailableResources):
    """
    determine if the request can be satisfied by available resources
    """

    canPayOff = True

    # check if there are resources available to satisfy the request. If so, it is safe.
    # subtract the vectors, if sum is >= 0, then resources are available to satisfy the request
    # in the available resources
    diff = list(map(int.__sub__, request, A_AvailableResources))

    for r in diff:
        if r > 0:
            canPayOff = False

    return canPayOff


def is_request_satisfied_by_paid_loans(request, numClient, E_TotalResources, R_MaximumRequest, C_CurrentAllocations, A_AvailableResources):
    """
    determine if the request can be satisfied by loans being paid back to the bank.
    can we complete any clients requests with available resources
    """

    canBeSatisfied = False

    #
    # calculate the total amount of potential resources available
    #
    # for each client if it can be satisfied with the available resources.
    # If it can be satisfied with available resources, add the current allocations to the
    # potentially available resources.

    potentialAvailableResources = A_AvailableResources.copy()

    # make a list of booleans
    alreadyPaidOffClient = [False] * numClient

    firstTime = True
    checkAgain = False

    # check all the clients until you do not need to check again
    while firstTime or checkAgain:

        # if you are checking again, set checkAgain to false
        if checkAgain:
            checkAgain = False

        # for each client find out if it can be satisfied with available resources
        for client in range(0, numClient):

            # how many resources are remaining and still needed by this client
            remainingNeededResources = list(map(int.__sub__, R_MaximumRequest[client], C_CurrentAllocations[client]))

            # if we use all the potentially available resources, what is owed
            owedResources = list(map(int.__sub__, remainingNeededResources, potentialAvailableResources))

            # if any of the owedResources are negative, we do not have enough available
            # resources to pay off the loan
            canPayOff = True
            for r in owedResources:
                if r > 0:
                    canPayOff = False

            # if we can pay off the loan and we have not already paid off the loan, add the current allocations
            # using the potential available resources and mark that we can pay off the client
            if canPayOff and (not alreadyPaidOffClient[client]):
                potentialAvailableResources = list(map(int.__add__, potentialAvailableResources, C_CurrentAllocations[client]))
                alreadyPaidOffClient[client] = True
                checkAgain = True

        # we have gone through the loop one time
        firstTime = False


    # see if the potentially available resources can satisfy the request
    canPayOff = True
    owedResources = list(map(int.__sub__, request, potentialAvailableResources))
    for r in owedResources:
        if r > 0:
            canPayOff = False

    # if can pay off with potential available resources, then the request can be satisfied
    canBeSatisfied = canPayOff

    return canBeSatisfied


def execute_the_request(request, client, C_CurrentAllocations, A_AvailableResources):
    """
    executive the request and adjust the current allocations and available resources
    """

    # adjust the balances
    for resource in range(0, len(gResourceTypes)):

        # subtract the request from available resources (but use max to keep it from being negative)
        A_AvailableResources[resource] = max(A_AvailableResources[resource] - request[resource], 0)

        # update the current allocations
        C_CurrentAllocations[client][resource] = C_CurrentAllocations[client][resource] + request[resource]


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
A_AvailableResources = E_TotalResources.copy()


#
# loop until user quits and ask for resource requests
#
request = []

userQuit = False

while not userQuit:

    print_status(numClient, E_TotalResources, R_MaximumRequest, C_CurrentAllocations, A_AvailableResources)

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

        request = get_client_request(int(client), R_MaximumRequest, C_CurrentAllocations)

        # print("Request = " + str(request))

        # check if the request is safe
        satisfiedByAvailableResources = is_request_satisfied_by_available(request, A_AvailableResources)

        if satisfiedByAvailableResources:
            print("Request can be satisfied by available resources.")
            safe = True

        satisfiedByPaidLoans = is_request_satisfied_by_paid_loans(request, numClient, E_TotalResources, R_MaximumRequest,
                                                                 C_CurrentAllocations, A_AvailableResources)

        if satisfiedByPaidLoans:
            print("Request can be satisfied by paid loans.")
            safe = True

        print("Request is for:")
        print_resource_vector(request)

        s = "Request for:" + str(request) + " is "

        if safe:
            s += "SAFE."
        else:
            s += "UNSAFE."
        print(s)

        # if the request is safe, execute the request
        if safe:
            print("Executing the request.")
            execute_the_request(request, int(client), C_CurrentAllocations, A_AvailableResources)
        else:
            print("Request can not be safely-satisfied and will not be executed.")

        # save request and if it is safe or unsafe into a txt file
        # save matrices printed nicely for debugging results

