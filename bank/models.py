from django.db import models

# Create your models here.

class Customer(models.Model):
    account_number = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    nid = models.IntegerField()
    f_name = models.CharField(max_length=50)
    m_name = models.CharField(max_length=50)
    
    occupation =  models.CharField(max_length=50)
    email = models.EmailField()
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'others')
    ]

    gender = models.CharField(max_length=1, choices=GENDER, default='M')
    
    ACCOUNT_CHOICE =[
        ('current','current'),
        ('savings','savings'),
    ]
    acc_type = models.CharField(max_length=7, choices=ACCOUNT_CHOICE,default='current')
    mobile_no = models.IntegerField()
    city = models.CharField(max_length=50)
    balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

# class statement(models.Model):
#     account_number = models.PositiveIntegerField(primary_key=True)
#     ACCOUNT_CHOICE =[
#         ('current','current'),
#         ('savings','savings'),
#     ]
#     acc_type = models.CharField(max_length=7, choices=ACCOUNT_CHOICE,default='current')
#     f_date = models.DateField()
#     t_date = models.DateField()

#     def __str__(self):
#         return self.account_number



# class statement(models.Model):
#     account = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     ACCOUNT_CHOICE =[
#         ('current','current'),
#         ('savings','savings'),
#     ]
#     acc_type = models.CharField(max_length=7, choices=ACCOUNT_CHOICE,default='current')
#     date = models.DateField()
#     amount = models.IntegerField()
    