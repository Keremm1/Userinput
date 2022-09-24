#Biz ne istiyoruz?Etkileşimli kabuk üzerinden kullanıcıdan girdi alan belli özelliklere sahip bir program yapmak istiyoruz.
#Özellikler:
#-Kullanıcının girdiği değerleri almalı.
#-Kullanıcıdan aldığı değerleri anlık olarak kontrol etmeli ve istenilen kalıba uygun olmayan girdi için aktif bir hata mesajı yollamalı.
#-Kullanıcı aktif olarak isterse girdiği değerleri sisteme yollamadıysa silebilmeli.
#-1 ile gönderiyi sisteme ilşetebilmeli.
#Plan:
#1-Girdiyi alma yolumuz?
#2-Girdiyi anlık aktif kontrol etme?
#3-Girdinin durumuna göçre hata veya onay mesajı gönderme?
#4-Girdi silme özelliği eklemeli?
#5-1 tuşu ile veriyi onaylayıp sisteme gönderme?
#6-Gerekli olabilecek hataları göze alma.(UniEncodeError gibi)
#1-Şartları kontrol et yani veri için kotnrol mekanizması geliştir
#2-Döngüde sorun olmadığından emin ol yani her program döngünün başına geldiğinde hata olup olmadığını kontrol et.


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