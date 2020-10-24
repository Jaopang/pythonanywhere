from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.question_text}'

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField(default=0)
    offer = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.name} - {self.img} - {self.price} - {self.offer} '

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question.question_text} - {self.choice_text} - {self.votes}'

class Oxestype(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.text}'

class Oxes(models.Model):
    Oxes_type = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price= models.IntegerField(default=0)

    def __str__(self):
        return f'{self.Oxes_type.text} - {self.name} - {self.price} price '