import sys

def initial_slambook():
    row = int(input("Enter the number of people that will be answering the questions: "))
    cols = 5

    slam_book = []
    for i in range(row):
        print("\nEnter contact %d details in the following order (ONLY): " % (i+1))
        print("NOTE: * indicates mandatory fields")
        print("..................................................................................")
        temp = []
        
        name = str(input("Enter name: ")).strip()
        if not name:
            sys.exit("Name is a mandatory field. Processing exit due to blank field...")
        temp.append(name)
        
        age = str(input("Enter age: ")).strip()
        temp.append(age)
        
        hobbies = str(input("Enter your hobbies: ")).strip() or None
        temp.append(hobbies)
        
        favorites = str(input("Enter your favorite color, animal, number, sport, B.F.F, and grade: ")).strip() or None
        temp.append(favorites)
        
        opinion = str(input("Enter something you hate and like about the person who made this slam book: ")).strip() or None
        temp.append(opinion)
        
        slam_book.append(temp)
    
    print(slam_book)
    return slam_book

def thanks():
    print("***********************************************************************************")
    print("Thank you for checking out the slam book")
    print("Please visit again!")
    print("***********************************************************************************")
    sys.exit("Goodbye, have a nice day!")

def instructions():
    print("..................................................................................")
    print("\t\tHOW TO USE A SLAM BOOK: It's simple! I will have questions written in this book. Answer them, and once you're done, give it to your friend. They will repeat the process. Have Fun!!! ")
    print("..................................................................................")

def menu():
    print("***********************************************************************************")
    print("\t\t\t\tSLAM BOOK DIRECTORY")
    print("***********************************************************************************")
    print("\tYou can now perform the following operations in this slam book\n")
    print("1. Answer questions")
    print("Other number. Exit slam book")
    try:
        choice = int(input("Please enter your choice: "))
    except ValueError:
        print("Invalid input. Exiting slam book.")
        sys.exit()
    return choice

def main():
    print("..................................................................................")
    print("Hello dear friend, welcome to my slam book")
    print("You may now proceed to explore my slam book")
    print("..................................................................................")
    
    while True:
        choice = menu()
        if choice == 1:
            initial_slambook()
        else:
            thanks()

if __name__ == "__main__":
    main()
