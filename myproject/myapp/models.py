from django.db import models

class test_Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Pathology_Test(models.Model):
    id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=100)
    category = models.ForeignKey(test_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.test_name

class Pathology_Test_Master(models.Model):
    id = models.AutoField(primary_key=True)
    test = models.ForeignKey(Pathology_Test, on_delete=models.CASCADE)
    parameter = models.TextField()
    expected_result = models.CharField(max_length=100)
    result_unit = models.CharField(max_length=100)

    def __str__(self):
        return self.test.test_name