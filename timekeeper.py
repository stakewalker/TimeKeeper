import functions

def main():
    # Listen to messages 
    print("TimeKeeper running!")
    while True:
        # Runs bot forever
        functions.tg_bot.polling()

if __name__ == "__main__":
    main()