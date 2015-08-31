#-*- coding: utf-8 -*-

text = "Gachon\nUniversity\nIndustrial\nEngineering\n"

# 1번째 줄 삭제
def delete_line(text):

    # Input:
    #   - 명령어
    # Output:
    #   - 명령어를 입력했을 때의 결과값(지정 행 삭제)
    # Examples:
    #   >>> delete_line(command)
    #   Gachon
    #   University
    #   Industrial
    #   >>> delete_line(command)
    #   University
    #   Industrial
    #   Engineering

    delete_text = text
    # ===Modify codes below=============

    command = ""
    result = ""

    # ==================================

    return command, result

# 2행으로 커서 이동, 단어 삭제
def delete_word(text):

    # Input:
    #   - move_command : 지정 행으로 이동하는 명령어
    #   - delete_command : 단어 지우는 명령어
    # Output:
    #   - 명령어를 입력했을 때의 결과값(해당 행으로 가서 첫번째 단어 지우기)
    # Examples:
    #   >>> delete word(text)
    #   University
    #   Industrial
    #   Engineering

    delete_text = text
    # ===Modify codes below=============

    move_command = ""
    delete_command = ""
    result = ""

    # ==================================

    return move_command, delete_command, result

# 1행~2행 복사, 마지막 행에 붙여넣기
def copy_and_paste_1(text):

    # Input:
    #   -copy_command : 복사 명령어
    #   -paste_command : 붙여넣기 명령어
    # Output:
    #   - 명령어를 입력했을 때의 결과값(지정 행 복사, 붙여넣기)
    # Examples:
    #   >>> copy_and_paste_1(text)
    #   Gachon
    #   University
    #   Industrial
    #   Engineering
    #   Gachon
    #   University

    copy_text = text
    # ===Modify codes below=============

    copy_command = ""
    paste_command = ""
    result = ""
    # ==================================

    return copy_command, paste_command, result

# 1행 복사 후 5행에 붙여넣기(동시 진행)
def copy_and_paste_2(text):

    # Input:
    #   - command : 복사, 붙여넣기 동시 명령어
    # Output:
    #   - 명령어를 입력했을 때의 결과값(지정 행 복사, 붙여넣기)
    # Examples:
    #   >>> copy_and_paste(text, command) #:2co5
    #   Gachon
    #   University
    #   Industrial
    #   Engineering
    #   University

    copy_text = text

    # ===Modify codes below=============

    command = ""
    result = ""

    # ==================================

    return result

#gachon인 단어를 찾아(대문자 소문자 구분 없음) University로 모두 수정하기
def modify_word():
    modify_text = "Gachon gAchon gaChon gacHon gachOn gachoN"

    # Input:
    #   - command: 문자열 검색 및 수정 명령어
    # Output:
    #   - 명령어 입력했을 때의 결과값(문자열 탐색 및 수정)
    # Examples: gachon 을 new로 수정할 경우
    #   >>> modify_word()
    #   new new new new new new

    # ===Modify codes below=============

    command = ""
    result = ""

    # ==================================

    return command, result


if __name__ == "__main__":

    print ("Delete Line Test")
    print (delete_line(text))
    print (delete_line(text)==(":4d", "University\nIndustrial\nEngineering\n"))
    print ("Delete Line Test Closed \n")

    print ("Delete Word Test")
    print (delete_word(text))
    print (delete_word(text)==(":2", ":dw", "Gachon\nIndustrial\nEngineering\n"))
    print ("Delete Word Test Closed \n")

    print ("Copy and Paste First Test")
    print (copy_and_paste_1(text))
    print (copy_and_paste_2(text)==(":1,4y", "Gachon\nUniversity\nIndustrial\nEngineering\nGachon\nUniversity\nIndustrial\nEngineering\n"))
    print ("Copy and Paste First Closed \n")

    print ("Copy and Paste Second Test")
    print (copy_and_paste_2(text))
    print (copy_and_paste_2(text)==(":1co5", "Gachon\nUniversity\nIndustrial\nEngineering\nGachon"))
    print ("Copy and Paste Second Test Closed \n")

    print ("Find and Modify Word Test")
    print (modify_word())
    print (modify_word()==("%s/gachon/University/gi", "University\nUniversity\nUniversity\nUniversity\nUniversity\nUniversity"))
    print ("Find and Modify Word Test Closed \n")


