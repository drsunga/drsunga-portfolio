#########################################################################
#             REFACTORING; SAVING AND READING DATA IN JSON           #
#########################################################################

from pathlib import Path
import json

def get_stored_username(path):
    """GET STORED USERNAME IF AVAILABLE"""
    if path.exists():
        contents = path.read_text()
        if not contents.strip():
            return None
        
        try:
            username = json.loads(contents)
            return username
        except json.JSONDecodeError:
            return None
    return None
    
def get_new_username(path):
    """PROMPT FOR NEW USERNAME"""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """GREET USER BY THE NAME"""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f'Welcome back, {username}')
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()