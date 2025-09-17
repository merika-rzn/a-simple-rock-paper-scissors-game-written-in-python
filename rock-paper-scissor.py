import random

choices = ["rock", "paper", "scissor"]
user_points = 0
AI_points = 0
round_user = input("how many rounds you want to play? ")
r_u_int = int(round_user)
round_number = 1

while round_number <= r_u_int:
    user_choice = input(f"Round {round_number} - choose between rock / paper / scissor: ").lower()

    # ورودی اشتباه
    while user_choice not in choices:
        print("❌ Please choose one of: rock, paper, scissor")
        user_choice = input(f"Round {round_number} - choose again: ").lower()

    # انتخاب تصادفی AI
    AI_choice = random.choice(choices)
    print(f"👉 You: {user_choice} VS AI: {AI_choice}")

    # بررسی نتیجه
    if user_choice == AI_choice:
        print("⚖️ Result: both same")
    elif (user_choice == "rock" and AI_choice == "scissor") or \
         (user_choice == "paper" and AI_choice == "rock") or \
         (user_choice == "scissor" and AI_choice == "paper"):
        user_points += 1
        print("🎉 You win this round!")
    else:
        AI_points += 1
        print("🤖 AI wins this round!")

    print(f"Score → You: {user_points} | AI: {AI_points}\n")
    round_number += 1

# نتیجه نهایی
print("🏁 Final Result:")
if user_points > AI_points:
    print(f"🎉 You win with {user_points} points!")
elif AI_points > user_points:
    print(f"🤖 AI wins with {AI_points} points!")
else:
    print("⚖️ It's a draw!")

print("\nThanks for playing Rock-Paper-Scissors! 🎮")
