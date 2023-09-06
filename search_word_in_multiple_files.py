import os
text = input("Please enter text: ")
print(f"You have entered \"{text}\" word to search.")
path = os.getcwd()
#current_path
def searchText(path):
    
    os.chdir(path)
    files = os.listdir()
    #print(files)
    for file_name in files:
        #print(file_name)
        abs_path = os.path.abspath(file_name)
        
        if os.path.isdir(abs_path):
            searchText(abs_path)
            
        if os.path.isfile(abs_path):
             with open(file_name, 'rb') as f:
                 text1= f.read()
                 if text.lower() in text1.decode('latin-1'):
                     final_path = os.path.abspath(file_name)
                     print('---' +text.upper() + " word found in this path " + final_path)
                 else:
                     pass
                     #print("No match found in " + abs_path)
    #pass
onoff = 'off'
while onoff=='off':
    switch = input("word search/off: ")
    text = switch
    if switch==onoff:
        break
    searchText(path)
    
