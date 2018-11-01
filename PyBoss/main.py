import os
import csv

csvpath = os.path.join("..", "PyBoss", 'employee_data.csv')

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

emp_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []

with open(csvpath, 'r', newline = '', encoding = 'utf-8') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter= ",")
    
    header = next(csvreader)
    
    for i in csvreader:
        emp_id.append(i[0])
        name = i[1].split(" ")
        first_name.append(name[0])
        last_name.append(name[1])
        dob_convert = i[2].split("-")
        dob.append(dob_convert[0] + "/" + dob_convert[1] + "/" + dob_convert[2])
        ssn_convert = i[3].split("-")
        ssn.append("***-**-" + ssn_convert[2])
        state.append(us_state_abbrev[i[4]])

    new_list = zip(emp_id, first_name, last_name, dob, ssn, state)

"""
    print(emp_id)
    print(first_name)
    print(last_name)    
    print(dob)
    print(ssn)
    print(state)
"""

output_file = os.path.join("..", "PyBoss", 'employees_list.csv')
with open(output_file, 'w') as csvfile:
    write = csv.writer(csvfile, delimiter= ",")
    write.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    
    for j in new_list:
        write.writerow(j)
    
                          