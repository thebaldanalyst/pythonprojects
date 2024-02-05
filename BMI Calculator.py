#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator

# In[7]:


name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI > 0:
    if(BMI<18.5):
        print(name +", you are underweight. You need to go on a diet to build your BMI!")
    elif(BMI<=24.9):
        print(name +", you are normal weight. Awesome, keep up the healthy lifestyle.")
    elif(BMI<=29.9):
        print(name +", you are overweight. You need to exercise more.")
    elif(BMI<=34.9):
        print(name +", you are obese. You need to go on a weight loss diest and exercise more!")
    elif(BMI<=29.9):
        print(name +", you are severly obese. You need to avoid unhealthy lifestyle and professional help!!")
    else:
        print(name +", you are morbidly obese.You need a change from unhealthy habits, lifestyle and seek professional help!!!")
else:
    print("Enter a valid input")


# In[ ]:




