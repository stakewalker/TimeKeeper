import fns
from dotenv import load_dotenv

load_dotenv()

def main():
    # Keep listening to messages on Telegram group
    while True:
        fns.handle_message(message)

if __name__ == "__main__":
    main()
