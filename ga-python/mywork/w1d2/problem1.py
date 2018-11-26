time = 17

# If the time of day is before 9 a.m. --> print the quote 
# "Morning is wonderful. Its only drawback is that it comes at such an inconvenient time of day."
if time < 9:
    print("Morning is wonderful. Its only drawback is that it comes at such an inconvenient time of day.")

# Otherwise if the time of day is before or exactly 4 p.m. --> print the quote 
# "Working hard or hardly working?"
elif time <= 16:
    print("Working hard or hardly working?")

# Otherwise, if the time of day is before 8 p.m. --> print the quote 
# "How did it get so late so soon?"
elif time < 20:
    print("How did it get so late so soon?")

# Otherwise if the time of day is before 10 p.m. --> print the quote 
# "A day without sunshine is like, you know, night."
elif time < 22:
    print("A day without sunshine is like, you know, night.")

# Otherwise, for any time 10 p.m. or later --> print the quote 
# "Burning the midnight oil!"
elif time > 22:
    "Burning the midnight oil!"