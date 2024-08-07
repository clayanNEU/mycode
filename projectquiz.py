#!/usr/bin/python3
# city to live in

def city_quiz():
    print("Welcome to the quiz")
    print("where are you thinking about visting and staying?")

    # city scores all start at 0
    nyc_score = 0
    sf_score = 0
    chicago_score = 0
    miami_score = 0
    austin_score = 0

    # questions and choices mixed
    questions = [
        {
            "question": "What type of weather do you prefer?",
            "choices": [
                "A. Cold winters and hot summers",
                "B. Mild and foggy",
                "C. Cold winters and mild summers",
                "D. Hot and sunny year-round",
                "E. Warm and sunny with occasional rain"
            ],
            "scores": {
                "A": "chicago",
                "B": "sf",
                "C": "nyc",
                "D": "miami",
                "E": "austin"
            }
        },
        {
            "question": "What is your ideal weekend activity?",
            "choices": [
                "A. Attending Broadway shows or exploring museums",
                "B. Visiting tech expos or hiking in nature",
                "C. Exploring diverse culinary scenes and festivals",
                "D. Going to the beach and enjoying nightlife",
                "E. Enjoying live music and food trucks"
            ],
            "scores": {
                "A": "nyc",
                "B": "sf",
                "C": "chicago",
                "D": "miami",
                "E": "austin"
            }
        },
        {
            "question": "What is your preferred mode of transportation?",
            "choices": [
                "A. Subway and public transport",
                "B. Biking or electric scooters",
                "C. Walking and public transport",
                "D. Driving or rideshares",
                "E. Walking and cycling"
            ],
            "scores": {
                "A": "nyc",
                "B": "sf",
                "C": "chicago",
                "D": "miami",
                "E": "austin"
            }
        },
        {
            "question": "What kind of job market appeals to you?",
            "choices": [
                "A. Finance and media",
                "B. Technology and startups",
                "C. Diverse industries including tech and manufacturing",
                "D. Hospitality and tourism",
                "E. Technology and creative industries"
            ],
            "scores": {
                "A": "nyc",
                "B": "sf",
                "C": "chicago",
                "D": "miami",
                "E": "austin"
            }
        },
        {
            "question": "How important is nightlife to you?",
            "choices": [
                "A. Very important, I love vibrant nightlife",
                "B. Somewhat important, I enjoy occasional outings",
                "C. I prefer cultural events over nightlife",
                "D. Extremely important, I live for the nightlife",
                "E. I like relaxed venues with live music"
            ],
            "scores": {
                "A": "nyc",
                "B": "sf",
                "C": "chicago",
                "D": "miami",
                "E": "austin"
            }
        }
    ]

    # question index
    index = 0
    #loop now
    while index < len(questions):
        q = questions[index]
        #print question
        print(q["question"])
        # for each choice in choice
        for choice in q["choices"]:
            print(choice)

        # get user input and clean
        answer = input("Choose an option (A, B, C, D, E): ").strip().upper()

        if answer in q["scores"]:
            #increment
            if q["scores"][answer] == "nyc":
                nyc_score += 1
            elif q["scores"][answer] == "sf":
                sf_score += 1
            elif q["scores"][answer] == "chicago":
                chicago_score += 1
            elif q["scores"][answer] == "miami":
                miami_score += 1
            elif q["scores"][answer] == "austin":
                austin_score += 1

            # move to next question
            index += 1
        else:
            print("Invalid choice, enter A, B, C, D, or E.\n")



    # determine scores
    max_score = max(nyc_score, sf_score, chicago_score, miami_score)
    if nyc_score > max_score:
        result = "New York City"
    elif sf_score > max_score:
        result = "San Francisco"
    elif chicago_score > max_score:
        result = "Chicago"
    elif miami_score > max_score:
        result = "Miami"
    elif austin_score > max_score:
        result = "Austin"
    else:
        result = "a different city may suit you"
    print(f"\nBased on your answer, {result} is the best pick!")

#run it
city_quiz()
