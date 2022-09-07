from django.db import models
# Create your models here.
class tbl_account(models.Model):
    account_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    role = models.CharField(max_length=40)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    class Meta:
        db_table = "tbl_account"
class tbl_idgen(models.Model):
    account_id = models.IntegerField()
    parent_id = models.IntegerField()
    student_id = models.IntegerField()
    complaint_id = models.IntegerField()
    action_id = models.IntegerField()
    policeaction_id = models.IntegerField()
    welfareaction_id = models.IntegerField()
    awareness_id = models.IntegerField()
    notification_id = models.IntegerField()
    complaints_id = models.IntegerField()
    class Meta:
        db_table = "tbl_idgen"
class tbl_complaint(models.Model):
    complaint_id = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    student_id = models.CharField(max_length=30)
    complaint = models.CharField(max_length=40)
    complaint_dt = models.CharField(max_length=30)
    accused = models.CharField(max_length=30)
    accused_dt = models.CharField(max_length=30)
    remarks = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    
    class Meta:
        db_table = "tbl_complaint"
class tbl_complaint1(models.Model):
    complaints_id = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    student_id = models.CharField(max_length=30)
    complaint = models.CharField(max_length=40)
    complaint_dt = models.CharField(max_length=30)
    accused = models.CharField(max_length=30)
    accused_dt = models.CharField(max_length=30)
    remarks = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    
    class Meta:
        db_table = "tbl_complaint1"
class tbl_action(models.Model):
    action_id = models.CharField(max_length=30)
    complaint_id = models.CharField(max_length=30)
    views = models.CharField(max_length=30)
    suggestions = models.CharField(max_length=40)
    actiondetails = models.CharField(max_length=30)
    redirectedTo = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    
    class Meta:
        db_table = "tbl_action"
class tbl_policeaction(models.Model):
    policeaction_id = models.CharField(max_length=30)
    account_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    complaint_id = models.CharField(max_length=30)
    remarks = models.CharField(max_length=30)
    action = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    
    class Meta:
        db_table = "tbl_policeaction"
class tbl_welfareactn(models.Model):
    welfareaction_id = models.CharField(max_length=30)
    account_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    complaint_id = models.CharField(max_length=30)
    remarks = models.CharField(max_length=30)
    action = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    class Meta:
        db_table = "tbl_welfareactn"

class tbl_parentreg(models.Model):
    parent_id = models.CharField(max_length=30)
    student_id = models.CharField(max_length=30)
    reg_no = models.CharField(max_length=40)
    parent_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    class Meta:
        db_table = "tbl_parentreg"

class tbl_studentreg(models.Model):
    student_id = models.CharField(max_length=30)
    reg_no = models.CharField(max_length=40)
    student_name = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    semester = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    class Meta:
        db_table = "tbl_studentreg"
class tbl_login(models.Model):
    user_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    class Meta:
        db_table = "tbl_login"
class tbl_notification(models.Model):
    notification_id = models.CharField(max_length=30)
    notification = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    class Meta:
        db_table = "tbl_notification"
class tbl_awareness(models.Model):
    awareness_id = models.CharField(max_length=30)
    awareness_news = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    class Meta:
        db_table = "tbl_awareness"