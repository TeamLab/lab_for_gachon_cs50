author__ = 'samsung'

def oddEvenCheck(a,b):
    # '''
    # Input:
    #   -a: 실수 값 (Integer of float)
    #   -b: 실수 값 (Integer of float)
    # Output:
    #a 와 b 합이 짝수이면 Even 홀수이면 Odd
    # Examples:
    #   >>> oddEvenCheck(4,5)
    #   Odd
    #   >>> oddEvenCheck(2,2)
    #   Even
    # '''
    # pass
    # ===Modify codes below=============
    result = None
    # ==================================
    return result

def comparisonOperator(a, b):
    # '''
    # Input:
    #   -a: 실수 값 (Integer of float)
    #   -b: 실수 값 (Integer of float)
    # Output:
    #   -a와b의 곱이 10보다 클경우 BIgger Than 10
    #   -a와b의 곱이 10보다 같을 경우 Equal To 10
    #   -a와b의 곱이 10보다 작을경우 Smaller Than 10
    # Examples:
    #   >>> comparisonOperator(4,5)
    #   BIggerThan10
    #   >>> comparisonOperator(2,2)
    #   SmallerThan10
    # '''
    # pass
    # ===Modify codes below=============
    result = None
    # ==================================
    return result
def price(price):
    # '''
    # Input:
    #   -price(가격):실수 값 (Integer of float)
    # Output:
    #   -price(가격)가 10만원이하일 경우 10퍼샌트 할인,10만원초과일 경우 20퍼센트 할인
    # Examples:
    #   >>> comparisonOperator(40000)
    #   36000
    #   >>> comparisonOperator(110000)
    #   880000
    # '''
    # pass
    # ===Modify codes below=============
    result = None
    # ==================================
    return result
def AndOrNot_1():
    #1.False and False
    # ===Modify codes below=============
    return None
    # ==================================

def AndOrNot_2():
    #2.True or False
    # ===Modify codes below=============
    return None
    # ==================================

def AndOrNot_3():
    #3.4**2>10 or 10>4
    # ===Modify codes below=============
    return None
    # ==================================

def AndOrNot_4():
    #4.not 3**4 >4**3
    # ===Modify codes below=============
    return None
    # ==================================

def AndOrNot_5():
    #4.not 10%3 <= 10%2
    # ===Modify codes below=============
    return None
    # ==================================
def AndOrNot_6():
    #4.-(1**2)<2**0 and 10%10 <= 20-10*2
    #  ===Modify codes below=============
    return None
    # ==================================

if __name__ == "__main__":
    print ("Odd-even Check Test")
    print (oddEvenCheck(5,7)) # Expected Result: Even
    print (oddEvenCheck(4,7) == 'Odd') # Expected Result: True
    print (oddEvenCheck(3,9) == 'Odd') # Expected Result: False
    print ("Odd-even Check Test Closed \n")

    print ("Comparison Operator Test")
    print (comparisonOperator(4,5)) # Expected Result: "BIgger Than 10"
    print (comparisonOperator(2,2) == "Smaller Than 10") # Expected Result: True
    print (comparisonOperator(10,15) == "Smaller Than 10") # Expected Result: False
    print ("Comparison Operator Test Closed \n")

    print ("Discount Price Test ")
    print (price(40000)) # Expected Result: 36000
    print (price(50000) == 45000) # Expected Result: True
    print (price(110000) == 89000) # Expected Result: False
    print ("Discount Price Test Closed \n")

    print ("AndOrNot-1 TEST")
    print (AndOrNot_1() == True) # Expected Result: True
    print (AndOrNot_1() == False) # Expected Result: False
    print ("AndOrNot-1 TEST Closed \n")

    print ("AndOrNot-2 TEST")
    print (AndOrNot_2() == False) # Expected Result: True
    print (AndOrNot_2() == True) # Expected Result: False
    print ("AndOrNot-2 TEST Closed \n")

    print ("AndOrNot-3 TEST")
    print (AndOrNot_3() == True) # Expected Result: True
    print (AndOrNot_3() == False) # Expected Result: False
    print ("AndOrNot-3 TEST Closed \n")

    print ("AndOrNot-4 TEST")
    print (AndOrNot_4() == False) # Expected Result: True
    print (AndOrNot_4() == True) # Expected Result: False
    print ("AndOrNot-4 TEST Closed \n")
 
    print ("AndOrNot-5 TEST")
    print (AndOrNot_5() == True) # Expected Result: True
    print (AndOrNot_5() == False) # Expected Result: False
    print ("AndOrNot-5 TEST Closed \n")

    print ("AndOrNot-6 TEST")
    print (AndOrNot_6() == True) # Expected Result: True
    print (AndOrNot_6() == False) # Expected Result: False
    print ("AndOrNot-6 TEST Closed \n")

