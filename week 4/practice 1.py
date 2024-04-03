city_1 =  input("enter name of city 1 ")
city_2 = input("enter name of city 2 ")
#transfer city1 value  to temp
temp = city_1
city_2 = temp
#city1 is a free variable now
city_1 = city_2

print(f"the name of city 1 after swapping is {city_1} ") 
print(f"the name of city 2 after swapping is {city_2} ") 