import random

def rock_paper_scissors():
    choices = ["rock", "scissors", "paper"]
    winning_combinations = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    print("Гра: Камінь, Ножиці, Папір")
    print("Доступні варіанти: rock, scissors, paper")
    
    while True:
        user_choice = input("\nВаш вибір (або 'q' для виходу): ").lower()
        
        if user_choice == 'q':
            print("Дякуємо за гру!")
            break
        
        if user_choice not in choices:
            print("Невірний вибір. Спробуйте ще раз.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Комп'ютер вибрав: {computer_choice}")
        
        if user_choice == computer_choice:
            print("Нічия!")
        elif winning_combinations[user_choice] == computer_choice:
            print("Ви виграли!")
        else:
            print("Комп'ютер виграв!")

if __name__ == "__main__":
    rock_paper_scissors()