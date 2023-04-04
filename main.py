import pyshorteners

link = input("Enter your URL link: \n")

shortener = pyshorteners.Shortener()

new_link = shortener.tinyurl.short(link)

print("New short URL link: ")

print(new_link)
