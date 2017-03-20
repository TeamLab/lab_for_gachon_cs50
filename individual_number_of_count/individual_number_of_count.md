Lab # - n이상 m이하에서 각 숫자 개수 구하기 (Individual_number_of_count)
===================================================
Copyright 2016 © document created by TeamLab.Gachon@gmail.com

## Introduction
이번 과제는 조금 짧다. 그러나 간단하지 않다. 처음으로 수강자가 직접 함수를 작성한다. 나중에 보면 매우 쉬운 함수 이지만 지금은 어렵게 느껴질 것이다. 이미 포기할 순 없다. 해보자.


## 숙제 template 파일 다운로드
먼저 숙제 template 파일을 cs50 서버로 부터 다운로드 받는다. 로그인 후 나타나는 bash shell에서 다음과 같은 명령을 입력하자.
```bash
python3.4 submit_assignment.py -get individual_number_of_count
```  
`individual_number_of_count.py` 파일이 다운로드 될 것이다. 받자 마자 실험 차원에서 코드를 실행해보자. `python3.4 individual_number_of_count.py`를 입력하면 된다. 이제 다들 코드를 어떻게 실행하는 지는 알 것이다.  실행하면 아마 아래와 같은 에러 메세지가 뜰 것이다. 


## individual_number_of_count.py 파일 Overview

`vim editor`로 `individual_number_of_count.py`을 열어 전체적인 개요를 보자. `vi individual_number_of_count.py`명령으로 파일을 열어보면 main 함수와 여러개의 함수들이 존재할 것이다. 각 함수들은 여러분께서 직접 작성해서 제출해야 하는 함수이고, main 함수는 실제 individual_number_of_count를 실행하는 함수이다. 각 함수의 구현 내용은 아래와 같다
 수강생이 할일은 크게 두 가지다. 하나는 프로그램 수행을 위해 4개의 함수를 작성하는 것이고, 두 번째는 main 함수에 작성된 4개의 함수를 사용해서 각 숫자의 갯수를 구해 보는 것이다. 현재 코드는 헐렁하지만 여러분들이 빈 공간을 채우면 된다.
 
 

## think_positive_number 함수 수정하기
첫번째 함수는 console창에서 입력받은 값을 유효여부를 판단하는 함수이다. 이미 비숫한 함수를 change_decimal_to_n에서 작성해보았기 때문에 어렵지 않을 수도 있다. 아래 내용을 참고하여 think_positive_number 함수를 작성하자.

내용           | 구성 
--------       | ---
함수명      | think_positive_number
input 변수  | list
Process     | 입력 받은 list의 구성요소 모두가 0이상의 정수인지를 판별함
output 값   | True, False


## make_range_list 함수 수정하기
두 번째 함수다. 두 번째 함수는 입력 범위 사이에 있는 값들을 리스트로 만들어주는 함수다. 함수의 내용은 아래와 같다.

내용           | 구성 
--------       | ---
함수명      | make_range_list
input 변수  | list
Process     | 입력 받은 범위에 있는 모든 값들을 list로 만들어줌
output 값   | list


## make_number_list 함수 수정하기
마지막 함수다. 이번 함수는 자릿수들의 리스트를 만들어주는 함수다. 함수의 내용은 아래와 같다.

내용           | 구성 
--------       | ---
함수명      | make_number_list
input 변수  | list
Process     | 범위내 숫자들의 모든 자릿수의 값들을 중복없이 리스트로 반환
output 값   | list

## my_count 함수 수정하기
마지막 함수다. 이번 함수는 자릿수들의 갯수를 세어주는 리스트를 만들어주는 함수다. 함수의 내용은 아래와 같다.

내용           | 구성 
--------       | ---
함수명      | my_count
input 변수  | list
Process     | 범위내 숫자들의 모든 자릿수의 값들의 갯수를 세어 리스트로 반환
output 값   | list


## main 함수 수정하기
이제 마지막이다. main함수에서 해야할 것은 각 함수들을 엮어서 우리가 원하는 소수 판별 프로그램을 완성해 주는 것이다. 이를 위해서는 main 함수의 수정이 필요하다. main함수에 # ===Modify codes below================= 아랫 부분에 다음의 지시사항에 따라 코드를 작성해주기 바란다.
 
1. `input`이라는 built-in 함수를 이용하여 '숫자의 범위를 지정해주세요 ex)2,7 :' 문자열이 나오고 그 후 숫자 2개를 입력받는다.
2. 사용자로부터 입력받은 값이 유효하면 결과값을 출력 
3. 사용자의 입력값이 유효하지 않다면 '다시 입력해주세요.'를 출력해준다.
4. 프로그램 종료를 위해서는 `FINISH`를 입력해야 한다.

어떻게 보면 이 함수가 가장 간단한 함수이다. 위의 3개 함수를 호출하고 오타없이 입력만 해주면된다.


## 테스트 및 제출
두 함수를 모두 작성했다면 실행을 해보자. `bash shell`에서 `python3.4 individual_number_of_count.py` 명령어로 실행을 하면된다. 정확히 작성되었다면 아래와 같이 결과를 볼 수 있을 것이다.
```bash
각 숫자의 개수 구하기
==========================
숫자의 범위를 지정해주세요 ex)2,7 : 10,20
0 2
1 11
2 2
3 1
4 1
5 1
6 1
7 1
8 1
9 1
숫자의 범위를 지정해주세요 ex)2,7 : finish
==========================
프로그램이 종료 되었습니다.
```


## 숙제 제출하기
모든 함수를 다 수정했다면 아래와 같이 제출하자
```bash
python3.4 submit_assignment.py -submit individual_number_of_count.py
```

제대로 작성했다면 아래와 같은 메세지가 뜰 것이다.

```bash
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
think_positive_number|       PASS |             Good Job
     make_range_list |       PASS |             Good Job
    make_number_list |       PASS |             Good Job
            my_count |       PASS |             Good Job
                main |       PASS |             Good Job
-------------------- | ---------- | --------------------
```


## Next Work
느끼겠지만, 더 이상의 친절함은 없다. 점점 스스로 혼자 헤쳐나가야 한다. 많은 에러 메세지와 사투를 벌여야 하고, 왠지 모르지만 안되는 이유를 찾아야 한다. 이젠 구글에 익숙해 지길 바란다. 구글 검색이야 말로 최고의 프로그래머가 되는 지름길이다. 마지막 lab 으로 가자!

> **Human knowledge belongs to the world** - from movie 'Password' -


## Footnotes
