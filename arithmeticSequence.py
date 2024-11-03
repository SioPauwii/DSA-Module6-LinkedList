#arithmetic equation for solving the nth term in an arithmetic sequence
#identify the common difference and the first term(if not given)
#find nth term given two terms

def find_nth_term(first_term, common_difference, n):
    return first_term + (n - 1) * common_difference

def nth_term_two_given(first_term, second_term, first_term_pos, second_term_pos, n):
    common_difference = (second_term - first_term) // (second_term_pos - first_term_pos - 1)
    return first_term + (n - first_term_pos) * common_difference

def find_common_difference(prev_term, next_term):
    return next_term - prev_term

def main():
    print("Arithmetic Sequence Calculator")
    print("1. Find nth term given first term and common difference")
    print("2. Find nth term given two terms")
    print("3. Find common difference")
    print("4. Exit the progam")

    choice = input("Enter your choice (1/2/3/4): \n")

    if choice == "1":
        first_term = float(input("Enter the first term: "))
        common_difference = float(input("Enter the common difference: "))
        n = int(input("Enter the term number: "))
        print(f'The nth term is: {int(find_nth_term(first_term, common_difference, n))}\n\n')
    elif choice == "2":
        first_term = float(input("Enter the first term: "))
        second_term = float(input("Enter the second term: "))
        first_term_pos = int(input("Enter the position of the first term: "))
        second_term_pos = int(input("Enter the position of the second term: "))
        n = int(input("Enter the term number: "))
        print(f'The nth term is: {int(nth_term_two_given(first_term, second_term, first_term_pos, second_term_pos, n))}\n\n')
    elif choice == "3":
        prev_term = float(input("Enter the previous term: "))
        next_term = float(input("Enter the next term: "))
        print(f'The common difference is: {int(find_common_difference(prev_term, next_term))}\n\n')
    elif choice == "4":
        print("Exiting the program")
        exit()
    else:
        print("Invalid choice")

    main()

main()