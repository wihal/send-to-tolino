from pytolino.tolino_cloud import Client, PytolinoException
import os
import sys
from dotenv import load_dotenv
import time

try:
    load_dotenv()

    username = os.getenv('username')
    print(username)
    password = os.getenv('password')
except:
    print("Please set your username and password in .env file")
    time.sleep(5)

def main(file_path: str = None):

    if file_path is None:
        print("No file path provided.")
        time.sleep(5)  
    
    file_extension = os.path.splitext(file_path)[1].lower()
    
    client = Client()
    
    client.login(username, password)
    
    client.register()
    

    client.upload(file_path, extension=file_extension)


    client.logout()

    print("Done!")
    
if __name__ == "__main__":
    try: 
        file_path = sys.argv[1] 
    except:
        file_path = input("Enter file path: ")
        
    main(file_path)