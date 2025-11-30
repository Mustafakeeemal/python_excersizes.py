# Project: by using the list and set data structers, delete the variables of duplicated but
# hide them same name of the list and make them unduplicate.

#numbers_list:

numbers_list=[1,2,3,2,4,5,3,6,2,7,5,8]

# find the duplicated variables hide them in set data s:
numbers_set=set(numbers_list)
print(numbers_set)
# change set data structers to list:
numbers_list=list(numbers_set)
print(numbers_list)