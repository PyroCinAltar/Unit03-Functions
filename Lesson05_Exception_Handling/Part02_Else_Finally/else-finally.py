# try: 
#     score = int(input("Enter score: "))
# except ValueError:
#     print("Invalid Score")
# else: 
#     print(f"✅ Score Recorded: {score}")
    
    
def parse_command(message):
    """Parse a Discord command like !ban PlayerName 7days"""
    try:
        parts = message.split()
        command = parts[0]
        target = parts[1]
        duration = parts[2]
    except IndexError:
        print("❌Invalid command format-missing parts")
        return None
    else:
        print("✅Command parse success")
        if command.startswith("!"):
            print(f"⚡️Executing: {command}")
        return command, target, duration
    finally:
        print("This blokc rinsa regardless of ")
    
parse_command("!ban HelloName 7days")
result = parse_command("!ban HelloName 7days")
print(result)

