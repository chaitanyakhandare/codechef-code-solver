import pyautogui
import time
import sys, os, pyperclip

# Code console = Mouse position: (1137, 436)
# Chatgpt textbox = Mouse position: (516, 848)
 
# Steps
# M = select and copy question text MANUALLY
# START the program
# press ctrl + right (we are now in codechef)
# click on the code console
# press cmd + a
# press delete
# press ctrl + right (we are now in CHATGPT)
# click on the chatgpt textbox
# press cmd + v
# press enter
# M = COPY THE OUTPUT MANUALLY

# come to program and bcoz program is waiting to press enter
# after pressing enter manually, now execute that write_code function

# press cmd + v
# press enter
# press ctrl + d
# press ctrl + right (we are now in codechef)
# click on the code console

# and wait for program to write the code

# REPEAT THESE STEPS


def write_code():
    print("Enter the text you want to write: ")
    userText = sys.stdin.read() 

    print("\nGO TO CODE BOX, Pasting the output in 4 sec...")
    time.sleep(4)

    for line in userText.split("\n"):  
        pyautogui.write(line, interval=0.05)  
        pyautogui.press("enter")

    print("\nText written successfully!")


# make func to find current mouse position
def get_mouse_position():
    print("Move your mouse to the desired position and press Enter...")
    input()
    x, y = pyautogui.position()
    print(f"Mouse position: ({x}, {y})")
    return x, y


# main
if __name__ == "__main__":
    while True:

        ## Main thing = your desktops must be look like this ##
        ## 1.[VSCode] 2.[CodeChef] 3.[ChatGPT] then only this program will work ##

        # wait user to press enter
        input("\n\nPress Enter after copying the question manually...")
        time.sleep(1)

        # press ctrl + right (we are now in codechef)
        pyautogui.keyDown("ctrl")
        pyautogui.press("right")
        pyautogui.keyUp("ctrl")
        time.sleep(1)
        # click on the code console
        pyautogui.click(1137, 436)  # Code console position
        time.sleep(1)
        # press cmd + a
        pyautogui.keyDown("command")
        pyautogui.press("a")
        pyautogui.keyUp("command")
        time.sleep(1)
        # press delete
        pyautogui.press("delete")
        time.sleep(1)
        # press ctrl + right (we are now in CHATGPT)
        pyautogui.keyDown("ctrl")
        pyautogui.press("right")
        pyautogui.keyUp("ctrl")
        time.sleep(1)
        # click on the chatgpt textbox
        pyautogui.click(516, 848)  # ChatGPT textbox position
        time.sleep(1.5)
        # press cmd + v
        print("Pasting the question...")
        os.system('osascript -e "tell application \\"System Events\\" to keystroke \\"v\\" using command down"')

        time.sleep(1)
        # press enter
        pyautogui.press("enter")
        time.sleep(1)

        # wait user to press enter
        input("\nPress Enter after copying the output manually...\n")

        print("Enter the text you want to write: ")
        userText = pyperclip.paste()
        # userText = sys.stdin.read() 

        print("\nGO TO CODE BOX, Pasting the output in 4 sec...")
        time.sleep(4)

        for line in userText.split("\n"):  
            pyautogui.write(line, interval=0.05)  
            pyautogui.press("enter")

        print("\nText written successfully!")
        time.sleep(1)

        # press cmd + shift + down to remove extra brackets
        pyautogui.keyDown("command")
        pyautogui.keyDown("shift")
        pyautogui.press("down")
        pyautogui.keyUp("shift")
        pyautogui.keyUp("command")
        time.sleep(1)
        
        # press delete key
        pyautogui.press("delete")
        time.sleep(1)

        # press cmd + enter
        pyautogui.keyDown("command")
        pyautogui.press("enter")
        pyautogui.keyUp("command")
    
        # and wait for program to write the code
        endornot = input("\nWant to repeat? (y/n) ")
        if endornot.lower() != 'y':
            break
    
    print("Exiting the program...")
        
        
        
