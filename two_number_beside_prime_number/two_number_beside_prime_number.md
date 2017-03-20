Lab #- 소수의 개수 구하기 (Two_number_beside_prime_number)
======================================
Copyright 2016 © document created by TeamLab.Gachon@gmail.com


## Introduction
이번 lab에서는 개별 함수의 작성 그리고 각 함수들의 연결을 연습해 본다. 
이번 Count prime_number Lab은 사용자가 입력한 임의의 자연수 범위 내의 소수의 개수를 구해주는 프로그램을 만드는 것이다.


## 숙제 template 파일 다운로드
먼저 숙제 template 파일을 cs50 서버로 부터 다운로드 받는다. 로그인 후 나타나는 bash shell에서 다음과 같은 명령을 입력하자.
```bash
python3.4 submit_assignment.py -get two_number_beside_prime_number
```  
입력하면 다운로드 안내 메세지와 함께 `two_number_beside_prime_number.py` 파일이 다운로드 될 것이다. 


## count_prime_number.py 파일 Overview

`vim editor`로 `two_number_beside_prime_number.py`을 열어 전체적인 개요를 보자. `vi two_number_beside_prime_number.py`명령으로 파일을 열어보면 main 함수와 여러개의 함수들이 존재할 것이다. 각 함수들은 여러분께서 직접 작성해서 제출해야 하는 함수이고, main 함수는 실제 count_prime_number을 실행하는 함수이다. 각 함수의 구현 내용은 아래와 같다
 수강생이 할일은 크게 두 가지다. 하나는 프로그램 수행을 위해 3개의 함수를 작성하는 것이고, 두 번째는 main함수에 작성된 3개의 함수를 사용해서 소수의 개수와 소수의 리스트를 구해 보는 것이다. 현재 코드는 헐렁하지만 여러분들이 빈 공간을 채우면 된다.


## change_type_str_to_int_of_list 함수 수정하기
3개의 함수부터 작성해보자. 이미 함수 하나를 작성하는 것은 앞에서 연습해보았기 때문에 어렵지 않을 수도 있다. 아래 내용을 참고하여 change_type_str_to_int_of_list 함수를 작성하자.

내용           | 구성 
--------       | ---
함수명      | change_type_str_to_int_of_list
input 변수  | string type의 value를 가진 list
Process     | value가 정수일 경우는 결과값에 포함하고 그렇지 않을 경우 포함하지 않는다.
output 값   | integer type의 value를 가진 list


## number_check 함수 수정하기
두 번째 함수다. 두 번째 함수는 소수 판별을 위한 숫자들의 list를 만들어 주는 함수다. 함수의 내용은 아래와 같다.

내용           | 구성 
--------       | ---
함수명      | number_check
input 변수  | integer type의 value를 가진 list
Process     | 입력 받은 list의 최소값과 최대값을 포함하고 사이에 있는 자연수 중 2이상인 모든 수를 새로운 list로 만들어줌
output 값   | integer type의 value를 가진 list


## is_prime_number 함수 수정하기
마지막 함수다. 이번 함수는 소수 판별을 해주는 함수다. 함수의 내용은 아래와 같다.

내용           | 구성 
--------       | ---
함수명      | is_prime_number
input 변수  | integer type의 value를 가진 list
Process     | 입력 받은 list내의 모든 자연수를 소수인지 아닌지 판별
output 값   | integer type의 value를 가진 list


## main 함수 수정하기
이제 마지막이다. main 함수에서 해야할 것은 각 함수들을 엮어서 우리가 원하는 소수 판별 프로그램을 완성해 주는 것이다. 이를 위해서는 main 함수의 수정이 필요하다. main 함수에 # ===Modify codes below================= 아랫 부분에 다음의 지시사항에 따라 코드를 작성해주기 바란다.
 
1. `input`이라는 built-in 함수를 이용하여 숫자 2개를 입력받는다. 입력값을 `input_number`라는 변수에 저장한다.
2. input_number를 change_type_str_to_int_of_list 함수의 입력값으로 하여 change_type_str_to_int_of_list 함수를 호출하고, 그 결과값을 `number_list` 변수에 저장한다.
3. number_list를 number_check 함수의 입력값으로 하여 number_check를 호출하고, 그 결과값을 `checked_list` 변수에 저장한다.
4. checked_list를 이용하여 소수의 개수와 소수의 리스트를 출력해준다.
5. 만약 소수가 없을 경우 `범위 내에 소수가 없습니다.`를 출력해준다.
6. 만약 입력값이 없거나 범위가 지정되지 않는 경우 `잘못된 값입니다.`를 출력해준다.

어떻게 보면 이 함수가 가장 간단한 함수이다. 위의 3개 함수를 호출하고 오타없이 입력만 해주면된다.


## 테스트 및 제출
두 함수를 모두 작성했다면 실행을 해보자. `bash shell`에서 `python3.4 two_number_beside_prime_number.py` 명령어로 실행을 하면된다. 정확히 작성되었다면 아래와 같이 결과를 볼 수 있을 것이다. 아래 결과 중 둘째 줄과 셋째 줄인 `변환하고 싶은 숫자를 입력해 주세요: ` 와 `몇 진수로 변환할 것 입니까?: `가 출력되고 뒤에 `100`과 `2`는 사용자가 직접 입력하는 것이며, 다섯번째 줄에 `다시 하겠습니까?(Y/N)`가 출력되고 뒤에 `y`  모두 사용자가 직접 입력하는 항목이다.
```bash
소수의 개수 구하기
=========================
숫자의 범위를 지정해주세요. ex) 숫자,숫자 : 1,10
4 개 , [2, 3, 5, 7]
=========================
프로그램이 종료되었습니다.
```


## 숙제 제출하기
모든 함수를 다 수정했다면 아래와 같이 제출하자
```bash
python3.4 submit_assignment.py -submit two_number_beside_prime_number.py
```

제대로 작성했다면 아래와 같은 메세지가 뜰 것이다.

```bash
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
change_type_str_to_int_of_list|       PASS |             Good Job
        number_check |       PASS |             Good Job
     is_prime_number |       PASS |             Good Job
                main |       PASS |             Good Job
    
-------------------- | ---------- | --------------------
```


## Next Work
느끼겠지만, 더 이상의 친절함은 없다. 점점 스스로 혼자 헤쳐나가야 한다. 많은 에러 메세지와 사투를 벌여야 하고, 왠지 모르지만 안되는 이유를 찾아야 한다. 이젠 구글에 익숙해 지길 바란다. 구글 검색이야 말로 최고의 프로그래머가 되는 지름길이다. 마지막 lab 으로 가자!

> **Human knowledge belongs to the world** - from movie 'Password' -


## Footnotes


