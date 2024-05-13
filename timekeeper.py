import functions
from dotenv import load_dotenv

load_dotenv()

def main():
    # Keep listening to messages on Telegram group
    while True:
        functions.handle_message(message)

if __name__ == "__main__":
    main()
