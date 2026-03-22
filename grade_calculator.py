while True:
    try:
        Student_name = input("Enter Student Name: ")
        Enter_marks = int(input("Enter marks (0-100):"))

        if 0<= Enter_marks <= 100:
            print(f"📊 RESULT FOR {Student_name}:")
            print(f"Marks: {Enter_marks}/100")

            if 90 <= Enter_marks <= 100:
                print("Grade:A ")
                print("Excellent work! Very good! Keep it up! 🌟")

            elif 80<= Enter_marks <= 89:
                print("Grade:B ")
                print("Great job! You're doing really well—keep improving! 👍")

            elif 70 <= Enter_marks <= 79:
                print("Grade:C ")
                print("Good effort! Keep practicing and you’ll get even better! 📈")

            elif 60 <= Enter_marks <= 69:
                print("Grade:D ")
                print("Fair attempt! Put in a bit more effort to improve! 💪")

            else:
                print("Grade:F ")
                print("Needs improvement. Don’t give up—try again with more focus! 🔄")

                break

        else:
            print("❌ Invalid marks! Please enter between 0 and 100.\n")
    except ValueError:
        print("Invalid context, type ins number")