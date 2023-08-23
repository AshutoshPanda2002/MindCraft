class Character:
    
    def __init__(self, ethnicity: str, age: int, gender: str,
                 personality: str, backstory: str, relations: dict,
                 world_knowledge: str):
        # Run validations to the received arguments
        assert age > 0, f"Age {age} is not greater than zero."
        assert gender == "Male" or gender == "Female", "Gender must be either Male or Female."


        # Assignments to self object
        # self.name = name
        self.ethnicity = ethnicity
        self.age = age
        self.gender = gender
        self.personality = personality
        self.backstory = backstory
        self.relations = relations
        self.world_knowledge = world_knowledge

    def update_knowledge(self, fiction_update):
        self.world_knowledge = self.world_knowledge + " " + fiction_update
        

# Example Usage

# Alex = Character("European", 21, "Male", "Emo", "...", {"Father": "Ben"}, "...")
# Is name required or not?
# print(Alex.gender)
# Alex.update_knowledge("Dead.")