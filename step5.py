from re import X
import psycopg2

from tabulate import tabulate

headb = ["Build Number", "Name", "Number of items in the Build", "Price"]
headc = ["Build number its from", "Item Number", "Brand", "price", "name","Number of cores"]
headg = ["Build number its from", "Item Number", "Brand", "price", "name", "overclock speed", "Number of Ports"]
headr = ["Build number its from", "Item Number", "Brand", "price", "name", "type of ram", "GB's per stick"]
heads = ["Build number its from", "Item Number", "Brand", "price", "name", "Total amount of storage in GB's"]
headm = ["Build number its from", "Item Number", "Brand", "price", "name", "Number of Ports", "Size"]
cartt = ["name", "Price"]

conn = psycopg2.connect(database="postgres", user="chad0201", host="localhost", port="5432")
cursor = conn.cursor()


print("Welcome to the computer shop.")
print("What would you like to look for today?")
print("Press 1 for pre builds, 2 for cpu's, 3 for GPU's, 4 for Ram, 5 for storage, 6 for motherboards")
d1 = input()
while d1 != 0:
    if d1 == '1':
        print("We have 5 different pre builds available.")
        cursor.execute('select * from Builds;')
        allb= cursor.fetchall()
        print(tabulate(allb, headb))
        print("Would you like to add anything to your cart? if so type the item number that is associated with it if not press 0")
        d2 = input()
        if d2 == '1' or '2' or '3' or '4' or '5':
            s1= 'select buildnum, name, price from Builds where Builds.buildnum = ' + d2
            cursor.execute(s1)
            itemb= cursor.fetchall()
            print(tabulate(itemb, cartt))
            print("Would you like to see the review for that item?")
            s3= input()
            if s3 == 'Yes':
                s4= 'select review from reviews where reviews.buildnum = ' +d2
                cursor.execute(s4)
                rev= cursor.fetchall()
                print(rev)
            if s3 == 'no':
                print("Do you want to add this item to your cart?")
                s3= input()
                if s3== 'Yes':
                    s2= 'insert into cart(name, price) select name, price from Builds where Builds.buildnum = ' + d2
                    cursor.execute(s2)
                if s3 == 'no':
                    continue
        if d2 =='0':    
            print("Are you ready to check out? Press 0 is yes")
            d1= input()
    if d1 == '2':
        print('You have selected CPU')
        cursor.execute('select * from CPU;')
        allc= cursor.fetchall()
        print(tabulate(allc, headc))
        print("Would you like to add anything to your cart? if so type the item number that is associated with it if not press 0")
        d2 = input()
        if d2 == '6' or '7' or '8' or '9' or '10':
            s1= 'select itemnum, name, price from CPU where CPU.itemnum = ' + d2
            cursor.execute(s1)
            itemb= cursor.fetchall()
            print(tabulate(itemb, cartt))
            print("Would you like to see the review for that item?")
            s3= input()
            if s3 == 'Yes':
                s4= 'select review from reviews where reviews.itemnum = ' +d2
                cursor.execute(s4)
                rev= cursor.fetchall()
                print(rev)
            if s3 == 'no':
                print("Do you want to add this item to your cart?")
                s3= input()
                if s3== 'Yes':
                    s2= 'insert into cart(name, price) select name, price from CPU where CPU.itemnum = ' + d2
                    cursor.execute(s2)
                if s3 == 'no':
                    continue
        if d2 =='0':    
            print("Are you ready to check out? Press 0 is yes")
            d1= input()
    if d1 == '3':
        print('You have selected GPU')
        cursor.execute('select * from GPU;')
        allg=cursor.fetchall()
        print(tabulate(allg, headg))
        print("Would you like to add anything to your cart? if so type the item number that is associated with it if not press 0")
        d2 = input()
        if d2 == '11' or '12' or '13' or '14' or '15':
            s1= 'select itemnum, name, price from GPU where GPU.itemnum = ' + d2
            cursor.execute(s1)
            itemb= cursor.fetchall()
            print(tabulate(itemb, cartt))
            print("Would you like to see the review for that item?")
            s3= input()
            if s3 == 'Yes':
                s4= 'select review from reviews where reviews.itemnum = ' +d2
                cursor.execute(s4)
                rev= cursor.fetchall()
                print(rev)
            if s3 == 'no':
                print("Do you want to add this item to your cart?")
                s3= input()
                if s3== 'Yes':
                    s2= 'insert into cart(name, price) select name, price from GPU where GPU.itemnum = ' + d2
                    cursor.execute(s2)
                if s3 == 'no':
                    continue
        if d2 =='0':    
            print("Are you ready to check out? Press 0 is yes. if not ")
            d1= input()
    if d1 == '4':
        print('You have selected RAM')
        cursor.execute('select * from RAM;')
        allr=cursor.fetchall()
        print(tabulate(allr, headr))
        print("Would you like to add anything to your cart? if so type the item number that is associated with it if not press 0")
        d2 = input()
        if d2 == '16' or '17' or '18' or '19' or '20':
            s1= 'select itemnum, name, price from RAM where RAM.itemnum = ' + d2
            cursor.execute(s1)
            itemb= cursor.fetchall()
            print(tabulate(itemb, cartt))
            print("Would you like to see the review for that item?")
            s3= input()
            if s3 == 'Yes':
                s4= 'select review from reviews where reviews.itemnum = ' +d2
                cursor.execute(s4)
                rev= cursor.fetchall()
                print(rev)
            if s3 == 'no':
                print("Do you want to add this item to your cart?")
                s3= input()
                if s3== 'Yes':
                    s2= 'insert into cart(name, price) select name, price from RAM where RAM.itemnum = ' + d2
                    cursor.execute(s2)
                if s3 == 'no':
                    continue
        if d2 =='0':    
            print("Are you ready to check out? Press 0 is yes")
            d1= input()
    if d1 == '5':
        print('You have select Storage')
        cursor.execute('select * from Storage;')
        alls= cursor.fetchall()
        print(tabulate(alls, heads))
        print("Would you like to add anything to your cart? if so type the item number that is associated with it if not press 0")
        d2 = input()
        if d2 == '21' or '22' or '23' or '24' or '25':
            s1= 'select itemnum, name, price from Storage where Storage.itemnum = ' + d2
            cursor.execute(s1)
            itemb= cursor.fetchall()
            print(tabulate(itemb, cartt))
            print("Would you like to see the review for that item?")
            s3= input()
            if s3 == 'Yes':
                s4= 'select review from reviews where reviews.itemnum = ' +d2
                cursor.execute(s4)
                rev= cursor.fetchall()
                print(rev)
            if s3 == 'no':
                print("Do you want to add this item to your cart?")
                s3= input()
                if s3== 'Yes':
                    s2= 'insert into cart(name, price) select name, price from Storage where Storage.itemnum = ' + d2
                    cursor.execute(s2)
                if s3 == 'no':
                    continue
        if d2 =='0':    
            print("Are you ready to check out? Press 0 is yes")
            d1= input()
    if d1 =='6':
        print('You have selected Motherboards')
        cursor.execute('select * from Motherboard;')
        allm=cursor.fetchall()
        print(tabulate(allm, headm))
        print("Would you like to add anything to your cart? if so type the item number that is associated with it if not press 0")
        d2 = input()
        if d2 == '26' or '27' or '28' or '29' or '30':
            s1= 'select itemnum, name, price from Motherboard where Motherboard.itemnum = ' + d2
            cursor.execute(s1)
            itemb= cursor.fetchall()
            print(tabulate(itemb, cartt))
            print("Would you like to see the review for that item?")
            s3= input()
            if s3 == 'Yes':
                s4= 'select review from reviews where reviews.itemnum = ' +d2
                cursor.execute(s4)
                rev= cursor.fetchall()
                print(rev)
            if s3 == 'no':
                print("Do you want to add this item to your cart?")
                s3= input()
                if s3== 'Yes':
                    s2= 'insert into cart(name, price) select name, price from Motherboard where Motherboard.itemnum = ' + d2
                    cursor.execute(s2)
                if s3 == 'no':
                    continue
        if d2 =='0':    
            print("Are you ready to check out? Press 0 is yes")
            d1= input()
    if d1 == '0':
        print('Your cart has')
        cursor.execute('select * from cart;')
        cart= cursor.fetchall()
        print(tabulate(cart, cartt))
        print("would you like to remove anything from your cart? press 1 if yes and 2 if no")
        ans = input()
        if ans == '1':
            print("Type the name of the item you want to remove and put your answer in quotes")
            ans = input()
            ans1= 'delete from cart where name = ' +ans
            cursor.execute(ans1)
            cursor.execute('select * from cart;')
            cart = cursor.fetchall()
            print(tabulate(cart, cartt))
        if ans == '2':
            print("Are you finished shopping?")
            ans = input()
            if ans == 'yes':
                print('Which shipping option would you like?')
                print('1-day $40, 2-day $30, or if order is over 100 standard is free otherwise it is $9.99')
                ship=input()
                if ship == '1-day':
                    print('it will be there over night')
                    cursor.execute('select sum(price) from cart;')
                    total =cursor.fetchall()
                    total =total + 40
                    print('Your total is:'+ total)
                if ship == '2-day':
                    print('it will be there over night')
                    cursor.execute('select sum(price) from cart;')
                    total =cursor.fetchall()
                    total =total + 30
                    print('Your total is:'+ total)
                if ship == 'standard':
                    print('it will be there over night')
                    cursor.execute('select sum(price) from cart;')
                    total =cursor.fetchall()
                    if total >= 100:
                        print('Your total is:'+ total)
                    if total <= 100:
                        total = total +9.99
                        print('Your total is 9.99')



    