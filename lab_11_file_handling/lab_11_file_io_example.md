Lab #11 - File IO Example (file_io_example)
=======
Copyright 2015 © document created by TeamLab.Gachon@gmail.com

## Introduction
이번 Lab은 쉽다. 다행이다. 쉽다. 즐겁지 않은가? 쉽다.
이번 Lab은 Text Handling 시리즈의 첫 번째 Lab이다. 이번 Lab의 목표는 간단한 파일을 다운로드 받고, 파일안에 있는 정보를 추출하는 것 이다. 다행이다. 진짜 쉽다. 함수도 5개 밖에 없다. 바로 본론으로 들어가자.

## 숙제 template 파일 다운로드
먼저 숙제 template 파일을 cs50 서버로 부터 다운로드 받는다. 로그인 후 나타나는 `bash shell`에서 다음과 같은 명령을 입력하자. 이것부터 쉽게 느껴지지 않는가?

```bash
python3.4 submit_assignment.py -get file_io_example
```  

입력되면 다운로드 안내 메세지와 함께 `file_io_example.py` 파일이 다운로드 된다.

다음으로 이번 Lab에서 사용할 예제 파일을 다운로드 하자. 아래와 같이 bash shell에서 입력하면 된다.

```bash
wget https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/lab_11_file_handling/1984.txt
```  



## file_io_example.py 파일 Overview
`vim editor`로 `file_io_example.py`을 열어 전체적인 개요를 보자. 이번 Lab은 오직 5개의 함수로만 구성되어 있으며, Main 함수는 존재하지 않는다.

이제 수정해야 할 함수 리스트를 보자

함수           | 설명 
--------       | ---
get_file_contents | 문자열값으로 filename을 입력받아 해당 파일에 존재하는 모든 text 데이터를 문자열 형태로 반환함 
get_number_of_characters_with_blank | 문자열값으로 filename을 입력받아 해당 파일에 존재하는 모든 글자의 갯수를 integer 값으로 반환함 
get_number_of_characters_without_blank | 문자열값으로 filename을 입력받아 해당 파일에 존재하는 모든 글자의 갯수를 공백을 제외하고 integer 값으로 반환함. 단 여기서 공백은 " ", "\t", "\n" 을 의미함
get_number_of_lines | 문자열값으로 filename을 입력받아 해당 파일에 존재하는 모든 줄(line)수를  integer 값으로 반환함. 이때 마지막 줄은 count에서 제외함
get_number_of_target_words | 문자열값으로 filename과 찾고자하는 target_words을 입력받아 해당 파일에 존재하는 target_words와 같은 글자의 수를 대소문자와 상관없이 integer 값으로 반환함 


## 결과확인
너무 쉽다. 아마도 결과는 아래와 같이 나올 것이다.

```python
def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============



    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")
```
`main` 함수는 다음과 같은 규칙을 가진다.

1. 사용자가 0을 입력하면 종료된다.
2. 사용자가 대소문자에 상관없이 "h"또는 "help"를 입력하면 `get_help_message` 함수를 호출하여 아래와 같이 출력된다. 
```python
Input your message(H - Help, 0 - Exit): H
HELP - International Morse Code List
A: .-   B: -... C: -.-. D: -..  E: .
F: ..-. G: --.  H: .... I: ..   J: .---
K: -.-  L: .-.. M: --   N: -.   O: ---
P: .--. Q: --.- R: .-.  S: ...  T: -
U: ..-  V: ...- W: .--  X: -..- Y: -.--
Z: --..
```
3. 모스부호로 변환이 가능한 알파벳 문장이 입력되면 모스부호로 변환된 값이 출력된다.
```python
Input your message(H - Help, 0 - Exit): SOS
... --- ...
Input your message(H - Help, 0 - Exit): Hello!
.... . .-.. .-.. ---
Input your message(H - Help, 0 - Exit): This is Gachon
- .... .. ...  .. ...  --. .- -.-. .... --- -.
```
4. 알파벳으로 변환이 가능한 모스부호가 입력되면 알파벳으로 변환해준다.
```python
Input your message(H - Help, 0 - Exit): ... --- ...
SOS
Input your message(H - Help, 0 - Exit): ... . ...
SES
Input your message(H - Help, 0 - Exit): . -..- ---
EXO
Input your message(H - Help, 0 - Exit): .... --- -
HOT
Input your message(H - Help, 0 - Exit): . -..- .. -..
EXID
```
5. 그외 변환이 불가능한 입력일 경우 에러 메세지를 출력한다.
```python
Input your message(H - Help, 0 - Exit): I'm Gachon.
Wrong Input
Input your message(H - Help, 0 - Exit): This is "CS50".
Wrong Input
Input your message(H - Help, 0 - Exit): Hello 123!
Wrong Input
```

실제 실행된 프로그램의 예제화면은 아래와 같다.

![프로그램 실행 예시](https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/lab_10_morsecode/implementation_example.png)


## 숙제 제출하기
모든 함수를 다 수정했다면, 아래와 같이 제출하자
```bash
 python3.4 submit_assignment.py -submit morsecode.py
```  
제대로 작성했다면 아래와 같은 메세지가 뜰 것이다.
```python
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
is_validated_morse_code |       PASS |             Good Job
  encoding_character |       PASS |             Good Job
     is_help_command |       PASS |             Good Job
   decoding_sentence |       PASS |             Good Job
  decoding_character |       PASS |             Good Job
is_validated_english_sentence |       PASS |             Good Job
get_cleaned_english_sentence |       PASS |             Good Job
                main |       PASS |             Good Job
   encoding_sentence |       PASS |             Good Job
-------------------- | ---------- | --------------------
```  

## Next Work
꽤 많은 프로그램을 짜다보면 이 정도 Lab은 그다지 어렵지 않게 느껴질 수도 있다. 점점 Lab의 수준이 낮아지므로 이제 조금 긴장을 풀고 한개씩 해결해 나가는 것을 추천한다. 다음 시간에는 File Handling에 대한 Lab을 수행하게 된다. 앞으로는 훨씬 더 다양한 문제를 해결할 수 있을 것 이다.

> **Human knowledge belongs to the world** - from movie 'Password' -

## Footnotes

<b id="f1">1</b>: [Morse Code Wiki][1] 페이지로 이동하면 화단에 Morse Code를 들을 수 있다. [↩](#MorseCodeWiki)

[1]: https://en.wikipedia.org/wiki/Morse_code 