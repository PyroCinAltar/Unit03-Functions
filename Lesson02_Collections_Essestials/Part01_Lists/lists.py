'''
List Essentials:

Create => [1, 2, 3]
.append()    Adds to the end of the list(push in js)
.pop()       Removes from the end of the list(pop in js)
.insert(index, val)      Inserting at specified inxed value(splice in js)
slicing  => [start;end not included]
length and indexing are the same
'''

daily_likes = [500, 600, 750, 400]
usernames = ["@nasa", "@tswift", "@netflix"]
mixed_data = [500, "likes", "@user123", True]

first_day = daily_likes[0]
first_day = daily_likes[-1]
first_day = daily_likes[2]

first_three = daily_likes[0:3]
last_two = daily_likes[-2:]


# Post analyzer

def analyze_post(likes_lists):
    if likes_lists:
        total = sum(likes_lists)
        average = total / len(likes_lists)
        best_day = max(likes_lists)
        return(average, best_day)
    return "List is empty"


# Username formatter

def format_usernames(usernames):
    for i in range(len(usernames)):
        usernames[i] = "@" + usernames[i]
    return usernames

result = format_usernames(["nasa", 'tswift', 'netflix'])
print(result)
# prints => ['@nasa', '@tswift', '@netflix']


# Filter Trending Posts
post_likes = [500, 1200, 800, 1500, 600]

def trending_posts(post_list):
    trending = []
    for post in post_list:
        if post > 1000:
            trending.append(post)
    return trending

results = trending_posts(post_likes)
print(results)