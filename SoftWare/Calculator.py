
import random
import time
import numpy as np

# NAME 
name = input("โปรดใส่ชื่อของน้องสุนัข : ")
# print("Dog's name : " , name)

# WEIGHT 
weight  = float(input("โปรดใส่น้ำหนักของน้องสุนัข : ")); # Send to DB
# print("Dog's weight : " , weight)

# AGE
years = int(input("อายุน้อง กี่ ปี : " )) # Send to DB
months = int(input("อายุน้อง กี่ เดือน : ")) # Send to DB
# print("Dog's AGE : " , years , "years" , months ,"months")

# RESULT
print("น้องชื่อ : " , name)
print("น้ำหนักของ ", name , " : " , weight)
print("อายุของ ", name , " : " , years , " ปี " , months ," เดือน ")

# RER ความต้องการพลังงานขณะพัก
if weight >= 12 and weight <= 24 : # Send to DB
    rer = (30 * weight) + 70 
    print("Your dog need " , rer , "kcal per day")
else : # Send to DB
    rer2 = weight ** 0.75
    rer = rer2 * 70
    print("Your dog need " , rer , "kcal per day")

# DER ความต้องการพลังงานต่อวัน
if years == 0 and months <= 4 : # Send to DB
    der = 3 * rer 
    print("DER per day : ", der , "kcal/day")
else :
    Choice = input("Do your dog neutered(n) / Obese prone(o) / Weight loss(w) / Set normal(s) ? : ")
    if (Choice == 'n') : # Send to DB
        derN = 1.6 * rer
        print("You choose NEUTERED") 
        print("DER per day : ", derN , "kcal/day")
    elif (Choice == 'o') : # Send to DB
        derN = 1.4 * rer 
        print("You choose OBESE PRONE")    
        print("DER per day : ", derN , "kcal/day")
    elif (Choice == 'w') : # Send to DB
        derN = 1.0 * rer  
        print("You choose WEIGHT LOSS")   
        print("DER per day : ", derN , "kcal/day")
    elif (Choice == 's') : # Send to DB
        derN = 2 * rer  
        print("You choose SET NORMAL")   
        print("DER per day : ", derN , "kcal/day")
    else :
        print("Please, Enter 'n' or 'o' or 'w' or 's' ")

# แต่ละมื้อของอาหาร
meal = int(input("ใน 1 วันให้อาหารกี่มื้อ ( 2 , 3 )"))
if meal == 2 or meal == 3 :
    eats = derN / meal 
    print(name , "ควรได้ ", eats , "กิโลแคลต่อมื้อ")
else :
    print("กรุณาใส่ 2 หรือ 3 ")

# Per 1000 kcal
Omega6 = 6.2 # g.
Zinc = 95 # mg.
VitE = 15.5 # IU.
Calcium = 1.9 # g. 
Phosphorus = 1.9 # g.
Magnesium = 220 # mg.


nutrients = [ Omega6 , Zinc , VitE , Calcium , Phosphorus , Magnesium ]
allNutri = np.array(nutrients)
# KcalperDay = 800 
necessity = allNutri * derN / 1000 
print(necessity)


# CAMERA
# name = "สุนัขทดลอง"
# for i in range(1, 13):
#     Camera = random.randint(1,100) # การเกา , โรคผิวหนัง , ขนร่วง 
#     if Camera >= 71 and Camera <= 80  : # Send to DB, APP (Picture)
#         print("พบเห็น การเกา!! ของ ", name)
#         time.sleep(1)
#         print("เพิ่มการให้วิตามิน อาบน้ำ")
#         time.sleep(3)
#         print("////////////////////////////////////////////////////")
#     elif Camera >= 81 and Camera <= 90 : # Send to DB, APP (Picture)
#         print("พบเห็น โรคผิวหนัง!! ของ ", name)
#         time.sleep(1)
#         print("เพิ่มการให้วิตามิน ปรึกษาแพทย์")
#         time.sleep(3)
#         print("////////////////////////////////////////////////////")
#     elif Camera >= 91 and Camera <= 100  : # Send to DB, APP (Picture)
#         print("พบเห็น ขนร่วง!! ของ ", name)
#         time.sleep(1)
#         print("เพิ่มการให้วิตามิน, โอเมก้า อาบน้ำ")
#         time.sleep(3)
#         print("////////////////////////////////////////////////////")
#     else : # Send to DB, APP (Picture)
#         print("สุขภาพดี..")
#         time.sleep(3)
#         print("////////////////////////////////////////////////////")








