def write_file(file_name, file_content):
    try:
        with open(f'{file_name}.txt', 'w') as file:
            file.write(file_content)
        print(f"File '{file_name}.txt' successfully written.")
    except Exception as e:
        print(f"Error writing to file '{file_name}.txt': {e}")
        pass

def append_to_file(file_name, file_content):
    try:
        with open(f'{file_name}.txt', 'a') as file:
            file.write(file_content)
        print(f"Content appended to file '{file_name}.txt'.")
    except Exception as e:
        print(f"Error appending to file '{file_name}.txt': {e}")
        pass

def read_file(file_name):
    try:
        with open(f'{file_name}.txt', 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        print(f"Error reading file '{file_name}.txt': {e}")
        return None

    pass
