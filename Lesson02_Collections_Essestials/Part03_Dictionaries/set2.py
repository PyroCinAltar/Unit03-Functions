# Question 3
def calculate_engagement_rate(post):
    engagement = post.get("likes", 0) + post.get("comments", 0) + post.get("shares", 0)
    views = post.get('views')
    if views == 0:
        return 0
    rate = ((engagement / views) * 100)
    return f"{rate:.2f}"

post_stats = {"views": 1000, "likes": 50, "comemnts": 10, "shares": 5}
print(calculate_engagement_rate(post_stats))
post2_stats = {"views": 0, "likes": 50, "comemnts": 10, "shares": 5}
print(calculate_engagement_rate(post2_stats))

# {"alpha": 3, "beta": 1, "gamma":1}