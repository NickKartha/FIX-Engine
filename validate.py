#!/usr/bin/env python

#Validate valid order or non-order(reject) & Identify message type

input_TryAgain = 'no'
StopRun = 'no'

while StopRun != 'yes':

        #Prompt User for FIX message
        input_InFIXMsg = raw_input("Enter FIX Message: ")

        #Validate message

        while input_InFIXMsg not in ['35=D', '35=8']:
                print("Invalid message type. Please try again.")
                input_TryAgain = raw_input ("Enter Again: ")
        #       userInput = input ("Enter again?: ")
        #       userInput = userInput.lower ("")
        #       break();

        if input_TryAgain == ('yes'):
                StopRun = ('no')
                print('Never gonna Give you up - Rick Astley!')
        if input_TryAgain == ('no'):
                StopRun = ('yes')
                print('End of Program!')