class India():
    def capital(self):
        print("New Delhi is the capital of india")
    def language(self):
        print("Hindi is the most widely spoken language in India")
    def type(self):
        print("India is a developing country")
class USA():
    def capital(self):
        print("Washington D.C is the capital of USA")
    def language(self):
        print("English is the most widely spoken language in USA")
    def type(self):
        print("USA is a developed contry")
objIndia = India()
objUSA = USA()
for country in (objIndia,objUSA):
    country.capital()
    country.language()
    country.type()