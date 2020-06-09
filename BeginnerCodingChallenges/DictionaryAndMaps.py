class DictionaryMap():
    map_dictionary = {}
    # Update map with new items in order of key
    def insert(self, insertkey, insertvalue):
        self.map_dictionary[insertkey] = insertvalue

    # Read the value from the designated key
    def read(self, readkey):
        # Search for the value based on the key identifier
        try:
            return readkey + "=" + self.map_dictionary[readkey]
        except:
            return None

dict = DictionaryMap()

# Input dictionary length
dict_length = int(input())

# Insert values and respective keys based on amount of content entered
for _ in range(dict_length):
    content = input().rstrip().split()
    dict.insert(content[0], content[1])

# Checks for retrievable content until it runs out of the dictionary length
while True:
    try:
        key = input()
        value = dict.read(key)
        if value is None:
            print("Not found")
        else:
            print(value)
    except:
        break