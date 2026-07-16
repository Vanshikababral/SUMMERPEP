import os
from langchain_core.tools import tool

@tool
def app_opener(text:str)->str:
    """
    Opens VS Code, Chrome, or a local video based on the user's command.
    """

    # Update these paths according to your PC
    vs_code_path = r"C:\Users\hp\Desktop\Visual Studio Code.lnk"

    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    text = text.lower()

    if "vs code" in text or "visual studio code" in text:
        os.startfile(vs_code_path)
        return "Opening VS Code..."

    elif "chrome" in text:
        os.startfile(chrome_path)
        return "Opening Google Chrome..."
    
    else:
        return "Sorry, I don't know how to open that application."
    
# print(app_opener.invoke({"text": "Open VS Code"}))

print(app_opener.invoke({"text": "Open Chrome"}))

# print(app_opener.invoke({"text": "Play Video"}))
    

     