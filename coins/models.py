from django.db import models


class Coins(models.Model):
    """Model to store the coins."""
    id = models.AutoField(primary_key=True)
    value = models.IntegerField() # bigger coin is 500 Yen min_value=1, max_value=500
    year = models.IntegerField(max_length=4) # period may not go until 100 years but better to take space if we use gregorian year
    period = models.CharField(max_length=5) # usually 2 kanjis but better to take space
    number = models.IntegerField() # how much of this coin we have min_value=0
