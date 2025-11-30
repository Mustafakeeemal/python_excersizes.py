#Student Id (key) and Exams(value)  dict data structers = items()

Students={
    101:[85,90,78],
    102:[92,88,95],
    103:[75,54,70]
}

for student_id, exams in Students.items():
    print(f"Student Id: {student_id}")
    exam_no=1
    for notes in exams:
        print(f" {exam_no}. -  Exams Notes: {notes}")
        exam_no+=1
    print()