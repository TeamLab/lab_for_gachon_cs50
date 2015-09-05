# _*_coding : utf-8 _*_
def float_answer(a, b):
    # '''
    # Input:
    #   -a: 실수 값 (Integer of float)
    #   -b: a를 나누었을 때 몫이 나누어 떨어지지 않는 실수 값 (Integer of float)
    # Output:
    #   -a를 b로 나눈 값
    # Examples:
    #   >>> float_answer(7,2)
    #   3.5
    #   >>> float_answer(11,4)
    #   2.75
    # '''
    # pass
    # ===Modify codes below=============
	float(a)
	float(b)

	result = a/b 
    # ==================================
	return result

def fahrenheit_to_celsius(a):
    # '''
    # Input:
    #   - a: 화씨 온도(Integer of float)
    # Output:
    #   - a의 섭씨 온도
    # Examples:
    #   >>> fahrenheit_to_celsius(86)
    #   30
    #   >>> fahrenheit_to_celsius(60)
    #   15.56
    # '''
    # celsius = (fahrenheit - 32) / 1.8
    # pass
    # ===Modify codes below=============
	result = (float(a) - 32.0 ) / 1.8
    # ==================================
	return result

if __name__ == "__main__":
    print ("float_answer Test")
    print ( float_answer(7,2)) # Expected Result: 3.5
    print ( float_answer(11,4) == 2.75 ) # Expected Result: True
    print ("float_answer Test Closed \n")

    print ("fahrenheit_to_celsius Test")
    print (fahrenheit_to_celsius(86)) # Expected Result: 30
    print (fahrenheit_to_celsius(60)) # Expected Result: 15.56
    print (fahrenheit_to_celsius(73) == 22.78) # Expected Result: True
    print (fahrenheit_to_celsius(79) == 24) # Expected Result: False
    print ("fahrenheit_to_celsius Test Closed \n")

