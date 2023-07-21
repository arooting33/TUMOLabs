
#madlibs 2


def hospital():
    input_prompts_hospital = [
                        "enter number: ", "enter measure of time: ", "enter mode of transporation: ", "enter adjective(feeling): ","enter descriptive adjective: ",
                        "enter noun: ", "enter color: ", "enter part of body: ", "enter verb: ", "enter number: ", "enter noun: ", "enter noun: ", "enter body part: ",
                        "enter verb: ", "enter noun: ", "enter adjective: ", "enter silly word: ", "enter noun: "
                    ]
    user_inputs = []
    for prompt in input_prompts_hospital:
        user_input = input(prompt)
        user_inputs.append(user_input)

    hospital_story = f""" It was about {user_inputs[0]} {user_inputs[1]} ago when I arrived at the hospital in a {user_inputs[2]}. The hospital is a/an {user_inputs[3]} 
        place, there are a lot of {user_inputs[4]} {user_inputs[5]} here. There are nurses here who have {user_inputs[6]} {user_inputs[7]}. If someone wants to 
        come into my room I told them that they have to {user_inputs[8]} first. I’ve decorated my room with {user_inputs[9]} {user_inputs[10]}. Today I talked 
        to a doctor and they were wearing a {user_inputs[11]} on their {user_inputs[12]}. I heard that all doctors {user_inputs[13]} {user_inputs[14]} every day for breakfast. 
        The most {user_inputs[15]} thing about being in the hospital is the {user_inputs[16]} {user_inputs[17]}! """

    print(hospital_story)

def camping():
    input_prompts_camping = ["enter proper noun: ", "enter name", "enter noun(item): ", "enter adjective(feeling): ", "enter verb: ", 
                          "enter adjective(feeling): ", "enter animal: ", "enter verb(activity): ", "enter color: ", 
                          "enter verb(ending in ing): ", "enter adverb(ending in ly): ", "enter number: ", "enter time frame: ", 
                          "enter color: ", "enter animal: ", "enter number: ", "enter silly word: ", "enter noun: "]
    user_inputs = []
    for prompt in input_prompts_camping:
        user_input = input(prompt)
        user_inputs.append(user_input)

    camping_story = f"""This weekend I am going camping with {user_inputs[0]} {user_inputs[1]}. I packed my lantern, sleeping bag, and {user_inputs[2]}. I am so 
          {user_inputs[3]} to {user_inputs[4]} in a tent. I am {user_inputs[5]} we might see a(n) {user_inputs[6]}, I hear they’re kind of dangerous. 
          While we’re camping, we are going to hike, fish, and {user_inputs[7]}. I have heard that the {user_inputs[8]} lake is great for {user_inputs[9]}. 
          Then we will {user_inputs[10]} hike through the forest for {user_inputs[11]} {user_inputs[12]}. If I see a {user_inputs[13]} {user_inputs[14]} while hiking, 
          I am going to bring it home as a pet! At night we will tell {user_inputs[15]} {user_inputs[16]} stories and roast {user_inputs[17]} around the campfire!!"""

    print(camping_story)


def enchanted():
    input_prompts_enchanted = [
                "enter proper noun: ", "enter name", "enter adjective: ", "enter color: ", "enter animal: ", "enter place: ",
                "enter adjective: ", "enter creature(plural): ", "enter adjective: ", "enter creature(plural): ", "enter type of room: ",
                "enter noun: ", "enter noun: ", "enter noun(plural): ", "enter adjective: ", "enter noun: ", "enter number: ",
                "enter time frame: ", "enter verb(ending in ing): ", "enter adjective: ", "enter noun: "
            ]

    user_inputs = []
    for prompt in input_prompts_enchanted:
        user_input = input(prompt)
        user_inputs.append(user_input)

    enchanted_story = f"""Dear {user_inputs[0]} {user_inputs[1]}, I am writing to you from a {user_inputs[2]} castle in an enchanted forest. I found myself here one day after going for 
          a ride on a {user_inputs[3]} {user_inputs[4]} in {user_inputs[5]}. There are {user_inputs[6]} {user_inputs[7]} and {user_inputs[8]} {user_inputs[9]} here! In the 
          {user_inputs[10]} there is a pool full of {user_inputs[11]}. I fall asleep each night on a {user_inputs[12]} of {user_inputs[13]} and dream of {user_inputs[14]} {user_inputs[15]}. 
          It feels as though I have lived here for {user_inputs[16]} {user_inputs[17]}. I hope one day you can visit, although the only way to get here now is 
          {user_inputs[18]} on a {user_inputs[19]} {user_inputs[20]}!!"""

    print(enchanted_story)


def choose_story():
    print("Choose a story to play:")
    print("1. Hospital")
    print("2. Camping")
    print("3. Enchanted")
    
    user_choice = input("Enter the number of the story you want to play: ")

    if user_choice == "1":
        hospital()
    elif user_choice == "2":
        camping()
    elif user_choice == "3":
        enchanted()
    else:
        print("Invalid choice. Please enter a valid number 1, 2, or 3.")

# Call the choose_story() function to start the story selection process
choose_story()
