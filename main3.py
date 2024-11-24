import dbhelper3



while True:
   print("Enter 1 table creation \n enter 2 for insert \n enter 3 show all records  \n enter 4 for exit" )

   option = int(input("Enter the option:"))

   if option==1:
      dbhelper3.create_query()

   elif option==2:
      dbhelper3.insert_query()

   elif option==3:
      dbhelper3.show_all()  

   elif option==4:
      dbhelper3.exit_parkinglot()

   else:
      print("Invalid option. Please try again.")