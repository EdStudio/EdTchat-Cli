import os


class Env:
    def __init__(self, debug=False):
        self.debug = debug
        # Check if .env file exists
        if not os.path.isfile(".env"):
            # Create .env file
            open(".env", "w").close()
            # Check if debug is enabled
            if self.debug:
                # Print debug message
                print("Create .env file")

        # Recheck if .env file exists
        if not os.path.isfile(".env"):
            # Raise error
            raise Exception("Could not create .env file")

    def get(self, value):
        # Check if .env file exists
        if os.path.isfile(".env"):
            # Open .env file
            file = open(".env", "r")
            # Read all lines
            lines = file.readlines()
            # Loop through lines
            for line in lines:
                # Check if line contains value
                if line.startswith(value):
                    # Return value
                    return line.split("=")[1]
            # Close file
            file.close()

        return None

    def set(self, value, data):
        if self.get(value) is not None:
            self.modify(value, data)
            if self.debug:
                print(f"Modify {value} to {data}")
        else:
            print("Set " + value + " to " + data)
            
            # Ajoute la valeur à la fin du fichier
            file = open(".env", "a")
            file.write(value + "=" + data + "\n")
            file.close()

    def remove(self, value):
        # Check if .env file exists
        if os.path.isfile(".env"):
            # Open .env file
            file = open(".env", "r")
            # Read all lines
            lines = file.readlines()
            # Loop through lines
            for line in lines:
                # Check if line contains value
                if line.startswith(value):
                    # Remove line
                    lines.remove(line)
            # Close file
            file.close()

    def modify(self, value, data):
        while self.get(value) is not None:
            self.remove(value)
        self.set(value, data)
