from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
data_employees = [
    {
        "name": "John Doe",
        "birth_date": "1984-04-15",
        "hire_date": "2010-05-20",
        "department": "Sales"
    },
    {
        "name": "Jane Dartmund",
        "birth_date": "1990-03-08",
        "hire_date": "2015-02-10",
        "department": "Finance"
    },
    {
        "name": "Alice Chou",
        "birth_date": "1984-02-18",
        "hire_date": "2012-09-18",
        "department": "Sales"
    },
    {
        "name": "Bob Mikel",
        "birth_date": "1978-04-30",
        "hire_date": "2018-11-05",
        "department": "Engineering"
    },
    {
        "name": "Eva King",
        "birth_date": "1979-03-18",
        "hire_date": "2013-07-12",
        "department": "Finance"
    }]

@app.route("/birthdays")
def birthday_search():
    month = request.args.get("month")
    month_numb = datetime.strptime(month, "%B").month
    department = request.args.get("department")
    list_total = {"total": 0,
                "employees":[]}
    for key in data_employees:
        if key["department"]== department:
            if datetime.strptime(key["birth_date"],"%Y-%m-%d").month == month_numb:       
                list_total["total"] +=1
                new_empl = {"name": key["name"],"birthday": datetime.strptime(key["birth_date"], "%Y-%m-%d").strftime("%B %d")}
                list_total["employees"].append(new_empl)
    return jsonify(list_total)

@app.route("/anniversaries")
def anniversaries_search():
    month = request.args.get("month")
    department = request.args.get("department")
    year = datetime.now().year
    month_numb = datetime.strptime(month, "%B").month
    list_total = {"total": 0,
                "employees":[]}
    for key in data_employees:
        if key["department"]== department:
            if datetime.strptime(key["birth_date"],"%Y-%m-%d").month == month_numb: 
                year_anniv = datetime.strptime(key["birth_date"],"%Y-%m-%d").year
                delta_yer = year-year_anniv
                if delta_yer %10 == 0 or delta_yer %10 == 5:
                    list_total["total"] +=1
                    new_empl = {"name": key["name"],"birthday": datetime.strptime(key["birth_date"], "%Y-%m-%d").strftime("%B %d"),"anniversary": delta_yer}
                    list_total["employees"].append(new_empl)
    return jsonify(list_total)

    

# data_department = request.args.get("department")
# department = data.get("department")
# month = data.get("month")
# 


if __name__ == "__main__":
   app.run(debug=True)