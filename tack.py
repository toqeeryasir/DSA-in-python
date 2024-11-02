# We can build a stack by using list.
# Lets creat an imaginary stack of website pages that we have wisited.
browsing = ["https://www.youtube.com/",
            "https://www.youtube.com/watch?v=uKi_0hDA16E",
            "https://www.youtube.com/watch?v = 63Mvsw-3iEc"
            ]

# If we wanna add new items to our stack we will use append methode.
browsing.append("https://www.youtube.com/watch?v=MqdOQBWW-Nk")

# If we wanna remove an item from our stack we will use pop methode and it will remove an item from the last pushed index.
browsing.pop()

# To check last item in our stack first we will use if statement and not operator to check is out stack is not empty, then we will pass negative -1 index.
if not browsing:
    print("Stack is empty")
print(browsing[-1])


# Lets build an imagenary stack for web_browsing.
browsing_session = []
while True:
    ans = input(
        "Press '1' to add session\nPress '0' to return to previous session\n")
    if ans == '1':
        session = input("Input session: ")
        browsing_session.append(session)
    elif ans == '0':
        if browsing_session:
            browsing_session.pop()
            if browsing_session:
                print("Back to previous session:", browsing_session[-1])
            else:
                print("You haven't any session! You were in last session")
        else:
            print("No sessions to return to!")
