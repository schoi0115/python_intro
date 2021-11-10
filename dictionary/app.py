monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    0: "January"
}

print(monthConversions["Sep"])
print(monthConversions.get("Sep", "Not a valid Key"))
print(monthConversions.get("Lov", "Not a valid Key"))
print(monthConversions.get(0, "Not a valid Key"))