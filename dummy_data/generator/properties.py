
import progressbar

from api.models import Property


def generate():
    print(f"Generating properties")
    users_json="234567890-98765"
    for i in progressbar.progressbar(range(10)):
        property_address = "Str Dritan Hoxha" + str(i)
        listing_price = i+2000
        generate_property(property_address,listing_price)

def generate_property(property_address,listing_price):
    property = Property.objects.create(property_address=property_address,listing_price=listing_price)
    property.save()