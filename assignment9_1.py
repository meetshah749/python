class File_Operations:
    def read_file(self, filename):
        try:
            with open(filename, "r") as file:
                content = file.read()
            return content
        except FileNotFoundError:
            raise FileNotFoundError("File not found.")
        except Exception as e:
            raise Exception(e)

    def write_file(self, filename, content):
        try:
            with open(filename, "a") as file:
                file.write(content)
            print("Data successfully written to file.")
        except Exception as e:
            raise Exception(f"Error! Data not written successfully.")
        
    def write(self,filename):
        try:
            with open(filename,"w") as file:
                file.write()
        except IOError as e:
            print("An error occurred while opening or writing to the file:", str(e))

    
    def write_lin(self,filename):
        try:
            with open(filename,"w") as file:
                file.writelines()
        except IOError as e:
            print("An error occurred while opening or writing to the file:", str(e))


# User-defined exception
class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message

    def msg(self):
        return self.message