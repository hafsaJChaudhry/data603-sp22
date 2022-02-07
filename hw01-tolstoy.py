# text file path: /Users/hafsachaudhry/Downloads/2600-0.txt
import re
print("Hello! Welcome to hafsa's hw-01 for data603!\n")

try:
    # 1. OPEN AND READ TEXT
    with open("/Users/hafsachaudhry/Downloads/2600-0.txt") as story:
        text = story.read()
        print("...reading story...    :)")

        # 2. CLEAN UP TEXT so that it is...
        text = text.lower()       # all lower case
        text = "".join([i for i in text if not i.isdigit()])    # has no numbers
        text = text.replace("www", "")      # links www.
        text = text.replace("com", "")      # links .com
        text = text.replace("org", "")      # links .org

        # removes all wonky special ASCII characters including quotation marks
        # leaves behind A-z, new line, space, dashes
        text = re.sub("[^A-z \n\-]","",text)
        #text = text.strip("[]")

        # add all texts into a list (per word) and sort
        words = text.split()
        words = [wrd.strip("[]-''") for wrd in words] # remove extra characters that were missed smhhhhh

        # 3. FIND UNIQUE WORDS
        # set only holds unique values which is what we want
        unique = set(words)
        #print(sorted(unique))    # to visually check if there's repeats

        # 4. CALCULATE NUMBER OF UNIQUE WORDS
        # pretty sure to just count length of the set...unless I misunderstood directions
        print("There are {} total unique words in this story!!".format(len(unique)))
        print("This total does not include special characters and numbers. \nAlso removes words like \"www\", \"com\", \"org\" that were noticed when reading the text file.")


except FileNotFoundError:
    print("hmm...that path or file does not exist.")
    print("please make sure plain text story is downloaded and update path name to open the story!")
except Exception:
    print("Something isn't working....")


