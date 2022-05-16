password = 'a123456'
typing_num = 3 #剩餘機會


while typing_num > 0:
    typing_num = typing_num - 1
    typing_pwd = input("請輸入密碼: ")

    if typing_pwd == password:
        print ("登入成功")
        break

    else:
        print ("密碼錯誤!")
        if typing_num > 0:
            print ("還剩下", typing_num, "次機會")

    

