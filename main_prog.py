"""
-------------------------------------------------------------------
Programming Assignment 2
-------------------------------------------------------------------
Name        : Manan Darji
Roll Number : CS22MTECH14004
Subject     : Advance Data Structure and Algorithm (CS6013)
Topic       : Optimal Binary Search Tree
-------------------------------------------------------------------
"""
__author__ = "@Manan_Darji"
# -------------------------------------------------- INITIALIZATION --------------------------------------------------
InputList = []
ProbSet = set()
WordSet = set()
GoodToGO = True
# ---------------------------------------------- TO CHECK STATIC INPUT ------------------------------------------------------
# InputList = [ ('add', 0.3), ('ball', 0.5),('cat', 0.2)]
# InputList = [
#     ("a", 0.22),
#     ("am", 0.18),
#     ("and", 0.2),
#     ("egg", 0.05),
#     ("if", 0.25),
#     ("the", 0.02),
#     ("two", 0.08),
# ]
# ----------------------------------------------- INPUT -----------------------------------------------------
print("-" * 100)
N = int(input("How many strings do you want to insert in the BST : "))
print("-" * 100)
print(
    "Enter "
    + str(N)
    + " strings in sorted Dictionary order along with their probabilities: "
)
print("-" * 100)
print("Enter in pair of name and probabilities Ex. 'Banana 0.25' ")
print("-" * 100)
for i in range(N):
    print("Enter Entry No " + str(i+1), end=" : ")
    p, q = input().strip().split(" ")
    InputList.append((p, float(q)))
print("-" * 100)
# ------------------------------------------------- VERIFYING PREREQUISITES ---------------------------------------------------
TotalProbability = 0
LastStr = "a"
# Here we are verifying all prerequisites
for x in InputList:

    # Check for all Distinct Input Words
    if x[0] in WordSet:
        print("The Words are not distinct.")
        GoodToGO = False
    else:
        WordSet.add(x[0])

    # Check for all Distinct Probabilities
    if x[1] in ProbSet:
        print("The probabilities are not distinct.")
        GoodToGO = False
    else:
        ProbSet.add(x[1])

    # Check For Sorted input / Here we are checking that last word is alphabetically small
    if x[0] < LastStr:
        print("The strings entered are not in sorted order.")
        GoodToGO = False
    else:
        LastStr = x[0]

    # Adding all Probabilities to verify later
    TotalProbability += x[1]

# To Handel some small round-off error using some bounds
if TotalProbability < 1.000001 and TotalProbability > 0.999999:
    pass
else:
    print("The probabilities don’t add up to 1.")
    GoodToGO = False

# Check point to check that all prerequisite conditions satisfied or not
if not GoodToGO:
    exit()
# ------------------------------------------------ MEMOIZATION INITIALIZATION----------------------------------------------------
# Length Of Input
InpLen = len(InputList)

# Declared 2 Dynamic Tables for score DP and Root DP
mamo = [[0 if i == j else "x" for j in range(InpLen + 1)] for i in range(InpLen + 1)]
mamoR = [[0 if i == j else "x" for j in range(InpLen + 1)] for i in range(InpLen + 1)]

# ----------------------------------------------------------------------------------------------------

def ProbSum(i, j):
    """This Function Used to Calculate The Summation of Probabilities given some range

    Args:
        i (int): This is Start Range
        j (int): This is End of the Range

    Returns:
        Float : This return Float Sum of Probabilities.
    """
    global InputList
    s = 0
    for k in range(i, j):
        s += InputList[k][1]
    return s

# ----------------------------------------------------------------------------------------------------

def OptimalBST(i, j):
    """This is The Function We used to Calculate Cost for OptimalBST

    Args:
        i (int): Starting Index
        j (int): Ending Index

    Returns:
        _type_: _description_
    """
    # BaseCase
    # Return if we have i == j
    if i == j:
        return 0

    # Declare some min value to keep track of min value from different root calls
    MinVal = float("inf")
    MinValRoot = -1

    # Iterate and Recursively Call for all Root values to find best root value
    for k in range(i + 1, j + 1):

        # Here Using Memoization we are checking if we already have value for current rec call
        # If not we Find the Value
        if mamo[i][k - 1] == "x":
            mamo[i][k - 1] = OptimalBST(i, k - 1)

        if mamo[k][j] == "x":
            mamo[k][j] = OptimalBST(k, j)

        # Simple Addition When Root is k
        val = mamo[i][k - 1] + mamo[k][j]

        # Here We Keep Track of Minimum value Root and cost
        if val < MinVal:
            MinVal = val
            MinValRoot = k

    # Adding Min cost with That Words Probability
    mamo[i][j] = MinVal + ProbSum(i, j)
    # Adding Best Root to print Pre Order Later
    mamoR[i][j] = MinValRoot

    # Returning Cost
    return mamo[i][j]

# ----------------------------------------------------------------------------------------------------

def PrintPreOrder(i, j):
    """This Function We Used to Print PreOrder Of Any BST.
    Here we just Print Words In Pre-Order form.

    Args:
        i (int): This is Starting Index
        j (int): This is Ending Index

    Returns:
        none: We return Nothing
    """
    if i == j:
        return 0
    k = mamoR[i][j]
    print(InputList[k - 1][0], end=" ")
    PrintPreOrder(i, k - 1)
    PrintPreOrder(k, j)

# ------------------------------------------------- MAIN FUNCTION CALL ---------------------------------------------------

print("-" * 100)
print("The minimum expected total access time is %0.4f" % OptimalBST(0, InpLen) + ".")
print("-" * 100)
print(
    "Pre-order traversal of the BST that provides minimum expected total access time is:"
)
PrintPreOrder(0, InpLen)
print()
print("-" * 100)
# ----------------------------------------------------------------------------------------------------

