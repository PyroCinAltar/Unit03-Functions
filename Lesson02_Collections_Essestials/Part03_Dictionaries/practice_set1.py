# Question 1
'''
{"key_a": "value1", "key_b": 150, "key_d": 50}
False
'''

# Question 2
'''
120
60
'''

# Question 3
def get_user_bio(user):
    return user.get("bio", "No bio available.")

print(get_user_bio({"username": "coder", "bio": "Python enthusiast"}))
print(get_user_bio({"username": "newbie"}))


# Question 4
'''
50
160
'''

# Question 5
'''
2
'''

# Question 6
def get_total_engagement(post):
    likes = post.get("likes", 0)
    shares = post.get("shares", 0)
    comments = post.get("comments", 0)
    return likes + shares + comments

print(get_total_engagement({"likes": 100, "comments": 20, "shares": 10}))
print(get_total_engagement({"likes": 50, "comments": 5}) )
print(get_total_engagement({"views": 1000}))


# Question 7
'''
3
3
'''

# Question 8
'''
{"key1": "value1", "key2": 200, "key3": 50}
{"key1": "value1", "key2": 100, "key4" = True}
'''

# Question 9
def find_most_followers(users):
    if users:
        most_followed = ""
        most_followers = 0
        for user in users:
            if user["followers"] > most_followers:
                most_followers = user["followers"]
                most_followed = user["username"]
        return most_followed
    return None
    
users_list = [
{"username": "alex","followers": 1000},
{"username": "sam","followers": 5000},
{"username": "jordan","followers": 3000}
]

print(find_most_followers(users_list))