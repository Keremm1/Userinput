# Userinput
How to do input of added from user can control actively in interactive shell, here we are i work to do the program about this question.
import os,sys,msvcrt,time
clear = lambda : os.system('cls')
clear()
zet = 0
anan = open("anan.txt","w",encoding="UTF-8")
valla = open("valla.txt","w",encoding="UTF-8")
valla = open("valla.txt","r+",encoding="UTF-8")
anan = open("anan.txt","r+",encoding="UTF-8")
valla.write(" "*7)
valla.write("\nThe length of user name can't be lower than 6 characters.")
valla.seek(0)
def apply_file(a,verify):    
    if verify == True:
        for i in a:
            valla.seek(len(a))   
            print(i,file=valla,flush=True,end="")
    if verify == False:
        for i in a:
            anan.seek(len(a))                    
            print(i,file=anan,flush=True,end="")
keys = 0
end_value = []

while True:
    try:
        yener = False
        key = msvcrt.getch()
        ker = key.decode("UTF-8")
        if key == b'\x08':
            if len(end_value)>0:
                end_value.remove(end_value[len(end_value)-1])
                keys-=1
                apply_file(end_value,True)
                apply_file(end_value,False)
                if 1 <= keys <= 5:
                    end_value.append(ker)
                    apply_file(end_value,True)
                    apply_file(end_value,False) 
                    valla.seek(0)
                    clear()
                    print(valla.read())
                elif 15>keys>5:
                    end_value.append(ker)
                    apply_file(end_value,False) 
                    anan.seek(0)
                    clear()
                    print(anan.read())
                continue
        elif key == b'\r' :
            continue
        elif key == b'1':
            print("Program has been closed.")
            break
        else:
            keys+=1
            if 1 <= keys <= 5:
                end_value.append(ker)
                apply_file(end_value,True)
                apply_file(end_value,False) 
                valla.seek(0)
                clear()
                print(valla.read())
            elif 15>keys>5:
                end_value.append(ker)
                apply_file(end_value,False) 
                anan.seek(0)
                clear()
                print(anan.read())   

            elif keys >= 15:
                pass
    except (UnicodeEncodeError,UnicodeDecodeError):
        print("The user name has invalid characters.")

        

anan.close()
valla.close()
