#Kallen 0.0.1

"""
WHAT THIS IS?

TO DO LIST:
- Add ChatGPT instanse and connect it to the Discord bot
- Play music from YouTube
"""

import dbReader
import bot

def main():
    print("Hi! Would you want me to start my Discord Bot?");
    op= int(input("Yes(1) or No(0)"));
    if op == 1:
        bot.run_discord_bot();
    else:
        print("Well... there's nothing else I can do. \nBye!!");

if __name__=='__main__':
    main();