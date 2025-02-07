import pyautogui
import time
import pyperclip

def search_contact(contact):
    """
    Searches for a contact on WhatsApp Web.
    Uses fixed coordinates here (adjust as needed) or image recognition.
    """
    try:
        time.sleep(2)  # Wait for WhatsApp Web to load
        # Click on the search box (update coordinates or use locateOnScreen)
        pyautogui.click(150, 150)  # Adjust these values to match your screen!
        time.sleep(1)
        # Type the contact name
        pyautogui.write(contact, interval=0.1)
        time.sleep(2)
        # Click on the contact in the search results (update coordinates as needed)
        pyautogui.click(222, 222)  # Adjust these values to select the contact
        time.sleep(1)
    except Exception as e:
        print("Error in search_contact:", e)

def copy_message():
    """
    Copies the latest message from the chat area and returns the text.
    """
    try:
        # Click in the message area (adjust coordinates to your layout)
        pyautogui.click(577, 909)  # Change these values as needed
        time.sleep(1)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.5)
        return pyperclip.paste()
    except Exception as e:
        print("Error in copy_message:", e)
        return ""

def wait_for_reply(timeout=60, poll_interval=5):
    """
    Waits for a new reply for up to `timeout` seconds.
    Polls every `poll_interval` seconds.
    Returns the new message if detected; otherwise, returns None.
    """
    start_time = time.time()
    initial_message = copy_message()
    while time.time() - start_time < timeout:
        time.sleep(poll_interval)
        new_message = copy_message()
        if new_message != initial_message and new_message.strip() != "":
            return new_message
    return None
