from django.db import models
from django.contrib.auth.models import User
# TABLE FEEDBACK(FORM_NO INT PRIMARY KEY, PLAYER_ID INT NOT NULL, EMPLOYEE_ID INT, COMMENT VARCHAR(1000) NOT NULL,POSITIVE_NEGATIVE ENUM('P','N') NOT NULL,FOREIGN KEY(PLAYER_ID) REFERENCES PLAYER(ID),FOREIGN KEY(EMPLOYEE_ID) REFERENCES EMPLOYEE(ID));
class feedback(models.Model):
	pn = [('P','POSITIVE'),('N','NEGATIVE')]
	form_no = models.AutoField(primary_key = True)
	player_id = models.ForeignKey(User,default=1, on_delete=models.CASCADE,blank = False)
	#employee_id = models.ForeignKey(User,blank = True)
	comment = models.TextField(max_length=1000, blank = False)
	positive_negative = models.CharField(max_length=1,choices=pn)
	def __str__(self):
		return "Feedback No " + str(self.form_no) + " " + self.comment 

