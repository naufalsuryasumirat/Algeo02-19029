"""string = "Baca juga: Hancurkan Arsenal, Jamie Vardy Kejar Top Skorer Abadi Man United"
if "Baca juga:" in string :
    print("yes")"""


names = ['bob', 'marley', 'bean']
age = [10, 22, 8]
location = ['indonesia', 'singapore', 'malaysia']
test_array = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
test_dictionary = [{"toy" : "Linus", "toy2" : "linus"}, {"toy" : "Linus", "toy2" : "linus"}, {"toy" : "Linus", "toy2" : "linus"}]


dictionary = [{"name" : val[0], "age" : val[1], "location" : val[2], "array" : val[3], "toys" : val[4]} for val in zip(names, age, location, test_array, test_dictionary)]
print(dictionary)

"""for x in dictionary:
    print(x)"""

#name = dictionary.get("name")
#print(name)

thisdict = {"brand" : "Ford", "model" : "Mustang", "year" : 1964}
x = thisdict.get("brand")
#y = dictionary[0].get("name")
y = dictionary[0].get("toys").get("toy2")
print(x)
print(y)

