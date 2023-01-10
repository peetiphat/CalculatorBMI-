class BMICalculator():
    def calBmi(self, height, weight):
        self.bmi = float(weight/(height*height))

    def criterion(self):
        if self.bmi > 25:
            return ("Fat")

        elif self.bmi > 18.5:
            return("Normal")

        elif self.bmi < 18.5:
            return("less")

    def result(self):
        return self.bmi

bm = BMICalculator()
print (" ----BMI Calculator---- ")
weight = float(input("Enter weight (kg.): "))
height = float(input("Enter height (m.): "))
bm.calBmi(height, weight)
print("Your BMI is:", bm.result())
print("You're", bm.criterion())
