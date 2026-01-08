questions = [
  ["Who is Shah Rukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 2],
  ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
  ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
  ["Who developed the theory of relativity?", "Isaac Newton", "Albert Einstein", "Nikola Tesla", "Galileo Galilei", 2],
  ["Which gas do humans need to breathe in order to survive?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Helium", 1],
  ["In computing, what does 'CPU' stand for?", "Central Processing Unit", "Computer Personal Unit", "Central Power Utility", "Control Process Unit", 1],
  ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 3],
  ["Which is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean", 3],
  ["What is H2O commonly known as?", "Salt", "Hydrogen", "Water", "Oxygen", 3],
  ["Which programming language is known for its snake logo?", "C++", "Python", "Java", "Ruby", 2],
  ["Which company created the iPhone?", "Samsung", "Apple", "Microsoft", "Google", 2]
]

prizes = [10000, 32000, 40000, 50000, 100000, 200000, 300000, 400000, 500000, 600000, 100000]

i = 0

for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    
    # Check whether the answer is correct or not
    a = int(input("Enter Your Answer: 1 for A, 2 for B, 3 for C, 4 for D\n"))
    if(question[5] == a):
        print("Correct Answer")
    else:
        print(f"Incorrect, the Correct Answer was {question[5]}")
        print("Better luck Next Time!")
        break
    
    print(f"You won {prizes[i]}!")
    i += 1
