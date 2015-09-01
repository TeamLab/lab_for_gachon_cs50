author__ = 'seri'
#-*- coding:utf-8-*-

def datatype_1():
    # >>> print 5
    # 5
    # 5의 데이터 타입은?(Integer,Real number,String)
    return None

def datatype_2():
    # >>> print 4.0
    # 4.0 의 데이터 타입은?(Integer,Real number,String)
    return None

def datatype_3():
    # >>> print 34 + 60
    # 94
    # 94의 데이터 타입은?(Integer,Real number,String)
    return None

def datatype_4():
    # >>> print 3.4 + 7.5
    # 10.9
    # 5의 데이터 타입은?(Integer,Real number,String)
    return None

def datatype_5():
    # >>> print "Hello,World!"
    #
    # "Hello,World!"의 데이터 타입은?(Integer,Real number,String)
    return None

def variable_1():
   # >>>teacher= "Mr.Choi"
   # >>>print teacher
    return None

def variable_2():
    # >>> Gachon=10
    # >>> Univercity=9
    # >>>print gachon+univercity
   return None

def variable_3():
    # >>> apple=5
    # >>> samsung =7
    # >>> shaomi =6
    # >>> print "apple"+"samsung"+"shaomi"
    return None

def variable_4():
    # >>> age =5
    # >>> age= age +7
    # print age
    return None

if __name__ == "__main__":
    print (" Datatype_1 Test")
    print (datatype_1()=="Integer") # Expected Result: True
    print (datatype_1()=="Real number") # Expected Result: False
    print (" Datatype_1 Closed \n")

    print ("Datatype_2 Test")
    print (datatype_2()=="Real number") # Expected Result: True
    print (datatype_2()=="Integer") # Expected Result: False
    print ("Datatype_2 Closed \n")

    print ("Datatype_3 Test")
    print (datatype_3()=="Integer") # Expected Result: True
    print (datatype_3()=="Real number") # Expected Result: False
    print ("Datatype_3 Closed \n")

    print ("Datatype_4 Test")
    print (datatype_4()=="Real number") # Expected Result: True
    print (datatype_4()=="Integer") # Expected Result: False
    print ("Datatype_4 Closed \n")

    print ("Datatype_5 Test")
    print (datatype_5()=="String") # Expected Result: True
    print (datatype_5()=="Integer") # Expected Result: False
    print ("Datatype_5 Closed \n")

    print (" variable_1 Test")
    print (variable_1()=="Mr.Choi") # Expected Result: True
    print (" variable_1 Closed \n")

    print (" variable_2 Test")
    print (variable_2()==19) # Expected Result: True
    print (variable_2()=="GachonUniversity") # Expected Result: False
    print (" variable_2 Closed \n")

    print (" variable_3 Test")
    print (variable_3()== "applesamsungshaomi") # Expected Result: True
    print (variable_3()==18) # Expected Result: False
    print (" variable_3 Closed \n")

    print (" variable_4 Test")
    print (variable_4()== 12) # Expected Result: True
    print (variable_4()== 5) # Expected Result: False
    print (" variable_4 Closed \n")

