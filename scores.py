from cs50 import get_int

scores = [80, 66, 70, 70]

average = sum(scores) / len(scores)
print(f"Average score: {average}")

# Appends to the list and makes it a bit more dynamic 
points = []
for i in range(3):
    point = get_int("Points: ")
    points.append(point) # Alternatively you can use points += [point] 

average_points = sum(points) / len(points)
print(f"Average points: {average_points}")