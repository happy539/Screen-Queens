import random

mystery = ['The Girl on the Train with Emily Blunt', 
'A Simple Favor with Blake Lively and Anna Kendrick','Murder Mystery with Jennifer Aniston','Now You See Me with Isla Fisher','Knives Out with Ana de Armas','Annihilation with Tessa Thompson and Natalie Portman', 'Enola Holmes with Millie Bobby Brown', 'Taking Lives with Angelina Jolie', "Before I go to Sleep with Nicole Kidman", "Riverdale with Lili Reinhart, Camila Mendes, Vanessa Morgan, and Madelaine Petsch",]

comedy = ['Mean Girls with Rachel McAdams, Lindsay Lohan, Amanda Seyfried, and Lizzy Caplan', "Murder Mystery with Jennifer Aniston","Knives Out with Ana de Armas", "Legally Blonde with Reese Witherspoon","Jumanji: Welcome to the Jungle with Karen Gillan","Pitch Perfect with Anna Kendrick and Rebel Wilson", "The Hustle with Anne Hathaway and Rebel Wilson", "Isn't it Romantic? with Rebel Wilson", "Modern Family with Ariel Winter, Julie Bowen, Sofia Vergara, and Sarah Hyland", "The Office with Jenna Fischer and Angela Kinsey","That 70s Show with Mila Kunis and Laura Prepon","Miss Congeniality with Sandra Bullock", "Victorious with Victoria Justice, Elizabeth Gillies, Daniella Monet, and Ariana Grande"]

action = ["Avengers Series with Scarlett Johansson and Elizabeth Olsen", "Guardians of the Galaxy series with Zoe Saldana","WandaVision with Elizabeth Olsen", "Suicide Squad with Margot Robbie", "Wonder Woman with Gal Gadot","Birds of Prey with Margot Robbie","Spiderman: Homecoming with Zendaya", "Spiderman: Far From Home with Zendaya", "Spiderman 1,2, and 3 with Kirsten Dunst", "Captain Marvel with Brie Larson", "The Amazing Spiderman series with Emma Stone"]

fantasy =['Harry Potter with Emma Watson', "Aladdin with Naomi Scott","Edward Scissorhands with Winona Ryder","Cats with Judi Dench, Taylor Swift, and Rebel Wilson","The Witches with Anne Hathaway, Octavia Spencer, and Kristin Chenoweth","Pirates of the Caribbean with Keira Knightley and Penelope Cruz", "Into the Woods with Emily Blunt and Anna Kendrick","Insatiable with Debby Ryan"]

romance = ['Love Actually with Keira Knightley',"The Notebook with Rachel McAdams","La La Land with Emma Stone","Five Feet Apart with Haley Lu Richardson","Midnight Sun with Bella Thorne","The Sun is Also A Star with Yara Shahidi"]

horror = ["IT: Chapter 2 with Jessica Chastain","Us with Lupita N'Yongo","The Babysitter with Samara Weaving","A Quiet Place with Emily Blunt"]

name = str(input("Enter your name ")) 

print("Hi" " " + name + " " + "I am going to recommend some movies and shows with these powerful actresses!")

print(" ")
print("1. Mystery")
print("2. Comedy")
print("3. Action")
print("4. Fantasy")
print("5. Romance")
print('6. Horror')
print(" ")

i = int(input("Enter your choice "))
while i > 6 or i < 1: 
    print(" ")
    print("Invalid input")
    print(" ")
    i = int(input("Enter your choice "))
if i == 1: 
  print("I recommend" + " " + random.choice(mystery) + " " +"for you.")
if i == 2: 
  print("I recommend" + " " + random.choice(comedy) + " " +"for you.")
if i == 3: 
  print("I recommend" + " " + random.choice(action) + " " +"for you.")
if i == 4: 
  print("I recommend" + " " + random.choice(fantasy) + " " +"for you.")
if i == 5: 
  print("I recommend" + " " + random.choice(romance) + " " +"for you.")
if i == 6: 
  print("I recommend" + " " + random.choice(horror) + " " +"for you.")

 
