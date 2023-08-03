'''Task 1: Create a Dictionary from Lists of Keys and Values'''

keys = ["name", "age", "city", "country"]
values = ["Ram", 25, "Kathmandu", "Nepal"]
result_dict = {k: v for k, v in zip(keys, values)}
print(result_dict)


'''Task 2: Filter Students with Scores More Than 80'''

student_scores = {
    "Ram": 90,
    "Shyam": 75,
    "Hari": 82,
    "Sita": 95,
    "Gita": 78,
    "Rita": 88
}

high_scorers = {name: score for name, score in student_scores.items() if score > 80}
print(high_scorers)
