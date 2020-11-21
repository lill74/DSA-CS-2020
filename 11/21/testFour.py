name = "Lee"
print(type(name))
# Output: <class 'int'>

name = 1.0
print(type(name))
# Output: <class 'float'>

age = input("What is your age?")
# input의 값은 str을 갖는다
age = int(age) + 1
# str에서 int로 형변환(Casting)을 해준다
print("My name is " + str(age))
# int에서 str로 형변환(Casting)을 해준다
