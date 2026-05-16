def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [[1, 'John Doe', 'V'], [2, 'Jane Doe', 'V'], [3, 'Jack Dane', 'VI'], [4, "James Doe", 'VI'], [5, 'Lily Doe', 'VII']]

print("\n Original List of Lists : ")
print(students)
print("\n Converted Lists to Dictionary : ")
print(test(students))