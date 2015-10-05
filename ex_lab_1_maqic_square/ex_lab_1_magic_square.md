Extreme Lab #1 - 마방진 (Magic Square)
=======
Copyright 2015 © document created by TeamLab.Gachon@gmail.com

## Introduction
처음으로 나오는 Extreme Homework. 이때까지 모든 Lab은 모두가 할 수 있게 설계되었다면 이번 숙제는 정말 열심히 따라온 학생들만 풀수 있는 어려운 Lab이다.
이번 Lab은 마방진 게임이다. 드라마 "뿌리깊은 나무" 에서 어린 세종으로 나왔던 송중기가 시간을 보내기 위해 열심히 풀었던 문제이기도 하다

 ![송중기는 잘 생겼다](https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/ex_lab_1_maqic_square/magic_square.png)

마방진 문제는 의외로 간단하다. 그러나 로직을 for문과 if문으로 표현하는데 익숙하지 않다면 표현하는데 상당한 어려움을 겪게 될 것이다. 

## 숙제 template 파일 다운로드
먼저 숙제 template 파일을 cs50 서버로 부터 다운로드 받는다. 로그인 후 나타나는 bash shell에서 다음과 같은 명령을 입력하자.
```bash
python3.4 submit_assignment.py -get magic_square
```  
정상적으로 다운했다면 현재 디렉토리에 `magic_square.py` 파일 생성되었을 것이다. `ls` 명령어로 확인하자.

## baseball_game.py 파일 Overview
`vim editor`로 `magic_square.py`을 열어 전체적인 개요를 보자. `vi magic_square.py`명령으로 파일을 열어보면 `main` 함수와 여러개의 함수들이 존재할 것이다. 각 함수들은 여러분께서 직접 작성해서 제출해야 하는 함수이고, `main` 함수는 실제 마방진 프로그램을 실행하는 함수이다. 각 함수의 구현 내용은 아래와 같다.

함수           | 설명 
--------       | ---
get_zero_matrix    | 정수형(integer)값을 N을 입력받아, N by N 정사각 행렬 형태인 two dimensional list를 반환함. list내 모든 element의 값은 0으로 초기화되어 있음
is_validate_number | 문자열(string) 값을 입력받아, 값이 정수형 문자열이고 3보다 크고 20보다 작을 경우에는 True 그렇지 않을 경우에는 False를 반환함
is_4even_number    | 정수형(integer)값을 N을 입력받아, N이 4의 배수이면 True 그렇지 않으면 False를 반환함
is_odd_number      | 정수형(integer)값을 N을 입력받아, N이 홀수이면 True 그렇지 않으면 False를 반환함
get_4even_magic_square | 4의 배수인 정수형(integer) 문자열(string)값 N을 입력받아, 마방진으로 구성된 N by N 정사각 행렬을 반환함. 반환되는 정사각행렬은 two dimensional list로 되어있음  
get_odd_magic_square   | 홀수인 정수형(integer) 문자열(string)값 N을 입력받아, 마방진으로 구성된 N by N 정사각 행렬을 반환함. 반환되는 정사각행렬은 two dimensional list로 되어있음  
is_magic_sqaure        | 정사각행렬 형태의 two dimensional list를 입력받아, 입력받은 list가 마방진인지 아닌 확인함

## 마방진 이해하기
마방진은 

- n*n개의 수를 가로, 세로, 대각선 방향의 수를 더하면 모두 같은 값이 나오도록 n × n 행렬에 배열한 것
- 일반적으로 마방진의 각 칸에는 1부터 n*n까지의 수가 한 개씩 들어감. n이 2일 때를 제외하고 항상 존재

간단한 3 by 3 행렬의 마방진은 다음 예제와 같다 ([메모리스트의 상상 노트][1]).

![마방진 예제](https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/ex_lab_1_maqic_square/magic_square_example.png
)


