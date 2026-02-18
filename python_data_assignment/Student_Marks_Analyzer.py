marks = [78, 85, 90, 65, 88, 92, 80, 74]
print("All Marks:", marks)
print("First 3 marks:", marks[:3])
print("Last 3 marks:", marks[-3:])
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

# Print results
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
