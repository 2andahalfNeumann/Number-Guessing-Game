import random
import time
from datetime import datetime
import data_reach as dr

def game_welcome_screen():
        print(
                "\n\nWelcome to the Number Guessing Game!"
              + "\nI'm thinking of a number between 1 and 100.")

        print( 
                "\nPlease pick a difficulty below:" 
              + "\n1 : Easy (10 chances and 2 hints)"
              + "\n2 : Medium (5 chances and 1 hint)"
              + "\n3 : Hard (3 chances)"
              + "\n\nOptions:"
              + "\n4 : View Scores"
              + "\n5 : Exit")
        
        while True:
            try:
                choice = int(input("\nEnter your choice: "))
                if choice in [1, 2, 3, 4, 5]:
                    break
                else:
                    print("\nPlease pick a number from 1 to 5!")
            except ValueError: 
                print("\nPlease pick a number from 1 to 5!")
            
        options = {
            1: game_easy,
            2: game_medium,
            3: game_hard,
            4: view_scores,
            5: 5
            }
        
        if choice == 5:
            print("\nExiting program")
            exit()
        else:
            action = options.get(choice)
            if action:
                action()
                
# Function for viewing scores                
def view_scores():
    print(
            "\nPlease select for the following: "
          + "\n1 : View All Scores"
          + "\n2 : View Top 5"
          + "\n0 : Go back"
          )

    while True:
        vs_choice = input("Please enter a number: ")
        if vs_choice == '1':
            return all_scores()
        elif vs_choice == '2':
            return view_best_scores()
        elif vs_choice == '0':
            game_welcome_screen()
        else:
            print("\nInvalid number. Please try again!")

