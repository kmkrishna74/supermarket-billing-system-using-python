from datetime import datetime
name=input("Enter your name: ")
# list of items 
print(30*'*')
list=''' 
         Rice       Rs 50/-  per Kg
         Sugar      Rs 30/-  per Kg
         Salt       Rs 20/-  per Kg
         Oil        Rs 110/- per Kg
         Colgate    Rs 70/-  per Kg
         panner     Rs 120/- per Kg
         Maggie     Rs 100/- per Kg
         Boost      Rs 152/- per each
         '''
#choosing the option to display items details or to exit
option=int(input("Enter '1' to display list of items & '0' to EXIT:"))
if option ==1:
    print(list)
if option ==0:
    print("you have exited")
    
# defining the variables
price=0
pricelist=[]
totalprice=0
finalprice=0
itemlist=[]
quantitylist=[]
plist=[]

#assigning Rates for the items 
items={'rice':50,'sugar':30,'salt':20,'oil':110,'colgate':70,'panner':120,'maggie':100,'boost':152}

for i in range(len(items)):
    inp=int(input("If you want to buy items press '1' & '0' to EXIT:"))
    if inp==0:
        break
    if inp==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))           
            totalprice+=price
            itemlist.append(item)
            quantitylist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry you entered item is not available")
    else:
        print("you entered Wrong option")
    inp1=input("Can I Bill the Items Y or N: ")
    if inp1=='Y' or 'y':
        pass      
        if finalamount!=0:
            print(30*' ',"Mk supermarkets",30*' ')
            print(30*' ',"NAGALLAVARIPALEM",30*' ')
            print(30*' ',"NAME:",name,30*' ')
            print(20*'*',"date & time:",datetime.now(),30*'*')
            print(30*'-')
            print("sno",8*' ',"items",3*' ',"quantity",3*' ',"price")
            for i in range(len(pricelist)):
                print(i,10*' ',itemlist[i],10*' ',quantitylist[i],10*' ',plist[i])
            print(75*'-')
            print(50*' ',"totalamount:",'Rs',totalprice)
            print(50*' ',"gst amount","rs",gst)
            print(75*'-')
            print(50*' ',"finalamount:",'Rs',finalamount)
            print(75*'-')
            print(50*' ',"Thanks for visiting, visit again..!")