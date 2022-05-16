password = 'a123456'
typing_num = 0


while True:
    typing_num = typing_num + 1
    if typing_num > 3:
        print ("錯誤超過三次，自動關閉程式")
        break

    typing_pwd = input("請輸入密碼: ")
    
    if typing_pwd != password:
        if (3 - typing_num) > 0:
            print ("密碼錯誤! 還有",str(3 - typing_num),"次機會")
    
    else:
        print ("登入成功")
        break
    

