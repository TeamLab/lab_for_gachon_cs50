# 데이터 형변환================================================

def str_to_int(string):
  
	# """
  #	Input:
	# 	-string: 문자열(숫자형태의 문자열) 
	# Output:
	# 	-int: 정수 값
	# Examples:
	# 	>>> str_to_int("3")
	# 	3
	# 	>>> str_to_int("135")
	# 	135
	# """
	# ===Modify codes below=================
	
	result = None

	# ======================================

	return result


def str_to_float(string):

	# """
  #	Input:
	# 	-string: 문자열(숫자형태의 문자열) 
	# Output:
	# 	-float: 소수를 가지는 수
	# Examples:
	# 	>>> str_t0_float("3")
	# 	3.0
	# 	>>> add_string_number("135.4567")
	# 	135.4567
	# """
	# ===Modify codes below=================
	
	result = None

	# ======================================

	return result


def number_to_str(integer):

	# """
	# Input:
	# 	-number: 실수 값
	# Output:
	# 	-string: 문자열
	# Examples:
	# 	>>> number_t0_str(3)
	# 	"3"                             #파이썬 쉘에선 저렇게 출력되는데 리눅스 쉘에서 .py를 실행시키면 3으로 출력됨
	# 	>>> number_to_str(-3.456)
	# 	"-3.456"
	# """
	# ===Modify codes below=================
	
	result = None

	# ======================================

	return result

# integer와 string 더하기===============================================

def add_string_number(string, number):
	# """
	# Input:
	# 	-string: 문자열 
	# 	-number: 실수 값
	# Output:
	# 	-문자열과 실수 값의 연결
	# Examples:
	# 	>>> add_string_number("Gachon", 3)
	# 	"Gachon3"
	# 	>>> add_string_number("jiho",14)
	# 	"jiho14"
	# """
	# ===Modify codes below=================
	
	result = None

	# ======================================

	return result

# string과 string 더하기================================================

def add_string_string(str_1, str_2):
	# """
  #	Input:
	# 	-str_1: 문자열
	#		-str_2: 문자열
	# Output:
	# 	-str: 두 문자열의 연결
	# Examples:
	# 	>>> add_string_string("3", "흐흐흐")
	# 	"3흐흐흐"
	# 	>>> add_string_string("135", "45.76")
	# 	"13545.76"
	# """
	# ===Modify codes below=================
	
	result = None

	# ======================================

	return result

# 사칙연산==============================================================

def associative_law_add(a, b, c):

	# """
	# <설명>
	#		아래의 연산에 결합법칙을 적용해 계산하여라.
	#		(a + b) + c
	# Input:
	# 	-a, b, c: 실수 값  
	# Output:
	# 	-결합법칙이 적용되어 계산된 실수 값
	# Examples:
	# 	>>> commutative_law(3, 4, 5)
	# 	12
	# """
	# ===Modify codes below=================
	
	result = None

	# ======================================

	return result


def associative_law_mutiple(a, b, c):

	# """
	# <설명>
	#		아래의 연산에 결합법칙을 적용해 계산하여라.
	#		(a * b) * c
	# Input:
	# 	-a, b, c: 실수 값 
	# Output:
	# 	-결합법칙이 적용되어 계산된 실수 값
	# Examples:
	# 	>>> distributive_law(3, 4, 5)
	# 	60
	# """
	# ===Modify codes below=================
	
	result = None

	# ======================================

	return result


def distributive_law(a, b, c):

	# """
	# <설명>
	#		아래의 연산에 분배법칙을 적용해 계산하여라.
	#		a * (b + c)
	# Input:
	# 	-a, b, c: 실수 값 
	# Output:
	# 	-분배법칙이 적용되어 계산된 실수 값
	# Examples:
	# 	>>> distributive_law(3, 4, 5)
	# 	27
	# """
	# ===Modify codes below=================
	
	result = None

	# ======================================

	return result


def commutative_law_add(a, b):	

	# """
	# <설명>
	#		아래의 연산에 교환법칙을 적용해 계산하여라.
	#		a + b
	# Input:
	# 	-a, b: 실수 값 
	# Output:
	# 	-교환법칙이 적용되어 계산된 실수 값
	# Examples:
	# 	>>> commutative_law_add(3, 4)
	# 	7
	# """
	# ===Modify codes below=================
	
	result = None

	# ======================================

	return result


def commutative_law_mutiple(a, b):

	# """
	# <설명>
	#		아래의 연산에 교환법칙을 적용해 계산하여라.
	#		a * b
	# Input:
	# 	-a, b: 실수 값 
	# Output:
	# 	-교환법칙이 적용되어 계산된 실수 값
	# Examples:
	# 	>>> commutative_law_mutiple(3, 4)
	# 	12
	# """
	# ===Modify codes below=================
	
	result = None

	# ======================================

	return result

