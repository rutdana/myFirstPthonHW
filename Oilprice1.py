while True:
    # หน้าจอเเสดงค่าน้ำมัน
    print('#'*80)
    print('#' + ' '*33 + 'MENU' + ' '*41+'#')
    print('#' + ' '*33 + '(1)GASOLINE95  29.16' + ' '*25+'#')
    print('#' + ' '*33 + '(2)GASOLINE91  25.31' + ' '*25+'#')
    print('#' + ' '*33 + '(3)GASOLHOL95  21.2' + ' '*26+'#')
    print('#' + ' '*33 + '(4)GASOLHOL91  21.68' + ' '*25+'#')
    print('#' + ' '*33 + '(5)GASOLHOLe20 21.2' + ' '*26+'#')
    print('#' + ' '*33 + '(6)DIESL       21.1' + ' '*26+'#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' * 80)
    O = input("ต้องการเดิมนเำมันอะไร?")
    print('#'*80)
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' ' * 29 + '(1)money/litre' + ' ' * 35 + '#')
    print('#' + ' ' * 29 + '(2)litre/money' + ' ' * 35 + '#')
    for i in range(17):
        print('#' + ' '*78 + '#')
    print('#'*80)
    M = input()
    # ค่า1.money/litre or 2.litre/money

    print('#'*80)
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*31 + 'ต้องการเติมเท่าไหร่?' + ' ' * 31 + '#')
    for i in range(18):
        print('#' + ' '*78 + '#')
    print('#'*80)
    # ต้องการเติมน้ำมันยี่ห้ออะไร
    P = int(input("ต้องการเติมเท่าไหร่?"))
    # เติมน้ำมันกี่ลิตร
    A = O.upper()
    # เป็นตัวพิมพ์ใหญ่

    print('#'*80)
    print('#' + ' '*78 + '#')
    print('#'*80)
    print('#'+' '*31 + 'เติมกี่ลิตร/ราคาเติมเท่าไหร่' + ' '*26 + '#')
    print('#'*80)
    if "1" in M:
        # เเทนค่า 1.money/litre
        if "1" in A:
            D = (P/29.16)
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "Oil", '%.2f' % D, "ลิตร" + ' ' * 36 + '#')
            print('#'*80)
        elif "2" in A:
            D = (P/25.30)
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "Oil", '%.2f' % D, "ลิตร" + ' ' * 36 + '#')
            print('#'*80)
        elif "3" in A:
            D = (P/21.68)
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "Oil", '%.2f' % D, "ลิตร" + ' ' * 36 + '#')
            print('#'*80)
        elif "4" in A:
            D = (P/20.2)
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "Oil", '%.2f' % D, "ลิตร" + ' ' * 36 + '#')
            print('#'*80)
        elif "5" in A:
            D = (P/21.2)
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "Oil", '%.2f' % D, "ลิตร" + ' ' * 36 + '#')
            print('#'*80)
        elif "6" in A:
            D = (P/21.1)
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "Oil", '%.2f' % D, "ลิตร" + ' ' * 36 + '#')
            print('#'*80)
        else:
	# ราคาน้ำมันทั้งหมด
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "กรุณาเลือกจำนวนเงินใหม่" + ' ' * 36 + '#')
            print('#'*80)
	# เลือกจำนวนเงินที่จะเติม
    elif "2" in M:
	# เเทนค่า 2.litre/money
        if "1" in A:
            D = (P*29.16)
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "price", D, "฿" + ' ' * 34 + '#')
            print('#'*80)
        elif "2" in A:
            D = (P*25.30)
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "price", D, "฿" + ' ' * 34 + '#')
            print('#'*80)
        elif "3" in A:
            D = (P*21.68)
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "price", D, "฿" + ' ' * 34 + '#')
            print('#'*80)
        elif "4" in A:
            D = (P*20.2)
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "price", D, "฿" + ' ' * 34 + '#')
            print('#'*80)
        elif "5" in A:
            D = (P*21.2)
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "price", D, "฿" + ' ' * 34 + '#')
            print('#'*80)
        elif "6" in A:
            D = (P*21.1)
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "price", D, "฿" + ' ' * 34 + '#')
            print('#'*80)
        else:
	
	# ราคาน้ำมันทั้งหมด
            print('#'*99)
            print('#' + ' ' * 29 + "กรุณาเลือกน้ำมันชนิดใหม่" + ' ' * 36 + '#')
            print('#'*99)

	# เลือกน้ำมันชนิดใหม่
    else:
        print("กรุณาเเจ้งพนักงาน")
	# กรุณนาเเจ้งพนักงาน
    print("5 - exit,  0 - back the menu. ")
    f = "5"
	# กด 5 จะออก
    s = "0"
	# กด 0 จะกลับไปที่เมนู

    e = input()
    while not(e in '50'):
        print("5 - exit,  0 - back the menu ")
        e = input()
    if(e != s):
        break