# Function for viewing all scores        
def all_scores():
    print("\n" + "-" * 40 + "\n")
    score_list = dr.load_attempts()
    if not score_list:
        print("-" * 40 + "\n")
        print("\nNo scores available!")
        print("\nReturning to home screen in 5 seconds...")
        time.sleep(5)
        return game_welcome_screen()

    # Page setup
    scores_per_page = 3
    total_scores = len(score_list)
    total_pages = (total_scores // scores_per_page) + (1 if total_scores % scores_per_page != 0 else 0)
    page_number = 1
    while True:
        print(f"\nPage {page_number}/{total_pages}")
        print("-" * 40)
        # Scores for current page
        start_idx = (page_number - 1) * scores_per_page
        end_idx = (min(page_number * scores_per_page, total_scores))
        for i in range(start_idx, end_idx):
            score = score_list[i]
            print(f"\nAttempt {i + 1}:")
            print(
                      f"   Attempt made {score['attempt_datetime']}"
                    + f"\n   Difficulty: {score['difficulty']}"
                    + f"\n   Total Attempts Used: {score['total_attempts']}"
                    + f"\n   Final Guess: {score['correct_number']}"
                    + f"\n   Time Spend: {score['total_time']}"
                    )
            print("\n" + "-" * 40)  

        if page_number < total_pages:
            next_action = input("\nPress enter to continue - Press 1 to go back - Press 0 to exit: \n")
            if next_action == '0':
                view_scores()
            elif next_action == '1':
                if page_number >= 2:
                    page_number -= 1
                else:
                    page_number = 1
            else:
                page_number += 1
        elif page_number == total_pages:
            next_action = input("\nPress 1 to go back - Press 0 to exit: \n")
            if next_action == '0':
                view_scores()
            elif next_action == '1':
                page_number -= 1
        else:
            next_action = input("\nPress 1 to go back - Press 0 to exit: \n")
            if next_action == '0':
                view_scores()
            elif next_action == '1':
                page_number -= 1

def view_best_scores():
    print("\n" + "-" * 40 + "\n")
    score_list = dr.load_attempts()
    if not score_list:
        print("-" * 40 + "\n")
        print("\nNo scores available!")
        print("\nReturning to home screen in 5 seconds...")
        time.sleep(5)
        return game_welcome_screen()
    
    valid_score_list = [score for score in score_list if isinstance(score['correct_number'], int)]
    sorted_data = dr.sorted_score_list(valid_score_list)

    for i, score in enumerate(sorted_data[:5]):
        print(f"\nAttempt Number {i + 1}:")
        print(
                  f"   Attempt made {score['attempt_datetime']}"
                + f"\n   Difficulty: {score['difficulty']}"
                + f"\n   Total Attempts Used: {score['total_attempts']}"
                + f"\n   Final Guess: {score['correct_number']}"
                + f"\n   Time Spend: {score['total_time']}"
                )
        print("\n" + "-" * 40)  
        4
    next_action = input("\nPress 0 to exit: ")
    if next_action == '0':
        view_scores()
    elif next_action != '0':
        while True:
            next_action = input("\nInvalid number - Press 0 to exit: ")
            if next_action == '0':
                view_scores()

# Gamemodes
def game_easy():
    print("\nGreat! You have selected the Easy difficulty level. \nYou get a total of 2 hints.")
    chances = int(10)
    number_game(chances, "Easy")

def game_medium():
    print("\nGreat! You have selected the Medium difficulty level. \nYou get a total of 1 hint.")
    chances = int(5)
    number_game(chances, "Medium")

def game_hard():
    print("\nGreat! You have selected the Hard difficulty level.")
    chances = int(3)
    number_game(chances, "Hard")

#Game mechanics
def number_game(chances, difficulty):
    game_number = random.randint(0, 100)
    total_time = 0
    total_attempts = 0
    correct_guess = None
    attempt_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for chance in range(chances):
        start_time = time.time()
        while True:
            try:
                print(f"\nAttemps left: {chances - chance}/{chances}")
                guess = int(input("Enter your guess: "))
                if 0 <= guess <= 100:
                    break
                else:
                    print("Please select a number between 1 and 100.")
                    continue
            except ValueError:
                print("Invalid input. Please select a number between 1 and 100.")
           
        end_time = time.time() - start_time

        total_time += end_time
        total_attempts += 1
    
        if difficulty == 'Easy':
            if chance == 4:
                print("\n" * 2)
                print(f"\nHint: The number is between {max(1, game_number - random.randint(5, 15))} and {min(100, random.randint(5, 15) + game_number)}")
            elif chance == 8:
                print("\n" * 2)
                print(f"\nLast chance! The number is between {max(1, game_number - random.randint(1, 5))} and {min(100, random.randint(1, 5) + game_number)}")
        if difficulty == 'Medium':
            if chance == 3:
                 print("\n" * 2)
                 print(f"\nLast chance! The number is between {max(1, game_number - random.randint(1, 10))} and {min(100, random.randint(1, 10) + game_number)}")

        if guess == game_number:
            print(f"\nCongratulations! You guessed the correct number in {chance + 1} attempts.")
            if total_time > 60:
                print(f"\nThis attempt took {total_time / 60:.2f} minute(s)")
            else:
                print(f"\nThis attempt took {total_time:.2f} seconds")
            
            correct_guess = game_number
            break

        elif guess < game_number:
            print("\n" + "-" * 20)
            print(f"\nThe number is GREATER than {guess}")
            
        elif guess > game_number:
            print("\n" + "-" * 20)
            print(f"\nThe number is LESS than {guess}")


    if total_attempts >= chances and correct_guess is None:
        print("\nUnfortunately you didn't guess the correct number."+ f"\nThe number was: {game_number}")
        correct_guess = "Did not guess the number"

    summary = dr.summary_data(difficulty, total_attempts, correct_guess, total_time, attempt_datetime)

    attempts = dr.load_attempts()
    attempts.append(summary)

    dr.save_attempts(attempts)

    cont_or_exit = str(input("\nDo you wish to try again? (Y/N): ")).strip().upper()
    if cont_or_exit == 'Y':
        game_welcome_screen()
    else:
        print("\nThanks for playing!")
        return

game_welcome_screen()