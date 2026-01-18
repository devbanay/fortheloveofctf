import random
import time
import string
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_random_char():
    # Use a mix of letters, numbers, and punctuation for the "matrix" look
    return random.choice(string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;':,./<>?")

def main():
    target_flag = "esch{take_a_chill_pill}"
    
    # "Encryption" phase: Start with a string of random garbage the same length as the flag
    current_display = [generate_random_char() for _ in range(len(target_flag))]
    
    # Indices we have successfully solved
    solved_indices = []

    clear_screen()
    print("\n" * 5)
    print("ESTABLISHING SECURE CONNECTION...".center(80))
    time.sleep(1.0)
    
    print("INTERCEPTING PACKET...".center(80))
    time.sleep(1.0)

    print("DECRYPTING DATA STREAM:".center(80))
    print("\n")

    # Animation Loop
    # We run enough iterations to solve the whole string
    # We want it to look like it's "finding" the characters
    
    while len(solved_indices) < len(target_flag):
        
        # 1. Update the display string
        for i in range(len(target_flag)):
            if i in solved_indices:
                # If it's solved, keep it as the correct char
                current_display[i] = target_flag[i]
            else:
                # If not solved, generate a new random char (the glitch effect)
                current_display[i] = generate_random_char()

        # 2. Randomly "solve" a new character occasionally
        # This controls the speed of the reveal. 
        if random.random() > 0.8: # 20% chance to solve a letter per frame
            # Find a list of unsolved indices
            remaining = [x for x in range(len(target_flag)) if x not in solved_indices]
            if remaining:
                # Pick one random index to "lock in"
                new_solve = random.choice(remaining)
                solved_indices.append(new_solve)
                current_display[new_solve] = target_flag[new_solve]

        # 3. Construct the frame
        # We put it in a box to make it look like a UI
        border_top = "+" + "-" * (len(target_flag) + 4) + "+"
        border_bot = "+" + "-" * (len(target_flag) + 4) + "+"
        
        content = "".join(current_display)
        
        # 4. Print Frame (Overwrite previous line to animate)
        # Using carriage return \r to stay on the same line mostly, but clear screen is safer for large boxes
        sys.stdout.write(f"\r     {border_top}     \n")
        sys.stdout.write(f"     |  {content}  |     \n")
        sys.stdout.write(f"     {border_bot}     ")
        
        # Move cursor up 2 lines so we overwrite next time
        sys.stdout.write("\033[F" * 2) 
        
        time.sleep(0.05) # Speed of the glitch

    # Final Clean Print to ensure it stays on screen
    print("\n" * 3)
    print("ACCESS GRANTED.".center(40))
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAborted.")