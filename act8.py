#!/usr/bin/env python

import random

def main():
    """Start a Top 5 Sekolah Terbaik SPM 2023 in Kedah guessing game."""
    print("Top 5 Sekolah Terbaik SPM 2023 in Kedah!")
    
    school = [
        "SMK Taman Jelutong",
        "SBPI Kubang Pasu",
        "Maktab Mahmud Pendang",
        "SMK Sultanah Asma",
        "SMA Hidayah Islamiah"
        ]
    
    x =random.choice(school)
    max_trials= 3
    trial=0
    guess = None
    #print(x)
    while trial<max_trials:
        guess = str(input("Apakah Top 5 Sekolah Terbaik SPM 2023 di Kedah? "))
        
        if x == guess:
            print(f"You guessed.Congratulations you got it right!".format(guess))
            break
        else:
            print(f"Unfortunately you got the wrong answer.".format(guess))
            print(f"You have {max_trials} chances remaining.")
            max_trials -= 1
        if max_trials == 0:
            print(f"out of attempts. The genre is actually {x}.".format(guess))
        
main()