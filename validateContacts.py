import json
import re


class Record():

    def __init__(self, fullName, cityName, phoneNumber, emailAddress):
        self.fullName = fullName
        self.cityName = cityName
        self.phoneNumber = phoneNumber.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        self.emailAddress = emailAddress

        self.validEmail  = bool(re.match('^[a-zA-Z0-9-.]+@[a-zA-Z0-9-.]+\..+$', emailAddress))
        self.validPhone = bool(re.match("^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$", self.phoneNumber))


#Opening file and loading json data
f = open("Web Developer Test",)
data = json.load(f)
f.close()

records = []
for record in data:
    fullName = record['fullName']
    cityName = record['cityName']
    phoneNumber = record['phoneNumber']
    emailAddress = record['emailAddress']

    record = Record(fullName, cityName, phoneNumber, emailAddress)
    records.append(record)

#STEP 1: Listing all contacts in ascending order and printing validation errors
for record in  sorted(records, key=lambda records: records.fullName):
    validOrInvalid = "Valid"
    if record.validPhone:
        if not record.validEmail:
            validOrInvalid = "Email is invalid."
    else:
        if record.validEmail:
            validOrInvalid = "Phone is invalid."
        else:
            validOrInvalid = "Email and Phone are invalid."
    print(record.fullName, "->" ,validOrInvalid)

#Combining the errors in cities and storing in dictionary
cities = {}
print()
for record in records:
    errors = int(not record.validPhone) + int(not record.validEmail)
    if record.cityName not in cities:
        cities[record.cityName] = errors
    else:
        cities[record.cityName] += errors

#sTEP2: Sorting the dictionary in displaying them
for item in sorted(cities.items(), key=lambda x: x[1], reverse=True):
    print(item[0], item[1])