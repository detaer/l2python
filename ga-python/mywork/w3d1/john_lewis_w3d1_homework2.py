# John Lewis w3d1 homework2
employees = [{
    "name": "Ron Swanson",
    "age": 55,
    "department": "Management",
    "phone": "555-1234",
    "salary": "$87,000"
},
{
    "name": "Leslie Knope",
    "age": 43,
    "department": "Middle Management",
    "phone": "555-4321",
    "salary": "$97,000"
},
{
    "name": "Andy Dwyer",
    "age": 29,
    "department": "Management",
    "phone": "555-1122",
    "salary": "$22,000"
},
{
    "name": "April Ludgate",
    "age": 21,
    "department": "Administration",
    "phone": "555-3345",
    "salary": "$187,000"
}
]
# employees = ["Bitter_Moustache_Employee", "Waffle_Boss_Employee", "Dave_Matthews_Tribute_Employee", "Modest_Goth_Employee"]
# employees = [Bitter_Moustache_Employee, Waffle_Boss_Employee, Dave_Matthews_Tribute_Employee, Modest_Goth_Employee]
# expected output
# Ron Swanson in Management can be reached at 555-1234.
# Leslie Knope in Middle Management can be reached at 555-4321.
# Andy Dwyer in Shoe Shining can be reached at 555-1122.
# April Ludgate in Administration can be reached at 555-3345.
for each in employees: 
    print(each["name"], " in ", each["department"], " can be reached at ", each["phone"], ".", sep='')

# actual output
# Ron Swanson in Management can be reached at 555-1234.
# Leslie Knope in Middle Management can be reached at 555-4321.
# Andy Dwyer in Management can be reached at 555-1122.
# April Ludgate in Administration can be reached at 555-3345.
