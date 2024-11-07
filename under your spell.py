import sys
from time import sleep
import time

def apply_gradient(text):
    # Define the gradient colors for an "apocalypse" vibe
    colors = [
        "\033[38;5;88m",  # Dark red
        "\033[38;5;130m", # Orange-red
        "\033[38;5;94m",  # Deep orange
        "\033[38;5;136m", # Orange
        "\033[38;5;166m", # Dark orange
        "\033[38;5;202m", # Red-orange
        "\033[38;5;208m", # Orange-red
        "\033[38;5;124m", # Red
        "\033[38;5;88m"   # Dark red
    ]
    
    gradient_text = ''
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        gradient_text += color + char
    gradient_text += "\033[0m"  # Reset color
    return gradient_text

def print_lyrics():
    lines = [
        ("you keep me under your spell", 0.05),
        ("It's like I waited too long", 0.05),
        ("But all the scars you can see", 0.05),
        ("They're permanent and I'm not", 0.05),
        ("I want an innocent love", 0.05),
        ("The rest of time", 0.05),
        ("But all the scars you can see when I take my clothes off", 0.05),
        ("Oh, ah-ah, uh-ah, ah-ah, oh", 0.05),  
        ("Oh-oh, ah-ah, uh-ah, ah-ah", 0.05)
    ]

    delays = [0.3, 0.3, 0.3, 0.3, 
              0.3, 0.3, 0.3, 0.3, 0.3, 0.3]

    for i, (line, char_delay) in enumerate(lines):
        if "Oh, ah-ah, uh-ah, ah-ah, oh" in line:
            line = line.replace("Oh, ah-ah, uh-ah, ah-ah, oh", apply_gradient("Oh, ah-ah, uh-ah, ah-ah, oh"))
            char_delay = 0.02  
        for char in line:
            print(char, end='', flush=True)
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()