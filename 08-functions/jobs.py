def person(f_name, l_name, job):
    employee = {}
    employee["first_name"] = f_name
    employee["second_name"] = l_name
    employee["job"] = job
    return employee

person1 = person("john", "smith", "accounts")
person2 = person("josh", "smithy", "hr")
person3 = person("joan", "smithers", "sales")

print(person1)
print(person2)
print(person3)