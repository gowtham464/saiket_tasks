def write():
    txt=input("enter you want add: ")
    with open(r"D:\python\saiket\furits.txt","r+") as f:
        f.write(txt.strip() + "\n")
        
def read():
    with open(r"D:\python\saiket\furits.txt","r+") as f:
        view_file=f.read()
        print(view_file)
        print("\n")
        
def append():
    txt=input("enter you want add: ")
    with open(r"D:\python\saiket\furits.txt","a") as f:
        f.write(txt.strip() + "\n")   
        
def find_replace():
    with open(r"D:\python\saiket\furits.txt","r+") as f:
        viewed_file=f.read()   
        find_word=input("enter a find word: ")
        word_replace=input("enter a replace word: ")
        if find_word in viewed_file:
            viewed_file=viewed_file.replace(find_word,word_replace)
            print(viewed_file)
        else:
            print(find_word,"this word not in file..")
            
#display the menu
def file():
        while True:
            print("***choice the menu option***")
            print("1.write...")
            print("2.read...")
            print("3.append...")
            print("4.find_replace")
            print("5.exit...")
            
            choice=int(input("enter a your option number: "))
            if choice == 1:
                write()
            elif choice == 2:
                read()
            elif choice == 3:
                append()
            elif choice == 4:
                find_replace()
            elif choice == 5:
                print("exit...! the file handling... ")
                exit()
            else:
                print("invalid choice!.. try again")
        
file()
            