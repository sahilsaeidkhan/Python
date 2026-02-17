
# Single-level Inheritance 

class Diploma:
    exam_level = "medium"
    job_chances = "medium - low salary"

class Btech(Diploma):
    college = "Galgotias University"
    fees = 1_80_000

B1 = Btech()
print(B1.job_chances)
print(B1.fees)




























# Multi-level Inheritance 

class Nani:
    type = "cute"
    age = 90
    address = "Azamgarh"

class Ammi(Nani):
    type = "more_cute"
    age = 55
    address = "Lucknow"

class Appi(Ammi):
    type = "okay-okay"
    age = 26
    address = "lucknow"

class Girlfriend(Appi):
    type = "Dayn-chudail...."
    age = "looks older than Nani"
    address = "future nark"

Gf = Girlfriend()
print(Ammi.age)