def append_data_to_file(roll_number, name, class_name, file="data.txt"):
    with open(file, "a") as f:
        f.writelines([f"Roll Number: {roll_number}\n", f"Name: {name}\n", f"Class: {class_name}\n"])

    with open(file, "r") as f:
        data = f.readlines()
        print("".join(data))

# Example usage
append_data_to_file("123456", "John Doe", "10th Grade")