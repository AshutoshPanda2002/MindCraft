# Zero-Shot Text Classification for Battle NPC Commands.

# Importing the pipeline function from the transformers library
from transformers import pipeline

# Creating a zero-shot classification pipeline
classifier = pipeline("zero-shot-classification")

# Defining a battle_npc class
class battle_npc:

    # Initializing the class
    def __init__(self) -> None:
        pass

    # Defining a command method that takes a command string as input
    def command(self, command: str):
        # Defining the candidate labels for classification
        candidate_labels = ["Attack", "Follow Me", "Fallback"]
        # Using the zero-shot classification pipeline to classify the command
        action = classifier(command, candidate_labels)
        # Extracting the labels and scores from the classification result
        labels = action['labels']
        scores = action['scores']
        # Finding the index of the maximum score
        max_score_index = scores.index(max(scores))
        # Getting the label with the maximum score
        label = labels[max_score_index]
        # Returning the label with the maximum score
        return label
    
# Example Usage

# from Battle_NPC import battle_npc
# Alex = battle_npc()
# label = Alex.command("Destroy that man for me!")
# print(label)