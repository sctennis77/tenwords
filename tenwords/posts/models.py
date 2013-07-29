from django.db import models

# Create your models here.


class Entry(models.Model):
	"""class to store user entries,
	text = what the user entered,
	emotion = the selected emotion
	numwords = how many words the text is (max = 10)
	posted = date entry created
	updatd = last updated date"""
	
	text = models.TextField(max_length=None)
	emotion = models.CharField(max_length=20)
	posted = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		uni_str = "text: {0}\nemotion: {1}\nposted: {2}\n".format(self.text,self.emotion,str(self.posted))
		return uni_str
