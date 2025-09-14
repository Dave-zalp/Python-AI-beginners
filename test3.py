# This exercise focuses on practicing basic Python data structures. You will:
#
# - Create a list of 5 students’ names and their ages.
#
# - Use a dictionary to store and access the students’ ages.


# Write a program to iterate through the dictionary and print each student's name along with their age.
# This helps you become familiar with how Python handles data collections.


first_list=['jane', 'sarah','stephen']

second_list = [18,19,20]


my_dict = {}



for k, v in zip(first_list,second_list):

    my_dict[k] =v





print(my_dict)





for key,value in my_dict.items():

    print(f"{key} is {value} years old")

