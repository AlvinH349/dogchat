dogs = [
    {
    "name": "Mary",
    "handle" : "ma",
    "bio": "Hi, I am Mary. I love to play games everyday!",
    "age": 3,
    "likes": 2
    },

    {
    "name": "Carlie",
    "handle" : "char",
    "bio": "Hi, I am Charlie. I love to eat food everyday!",
    "age": 7,
    "likes": 1
    },

    {
    "name": "Nessie",
    "handle" : "nes",
    "bio": "Hi, I am Nessie. I love to sleep everyday!",
    "age": 9,
    "likes": 0
    }

]

#retrieve dog name based upon the handle name
def get_dog_by_handle(handle):
    for dog in dogs:
        if dog['handle'] == handle:
            return dog
    return None

posts = [
    ("ma", "I am going to Cali"),
    ("ma", "I took a walk"),
    ("char", "I ate the bag"),
    ("ma", "I did a trick"),
    ("nes", "I was in training"),
    ]

# returns the list of post based upon the user handle
def get_posts_by_handle(handle):
    results = []
    for post in posts:
        if post[0] == handle:
            results.append(post)
    return results