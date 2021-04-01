class Grumpy(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS!")
        return super().__repr__()

    def __missing__(self, key):
        print(f"{key} AIN'T HERE!")

    def __setitem__(self, key, value):
        print("ALWAYS CHANGING THE DICT!")
        print("OH, FINE...")
        super().__setitem__(key, value)

d = Grumpy({"one": "two", "three": "four"})
print(d)
d['five'] = 'six'