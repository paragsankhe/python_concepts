class Animal:

    def __init__(self):
        print("object is created")

    def __del__(self):
        print("object is destroyed")

anmlobj = Animal()
del anmlobj