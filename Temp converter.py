# Celsius = float(input())
# Fahrenheit = float(input())
# Kelvin = float(input())
# Rankine = float(input())
while True:
  print(" JHAF EDITING \n Temperature Converter \n \n Celsius to Fahrenheit = c2f \n Celsius to Kelvin = c2k \n Celsius to Rankine = c2r \n Fahrenheit to Celsius = f2c \n Fahrenheit to Kelvin = f2k \n Fahrenheit to Rankine = f2r \n Kelvin to Celsius = k2c \n Kelvin to Fahrenheit = k2f \n Kelvin to Rankine = k2r \n Rankine to Celsius = r2c \n Rankine to Fahrenheit = r2f \n Rankine to Kelvin = r2k \n ")
  def choice_chk():
    error_chk = input("\n What to do? ").lower()
    choice_list = 'c2f', 'c2k', 'c2r', 'f2c', 'f2k', 'f2r', 'k2c', 'k2f', 'k2r', 'r2c', 'r2f', 'r2k'
    while(len(error_chk) != 3 or error_chk not in choice_list):
      error_chk = input("Error, please look at the list.\nWhat to do? ").lower()
    return error_chk

  choice = choice_chk()
  if choice == "c2f":
      print(" \n Celsius to Fahrenheit ")
      def Celsius():
        while True:
          try:
            C_error_chk = float(input(" Celsius = "))
          except ValueError:
            print(" Please input a number. Try again.")
            continue
          else:
            return C_error_chk
      Celsius_Value = Celsius()
      print(f"{Celsius_Value} degree Celsius (°C) is equals to {(Celsius_Value * 9) / 5 + 32} degree Fahrenheit (°F) \n ")
  elif choice == "c2k":
      print(" \n Celsius to Kelvin ")
      def Celsius():
        while True:
          try:
            C_error_chk = float(input(" Celsius = "))
          except ValueError:
            print(" Please input a number. Try again.")
            continue
          else:
            return C_error_chk
      Celsius_Value = Celsius()
      print(f"{Celsius_Value} degree Celsius (°C) is equals to {Celsius_Value + 273.15} Kelvin (K) \n ")
  elif choice == "c2r":
      print(" \n Celsius to Rankine ")
      def Celsius():
        while True:
          try:
            C_error_chk = float(input(" Celsius = "))
          except ValueError:
            print(" Please input a number. Try again.")
            continue
          else:
            return C_error_chk
      Celsius_Value = Celsius()
      print(f"{Celsius_Value} degree Celsius (°C) is equals to {(Celsius_Value * 9) / 5 + 491.67} Rankine (R) \n ")
  elif choice == "f2c":
      print(" \n Fahrenheit to Celsius ")
      def Fahrenheit():
        while True:
          try:
            F_error_chk = float(input(" Fahrenheit = "))
          except ValueError:
            print(" Please input a number. Try again.")
            continue
          else:
            return F_error_chk
      Fahrenheit_Value = Fahrenheit()
      print(f"{Fahrenheit_Value} degree Fahrenheit (°F) is equals to {((Fahrenheit_Value - 32) * 5)/9} degree Celsius (°C) \n ")
  elif choice == "f2k":
      print(" \n Fahrenheit to Kelvin ")
      def Fahrenheit():
        while True:
          try:
            F_error_chk = float(input(" Fahrenheit = "))
          except ValueError:
            print(" Please input a number. Try again.")
            continue
          else:
            return F_error_chk
      Fahrenheit_Value = Fahrenheit()
      print(f"{Fahrenheit_Value} degree Fahrenheit (°F) is equals to {(((Fahrenheit_Value - 32) * 5)/9) + 273.15} Kelvin (K) \n ")
  elif choice == "f2r":
      print(" \n Fahrenheit to Rankine ")
      def Fahrenheit():
        while True:
          try:
            F_error_chk = float(input(" Fahrenheit = "))
          except ValueError:
            print(" Please input a number. Try again.")
            continue
          else:
            return F_error_chk
      Fahrenheit_Value = Fahrenheit()
      print(f"{Fahrenheit_Value} degree Fahrenheit (°F) is equals to {Fahrenheit_Value  + 459.67} Rankine (R) \n ")
  elif choice == "k2c":
      print(" \n Kelvin to Celsius ")
      def Kelvin():
        while True:
          try:
            K_error_chk = float(input(" Kelvin = "))
          except ValueError:
            print(" Please input a number. Try again.")
            continue
          else:
            return K_error_chk
      Kelvin_Value = Kelvin()
      print(f"{Kelvin_Value} Kelvin (K) is equals to {Kelvin_Value - 273.15} degree Celsius (°C) \n ")
  elif choice == "k2f":
      print(" \n Kelvin to Fahrenheit ")
      def Kelvin():
        while True:
          try:
            K_error_chk = float(input(" Kelvin = "))
          except ValueError:
            print(" Please input a number. Try again.")
            continue
          else:
            return K_error_chk
      Kelvin_Value = Kelvin()
      print(f"{Kelvin_Value} Kelvin (K) is equals to {(Kelvin_Value - 273.15) * (9/5) + 32} degree Fahrenheit (°F) \n ")
  elif choice == "k2r":
      print(" \n Kelvin to Rankine ")
      def Kelvin():
        while True:
          try:
            K_error_chk = float(input(" Kelvin = "))
          except ValueError:
            print(" Please input a number. Try again.")
            continue
          else:
            return K_error_chk
      Kelvin_Value = Kelvin()
      print(f"{Kelvin_Value} Kelvin (K) is equals to {Kelvin_Value * 1.8} Rankine (R) \n ")
  elif choice == "r2c":
      print(" \n Rankine to Celsius ")
      def Rankine():
        while True:
          try:
            R_error_chk = float(input(" Rankine = "))
          except ValueError:
            print(" Please input a number. Try again.")
            continue
          else:
            return R_error_chk
      Rankine_Value = Rankine()
      print(f"{Rankine_Value} Rankine (R) is equals to {(Rankine_Value - 491.67) * (5/9)} degree Celsius (°C) \n ")
  elif choice == "r2f":
      print(" \n Rankine to Fahrenheit ")
      def Rankine():
        while True:
          try:
            R_error_chk = float(input(" Rankine = "))
          except ValueError:
            print(" Please input a number. Try again.")
            continue
          else:
            return R_error_chk
      Rankine_Value = Rankine()
      print(f"{Rankine_Value} Rankine (R) is equals to {Rankine_Value - 459.67} degree Fahrenheit (°F) \n ")
  elif choice == "r2k":
      print(" \n Rankine to Kelvin ")
      def Rankine():
        while True:
          try:
            R_error_chk = float(input(" Rankine = "))
          except ValueError:
            print(" Please input a number. Try again.")
            continue
          else:
            return R_error_chk
      Rankine_Value = Rankine()
      print(f"{Rankine_Value} Rankine (R) is equals to {Rankine_Value * (5/9)} Kelvin (K) \n ")
  if input("Do another (y/n)?").lower() == "n":
    break