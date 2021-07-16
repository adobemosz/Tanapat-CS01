a = int(input('คะแนนเก็บ ='))
b = int(input('ตะแนนสอบกลางภาค ='))
c = int(input('คะแนนสอบปลายภาค ='))
sum = a+b+c
if(80 <= sum <= 100  ):
    print('Grade A')
elif( 75 <= sum <= 79):
    print('Grade B+')
elif(70<= sum <= 74):
    print('Grade B')
elif(65 <= sum <= 69):
    print('Grade C+')
elif(60 <= sum <= 64):
    print('Grade C')
elif(55 <= sum <= 59):
    print('Grade D+')
elif(50 <= sum <= 54):
    print('Grade D')
elif(0 <= sum <= 49):
    print('Grade C')
else:
    print('invalid')
    