salary = input ('enter your salary:')
salary = float (salary)

if salary >= 10000:
   tax = salary * 0.10  # percentage of tax is just an example here.
   print("Your tax status:", tax, "$")
elif salary >= 8000:
   tax = salary * 0.05
   print("Your tax status:", tax, "$")
elif salary >= 5000:
   tax = salary * 0.025
   print("Your tax status:", tax, "$")
else:
    print ("This income is tax-exempt") 

   
   
