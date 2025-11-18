# Question 5:

'''
18.0
15.0
'''

# Question 6:

def make_notification(user, *messages, urgent=False):
    # Write your code here
    alert = f"{user} - {", ".join(messages)}"
    if urgent:
        alert = "URGENT: " + alert
    return alert
        
    pass

# Test Question 6
print(make_notification("admin", "Server down!", urgent=True))  # Should return: "URGENT: admin - Server down!"
print(make_notification("user", "Welcome", "Check inbox"))  # Should return: "user - Welcome, Check inbox"

# Question 7:

'''
SELECT name, email FROM users LIMIT 10
SELECT * FROM logs WHERE level='error' LIMIT 5
'''

# Question 8: Log Action Function
def log_action(actor, *actions, timestamp=None, **context):
    # Write your code here
    list = []
    for key, value in context.items():
        list.append(f"{key}={value}")
    return f"{actor}: {", ".join(actions)} | {", ".join(list)}"
    pass

# Test Question 8
print(log_action("bot", "login", "scan", source="API", ip="1.2.3.4"))  # Should return: "bot: login, scan | source=API, ip=1.2.3.4"