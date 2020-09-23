from suds.client import Client
import xmltodict, json

oil_price = {"Gasoline 95": 29.16,"Gasoline 91": 25.31,"Gasohol 95":21.2,"Gasohol 91":21.68,"Gasohol E20":21.2,"Diesel":21.1}
"""client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')
OilPrice = client.service.CurrentOilPrice(Language='thai')

OilPrice1 = xmltodict.parse(OilPrice) # ได้ผลลัพธ์เป็น json ในสตริง
Price = eval(json.dumps(OilPrice1)) # เรียกใช้งาน json ในสตริง


for i in Price["PTTOR_DS"]["FUEL"]:
    if("PRICE" in i):
        oil_price[i["PRODUCT"]] = float(i["PRICE"])"""

while True:
    # หน้าจอเเสดงค่าน้ำมัน
    print('#'*80)
    print('#' + ' '*33 + 'MENU' + ' '*41+'#')
    print('#' + ' '*33 + '(1)GASOLINE95  ' +
          '%.2f' %(oil_price["Gasoline 95"]) + ' '*25+'#')
    print('#' + ' '*33 + '(2)GASOLINE91  ' +
          '%.2f' %(oil_price["Gasoline 91"]) + ' '*25+'#')
    print('#' + ' '*33 + '(3)GASOLHOL95  ' +
          '%.2f' %(oil_price["Gasohol 95"]) + ' '*25+'#')
    print('#' + ' '*33 + '(4)GASOLHOL91  ' +
          '%.2f' %(oil_price["Gasohol 91"]) + ' '*25+'#')
    print('#' + ' '*33 + '(5)GASOLHOLe20 ' +
          '%.2f' %(oil_price["Gasohol E20"]) +' '*25+'#')
    print('#' + ' '*33 + '(6)DIESL       ' +
          '%.2f' %(oil_price["Diesel"]) +' '*25+'#')
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
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    if "1" in M:
        # เเทนค่า 1.money/litre
        if "1" in A:
            D = (P/oil_price["Gasoline 95"])
            print('')
            print('#' + ' ' * 29 + "Oil", '%.2f' % D, "ลิตร" + ' ' * 36 + '#')
            print('#'*80)
        elif "2" in A:
            D = (P/oil_price["Gasoline 91"])
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "Oil", '%.2f' % D, "ลิตร" + ' ' * 36 + '#')
            print('#'*80)
        elif "3" in A:
            D = (P/oil_price["Gasohol 95"])
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "Oil", '%.2f' % D, "ลิตร" + ' ' * 36 + '#')
            print('#'*80)
        elif "4" in A:
            D = (P/oil_price["Gasohol 91"])
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "Oil", '%.2f' % D, "ลิตร" + ' ' * 36 + '#')
            print('#'*80)
        elif "5" in A:
            D = (P/oil_price["Gasohol E20"])
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "Oil", '%.2f' % D, "ลิตร" + ' ' * 36 + '#')
            print('#'*80)
        elif "6" in A:
            D = (P/oil_price["Diesel"])
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
            D = (P*oil_price["Gasoline 95"])
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "price", D, "฿" + ' ' * 34 + '#')
            print('#'*80)
        elif "2" in A:
            D = (P*oil_price["Gasoline 91"])
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "price", D, "฿" + ' ' * 34 + '#')
            print('#'*80)
        elif "3" in A:
            D = (P*oil_price["Gasohol 95"])
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "price", D, "฿" + ' ' * 34 + '#')
            print('#'*80)
        elif "4" in A:
            D = (P*oil_price["Gasohol 91"])
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "price", D, "฿" + ' ' * 34 + '#')
            print('#'*80)
        elif "5" in A:
            D = (P*oil_price["Gasohol E20"])
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "price", D, "฿" + ' ' * 34 + '#')
            print('#'*80)
        elif "6" in A:
            D = (P*oil_price["Diesel"])
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
    print('#'*80)
    print('#' + ' '*78 + '#')
    print('#'*80)
    print('#'*80)
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#') 
    input()
    # กรุณนาเเจ้งพนักงาน
    print("5 - exit,  0 - back the menu. ")
    f = "5"
        # กด 5 จะออก
    s = "0"
        # กด 0 จะกลับไปที่เมนู

    e = input()
    if(e == f):
        break
            print('#'*80)
            print('#' + ' ' * 29 + "Oil", '%.2f' % D, "ลิตร" + ' ' * 36 + '#')
            print('#'*80)
        elif "3" in A:
            D = (P/oil_price["Gasohol 95"])
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "Oil", '%.2f' % D, "ลิตร" + ' ' * 36 + '#')
            print('#'*80)
        elif "4" in A:
            D = (P/oil_price["Gasohol 91"])
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "Oil", '%.2f' % D, "ลิตร" + ' ' * 36 + '#')
            print('#'*80)
        elif "5" in A:
            D = (P/oil_price["Gasohol E20"])
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "Oil", '%.2f' % D, "ลิตร" + ' ' * 36 + '#')
            print('#'*80)
        elif "6" in A:
            D = (P/oil_price["Diesel"])
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
            D = (P*oil_price["Gasoline 95"])
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "price", D, "฿" + ' ' * 34 + '#')
            print('#'*80)
        elif "2" in A:
            D = (P*oil_price["Gasoline 91"])
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "price", D, "฿" + ' ' * 34 + '#')
            print('#'*80)
        elif "3" in A:
            D = (P*oil_price["Gasohol 95"])
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "price", D, "฿" + ' ' * 34 + '#')
            print('#'*80)
        elif "4" in A:
            D = (P*oil_price["Gasohol 91"])
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "price", D, "฿" + ' ' * 34 + '#')
            print('#'*80)
        elif "5" in A:
            D = (P*oil_price["Gasohol E20"])
            print('')
            print('#'*80)
            print('#' + ' ' * 29 + "price", D, "฿" + ' ' * 34 + '#')
            print('#'*80)
        elif "6" in A:
            D = (P*oil_price["Diesel"])
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
    print('#'*80)
    print('#' + ' '*78 + '#')
    print('#'*80)
    print('#'*80)
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#')
    print('#' + ' '*78 + '#') 
    input()
    # กรุณนาเเจ้งพนักงาน
    print("5 - exit,  0 - back the menu. ")
    f = "5"
        # กด 5 จะออก
    s = "0"
        # กด 0 จะกลับไปที่เมนู

    e = input()
    if(e == f):
        break
