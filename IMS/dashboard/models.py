from django.db import models



class Measure(models.Model):

      measure=models.CharField(max_length=100)
      def __str__(self):
          return self.measure




class Inventory(models.Model):
      inventory_category=models.CharField(max_length=250)
      inventory_description=models.CharField(max_length=250)
      measure_Unit = models.ForeignKey(Measure,on_delete=models.CASCADE)
      
      def __str__(self):
          return self.inventory_category


class Purchase(models.Model):
      purchase_date=models.DateField()
      inventory_category=models.ForeignKey(Inventory,on_delete=models.CASCADE)
      frontend_measure=models.ForeignKey(Measure,on_delete=models.CASCADE)
      frontend_quantity = models.IntegerField()
      purchase_price=models.FloatField()
      backend_measure=models.CharField(max_length=100)
      backend_quantity = models.IntegerField()
      
      def __str__(self):
          return str(self.purchase_date)


