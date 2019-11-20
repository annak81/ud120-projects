#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

print "Available features:"
features = enron_data.values()      #[enron_data[person]  for person in enron_data]
print sorted(features[0].keys())
print "########################"

print "Available people:"
people = enron_data.keys()
print sorted(people)
print "########################"
print ""

print "Number of people: ", len(enron_data)

features_per_person = {person : len(enron_data[person]) for person in enron_data}
print "Number of features per person: ", max(features_per_person.values())

pois = {person: features  for (person, features) in enron_data.items() if features["poi"] == 1}
print "Number of Persons of Interest (POI): ", len(pois)

print "Stock belonging to JAMES PRENTICE: ", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Emails to POIs from WESLEY COLWELL: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Stock options exercised by JEFFREY K SKILLING: ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

import operator
total_payments = {person: features["total_payments"] for (person, features) in enron_data.items() if features["total_payments"] != "NaN" }
sorted_payments = sorted(total_payments.items(), key = operator.itemgetter(1), reverse=True)
print "People with largest total payments:"
for val in [0,1,2,3]:
    print sorted_payments[val]

valid_salary = {person: features for (person, features) in enron_data.items() if features["salary"] != "NaN" }
print "People with valid salary: ", len(valid_salary), " => ", len(valid_salary) / float(len(enron_data))*100, "%"

valid_email = {person: features for (person, features) in enron_data.items() if features["email_address"] != "NaN" }
print "People with valid email: ", len(valid_email), " => ", len(valid_email) / float(len(enron_data))*100, "%"


invalid_payments = {person: features for (person, features) in enron_data.items() if features["total_payments"] == "NaN" }
print "People with NO payment info: ", len(invalid_payments), " => ", len(invalid_payments) / float(len(enron_data))*100, "%"


invalid_payments_poi = {person: features for (person, features) in enron_data.items() if features["total_payments"] == "NaN" and features["poi"] == 1 }
print "POIs with NO payment info: ", len(invalid_payments_poi), " => ", len(invalid_payments_poi) / float(len(pois))*100, "%"


# remove TOTAL, it should not be in the list!
enron_data.pop("TOTAL", 0)
stock_options = [features["exercised_stock_options"] for features in enron_data.values() if (features["exercised_stock_options"] != "NaN")]
print "Exercised stock options"
#print sorted(stock_options)
print "MIN: ", min(stock_options)
print "MAX: ", max(stock_options)
salary = [features["salary"] for features in enron_data.values() if (features["salary"] != "NaN")]
print "Salary"
print "MIN: ", min(salary)
print "MAX: ", max(salary)
#for person, features in enron_data.iteritems():
#   if features["poi"]:
#        print features["poi"], " - ", person, ": ", features["salary"]






