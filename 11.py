point_dict = {
    '001': (100,88,81),
    '002': (60,70,80),
}
for student_id in point_dict:
    points = point_dict[student_id]
    subject_number = len(points)
    japanese, english, mathmatics = points
    total = japanese + english + mathmatics
    print(total)