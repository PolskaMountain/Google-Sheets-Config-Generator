import gspread
from oauth2client.service_account import ServiceAccountCredentials
import numpy as np
import os

#Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
file_name = 'client-secret.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

def main():
    generate_config("Rebelka")
    generate_config("Policja")

def generate_config(name):

    print("Generating config: " + name + ".cpp")

    try:
        sheet = client.open('Configi').worksheet(name)
    except:
        print("Errow while opening: " + name + " worksheet")
        return
        
    val = sheet.get_all_records()

    try:
        os.remove("out/" + name + ".cpp")
    except:
        print("No " + name + ".cpp. Skipping...")

    file = open("out/" + name + ".cpp", "x")

    for x in val:
        x = list(x.items())
        x = np.array(x)
        print(name + ".cpp > Adding new row")
        file.write('{"' + x[0][1] + '", ' + x[1][1] + ', ' + x[2][1] + ', -1, -1, "' + x[3][1] + '"};\n' )

if __name__ == "__main__":
    main()


