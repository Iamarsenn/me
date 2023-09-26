try:
    hours=float(input("write here your work hours "))
    rate=float(input("write here your rate "))
    if hours > 40:
        salary = 40 * rate + ((hours - 40) * 1.5 * rate)
    else:
        salary = rate * hours
    print(salary)
except:
    print("wrong data")

# try:
#     score=int(input("write here your score "))
#     if score >100 or score<0:
#         print("wrong data")
#         pass
#     elif score >=90:
#         print("your grade is A")
#     elif score >= 80:
#         print("your grade is B")
#     elif score >= 70:
#         print("your grade is C")
#     elif score >= 60:
#         print("your grade is D")
#     elif score < 60:
#         print("your grade is F")
# except:
#     print("wrong data")

# count = 0
# sum = 0
# while True:
#     number=input("write here your number:")
#     if number=="done":
#         break
#     try:
#         number2=float(number)
#         sum+=number2
#         count+=1
#     except:
#         print("wrong data,write number")
# if count>0:
#     sredni=sum/count
#     print("sum is ",sum,"and count is ",count,"and average is ",sredni)
# else:
#     print("no numbers")
#     print("there is no sum,count and average")
