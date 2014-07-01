from requests import *

def brute():
    for k in range(2, 3):
        for a in range(65, 75):
            for i in range(1,11):
                re = post("https://student.people.co/api/challenge/battleship/bcc533d5cc24/boards/live_board_" + str(k) + "/" + chr(a) + str(i))
                   

def a():
    print "thinking..."
    searchList = [("carrier", 5), ("submarine", 3)]
    for a in range(65, 75):
        for i in range(1,11):
            re = post("https://student.people.co/api/challenge/battleship/bcc533d5cc24/boards/test_board_1/" + chr(a) + str(i))
            if re.json()["is_hit"]:
                for item in searchList:
                    if not ((item[1] + i > 10) or (i - item[1]) < 0)):
                        re = post("https://student.people.co/api/challenge/battleship/bcc533d5cc24/boards/test_board_1/" + chr(a) + str(i+1))
                        if(re.json()["is_hit"]):
                            for index in range(2, item[1] + 1):
                                re = post("https://student.people.co/api/challenge/battleship/bcc533d5cc24/boards/test_board_1/" + chr(a) + str(i+index)                                       
                    else if not ((item[1] + a > 10) or (a - item[1]) < 0)):
                            re = post("https://student.people.co/api/challenge/battleship/bcc533d5cc24/boards/test_board_1/" + chr(a+1) + str(i))       
                            if(re.json()["is_hit"]):
                                for index in range(2, item[1] + 1):
                                    re = post("https://student.people.co/api/challenge/battleship/bcc533d5cc24/boards/test_board_1/" + chr(a+1) + str(i)
