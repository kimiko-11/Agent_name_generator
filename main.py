import random

name_list = ["Orion", "Barracuda", "Amethyst", "Blade", "Wasp", "Nemesis", "Fury", "Cobra", "Tempest", "Leo", "Scythe"] # Note the order change

agent_names=[]

def passcode_generator():
    for step in name_list:
        a = step


        for step in name_list:
            b = step
            if a != b and (b+" "+a) not in agent_names: # to check for duplicate in reverse order

                c = a + " " + b
                agent_names.append(c)


    for name_pair in agent_names:# for printing names one below the other
        print(name_pair)

passcode_generator()
