from django.db import models

# Create your models here.

class Dojo(models.Model):
    name = models.CharField(max_length = 45)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now  = True)

# Seattle = Dojo.objects.create(
#     name = 'Dojo Seattle',
#     city = 'Seattle',
#     state = 'WA',
# )

# Dallas = Dojo.objects.create(
#     name = 'Dojo Dallas',
#     city = 'Dallas',
#     state = 'TX',
# )

# Los_Angeles = Dojo.objects.create(
#     name = 'Dojo Los Angeles',
#     city = 'Los Angeles',
#     state = 'CA',
# )

# Chicago = Dojo.objects.create(
#     name = 'Dojo Chicago',
#     city = 'Chicago',
#     state = 'IL',
# )

# Arlington = Dojo.objects.create(
#     name = 'Dojo Arlington',
#     city = 'Arlington',
#     state = 'VA',
# )

class Ninja(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    dojo = models.ForeignKey(Dojo, related_name = 'ninjas', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now  = True)


# Judge = Ninja.objects.create(
#     first_name = 'Judge'
#     last_name = 'Smith'
#     dojo = Dojo.objects.get(id = )
# )

# Gary = Ninja.objects.create(
#     first_name = 'Gary'
#     last_name = 'Holler'
# )

# Michael = Ninja.objects.create(
#     first_name = 'Michael'
#     last_name = 'Stovall'
# )

# Joel = Ninja.objects.create(
#     first_name = 'Joel'
#     last_name = 'Okoh'
# )

# Will = Ninja.objects.create(
#     first_name = 'Will'
#     last_name = 'Draheim'
# )
