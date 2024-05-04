if __name__ == "__main__":
    # import the copy installed in the local package repository
    #from name_generator_nicomp.NameGenerator import NameGenerator
    
    # Import the copy in this project
    from src.name_generator_nicomp.NameGenerator import NameGenerator

    #print("Name Generator")
    nouns_to_add = ["Turtle", "Alligator"]
    adjectives_to_add = ["Active", "Agorophobic"]
    nameGenerator = NameGenerator(nouns_to_add = nouns_to_add, adjectives_to_add = adjectives_to_add)
    #print(data[0], "\n", data[1])
    num_of_names = 700
    generated_names = set()
    print("__str__():", nameGenerator.__str__())
    print("Generating", num_of_names, "random names...")
    for i in range(0, num_of_names):
        generated_names.add(nameGenerator.generate_name())
                            
    print(num_of_names, "names generated")
 
    print("Scanning for an added name used in a genrated name...")
    for noun in nouns_to_add:
        print("\t","Scanning for", noun)
        while True:
            name = nameGenerator.generate_name()
            if name.endswith(noun):
                print("\t\t",name)
                break
    print("Scanning for an added adjective used in a genrated name...")
    for adjective in adjectives_to_add:
        print("\t","Scanning for", adjective)
        while True:
            name = nameGenerator.generate_name()
            if name.startswith(adjective):
                print("\t\t",name)
                break
    print("__str__():", nameGenerator.__str__())
    print("one more name:", nameGenerator.generate_name())
    print("__str__():", nameGenerator.__str__())
