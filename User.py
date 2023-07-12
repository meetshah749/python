def register():
    user = input("Enter Username: ")
    password = input("Enter Password: ")
    pos = input("Enter your Position in team: ")

    try:
        
        f = open("user.txt", "+w")
        usernames = [line.split(",")[0] for line in f]
        # f.close()
            
        if user in usernames:
            print("Username already exists. Please choose a different username.")
            return

        f = open("user.txt", "+a")
        f.writelines(f"{user},{password},{pos}\n")
        # f.close()

        print("Welcome!")
    except FileNotFoundError:
        print("Error: 'user.txt' file not found.")
        return