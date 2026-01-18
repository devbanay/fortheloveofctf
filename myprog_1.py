import random
import time
import string
import sys
import base64
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_target_flag():
    # The flag is obfuscated here so it cannot be read directly from the source code.
    # It is decoded only when the script runs.
    # Base64 for "esch{this_aint_it_mate}"
    obfuscated_data = "ZXNjaHt0aGlzX2FpbnRfaXRfbWF0ZX0="
    
    # Decode to bytes, then to string
    return base64.b64decode(obfuscated_data).decode('utf-8')

def generate_random_char():
    # Generates a random character for the "glitch" effect
    return random.choice(string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;':,./<>?")

def main():
    # 1. Decode the flag silently in the background
    target_flag = get_target_flag()
    
    # 2. Setup the animation variables
    # We start with a list of random characters equal to the flag's length
    current_display = [generate_random_char() for _ in range(len(target_flag))]
    solved_indices = []

    # 3. Intro Sequence
    clear_screen()
    print("\n" * 2)
    print(" [ SYSTEM ALERT ] : ENCRYPTED PACKET DETECTED")
    time.sleep(0.8)
    print(" [ ... ] : INITIATING BRUTE FORCE DECRYPTION...")
    time.sleep(1.0)
    print("\n")

    # 4. The Decryption Loop
    # Keep looping until we have solved every character index
    while len(solved_indices) < len(target_flag):
        
        # Update every character in the display
        for i in range(len(target_flag)):
            if i in solved_indices:
                # If we've already cracked this letter, keep it correct
                current_display[i] = target_flag[i]
            else:
                # If not, show a random glitch character
                current_display[i] = generate_random_char()

        # Randomly "crack" a new character
        # 15% chance per frame to find a correct letter
        if random.random() > 0.85: 
            unsolved = [x for x in range(len(target_flag)) if x not in solved_indices]
            if unsolved:
                new_index = random.choice(unsolved)
                solved_indices.append(new_index)
                current_display[new_index] = target_flag[new_index]

        # 5. Render the Frame
        output_string = "".join(current_display)
        
        # UI Formatting
        border = "=" * (len(target_flag) + 4)
        
        # ANSI Escape Codes to overwrite the previous lines
        sys.stdout.write(f"\r    +{border}+\n")
        sys.stdout.write(f"    |  {output_string}  |\n")
        sys.stdout.write(f"    +{border}+")
        
        # Move cursor up 2 lines to prepare for next overwrite
        sys.stdout.write("\033[F" * 2)
        sys.stdout.flush()
        
        # Animation speed
        time.sleep(0.05)

    # 6. Final Clean Output
    # Move cursor down past the animation
    print("\n" * 3)
    print(" [ SUCCESS ] : FLAG CAPTURED.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Decryption Aborted.")
