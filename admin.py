# Using open() fucntion
file_path = "admin.txt"

# Open file in write mode
with open(file_path, 'w') as file:
    # Write data to the file
    file.write("Admin User\n")
    file.write("Admin Name, Admin Password, Admin Email\n")
    file.write("HOW YONG-HENG, helloworld13, howyongheng@admin.com\n")

print(f"File '{file_path}' creatad successfully.")