# 지수연산=============================================================

def exponent(base, power):

	# """
	# <설명>
	#		다음의 곱셈연산을 지수연산으로 바꿔 계산하여라.
	#		base * base * base * ... * base
	# Input:
	# 	-base, power: 실수 값 
	# Output:
	# 	-지수연산이 적용되어 계산된 값
	# Examples:
	# 	>>> exponent(3, 4)
	# 	81
	# """
	# ===Modify codes below=================
	
	result = None

	# ======================================

	return result

# 증가, 감소=========================================================

def increment_by_k(number, k)

	# """
	# <설명>
	#		아래의 식을 다른 방법으로 표현해라.
	#		number = number + k
	# Input:
	# 	-number, k: 실수 값 
	# Output:
	# 	-실수 값
	# Examples:
	# 	>>> increment_by_k(3, 4)
	# 	7
	# """
	# ===Modify codes below=================
	
	result = None

	# ======================================

	return result


def decrement_by_k(number, k):
	
	# """
	# <설명>
	#		아래의 식을 다른 방법으로 표현해라.
	#		number = number - k
	# Input:
	# 	-number, k: 실수 값 
	# Output:
	# 	-실수 값
	# Examples:
	# 	>>> commutative_law(3, 4)
	# 	-1
	# """
	# ===Modify codes below=================
	
	result = None

	# ======================================

	return result



return result
if __name__ == '__main__':
    print ("Str_to_int Test")
    print (str_to_int("56")) # Expected Result: 56
    print (str_to_int("27") == 27) # Expected Result: True
    print ("Str_to_int Test Closed \n")


    print ("Str_to_float Test")
    print (Str_to_float("8.4501")) # Expected Result: 8.4501
    print (Str_to_float("3.4") == 3.4) # Expected Result: True
    print (Str_to_float("6.74") == 9.8) # Expected Result: False
    print ("Str_to_float Test Closed \n")

    print ("Number_to_string Test")
    print (Number_to_string Test(56)) # Expected Result: "56"
    print (Number_to_string Test(4.751) == "4.751") # Expected Result: True
    print (Number_to_string Test(3) == "17") # Expected Result: False
    print ("Number_to_string Test Test Closed \n")

    print ("Add_string_number Test")
    print (Add_string_number("67",5)) # Expected Result: "675"
    print (Add_string_number("Gachon",4) == 2) # Expected Result: False
    print (Add_string_number("Gachon", 15) == "Gachon15") # Expected Result: True
    print ("Add_string_number Test Closed \n")

    print ("Add_string_string Test")
    print (Add_string_string("1.4", "1.5")) # Expected Result: "1.41.4"
    print (Add_string_string("이길", "여") == 15) # Expected Result: False
    print ("Add_string_string Test Closed \n")

    print ("Associative_law_add Test")
    print (Associative_law_add(3,5,4)) # Expected Result: 12
    print (Associative_law_add(10,5,67) == 15) # Expected Result: False
    print ("Associative_law_add Test iClosed \n")

    print ("Associative_law_multiple Test")
    print (Associative_law_multiple(3,5,2)) # Expected Result: 30
    print (Associative_law_multiple(10,5,1) == 50) # Expected Result: True
    print ("Associative_law_multiple Test Closed \n")

    print ("Distributive_law Test")
    print (Distributive_law(3,5,2)) # Expected Result: 21
    print (Distributive_law(10,5,2) == 70) # Expected Result: True
    print ("Distributive_law Test Closed \n")

    print ("Commutative_law_add Test")
    print (Commutative_law_add(3,5)) # Expected Result: 8
    print (Commutative_law_add(9,5) == 14) # Expected Result: True
    print ("Commutative_law_add Test Closed \n")

    print ("Commutative_law_multiple Test")
    print (Commutative_law_multiple(3,5)) # Expected Result: 15
    print (Commutative_law_multiple(10,5) == 40) # Expected Result: False
    print ("Commutative_law_multiple Test Closed \n")

    print ("Exponent Test")
    print (Exponent(3,5)) # Expected Result: 243
    print (Exponent(10,5) == 15) # Expected Result: False
    print ("Exponent Test Closed \n")	

    print ("Increment_by_k Test")
    print (Increment_by_k(146,5)) # Expected Result: 151
    print (Increment_by_k(10,5) == 15) # Expected Result: True
    print ("Increment_by_k Test Closed \n")

    print ("Decrement_by_k Test")
    print (Decrement_by_k(3,5)) # Expected Result: -2
    print (Decrement_by_k(10,5) == 15) # Expected Result: False
    print ("Decrement_by_k Test Closed \n")















