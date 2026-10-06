from datetime import timedelta

age = int(input("age "))

seconds = timedelta(days=age * 365).total_seconds()

print( int(seconds), "secand")
