print("hello")
my_var = 10
print(my_var)
my_name = "asaf"
print(my_name)
# comments
is_true = False
my_list = ["asaf", "brot", 41, True]
print(my_list[1])
my_dict = {"name" : "asaf",
             "lname": "brot",
              "age":"41",
             "is_married":True}
print(my_dict["name"])
print(my_dict.keys())
my_number = 5 * 2
my_other = 5 * " asaf"
print(my_other)

if my_number == 10:
    print(f"my number is : {my_number}")

fname = "asaf"
lname = "brot"

# all 3 options will display the same output
print(f"hello {fname} {lname}")
print("hello " + fname + " " + lname)
print("hello %s %s" % (fname, lname))





