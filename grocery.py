import os
import json
grocery={'count':0,'grocery list':[]}

def clear():
    os.system("clear")

def save_file():
    with open('grocerymanagment.json','w+')as file:
        json.dump(grocery,file,indent=4)
        print("added succesfully")

def add_product():
    clear()
    flag=0
    while flag==0:
        try:
            idno=int(input("Item id: "))
            item=input("Item name: ")
            price=float(input("Item price: "))
            qty=float(input("Item qty: "))
            flag=1
        except:
            print("invalid character")
    grocery_item={
        'idno':idno,
        'item':item,
        'price':price,
        'qty':qty
    }
    grocery['count']+=1
    grocery['grocery list'].append(grocery_item)
    print("f{idno}id number added successfully")


def display_product():
    clear()
    flag=0
    idno=int(input("Item id: "))
    for item in grocery:
        if item["idno"]==idno:
            print(item)
            flag = 1
            break
    if flag == 0:
        print('Item not exists')

def delete_product():
    clear()
    flag = 0
    try:
        idno=int(input("enter id number to delete : "))
        for item in grocery['grocery list']:
            if item['idno']==idno:
                grocery['grocery list'].remove(item)
                grocery['count']-=1
                print('delete')
                flag = 1
                save_file()
                break
        if flag == 0:
            print('Item not exists')
    except:
        print("invalid character")

def search_product():
    clear()
    flag = 0
    try:
        idno=int(input("enter id number to search : "))
        for item in grocery["grocery list"]:
            if item['idno']==idno:
                print("Item exists")
                print(f"Id: {item['idno']},Item: {item['item']}, Price: {item['price']}, Qty: {item['qty']}")
                flag = 1
                break
        if flag == 0:
            print('Item not exists')
    except:
        print("invalid character")
    
def update_product():
    clear()
    flag = 0
    idno=int(input("Provide Item Id: "))
    qty=int(input("Provide Item Qty: "))
    for item in grocery["grocery list"]:
        if item['idno']==idno:
            item['qty'] = qty
            flag = True
    if flag == 0:
        print('Item not exists')
def main():
    clear
while True:
    try:
        print("\n__Options__")
        print("1 Add Product")
        print("2 Display Product")
        print("3 Delete Product")
        print("4 Search Product")
        print("5 Update Product")
        print("6 save_file")
        print("7 Exit")
        choice=int(input("Enter your choice: "))

        if choice == 1:
            add_product()
        elif choice == 2:
            display_product()
        elif choice == 3:
            delete_product()
        elif choice == 4:
            search_product()
        elif choice == 5:
            update_product()
        elif choice == 6:
            save_file()
        elif choice==7:
            break
        else:
            print("--Invalid Input--")
    except:
        print("invalid character")

if __name__=='__main__':
    main()