## 수정후 테스트 하기  
제시된 각 함수를 위의 목적에 맞게 수정한 후 테스트를 실시해야 한다. 이번 부터는 특별한 테스트 코드를 제공해주지 않는다. 수강자가 직접 `python shell`이나 `main`함수에 수정 코드를 작성하여 실행해보기 바란다. 단, 테스트 코드예제는 각 함수의 주석(comment) 형태로 달려 있으니, 확인해 보기 바란다.

## 수정전 알아야 하는 것들
막상 해보면 어렵진 않지만, 하기전에는 어려운 것들이 있다. 예를 들면, 파이썬에서 list간의 merge를 위해서는 아래와 같은 코드를 사용할 수 있다.
```python
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']
c = a + b
```
저 방법외에 `a.extend(b)`를 하면 a 변수에 b list가 합쳐진다.
특정한 값이 해당 리스트에 존재하는지 확인하기 위해서는 `if value in list_data` 같은 표현을 쓸 수 있다. `value`라는 값이 `list_data`라는 list type에 들어가있는지 확인하는 구문이다. 당연히 if문 형식이기 때문에 `indentation`을 사용하여 실행 명령을 아래 적어줘야 한다. 아래와 같이 코드를 작성할 수 있다.
```python
result = []
if not(value in list_data):
    result.append(value)
```
위의 코드는 `value`값이 `list_data` list에 들어가 있지 않으면 `result` list에 `value`의 값을 추가하는 명령이다. 중요한 예시이니 꼭 이해하고 넘어가자.
list에서 특정한 값을 지우기 위해서는 `list_data.remove(특정한값)` 을 쓸 수 있다. 혹시나 노파심에 하는 말인데,  저 명령문에서 `list_data`는 list type의 변수명을 의미하면 `특정한값`은 지우고자 하는 값을 얘기한다. 예를 들어 `0`을 지우고 싶으면, 저기 `특정한값`에 `0`을 적어주면 된다.
list에 새로운 값을 추가하는 방법은 `list_data.append(추가하는값)`이다. 물론 문자열일때는 `'추가하는값'`을 붙여야함을 잊지말자
제일 작은 값을 찾는 방법은 `min(list_data)` 이고, 특정한 값이 list에 존재하는 갯수를 찾을 때는 `list_data.count(특정한값)`이다. 지금 설명하는 내용은 `number_of_cases`에 필요한 내용들이므로 숙제를 하기 바란다.

## 숙제 제출하기
모든 함수를 다 수정했다면, 아래와 같이 제출하자
```bash
 python3.4 submit_assignment.py -submit gowithflow.py
```  
제대로 작성했다면 아래와 같은 메세지가 뜰 것이다.
```python
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
 find_smallest_value |       PASS |             Good Job
         sum_of_list |       PASS |             Good Job
comparison_list_size |       PASS |             Good Job
    binary_converter |       PASS |             Good Job
      merge_and_sort |       PASS |             Good Job
      discount_price |       PASS |             Good Job
      odd_even_check |       PASS |             Good Job
     number_of_cases |       PASS |             Good Job
delete_a_list_element |       PASS |             Good Job
-------------------- | ---------- | --------------------
```  
아직도 몇몇 분들은 제출하기 전에 해당 코드를 테스트해보지 않고 제출한다. `unsupported error`가 가끔 나는데, 코드 자체가 분석 불가능할 경우나는 에러로 얼마나 수강자가 숙제에 무심한지 티를 내는 것이다. 반드시 `bash shell`에서 `python3.4 gowithflow.py` 명령으로 실행을 해보고 문제가 없을 경우에만 제출하도록 하자. 물론, 위의 명령을 실행하기 위해서는 자기 나름대로 테스트 코드를 만들어 봐야 한다.

## Next Work
Extreme Lab은 사실 A+를 받기 위한 필수 관문이다. 아무나 쉽게할 수 있는 

> **Human knowledge belongs to the world** - from movie 'Password' -

## Footnotes

[1]: http://memorist.tistory.com/151