# Zero-Shot Text Classification for Battle NPC Commands.

from transformers import pipeline
classifier = pipeline("zero-shot-classification")

class battle_npc:

    def __init__(self) -> None:
        pass

    def command(self, command: str):
        candidate_labels = ["Attack", "Follow Me", "Fallback"]
        label = classifier(command, candidate_labels)
        return label