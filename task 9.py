marks={'alice':85,'bob':80,'guna':70}
name=input("enter a student's name:")
if name in marks:
    print(f"{name}'s marks: {marks[name]}" )
else:
    print("student not found")
