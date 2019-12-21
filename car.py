class car():
    def __init__(self, name, color, model, company, tax):
        self.name = name
        self.color = color
        self.model = model
        self.company = company
        self.tax = tax
    def payer(self):
        if self.tax == "paid":
            print("taxes are cleared")
        else:
            print("Taxes are not cleared")
    def ours(self):
        if self.company == "Toyota":
            print("Car is Toyota made")
        else:
            print("Car is not Toyota made")
    def model(self):
        if self.model > 2017:
            print("Car can be repaired")
        else:
            print("Car cannot be repaired")
            
costumer1 = car("Umair", "white", "2019", "Toyota", "paid")
costumer2 = car("rizwan", "yelow", "2019", "Toyota", "paid")
costumer3 = car("hunain", "red", "2016", "Toyota", "un-paid")
costumer4 = car("maaz", "black", "1999", "toyota", "paid")
costumer5 = car("hammad", "jet black", "2018", "Toyota", "un-paid")
