import requests
import json

SERVER_URL = "http://localhost:5000"

def birthday_search(month,department):
   response = requests.get(f"{SERVER_URL}/birthdays", params = {"month": month, "department":department})
   date = response.json()
   print(f'Report for {department} department for {month} fetched')
   print(f'Total: {date["total"]}')
   print("Employees:")
   for key in date["employees"]:
      print(f'-{key['birthday']}, {key['name']}')


def anniversaries_search(month, department):
   response = requests.get(f"{SERVER_URL}/anniversaries", params = {"month": month, "department":department})
   date = response.json()
   print(f'Report for {department} department for {month} fetched')
   print(f'Total: {date["total"]}')
   print("Employees:")
   for key in date["employees"]:
      print(f'-{key['birthday']}, {key['name']}, {key["anniversary"]}')


# birthday_search("march", "Finance")   
anniversaries_search("march", "Finance")