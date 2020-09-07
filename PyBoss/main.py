# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Get Current working directory of main.py file
cwd = os.getcwd()

# Set path for file

csvpath = os.path.join(cwd, "Resources", "employee_data.csv")
csvpath = os.path.normcase(csvpath)
csvpath = os.path.normpath(csvpath)

employee_output_file = os.path.join(cwd, "output","output.csv")
employee_output_file = os.path.normcase(employee_output_file)
employee_output_file = os.path.normpath(employee_output_file)

# Create dictionary and list variables to iterate through each row in the file
employee_data = {}
emp_id = []
name_split = ""
first_name = []
last_name = []
date_of_birth_split = []
date_of_birth = []
masked_ssn = []
state_abbrev = []
employee_data_file = []

# Dictionary of US states and US states abbreviations
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

# Read the data file and print output
with open(csvpath,'r',encoding="utf-8") as employee_csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(employee_csv_file, delimiter=',')

    # Skip the header row first
    csv_header = next(csvreader)
    
    # Uncomment below line to print the stored csv_header
    print(f"CSV Header: {csv_header}")

# Load dictionary variable from the employee_date.csv source file, convert data and load new lists with converted values
with open(csvpath,'r', newline="") as employee_data_f:
    
    # read file into a dictionary
    employee_data = csv.DictReader(employee_data_f)
    
    # Append to list to create headers
    emp_id.append("Emp ID")
    first_name.append("First Name")
    last_name.append("Last Name")
    date_of_birth.append("DOB")
    masked_ssn.append("SSN")
    state_abbrev.append("State")
    
    # for each row in the file's dictionary
    for row in employee_data:
        
        # load Employee ID into list variable
        emp_id.append(row["Emp ID"])
        
        # Split Employee names into First Name and Last Name
        name_split = row["Name"].split(" ")
        
        # Load First Name into list variable
        first_name.append(name_split[0])
        
        # Load Last Name into list variable
        last_name.append(name_split[1])
        
        # Split date of birth into year, month and date
        date_of_birth_split = row["DOB"].split("-")
        
        # Format date of birth in MM/DD/YYYY and load int list variable
        date_of_birth.append(date_of_birth_split[1] + "/" + date_of_birth_split[2] + "/" + date_of_birth_split[0])
        
        # Fetch last four digits of SSN and load into list variable
        masked_ssn.append("***-**-" + row["SSN"][7:11])
        
        # Lookup State abbreviations dictionary and load state abbreviation into list variable        
        state_abbrev.append(us_state_abbrev[row["State"]])
        
# Zip all tranformed lists together into tuples for writing to file
employee_data_file = zip(emp_id, first_name, last_name, date_of_birth, masked_ssn, state_abbrev)

# Writing to file
with open(employee_output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # print out to file:
    writer.writerows(employee_data_file)