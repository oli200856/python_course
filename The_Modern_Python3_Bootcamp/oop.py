class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."

    @classmethod
    def from_string(cls, data_str):
        first,last,age = data_str.split(",")
        return cls(first,last,int(age))

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def __repr__(self):
        return f"{self.first} is {self.age}"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self,thing):
        return f"{self.first} likes {thing}"

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th Birthday!"


# user1 = User("Frodo", "Baggins", 51)
# user2 = User("Gandalf", "The Grey", None)

# print(user1.full_name())
# print(user2.full_name())
# print(user1.initials())
# print(user2.initials())
# print(user1.likes("Sam"))
# print(user2.likes("hobbits"))
# print(user1.birthday())
# print(User.active_users)
# User.display_active_users()

sam = User.from_string("Samwise,Gamgee,39")
# print(sam.first)
# print(sam.full_name())
print(sam)

