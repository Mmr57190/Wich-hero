from django.db import models

class PersonalityTest(models.Model):
    n = models.IntegerField(default=1)
    def __init__(self):
        self.superhero_scores = {
            'Superman': 0,
            'Spiderman': 0,
            'Wonder Woman': 0,
            'Iron Man': 0,
            'Batman': 0,
            'Captain America': 0,
            'Thor': 0,
            'Black Widow': 0,
            'Hawkeye': 0,
            'Black Panther': 0,
            'Captain Marvel': 0,
            'Ant-Man': 0,
            'Doctor Strange': 0,
            'Scarlet Witch': 0,
            'Vision': 0,
            'ArchiMan': 0
        }
    def __str__(self):
        return self.assign_superhero()
    
    def assign_image(self):
        superhero = 'img/' + max(self.superhero_scores, key=self.superhero_scores.get) + '.png'
        return superhero
    
    def img_path(self):
        l = []
        for key in self.superhero_scores:
            l += ['img/' + key + '.png']
        return l

    def all(self):
        return self.superhero_scores

    def assign_superhero(self):
        superhero = max(self.superhero_scores, key=self.superhero_scores.get)
        return superhero
