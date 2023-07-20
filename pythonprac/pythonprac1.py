birth_year = input("enter your birth year: ")
' this line of code allows the user to input thei birthyear' 
age = 2023 - int(birth_year)
' this line of code takes the current year (2023) and subtracts it from the users entered birthyear in order to calculate its age. '
'The reason we had to put `(int)infront of <birthyear> is because there would be an error otherwise since it wojld be an integer '
'subrat a string which will not work thus we did (int)<birthyear>'
print(age)
' this line prints out the answers '