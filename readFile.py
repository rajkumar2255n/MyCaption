def get_file_extension(filename):
    extension = filename.split('.')[-1]
    return extension

try:
    filename = input("Input the Filename: ")
    extension = get_file_extension(filename)
    if extension == 'py':
        print('It is a Python File')
        print(f"The extension of the file is: '{extension}'")
    elif extension == 'txt':
        print('It is a Text File')
        print(f"The extension of the file is: '{extension}'")
    else:
        print(f"The extension of the file is: '{extension}'")
        print('It is an unKnown file')
        
except IndexError:
    print("Please enter a valid filename with an extension.")
