import pyautogui
import time
# Open the Start menu (Windows key)
pyautogui.press('win')
# Type 'Chrome' and hit Enter
pyautogui.typewrite('Chrome')
pyautogui.press('enter')
# Wait for Chrome to open
time.sleep(2)
# Navigate to a website (e.g., OpenAI's homepage)
pyautogui.typewrite('https://openai.com')
pyautogui.press('enter')
