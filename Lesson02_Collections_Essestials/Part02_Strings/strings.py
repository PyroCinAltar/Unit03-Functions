def format_course_code(code):
    code = code.strip().upper()
    return code


print(format_course_code("      Hello, i am a [big shot]!    --Spamton G. Spamton    "))
print(format_course_code("   webdev101  "))
print(format_course_code("      Python202    "))
print(format_course_code("Java303"))



def count_hashtags(post):
    post.strip()
    count = post.count("#")
    return count

#   words = post.split()
#   count = 0
#   for word in words:
#       if word.startswith(""):
#           count +=1
#   return count

post1 = "Great gamer today! #BergenTech #GoGamrz #Pride"
post2 = "Meeting tomorrow in room 205"
post3 = "#Robotics team wins #StateChampoinships #STEM #BergenTech"

print(count_hashtags(post1))
print(count_hashtags(post2))
print(count_hashtags(post3))