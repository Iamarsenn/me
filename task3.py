seconds=int(input("write seconds here "))
int_hours=seconds//3600
int_minutes=(seconds-(int_hours*3600))//60
remaining_seconds=seconds-((int_hours*3600)+(int_minutes*60))
print(int_hours,"hours")
print(int_minutes,"minutes")
print(remaining_seconds,"seconds")
