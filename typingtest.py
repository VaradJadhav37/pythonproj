import time
import random

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error+=1
    return round(100-((error/len(partest))*100))

def count_words(text):
  return len(text.split())

def speed_time(time_s, time_e, userinput):
  time_delay = time_e - time_s
  words = count_words(userinput)
  speed = round((words / time_delay) * 60)  # Words per minute
  return speed

if __name__ == '__main__':
    while True:
        ck = input("Ready to test? (yes/no): ")
        if ck.lower() == "yes":
            test = [
                "The longest word in the English language is 'pneumonoultramicroscopicsilicovolcanoconiosis'.",
                "The average person falls asleep in seven minutes.",
                "The world's smallest bird is the bee hummingbird.",
                "The first-ever computer bug was an actual bug (a moth) found in a computer.",
                "Bananas are curved because they grow towards the sun.",
                "The human brain generates more electrical activity when asleep than when awake.",
                "Octopuses have three hearts.",
                "A group of jellyfish is called a bloom.",
                "The strongest muscle in the human body is the tongue.",
                "The original name for butterflies was 'flutter-by'.",
                "A snail can sleep for three years.",
                "The Eiffel Tower was originally meant to be temporary.",
                "The first-ever movie ticket cost one penny.",
                "The human body contains enough iron to make a small nail.",
                "The average person laughs about 17 times a day.",
                "The world's largest desert is the Antarctic.",
                "The only animal that can see ultraviolet light is a shrimp.",
                "The first-ever vending machine sold postcards.",
                "The longest recorded flight of a chicken is 13 seconds.",
                "The word 'queue' is the only word in the English language that is spelled the same way backwards.",
                "The human heart beats approximately 100,000 times a day.",
                "The world's largest living organism is a fungus.",
                "A cat has 32 muscles in each ear.",
                "The first-ever mobile phone call was made in 1973.",
                "The average person takes 15,000 steps a day.",
                "The world's deepest ocean is the Pacific.",
                "The human skeleton renews itself every ten years.",
                "The most common bird in the world is the domestic chicken.",
                "The first-ever computer game was called 'Spacewar!'.",
                "A starfish has no brain.",
                "The word 'hippopotamus' means 'river horse'.",
                "The first-ever hamburger was sold in 1904.",
                "The world's largest land animal is the African elephant.",
                "A dog's sense of smell is 1,000 to 10,000 times better than a human's.",
                "The first-ever email was sent in 1971.",
                "The average person spends about two years of their life dreaming.",
                "The world's tallest tree is a redwood.",
                "The first-ever Olympic Games were held in Greece in 776 BC."
            ]

            test1 = random.choice(test)
            print("***Typing Speed***")
            print(test1)
            print()

            start_time = time.time()
            testinput = input("Enter: ")
            end_time = time.time()

            speed = speed_time(start_time, end_time, testinput)
            errors = mistake(test1, testinput)

            print(f"Speed: {speed} w/sec")
            print(f"Accuracy: {errors}%")

        elif ck.lower() == "no":
            print("Thank you!")
            break
        else:
            print("Wrong input!")
