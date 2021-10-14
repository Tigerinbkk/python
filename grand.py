# score=input("ใส่คะแนนที่ทำได้ลงไป : ")
# score=int(score)

# if score >=80 and score <=100:
#     print(f"คะแนนทีไ่ด้ {score} เกรด : A")
# elif score >=60 and score <=79:
#     print(f"คะแนนทีไ่ด้ {score} เกรด : B")
# elif score >=50 and score <=59:
#     print(f"คะแนนทีไ่ด้ {score} เกรด : C")
# else:
#     print(f"คะแนนทีไ่ด้ {score} เกรด : D")

num,sum =(1,0)
while num <10:
    sum +=num
    if num>5:
        break
    print("valu of sum loop",num ,' = ')
    num+1
    print("here Outside loop")

