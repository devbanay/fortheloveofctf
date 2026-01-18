import random
import time
import string
import sys
import base64

def get_target_flag():
    obfuscated_data = "ZXNjaHt0YWtlX2FfY2hpbGxfcGlsbH0="
    return base64.b64decode(obfuscated_data).decode('utf-8')

def generate_random_char():
    return random.choice(string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;':,./<>?")

def main():
    target_flag = get_target_flag()
    current_display = [generate_random_char() for _ in range(len(target_flag))]
    solved_indices = []
    print("\n" * 2)
    print(" [ SYSTEM ALERT ] : ENCRYPTED PACKET DETECTED")
    time.sleep(0.8)
    print(" [ ... ] : INITIATING BRUTE FORCE DECRYPTION...")
    time.sleep(1.0)
    print("\n")
    while len(solved_indices) < len(target_flag):
        for i in range(len(target_flag)):
            if i in solved_indices:
                current_display[i] = target_flag[i]
            else:
                current_display[i] = generate_random_char()
        if random.random() > 0.85: 
            unsolved = [x for x in range(len(target_flag)) if x not in solved_indices]
            if unsolved:
                new_index = random.choice(unsolved)
                solved_indices.append(new_index)
                current_display[new_index] = target_flag[new_index]
        output_string = "".join(current_display)
        border = "=" * (len(target_flag) + 4)
        sys.stdout.write(f"\r    +{border}+\n")
        sys.stdout.write(f"    |  {output_string}  |\n")
        sys.stdout.write(f"    +{border}+")
        sys.stdout.write("\033[F" * 2)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n" * 3)
    print(" [ SUCCESS ] : FLAG CAPTURED.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Decryption Aborted.")
