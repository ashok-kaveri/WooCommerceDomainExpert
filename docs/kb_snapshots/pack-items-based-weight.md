# How to Pack Items Based on Weight?

**Source:** https://www.pluginhive.com/knowledge-base/pack-items-based-weight/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# How to Pack Items Based on Weight?

Shipping costs have historically been calculated on the basis of gross weight in Kilograms or pounds. To get real-time rates based on weight, select Parcel Packing Method as **Weight based** in the plugin Admin Settings. All orders above the Maximum weight limit will be split into several packages so that the weight of each package is below the limit.

The **[WooCommerce FedEx Shipping plugin](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** calculates shipping charges for each package and then adds them together to get the total order shipping cost. You can also choose to pack either the heaviest or lightest item first according to your need. The plugin also provides you option of packing the item(s) where you want to divide the weight of item equally in each pack.

While using **Weight based** option, make sure that you have set accurate weights for your products. If you need to do this now, go to your Products page and click on each product, in turn, to set the weight as shown below:

Product Page

* * *

The Admin settings for weight based packing are as shown below:

Weight-Based Settings

* * *

  1. **Parcel Packing Method** : If you wish to pack items according to their weight, select Weight based option.
  2. **Box Maximum Weight** : The weight limit do not limit the total order weight, but the weight of one shipping package. All orders above the Maximum weight will be split into several packages so that the weight of each package is below the maximum limit. Enter the Box Maximum Weight according to your business need.
  3. **Packing Process** : Plugin enables you to pack heavier items first or lighter items first. Also, you can pack the item(s) which are divided equally by weight. According to your business need, you can select the option from the available options.
     * Pack heavier items first
     * Pack lighter item first
     * Pack purely divided by weight

* * *

**Option 1:** **Pack heavier items first**

Among the Order items, the heaviest item is considered first for packing. All orders above the Maximum weight will be split into several packages so that the weight of each package is below the maximum limit. Let’s understand all the options through examples.

For the first two options(pack heavier items first and pack lighter items first), Suppose online store has seven product and you are adding all seven to your cart. Here is the list of items and their corresponding weights are as given below:

**Item name**| **Weight of the Item(lb)**  
---|---  
Gift1| 6  
Gift2| 1  
Gift3| 8  
Gift4| 2  
Gift5| 15  
Gift6| 3  
Gift7| 10  
  
* * *

The cart appears as shown below:

Cart

* * *

Items get packed into four boxes. You can see it on the **Edit Order** page as shown below:

Edit Order page

* * *

The content of all four boxes are as shown below:

Box Name| Item name| Weight of Items(lbs)  
---|---|---  
Pack1| Gift7, Gift4| 10 + 2  
Pack2| Gift3,Gift6,Gift2| 8+3+1  
Pack3| Gift1| 6  
Pack4| Gift5 packed individually since it weighs more than 12 lbs(maximum weight limit)| 15  
  
* * *

**Option 2: Pack lighter item first**

Among the Order items, the lightest item is considered first for packing. All orders above the Maximum weight will be split into several packages so that the weight of each package is below the maximum limit.  
For Example: Suppose, the order contains seven items( same as option 1). The cart appears as shown below:

Cart

* * *

Items get packed into four boxes. You can see it on the Edit Order page as shown below:

Edit Order Page

* * *

The content of all four boxes are as shown below:

Box Name| Item name| Weight of Items(lbs)  
---|---|---  
Pack1| Gift2,Gift4,Gift6,Gift1| 1+2+3+6  
Pack2| Gift3| 8  
Pack3| Gift7| 10  
Pack4| Gift5 packed individually since it weighs more than 12 lbs(maximum weight limit)| 15  
  
* * *

**Option 3: Pack purely divided by weight**

Total weight of the cart is divided by the maximum weight allowed for the box. All orders above the Maximum weight will be split into several packages so that the weight of each package is below the maximum limit. This option is most useful when you are trying to pack an item with a particular weight into different packs.

For example, a customer has ordered 3 units of cotton. Each unit consists of 15 lbs of cotton and so the total order is of 45 lbs. With this option, you can pack cotton into 4 packs (12 lbs maximum weight limit).

Cart

* * *

The item gets packed into four boxes. You can see it on the Edit Order page as shown below:

Edit Order Page

* * *

The content of all four boxes are as shown below:

Box Name| Item name| Weight of Items(lbs)  
---|---|---  
Pack1| Cotton| First 12 lbs  
Pack2| Cotton| Second 12 lbs  
Pack3| Cotton| third 12 lbs  
Pack4| Cotton| remaining 9 lbs  
  
[ Previous  Adjust WooCommerce FedEx Shipping Rates by Shipping Class  ](https://www.pluginhive.com/knowledge-base/woocommerce-shipping-fedex-live-rate-adjustment-based-on-shipping-classes/)

[ Next  How to troubleshoot WooCommerce FedEx Shipping Plugin  ](https://www.pluginhive.com/knowledge-base/troubleshooting-woocommerce-fedex-shipping-plugin/)
