Workinglab #4- Sort_english (영어분류기)
=======
Copyright 2016 © document created by TeamLab.Gachon@gmail.com

## Introduction
수많은 난관(=재미). 코딩변태가 되보자. 이 Lab은 사상최초로 어렵다. 이때까지 어려운 Lab은 없었다. 단지 조금 시간이 오래 걸리거나 약간 복잡하게 느껴졌을 뿐이다. 근데 이번엔 어렵다. 정말이다. 하지만 어려운 만큼 가장 여러분에게 도움이 많이 되는 숙제라고 믿는다. 참고로 2016년 지금 만드는 나도 포기하고 싶었다. 
본 Sort_english Lab은 간단한 영어분류(=배열) 프로그램이다. 내가 영어를 입력하면 컴퓨터가 분류한다. 분류하는 기준은 다음과 같다.

- 1) 영어단어가 많은 숫자부터 적은숫자순으로 배열한다. 단 배열할때 영어단어 X 영어단어의 개수 만큼 배열한다. 예를 들면 BABAB가 입력되면 BBBAA가 반환되야 한다. 
- 2) 만약 영어단어들간의 단어개수가 같다면 영어알파벳 우선에 따라 배열한다. 예를 들면 BBAA가 입력되면 A는 B보다 앞에있기(우선권이 있기)때문에 AABB가 반환되야 한다.

어떻게 할지 걱정될 수 도 있지만, 재밌으니까 많은 시간을 투자해보자.

## Sort_english Overview
본 Lab에서는 사용자의 입력에 대한 오류 처리를 실시한다. 여러분들도 가끔 웹 사이트에 접속할 때 잘못된 입력을 바로 잡아주는 프로그램을 본적이 있을 것이다. 하지만 이 프로그램은 잡아주는 것을 뛰어넘어 영어를 제외한 값이 들어오면 무시하고 영어만을 재배치하여 반환하다. (21세기는 자동화세계이다.) 예를 들면, "a123bbc"를 입력하면 123을 잘못된 입력값이라고 생각하고 "BBAC"를 반환해줄것이다. 하지만 아무것도 입력하지않거나 분류할 영어가 없다면 "Wrong input again"라는 문구를 띄어줄 것이다.

- 사용자가 영어와 영어가 아닌 값을 입력했을경우 영어만 분류하여 반환해준다.
- 사용자가 영어가 아닌 값만 입력했을 경우나 아무것도 입력안했을때 "Wrong input again"라는 문구를 띄어준다.

또한 이 프로그램은 무한반복되는 시스템인데 사용자가 그만하고 싶을때는 다음조건을 만족해야 한다.

- '0'을 입력해야 한다.

## 숙제 template 파일 다운로드
먼저 숙제 template 파일을 cs50 서버로 부터 다운로드 받는다. 로그인 후 나타나는 `bash shell`에서 다음과 같은 명령을 입력하자.

```bash
python3.4 submit_assignment.py -get sort_english
```  

입력되면 다운로드 안내 메세지와 함께 `sort_english.py` 파일이 다운로드 된다.

## baseball_game.py 파일 Overview
`vim editor`로 `sort_english.py`을 열어 전체적인 개요를 보자. `vi sort_english.py`명령으로 파일을 열어보면 `main` 함수와 여러개의 함수들이 존재할 것이다. 각 함수들은 여러분께서 직접 작성해서 제출해야 하는 함수이고, `main` 함수는 실제 sort_english을 실행하는 함수이다. 각 함수의 구현 내용은 아래와 같다.

함수           | 설명 
--------       | ---
input_english_value      | 프로그램에서 입력을 받아주는 함수이다. 이때 대소문자의 구분은 두지않는다. (우리프로그램은 결과값을 대문자로 반환해야한다. 뭘 쓸지 알아서 판단하자.) 또한 입력받을때 "영어를 입력해주세요. ex) CCBBAAA : "라는 문구를 띄어주면서 받아야 한다.
dict_of_english      | 영어단어의 개수가 같을 때 우선권을 부여해주려고 만든함수이다. dict형태로 만들어야 하며 A~Z까지 만들어줘야한다.당연히 대문자다.
count_element_method  | 영어단어들의 개수들을 해당하는 영어단어들과 dict형태로 만들어주는 함수이다. 여기서 영어단어가 아닌 문자들은 dict형태로 만들어지면 안된다.(여기서 21세기는 자동화시대를 보여준다.)
max_method | dict에 value중에서 가장 큰 값을 반환해준다.
check_method  | dict에 value중에서 변수로 들어오는 자연수가 몇개있는지 판단하여 1개이면 True, 2개 이상이면 False를 반환한다. 
delete_method   | dict에 value중에서 변수로 들어오는 자연수에 해당하는 dict의 해당하는 key, value를 삭제한다.
equal_method    | check_method의 반환값이 True일때 실행되는 함수인데 가장 큰 값이 1개일때 실행되는 함수이다.
unequal_method    | check_method의 반환값이 False일때 실행되는 함수인데 가장 큰 값이 2개이상일 때 실행되는 함수이다.

상당히 많고 재밌고, 게다가 재미있기까지 하다. 일단 재밌게 해결해보길 바란다.

## main 함수 수정하기 
`main`함수는 매우 쉽다. `main`함수의 기본 template은 아래와 같다.

```python
def main():
    user_input = 999
    print("Hello world")
```
일단 프로그램이 시작되면 "Hello world"라는 한 줄이 화면에 찍히고 시작한다. `main`함수의 개요는 다음과 같다.

- input_english_value함수를 통하여 user_input을받는다.
- user_input을 count_element_method를 통하여 dict형태로 만들어준 다음에 max_method함수를 이용하여 결과값을 반환받고 그 결과값으로 check_method를 실행시켜준다.
- check_method함수의 결과값에 따라 equal_method, unequal_method 함수를 실행해준다. 메인함수 안에서 result값을 통하여 이어준다.
- delete_method 위의 과정을 실행시켜준다음 사용한게 한번더 사용안되게 dict의 key, value값을 삭제시켜준다.
- user_input의 값에따라 결과는 overview부분을 한번 더 보자. 


## 숙제 제출하기
모든 함수를 다 수정했다면, 아래와 같이 제출하자
```bash
 python3.4 submit_assignment.py -submit baseball_game.py
```  
제대로 작성했다면 아래와 같은 메세지가 뜰 것이다.
```python
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
input_english_value  |       PASS |             Good Job
dict_of_english      |       PASS |             Good Job
count_element_method |       PASS |             Good Job
max_method           |       PASS |             Good Job
check_method         |       PASS |             Good Job
delete_method        |       PASS |             Good Job
equal_method  	     |       PASS |             Good Job
unequal_method       |       PASS |             Good Job
main		     |       PASS |             Good Job
-------------------- | ---------- | --------------------
```  
아마도 정말로 감격스러운 순간일 것이다. 고생했다. 

## Next Work
더 재밌는 숙제를 준비하겠다. 

> **Human knowledge belongs to the world** - from movie 'Password' -

## Footnotes

