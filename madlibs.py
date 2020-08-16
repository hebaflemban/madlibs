def main():
	time = input("Enter a number from 1 to 12:")
	items = input("Enter a noun (plural):")
	name = input("Enter a name:")
	scream = input("Enter any sentence:")
	action = input("Enter a verb:")

	story = " The story goes... \n It was %s o\'clock when I heard a knock at the door.\n I opened the door and there was a box full of %s with a note saying \"From Mr. %s \" \n Just as I closed the door I heard a scream \" %s \" \n I froze in place and all I could do was %s .\"  " %(time, items, name.capitalize(), scream.upper(), action )

	print(story)

if __name__ == '__main__':
	main()
