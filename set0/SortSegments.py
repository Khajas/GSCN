##################################
#   Khaja Anwar Ali Siddiqui
#   GS Coding Ninjas
#   SET 0
#   Q3
###################################

all_points = input("Give pairs!\n")

if len(all_points) == 0:
    exit(0)

points = {}
inv_points = {}

for point in all_points:
    points[point[0]], inv_points[point[1]] = point[1], point[0]

(abscissa, ordinate) = points.popitem()
sorted_points = [(abscissa, ordinate)]

while len(points):
    have_valid_points = False
    if ordinate in points:
        next_ordinate = points.get(ordinate)
        sorted_points.append((ordinate, next_ordinate))
        have_valid_points |= points.pop(ordinate)
        ordinate = next_ordinate

    if abscissa in inv_points:
        next_abscissa = inv_points.get(abscissa)
        sorted_points.insert(0, (next_abscissa, abscissa))
        have_valid_points |= points.pop(next_abscissa)
        abscissa = next_abscissa

    if not have_valid_points:
        raise Exception("No valid Segments!");

print(sorted_points)
