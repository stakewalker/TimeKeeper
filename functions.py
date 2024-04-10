import pytesseract
import re
import telebot
from telebot import types

def time_from_photo(img_obj):
    # Open the image file
    image = Image.open(img_obj)
    # Extract text from the image
    text = pytesseract.image_to_string(image)
    # Look for time pattern (hh:mm)
    time_pattern = re.compile(r'\b([01]?[0-9]|2[0-3]):[0-5][0-9]\b')
    matches = time_pattern.findall(text)
    return matches


tl_bot = telebot.TeleBot(TL_BOT_TOKEN)
@tl_bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_message(message):
    if message.chat.type == 'group':
        # Create a markup with Yes and No buttons
        markup = types.InlineKeyboardMarkup()
        yes_button = types.InlineKeyboardButton(text="Yes", callback_data="yes")
        no_button = types.InlineKeyboardButton(text="No", callback_data="no")
        markup.add(yes_button, no_button)
        
        # Send a confirmation message with the markup
        tl_bot.send_message(message.chat.id, f"Is it correct?", reply_markup=markup)

@tl_bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "yes":
        # Save the data
        # save_to_sheets(data)
        # Edit message accordingly
        tl_bot.answer_callback_query(call.id, "Success! ✅")
        tl_bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Success! ✅", reply_markup=None)
    else:
        # Ask again?
        tl_bot.answer_callback_query(call.id, "Please send the data again")
        tl_bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Please send the data again", reply_markup=None)
# Runs bot forever
tl_bot.polling()

def calculate_hours():
    pass

def save_to_sheets(data):
    pass

def exception():
    # For special days, when manual editing will be required
    pass
