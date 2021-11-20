from django.db import models
# Create your models here.
class biddoc(models.Model):
    denial_of_val   =models.IntegerField(verbose_name="Denial of Validity")
    init_price      =models.FloatField(verbose_name="Initial Price")
    deadline        =models.DateTimeField(verbose_name="Deadline")
    #new
    #bidcount:-The number of bids that have been placed for the auction.
    bidCount        =models.IntegerField(verbose_name="Bid Count") 
    #HighBidder:- Indicates if the buyer is the highest bidder.
    highBidder      =models.BooleanField(default=False,verbose_name="High Bidder")
    #An enumeration value that represents the current state of the auction, such as ACTIVE or ENDED.
    auctionStatus   =models.BooleanField(default=True,verbose_name="Auction Status") #True for active , false for Ended
    bid_doc_created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    def __str__ (self):
        return self.deadline

    def get_absolute_url(self):
            return f'/{self.slug}/'

    class Meta:
        ordering = ('deadline',)
    
