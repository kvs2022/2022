# def add(x,y):
#     a=float(x)
#     b=float(y)
    # a=int(x)
    # b=int(y)
    # return float(a+b)
    # return int(a+b)
# a=eval(input("Enter a no"))
# b=eval(input("Enter a no"))
# print(add(a,b))

# a=int(input("Enter a no"))
# b=int(input("Enter a no"))
# a=float(input("Enter a no"))
# b=float(input("Enter a no"))
# print(add(a,b))

# def add(x: int ,y: int):
#     x=input("Enter a no")
#     y=input("Enter a no")
#     return x+y
# # x=int(input("Enter a no "))
# # y=float(input("Enter a no "))
# print(add(3,4))



# Python3 implementation of First-Fit algorithm
 
# Function to allocate memory to
# blocks as per First fit algorithm
def firstFit(blockSize, m, processSize, n):
     
    # Stores block id of the
    # block allocated to a process
    allocation = [-1] * n
 
    # Initially no block is assigned to any process
 
    # pick each process and find suitable blocks
    # according to its size ad assign to it
    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                 
                # allocate block j to p[i] process
                allocation[i] = j
 
                # Reduce available memory in this block.
                blockSize[j] = 0 #- processSize[i]
 
                break
 
    print(" Process No. Process Size      Block no.")
    for i in range(n):
        print(" ", i + 1, "         ", processSize[i], "         ", end = " ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")
 
# Driver code
if __name__ == '__main__':
    blockSize = [100, 500, 200, 300, 600]
    processSize = [212, 417, 112, 426]
    m = len(blockSize)
    n = len(processSize)
 
    firstFit(blockSize, m, processSize, n)



    # 100, 500, 200, 300, 600
    # 212, 417, 112, 426