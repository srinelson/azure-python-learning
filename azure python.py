# Practice azure resource learning scripts
# This script is dummy structure of a real Azure SDK Script


class Resource:
    def __init__(self, name, type, location):
        self.name = name 
        self.type = type 
        self.location = location


# Dummy data 

mock_resource = [
    Resource("myVM", "Microsoft.compute/virtualmachines", "eastsus"),
    Resource ("myStorage", "Microsoft.Storage/storageAccounts", "westus"),
    Resource ("mySQLDB", "Microsoft.DBforMySQL/servers", "centralus")
]

print("Listing Azure Resources (Dummy Data)...\n")
for resource in mock_resource:
    print(f"Name: {resource.name}, Type: {resource.type}, Location: {resource.location}")


