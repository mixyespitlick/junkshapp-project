from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models


class Junkshop(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=200, null=True)
    owner_name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    location = models.PointField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now = True, null=True)

    def to_dict_json(self):
        return {
            'shop_name':self.shop_name,
            'owner_name':self.owner_name,
            'address':self.address,
        }


class Household(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    location = models.PointField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        user = User.objects.get(id=self.user_id)
        return "id=" + str(self.pk) + " username=" + user.username + " email=" + user.email


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
	    return "ID:" + str(self.pk) + " " + self.name


class Item(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
	    return "ID:" + str(self.pk) + " " + self.name


class Auction(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    seller = models.ForeignKey(Household, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
	    return "ID:" + str(self.pk) + " SELLER_ID:" + str(self.seller_id)


class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    bidder = models.ForeignKey(Junkshop, on_delete=models.CASCADE)
    bid_time = models.DateTimeField()

    def __str__(self):
        return "USER_ID:" + str(self.bidder_id) + " AUCTION_ID:" + \
        str(self.auction_id) + " " + str(self.bid_time) 
