# Name Generator

from pathlib import Path
import random
import importlib.resources

class NameGenerator:
    """
    Randomly generate names using a noun and an adjective. Similar to the names generated in a Kahoot game.
    """
    def __init__(self, noun_file = None, adjective_file = None, seed = None, guarantee_unique = True, nouns_to_add = [], adjectives_to_add = [], generated_names_to_not_use = []):
        """ Constructor
        :param noun_file str: The file with path if necessaary) containing the nouns to be used in generating names. Default to None.
        :param adjective_file str: The file with path if necessaary) containing the adjectives to be used in generating names. Defaults to None.
        :param seed int: The seed for the random number generator used when generating names. Defaults to None for a truly random experience.
        :param guarantee_unique bool: Do not return the same name twice. Defaults to True.
        :param nouns_to_add list: A list of nouns that supplements the nouns in the file specified above. Defaults to None.
        :param adjectives_to_ad listd: A list of adjectives that supplements the adjectives in the file specified above. Defaults to None
        :param generated_names_to_not_use list: A list of names that should not be returned from the generate_name method. Defaults to None.
        """
        #print("__init__")
        self.noun_file = noun_file
        self.adjective_file = adjective_file
        if self.noun_file == None:
            self.noun_file = "nouns.txt"            
        if self.adjective_file == None:
            self.adjective_file = "adjectives.txt"            
        self.nouns = None
        self.adjectives = None
        self.seed = seed
        self.guarantee_unique = guarantee_unique
        self.used_names = set()
        self.nouns_to_add = nouns_to_add
        self.adjectives_to_add = adjectives_to_add
        self.generated_names_to_not_use = generated_names_to_not_use
        self.seed = seed
        self.prepare()


    def read_data(self, file_name):
        data = []
        try:    
            with importlib.resources.open_text("src.data", file_name) as my_file:
                #read text file into list 
                data = my_file.read().split("\n")
        except:
            # Get the path to the current script's directory
            script_dir = Path(__file__).parent
                
            # Combine path and filename
            file_path = script_dir / file_name
                
            with open(file_path, 'r') as my_file:
                data = my_file.read().split("\n")
        return data
    
    def prepare(self):
        """ Set up the name generator. It's called from the constructor or you can call it again to start over.
        :return set: A 2-element set consisting of the lists of nouns and adjectives that will be used when generate_name is called
        """
        #print("prepare")
        if self.seed != None:
            random.seed(self.seed)

        if self.noun_file != None:
            self.nouns = list(self.read_data("nouns.txt"))
            #print("nouns:", self.nouns)
        if self.adjective_file != None:
            self.adjectives = list(self.read_data("adjectives.txt"))
            

        for noun in self.nouns_to_add:
            self.nouns.append(noun)
        for adjective in self.adjectives_to_add:
            self.adjectives.append(adjective)
        return (self.nouns, self.adjectives)

    def get_nouns(self):
        """ Get the nouns that will used to generate random names
        :return list: The list of nouns
        """
        return self.nouns
    
    def get_adjectives(self):
        """ Get the adjectives that will used to generate random names
        :return list: The list of adjectives
        """
        return self.adjectives
    
    def get_used_names(self):
        """ Get the generated names to this point
        :return set: The set of names that have been generated since the object was instantiated or prepare was invoked, whichever happened most recently.
        """
        return self.used_names
    
    def clear_generated_names(self):
        """ Clear the current set of generated names so names can be re-used when generate_name is called
        """
        self.used_names = set()

    def generate_name(self):
        """ Generate a random name
        :return str: the randonly generated name as a String
        """
        
        if len(self.nouns) * len(self.adjectives) == len(self.used_names):
            # Sanity check: are there any names left to generate? 
            print(len(self.nouns), len(self.adjectives), len(self.nouns) * len(self.adjectives), len(self.used_names))
            print("nouns:", self.nouns)
            print("adjectives:", self.adjectives)
            print("used_names:", self.used_names)
            raise RuntimeError('NameGenerator.generate_name: there are no more unused adjective/noun combinations')
        
        while True:
            generated_name = random.choice(self.adjectives) + random.choice(self.nouns)
            if generated_name in self.generated_names_to_not_use:
                continue
            if self.guarantee_unique:
                #print("***" , generatedName)
                if generated_name not in self.used_names:
                    self.used_names.add(generated_name)
                    break
            else:
                break
        return generated_name

    if __name__ == "__main__":
        print("Test main in NameGenerator.py...")
        nouns = []
        with importlib.resources.open_text("src.data", "nouns.txt") as my_file:
            #my_file = open(self.noun_file, 'r')
            #read text file into list 
            nouns = my_file.read().split("\n")
        print("nouns", nouns)    
    