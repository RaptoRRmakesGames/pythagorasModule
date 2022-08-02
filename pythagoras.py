def add(n, n1, n2=0, n3=0, n4=0, n5=0, n6=0, n7=0, n8=0, n9=0):
    
    # check how many numbers we will be adding
    
    nums = [n, n1, n2, n3, n4, n5, n6, n7, n8, n9]
    adding_nums = []

    for num in nums:
        if num > 0:
            adding_nums.append(num)

    nums = adding_nums
    
    # doing the adding and returning it
    
    sum = 0 
    
    for num in nums:
        sum += num
    
    return sum 
            
def substract(number, sub1, sub2=0, sub3=0, sub4=0, sub5=0, sub6=0, sub7=0, sub8=0, sub9=0):
    
    # taking out useless numbers
    nums =  [sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9]
    good_nums = []
    
    for num in nums:
        if num > 0:
            good_nums.append(num)
            
    nums = good_nums
    
    # doing the subtracting and returning it 
    
    takeout = 0
    
    for i in nums:
        takeout += i
    
    return number - takeout

def multiply(n, n1, n2=0, n3=0, n4=0, n5=0, n6=0, n7=0, n8=0, n9=0):
    
    # check if num is zero
    
    nums = [n, n1, n2, n3, n4, n5, n6, n7, n8, n9]
    adding_nums = []

    for num in nums:
        if num > 0:
            adding_nums.append(num)

    nums = adding_nums
    
    # multiply and return
    
    sum = nums[0]
    
    for i in nums:
        if i == nums[0]:
            continue
        sum *= i
    
    return sum

def divide(n, n1, n2=0, n3=0, n4=0, n5=0, n6=0, n7=0, n8=0, n9=0):
    
    # check if any num is 0
    nums = [n, n1, n2, n3, n4, n5, n6, n7, n8, n9]
    adding_nums = []

    for num in nums:
        if num > 0:
            adding_nums.append(num)

    nums = adding_nums
    
    # divide and return
    
    sum = nums[0]
    
    for i in nums:
        if i == nums[0]:
            continue
        sum /= i
        
    return sum

def getAverage(numbers):  
    try:
        divideby = len(numbers)
        average = 0
    
 
        for i in numbers:
            average += i
            
        return average / divideby
    except:
        print("please set 'getAverage' parameters as a list full of integers")

def getSquareRoot(num):
    return num ** 0.5

def raisePower(num, raiseto):
    return num ** raiseto

