# Instrument Game 1
# Question(" >", [""], 1), 
from dataclasses import dataclass
print("Welcome to my Quiz Game!")


def add(a, b):
    return a + b


def ask(question, answers, award):
    response = input(question)
    response = response.lower()
    if response in answers:
        print("Correct!")
        return award
    print("Incorrect!")
    return 0


@dataclass
class Question:
    question: str
    answers: list
    award: int

music = [
    Question("Who was the original drummer for The Beatles? >", ["pete best"], 1),
    Question("Will.i.am is best known for being part of which hip hop group? >", ["black eyed peas"], 1),
    Question("Who had a No.1 hit with 'Ice Ice Baby'? >", ["vanilla ice"], 1),
    Question("Who is the best-selling female artist of all time? >", ["madonna"], 1),
    Question("Which American hip hop duo had a 1986 hit with 'Push It'? >", ["salt-n-pepa"], 1),
    Question("'I got sunshine on a cloudy day' is the opening line to which Temptations song? >", ["my girl"], 1),
    Question("Beyonce rose to stardom as part of which girl band? >", ["destiny's child"], 1),
    Question("Who went solo in 1987 with the song 'Faith'? >", ["george michael"], 1),
    Question("Which artist is also known as Slim Shady? >", ["eminem"], 1),
    Question("'Hotel California' was a hit for which American band? >", ["the eagles"], 1),
]
movies = [
    Question("In The Matrix, does Neo take the blue pill or the red pill? >", ["red", "red pill"], 1),
    Question("For what movie did Tom Hanks score his first Academy Award nomination? >", ["big"], 1),
    Question("The head of what kind of animal is front-and-center in an infamous scene from The Godfather? >", ["horse", "a horse", "horse head", "a horse head"], 1),
    Question("In what 1976 thriller does Robert De Niro famously say 'You talkin to me?'? >", ["taxi driver"], 1),
    Question("What's the name of the anthemic dance near the beginning of The Rocky Horror Picture Show? >", ["the time warp", "time warp"], 1),
    Question("What Hollywood movie star plays himself in Zombieland? >", ["bill murray"], 1),
    Question("What is the highest-grossing R-rated movie of all time? >", ["joker"], 1),
    Question("What 1994 crime film revitalized John Travolta's career? >", ["pulp fiction"], 1),
    Question("Who voiced the sultry Jessica Rabbit in Who's Afraid of Roger Rabbit? >", ["kathleen turner"], 1),
    Question("What is the name of Quint's shark-hunting boat in Jaws? >", ["the orca"], 1),
]
computers = [
    Question("When was the first computer invented? >", ["1943"], 1),
    Question("Who is known as the father of computers? >", ["charles babbage"], 1),
    Question("What was the first computer system that used color display? >", ["apple 1"], 1),
    Question("When was the first 1 GB disk drive released in the world? >", ["1980"], 1),
    Question("What was the name of the first computer programmer? >", ["ada lovelace"], 1),
    Question("Which popular company designed the first CPU? >", ["intel", "intel corporations"], 1),
    Question("What does 'CD-ROM' stand for? >", ["compact disc read only memory", "compact disc read-only memory"], 1),
    Question("Which computer hardware device performs the functions like click, point, drag, or select. >", ["mouse"], 1),
    Question("What is the computer's main circuit board called? >", ["motherboard", "mother board"], 1),
    Question("What is the name of the system that manages and programs hardware resources for a computer? >", ["operating system", "os"], 1),
]
math = [
    Question("What is the only number that has the same number of letters as its meaning? >", ["4", "four"], 1),
    Question("What number does not have its own Roman numeral? >", ["zero", "0"], 1),
    Question("What is the only even prime number? >", ["two", "2"], 1),
    Question("What is the smallest perfect number? >", ["six", "6"], 1),
    Question("Is Pi a rational or irrational number? >", ["irrational"], 1),
    Question("Which number is considered a “magic number?” >", ["9", "nine"], 1),
    Question("What is the most popular lucky number? >", ["7", "seven"], 1),
    Question("What is the most popular two-digit number? >", ["13", "thirteen"], 1),
    Question("What are the only prime numbers that end in 2 and 5? >", ["2" + "5", "two" + "five"], 1),
    Question("How many lives are cats said to have? >", ["9", "nine"], 1),
]
instrument = [
    Question("Trumpet players make noise by blowing into what part of the instrument? >", [
             "mouthpiece"], 1),
    Question("How many strings does a bass guitar have? >", ["four", "4"], 1),
    Question("What musical instrument usually has black and white keys, as well as having two or more pedals? >", [
             "piano"], 1),
    Question("How many strings does a guitar have? >", ["six", "6"], 1),
    Question("What kind of guitar doesn't need an amplifier? >",
             ["acoustic"], 1),
    Question("Which member of an orchestra holds a baton? >",
             ["conductor"], 1),
    Question("What is the object that holds music for musicians to read? >", [
             "stand"], 1),
    Question("What do drummers use to hit their drums? >", ["sticks"], 1),
    Question("What kind of band usually performs in parades? >",
             ["marching"], 1),
    Question("What genre of music is popular for improvised solos? >",
             ["jazz"], 1),
]
office = [
    Question("What is the name of the company The Office employees work for? >", [
             "dunder mifflin"], 1),
    Question("What is the company's annual award ceremony called? >",
             ["the dundies"], 1),
    Question("Which character does tons of crosswords during the many meetings? >", [
             "stanley hudson", "stanley"], 1),
    Question("Who are the 3 main members of the Party Planning Committee? >", [
             "pam " + "angela " + "phylis", "angela" + "pam" + "phylis", "pam" + "phylis" + "angela", "angela" + "phylis" + "pam", "phylis" + "pam" + "angela", "phylis" + "pam" + "angela"], 1),
    Question("Who is the regional manager of the Stamford branch? >",
             ["josh porter", "josh"], 1),
    Question("How many episodes in total are there >?",
             ["201", "two hundred and one"], 1),
    Question("What season is Andy first introduced in? >", [
             "3rd season", "the 3rd season", "the third season", "third season", "third", "3rd", "3", "season 3", "season three"], 1),
    Question("In the episode “Christmas Party”, who does Kevin get for Secret Santa? >", [
             "himself", "kevin"], 1),
    Question("While playing who would you do in the office, Michael says he would have sex with which coworker? >", [
             "ryan", "ryan howard"], 1),
    Question("According to Michael, what was the nickname for Phyllis in high school? >", [
             "easy rider"], 1),
]
while True:
    quiz_list = ["The Office", " Instruments",
                 " Math", " Movies", " Music", " Computers"]
    quiz_list.sort()
    quizzes = print(quiz_list)
    playing = input(
        "Type the name of the quiz you'd like to take -- or type 'Q' to quit >").lower()

    if playing == "q":
        break
    print("Okay! Let's Play! :)")
    if playing == "instruments":
        score = 0
        for q in instrument:
            score += ask(q.question, q.answers, q.award)

        print("You got " + str(score) + " questions correct!")
        play_again = input(
            "Would you like to play again? (yes//quit) ").lower()
        if play_again == "yes":
            continue
        elif play_again == "quit":
            quit()
    elif playing == "the office":
        score = 0
        for q in office:
            score += ask(q.question, q.answers, q.award)

        print("You got " + str(score) + " questions correct!")
        play_again = input(
            "Would you like to play again? (yes//quit) ").lower()
        if play_again == "yes":
            continue
        elif play_again == "quit":
            quit()
    elif playing == "math":
        score = 0
        for q in math:
            score += ask(q.question, q.answers, q.award)

        print("You got " + str(score) + " questions correct!")
        play_again = input(
            "Would you like to play again? (yes//quit) ").lower()
        if play_again == "yes":
            continue
        elif play_again == "quit":
            quit()
    elif playing == "movies":
        score = 0
        for q in movies:
            score += ask(q.question, q.answers, q.award)

        print("You got " + str(score) + " questions correct!")
        play_again = input(
            "Would you like to play again? (yes//quit) ").lower()
        if play_again == "yes":
            continue
        elif play_again == "quit":
            quit()
    elif playing == "music":
        score = 0
        for q in music:
            score += ask(q.question, q.answers, q.award)

        print("You got " + str(score) + " questions correct!")
        play_again = input(
            "Would you like to play again? (yes//quit) ").lower()
        if play_again == "yes":
            continue
        elif play_again == "quit":
            quit()
    elif playing == "computers":
        score = 0
        for q in computers:
            score += ask(q.question, q.answers, q.award)

        print("You got " + str(score) + " questions correct!")
        play_again = input(
            "Would you like to play again? (yes//quit) ").lower()
        if play_again == "yes":
            continue
        elif play_again == "quit":
            quit()

#print("You got " + str(score) + " questions correct!")
#print("You got " + str((score/10) * 100) + "%.")
#play_again = input("To play again, tell me what is 2+2? ")
#answer = add(2, 2)
