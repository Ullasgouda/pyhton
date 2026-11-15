# colection litrels/data in a {}
# it is unorder
# it is mutable(we can change the elemnets )
# it storeds uniq data
# set()-> we creat set
# it is unhashable vales so it is not in order


# Data type       Hashable?    Example

# int             Yes          10
# float           Yes          10.5
# str             Yes          "Python"
# bool            Yes          True
# tuple            Sometimes    (10, 20)
# frozenset        Yes, if its elements are hashable frozenset({1, 2})
# list             No           [10, 20]
# set              No           {10, 20}
# dict             No           {"a": 10}


# Feature                     set       frozenset

# Mutable?                    Yes       No
# Allows duplicates?          No        No
# Ordered?                    No        No
# add()                       Yes       No
# remove()                    Yes       No
# union()                     Yes       Yes
# intersection()              Yes       Yes
# Can be a dictionary key?    No        Yes, if its elements are hashable
# Can be inside another set?  No        Yes, if its elements are hashable


sett = {"pyhton", True, False, None, 1211, 122.22, 3+3j}
print(len(sett))
print(id(sett))
print(type(sett))
# print(hash(sett))
print(sett)
for ele in sett:
    print(hash(ele), "->")
    print(id(ele), "->")
    print("*"*30)
# is is an empty set
ecc = set()
# add the element
sett.add("ullas")
# we can update multiple input using a list r tupe
sett.update(["java", "python", 66])
# delete the element
sett.pop()
sett.remove('ullas')
sett.discard('ullas')
sett.clear()
del (sett)

print(sett)
print("*"*100)
us1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
us2 = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U", 1}
# combining of 2 r more set in one set can be don by "union "and "|"
us3 = us1.union(us2)
print(us3)
us3 = us1 | us2
print(us3)
print("*"*100)
# it in the comen elmet in 2 set and it can be inselized by 'intersection' an '&' METHOD
print("intersection")
us3 = us2.intersection(us1)
print(us3)
us3 = us2 & us1
print(us3)
print("*"*100)
# semetric diffrence
us3 = us2.symmetric_difference(us1)
print(us3)
print("*"*100)
# updating hole set
us1.update(us2)
print(us1)
print("*"*100)
# intersection update is the thing to give the intersecting data and update it to the us2
us2.intersection_update(us1)
print(us2)
# int will give the difrenvc and updae the value
us2.difference_update(us1)
print(us2)
# symmetric_difference_update it is the element wihic will remove the same and combine and it will give the result
us2.symmetric_difference_update(us1)
print(us2)
# string comprehenstion
se = {x for x in range(1, 11) if x % 2 == 0}
print(se)
se1 = {x for x in range(0, 11) if x % 2 != 0}
print(se1)
