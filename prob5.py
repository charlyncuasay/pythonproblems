def problem_five():
    student_scores = [('John', 85), ('Maria', 92), ('Tom', 76), ('Sarah', 90)]
    lowest_score = student_scores[0]
    
    for student, score in student_scores:
        if score < lowest_score[1]:
            lowest_score = (student, score)
    print(f'Student with the lowest score is {lowest_score[0]} with a score of {lowest_score[1]}')

def divider():
    print("=" * 50)
    print()

def main():
    divider()
    problem_five()

if __name__ == "__main__":
    main()
