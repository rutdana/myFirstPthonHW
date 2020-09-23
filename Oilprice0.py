while True : 
    print('################################################################################')
    print('#                               MENU                                           #')
    print('#                       (1)GASOLINE95  29.16                                   #')
    print('#                       (2)GASOLINE91  25.31                                   #')
    print('#                       (3)GASOLHOL95  21.2                                    #')
    print('#                       (4)GASOLHOL91  21.68                                   #')
    print('#                       (5)GASOLHOLe20 21.2                                    #')
    print('#                       (6)DIESL       21.1                                    #')
    print('#                                                                              #')  
    print('#                                                                              #') 
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')    
    print('#                                                                              #')
    print('#                                                                              #')  
    print('#                                                                              #') 
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')    
    print('#                                                                              #')
    print('#                                                                              #')
    print('#                                                                              #')
    print('################################################################################')
    print("input 1.money/litre or 2.litre/money")
    M = input()
    O = input("ต้องการเดิมนเำมันอะไร?")
    P = int(input("ต้องการเติมเท่าไหร่?"))
    A = O.upper()
    D = 0 
    if "1" in M:
        if "1" in A:
            D = D +(P/29.16)
            print("Oil",'%.2f' %D , "ลิตร")
        elif "2" in A:
            D = D +(P/25.30)
            print("Oil",'%.2f' %D , "ลิตร")
        elif "3" in A:
            D = D +(P/21.68)
            print("Oil",'%.2f' %D , "ลิตร")
        elif "4" in A:
            D = D +(P/20.2)
            print("Oil",'%.2f' %D , "ลิตร")
        elif "5" in A:
            D = D +(P/21.2)
            print("Oil",'%.2f' %D , "ลิตร")
        elif "6" in A:
            D = D +(P/21.1)
            print("Oil",'%.2f' %D , "ลิตร")     
        else:
            print("กรุณาเลือกจำนวนเงินใหม่")
    elif "2" in M:
        if "1" in A:
            D = D +(P*29.16)
            print("price",D,"฿")
        elif "2" in A:
            D = D +(P*25.30)
            print("price",D,"฿")  
        elif "3" in A:
            D = D +(P*21.68)
            print("price",D,"฿")     
        elif "4" in A:
            D = D +(P*20.2)
            print("price",D,"฿")     
        elif "5" in A:
            D = D +(P*21.2)
            print("price",D,"฿")     
        elif "6" in A:
            D = D +(P*21.1)
            print("price",D,"฿")
        else :
             print("กรุณาเลือกน้ำมันชนิดใหม่")
    else :
        print("กรุณาเเจ้งพนักงาน")
    print("5 - exit,  0 - back the menu. ")
    f="5"
    s="0" 
    e=input()
    while not(e in '50'):
            print("5 - exit,  0 - back the menu ")
            e = input()
    if(e !=s):
       break
