input_data = input()

company_users = {}

while input_data != "End":
    company, employee = input_data.split(" -> ")

    if company not in company_users:
        company_users[company] = []

    if employee not in company_users[company]:
        company_users[company].append(employee)

    input_data = input()

for company_name in company_users:
    print(company_name)
    for employee_id in company_users[company_name]:
        print(f"-- {employee_id}")
