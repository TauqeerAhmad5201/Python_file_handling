import os 

if os.path.exists('my_text.txt'):    #checking whether file exists or not 
    os.remove('my_text.txt')
else: 
    print('The file does not exist.')

os.rmdir('directory_to_be_removed')