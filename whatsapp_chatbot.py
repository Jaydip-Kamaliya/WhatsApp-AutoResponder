import pyautogui
import time
import pyperclip
import whatsapp_utils

def send_message(message):
    """
    Sends a message in the current open WhatsApp chat.
    """
    try:
        pyperclip.copy(message)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1.5)  # Increased delay to ensure message is pasted properly
        
        # Optionally click in the message box to ensure focus
        pyautogui.click(628, 988)  # Adjust coordinates to your message input area
        time.sleep(0.5)
        
        pyautogui.press("enter")
        time.sleep(2)
    except Exception as e:
        print("Error in send_message:", e)


def conversation_flow(user_contact="My Number", ai_contact="ChatGPT", timeout=60, poll_interval=5):
    """
    Runs a continuous conversation:
      1. Greets the user (only once).
      2. Waits for the user's initial reply.
      3. Enters a loop where:
         - The user's reply is forwarded to the AI.
         - The bot waits for the AI's reply.
         - The AI's reply is forwarded back to the user.
         - The bot waits for the next user reply.
    
    If any waiting period exceeds the timeout, the conversation ends.
    """
    # Step 1: Greet the user (only once)
    whatsapp_utils.search_contact(user_contact)
    greeting = "Hello, I'm a chatbot created by Jaydip. \nHow can I help?"
    send_message(greeting)
    print("Greeting sent to", user_contact)
    
    # Step 2: Wait for the user's initial reply
    print("Waiting for user's initial reply...")
    user_reply = whatsapp_utils.wait_for_reply(timeout=timeout, poll_interval=poll_interval)
    if not user_reply:
        print("No reply received from", user_contact, "within the timeout. Ending conversation.")
        return False
    print("User replied:", user_reply)
    
    # Continuous conversation loop
    while True:
        # Forward the user's reply to the AI contact
        whatsapp_utils.search_contact(ai_contact)
        send_message(user_reply)
        print("User's reply forwarded to", ai_contact)
        
        # Wait for the AI's reply
        print("Waiting for AI's reply...")
        ai_reply = whatsapp_utils.wait_for_reply(timeout=timeout, poll_interval=poll_interval)
        if not ai_reply:
            print("No reply received from", ai_contact, "within the timeout. Ending conversation.")
            return False
        print("AI replied:", ai_reply)
        
        # Forward the AI's reply back to the user
        whatsapp_utils.search_contact(user_contact)
        send_message(ai_reply)
        print("AI's reply sent to", user_contact)
        
        # Now wait for the next user reply to continue the conversation
        print("Waiting for user's next reply...")
        user_reply = whatsapp_utils.wait_for_reply(timeout=timeout, poll_interval=poll_interval)
        if not user_reply:
            print("No further reply received from", user_contact, "within the timeout. Ending conversation.")
            return False
        print("User replied:", user_reply)

def main_loop():
    """
    Runs the conversation flow continuously.
    The conversation ends entirely if a timeout occurs in any phase.
    """
    conversation_successful = conversation_flow("My Number")
    if not conversation_successful:
        print("Conversation ended due to timeout.")

# Start the conversation flow.
main_loop()