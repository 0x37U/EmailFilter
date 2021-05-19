import os
os.system("cls")
print("""

 ██████╗ ██╗  ██╗██████╗ ███████╗██╗   ██╗
██╔═████╗╚██╗██╔╝╚════██╗╚════██║██║   ██║
██║██╔██║ ╚███╔╝  █████╔╝    ██╔╝██║   ██║
████╔╝██║ ██╔██╗  ╚═══██╗   ██╔╝ ██║   ██║
╚██████╔╝██╔╝ ██╗██████╔╝   ██║  ╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═════╝    ╚═╝   ╚═════╝ 
        Github : github.com/0x37U

""")
os.system("title [-] 0x37U Email filter") # change CMD title

filename = input("0x37U@List:~# ").strip() # Ask for list name

File = open(filename,"r").read().split("\n") # open list and read and split newlines with make list

os.system("mkdir Result") # create new folder
try:
    for i in File:
        b = i.split("@") # split "@" from line 
        c = open(f"Result\{b[1]}.txt","a") # create text file with domain name after split
        c.write(i+"\n") # write emails
        
except:
    print("Please check your list name")

print("\nPlease Check \"Result\" file UwU") # 
