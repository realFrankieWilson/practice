#!/usr/bin/python3
import time

def gift(name):
  message = f"""
  🎉🎂 Happy Birthday, {name}! 🎂🎉

  Wishing you a day filled with love, joy, and amazing tech adventures!
  May your code compile without errors and your projects flourish.

  Here's to another year of great achievements and fun challenges!

  Cheers! 🥳
  """
  return message

def display_art():
  art = r"""
     _    _      _                          _             
    | |  | |    | |                        | |            
    | |__| | ___| | ___ _ __ ___   ___ _ __| |_ ___ _ __  
    |  __  |/ _ \ |/ _ \ '_ ` _ \ / _ \ '__| __/ _ \ '_ \ 
    | |  | |  __/ |  __/ | | | | |  __/ |  | ||  __/ | | |
    |_|  |_|\___|_|\___|_| |_| |_|\___|_|   \__\___|_| |_|
    """
  print (art)

def main():
  name = input("Input your name to unluck my gift!: ")
  display_art()
  time.sleep(2)
  print(gift(name))

if __name__ == "__main__":
  main()
