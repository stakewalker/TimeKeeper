import functions

def main():
    # Keep listening to messages from user
    while True:
        # Runs bot forever
        functions.tg_bot.polling()

if __name__ == "__main__":
    main()
