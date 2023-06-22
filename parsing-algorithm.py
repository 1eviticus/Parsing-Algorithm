# parsing algorithm to remove specified ip addresses from a .txt file


# define function to read file, store contents as variable, and split into list
def update_file(import_file, remove_list):
    with open(import_file, "r") as file:
        ip_addresses = file.read()
    ip_addresses = ip_addresses.split()

    # loop through remove list and evaluate if 'element' is in list
    for element in remove_list:

        # remove 'elements' found in list
        if element in ip_addresses:
            ip_addresses.remove(element)

    # convert list back to a string and rewrite original file
    ip_addresses = "\n".join(ip_addresses)
    with open(import_file, "w") as file:
        file.write(ip_addresses)


# call the function
update_file("allow_list.txt", ["192.168.25.60", "192.168.90.124", "192.168.60.153"])

# read the edited file
with open("allow_list.txt", "r") as file:
    text = file.read()

print(text)
