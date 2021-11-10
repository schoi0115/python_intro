lucky_numbers = [4,6,1,85,31,12,54]
friends = ["Kevin", "Karen", "Jim", "Jim", "Shawn", "Barbara"]

#friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")  # takes two argument. first argument for where to locate and second argument for value. Least of the list will pushed
#friends.remove(1)
friends.pop()
print(friends.index("Kevin"))  # find the value
print(friends.count("Jim"))
friends.sort()  #sort does not work when the remove() being used, Sort does not include int from extend but string works
friends.reverse()

friends2 = friends.copy()

print(friends)
print(friends2)


friends.clear()
print(friends)
