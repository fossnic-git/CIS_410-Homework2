# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 17:15:05 2024

@author: fossn
"""

import Formulas

def title():
    """Displays the title"""
    print("Temperature Converter")

def menu():
    """displays a menu for options to convert"""
    print ("1. Convert Fahrenheit to Celsius")
    print ("2. Convert Celsius to Fahrenheit")
    print ("3. Exit")
    
def main():
    """Main function that runs the program"""
    title()
    
    while True:
        menu()
        option = int(input("\n Enter Option 1-3:"))
        
        if option == 1:
            f = float(input("Temperature in Farenheit:"))
            c = Formulas.F_to_C(f)
            print (f"{f}*F is {c}*C" )
        elif option == 2:
            c = float(input("Temperature in Celsius:"))
            f = Formulas.C_to_F(c)
            print (f"{c}*C is {f}*F" )
        elif option == 3:
            print("closing calculator")
            break
        else:
            print("options 1-3 only") 
            
main()
    
    