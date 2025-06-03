# Sample dataset for data science practice
# Each dictionary represents a person with their details

# List of dictionaries containing employee data
data = [
    {"name": "Alice", "age": 25, "city": "New York", "profession": "Data Scientist", "salary": 120000},
    {"name": "Bob", "age": 30, "city": "San Francisco", "profession": "Software Engineer", "salary": 150000},
    {"name": "Charlie", "age": 35, "city": "Los Angeles", "profession": "Product Manager", "salary": 140000},
    {"name": "Diana", "age": 28, "city": "Seattle", "profession": "UX Designer", "salary": 110000},
    {"name": "Eve", "age": 40, "city": "Chicago", "profession": "Data Analyst", "salary": 100000},
    {"name": "Frank", "age": 32, "city": "Austin", "profession": "DevOps Engineer", "salary": 130000},
    {"name": "Grace", "age": 29, "city": "Boston", "profession": "Machine Learning Engineer", "salary": 145000},
    {"name": "Henry", "age": 45, "city": "Denver", "profession": "IT Manager", "salary": 160000},
    {"name": "Ivy", "age": 26, "city": "Miami", "profession": "Data Engineer", "salary": 125000},
    {"name": "Jack", "age": 38, "city": "Portland", "profession": "Cloud Architect", "salary": 155000},
    {"name": "Karen", "age": 34, "city": "Dallas", "profession": "Cybersecurity Analyst", "salary": 135000},
    {"name": "Leo", "age": 27, "city": "San Diego", "profession": "Frontend Developer", "salary": 115000},
    {"name": "Mia", "age": 31, "city": "Phoenix", "profession": "Backend Developer", "salary": 125000},
    {"name": "Nathan", "age": 29, "city": "Philadelphia", "profession": "Full Stack Developer", "salary": 140000},
    {"name": "Olivia", "age": 36, "city": "Las Vegas", "profession": "Data Scientist", "salary": 150000},
    {"name": "Paul", "age": 41, "city": "Houston", "profession": "Database Administrator", "salary": 120000},
    {"name": "Quinn", "age": 33, "city": "Atlanta", "profession": "Cloud Engineer", "salary": 130000},
    {"name": "Rachel", "age": 37, "city": "Orlando", "profession": "AI Researcher", "salary": 160000},
    {"name": "Steve", "age": 39, "city": "Detroit", "profession": "Network Engineer", "salary": 125000},
    {"name": "Tina", "age": 28, "city": "Minneapolis", "profession": "Software Tester", "salary": 105000}
]

# Initialize an empty list to store salaries
my_list = []

my_list2 = []

for profession in data:
    print(profession["profession"])
    if profession["profession"] != "retail":
        print("We have yet to find a retail worker here")
    elif profession["profession"].lower() == "ai researcher":
        print("we actually have an AI researcher here ")
    else:
        print("your job has been replaced....")

# Loop through the dataset to extract salaries
for salary in data:
    print(salary["salary"])  # Print each salary
    my_list.append(salary["salary"])  # Add salary to the list

# Print the list of salaries
print(my_list)

# Initialize variables for calculating the average salary
total_sum = 0  # To store the sum of all salaries
len_of_list = len(my_list)  # Get the number of salaries

# Loop through the list of salaries to calculate the total sum
for figure in my_list:
    total_sum += figure  # Add each salary to the total sum
    employee_salary = total_sum / len_of_list  # Calculate the average salary


# Print the average salary
print(employee_salary)