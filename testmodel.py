class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max=255)

    class Meta:
        db_table = 'User'


class profile(models.Model):
    first_name = models.OneToOneField(User, primary_key=True)
    last_name = models.OneToOneField(User, primary_key=True)
    email= models.OneToOneField(User, primary_key=True)
    profile_picture= models.ImageField(default="../images/profile.jpg")

    class Meta:
        db_table = 'profiles'


class Category(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField()

    class Meta:
        db_table = 'categories'



class Product(models.Model):
    name = models.CharField(maxlength=45)
    price = models.IntegerField()
    categoryID = models.ManytoManyField(Category)

    class Meta:
        db_table = 'products'
