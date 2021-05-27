import joblib
experience = float(input("Enter Your Year Experiences:-"))
model=joblib.load("salary.h5")
salary=model.predict([[ experience ]])
print(f"Based On Your {experience} Years Of Experience, The Company Would be Provide You the {salary} bucks Salary!!! ")
