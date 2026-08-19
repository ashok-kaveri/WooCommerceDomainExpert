# UPS Packaging Charges with WooCommerce UPS Shipping Plugin

**Source:** https://www.pluginhive.com/knowledge-base/understanding-wordpress-ups-shipping-charges/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# UPS Packaging Charges with WooCommerce UPS Shipping Plugin

This article focuses on the various UPS package options, helping WooCommerce store owners understand how UPS box packaging calculations work. As a result, they can easily find the most cost-effective and efficient way to ship products worldwide using the [**WooCommerce UPS Shipping plugin.**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)

* * *

## **An Overview**

Shipping customers’ orders has become one of the most important aspects for WooCommerce store owners for quite some time now. Among all other processes involved in shipping, product packaging still seems a bit confusing for some store owners. This has made it very difficult for them to determine the accurate package and shipping cost based on their business needs.

* * *

## Manual Packaging Process

The basic aspect of packaging is the dimensions of the parcel. In the case of manual packaging, the idea is to manually measure the dimensions. Only then will the package be ready for shipment in a box. The other aspect is the weight of the whole package, including the box. Most of the shipping services work on the basis of weight. They have their charges based on the package weight.

So you can imagine the pain of manually measuring the dimensions of the package and then putting it in a suitable box. And when you think that the work is done, then again you have to weigh the whole parcel.

So overall, the idea of manual packing is like a nightmare to all online store owners.

But in WordPress, managing WooCommerce shipping is an easy task. Especially with our [**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)**.** It provides store owners with all the shipping methods offered by UPS, along with automatic rate calculations and label generation.

To further understand the concept of packaging and shipping, first, let us see how the shipping charges are actually calculated in UPS.

* * *

## How are the packing charges calculated?

Here are some things to keep in mind about the UPS shipping charges calculation:

  * The UPS parcel is based on the dimensions (length, breadth, height). Hence the package is prepared on the basis of volume (Length*Breadth*Height). The box that will be able to accommodate the required volume, will be used for shipping.
  * If multiple items need to be packed, the system will first look for a box that can hold 100% of the items. If no such box is available, it will choose the box that can accommodate the highest percentage of the items. In the second scenario, if there are two or more boxes that cannot hold all the items, the one that can hold the larger portion will be selected. The remaining items will then go through the same selection process again until all items are packed.
  * If there is a single product that is ready for shipping. But unfortunately, no custom box is big enough to accommodate it, then that item will be shipped individually.

These are the basis of package charging. But sometimes store owners may want to add additional charges or handling charges based on product dimensions and weight.

* * *

## Adding Handling charges using the WooCommerce UPS Shipping plugin

The WooCommerce UPS Shipping plugin lets store owners add additional handling charges from within the store. All you need to do is add these charges while selecting the UPS shipping method.

The screenshot below will show where and how these additional charges can be added:

* * *

### Price Adjustment by Value

Use this option to add a fixed amount to the shipping cost returned by the UPS API. This value will be added on top of the real-time rates, allowing you to cover additional handling or packaging charges.

**Example:****  
**If the UPS rate is $10 and you set a price adjustment of**$2** , the customer will see **$12** as the shipping cost.

* * *

### Price Adjustment by Percentage

Use this option to increase or decrease the UPS shipping cost by a certain percentage. This is helpful if you want to apply a uniform markup or discount across all shipping services.

**Example:****  
**If the UPS rate is $10 and you set a price adjustment of**10%** , the customer will see **$11** as the shipping cost.

The final shipping charges are fetched in real time from the UPS API and will be displayed to customers on the **Cart** or **Checkout** page.

* * *

**Note:**   
You can also enter a negative value for the price adjustment if you want to offer a discount on the shipping rate.

* * *

Now that you have understood the essence of the shipping charges calculation, here is a live scenario where a smart decision on the store owner’s part allowed his customers to save a lot of money over shipping.

* * *

### UPS Packaging Parameters

As a shipping service, UPS provides these two parameters when it comes to packaging and rate calculations:

  * **Weight**
  * **Dimensions**

UPS shipping services are subjected to the weight and physical dimensions of the package. Based on your region you can choose the unit of the above-mentioned parameters. You can manually select the unit using the WooCommerce UPS Shipping plugin.

The image below shows the unit options UPS Shipping plugin provides:

* * *

### UPS Parcel Packaging Methods

WooCommerce UPS Shipping plugin provides three parcel packaging methods which you can choose from the settings.

* * *

#### 1\. Default: Pack Items Individually

In this method, each item in the cart is treated as a separate package.  
Shipping rates are calculated for each item individually, based on its weight and dimensions.

#### 2\. Recommended: Pack into Boxes with Weights and Dimensions

This method is ideal for accurate rate calculation. Where most efficient boxes will be selected based on the Packing algorithm. This method uses the box dimensions and maximum package weight that can be shipped in a particular box. If a box is not able to accommodate the items, then another box is used and the charges are added to the total shipping cost accordingly.

#### 3\. Weight-Based: Calculate Shipping Based on Order Total Weight

With this method, The defined weight of the total package will determine the number of boxes used. If the weight exceeds the specified one, another box will be used for packaging. The weight-based shipping cost will be available to the customers in the cart.

* * *

### Box-Packaging in UPS Shipping

With the help of the WooCommerce UPS Shipping plugin, store owners can choose their **custom box** dimensions and weight limits. They can add these custom boxes and modify the weight and dimension limits from the plugin settings. The below screenshot displays two custom boxes with different weight capacities and dimensions.

Using custom boxes, store owners can save a lot of money as they can specify the dimensions which have the least space wastage. It is very useful in packing multiple items too, as the owner can specify the weight limit that he needs for the whole package.

Now you might be wondering about these dimensions mentioned in the image above.

  * **Outer dimensions** : The outer dimensions are the dimensions of the parcel. These dimensions are passed to the API and are then sent to the UPS.  

  * **Inner dimensions** : These are the package dimensions. These dimensions are the maximum dimensions that the item should have. Otherwise, the box will not be able to contain the product.  

  * **Box weight** : This is the weight of the parcel.  

  * **Max weight** : It is the combined weight of the package. It contains both the weight of the product as well as the box.  

  * **Max Quantity** : You can mention the maximum number of products that can fit into the box.

* * *

### A Live scenario using WooCommerce UPS Shipping plugin

Lets say, Steve runs a growing online sandal shop based in United State. With a loyal customer base across the U.S., he wanted to offer fast and reliable delivery options to keep his customers happy. That’s why he chose UPS services like **Next Day Air Early** , **Next Day Air** , **Next Day Air Saver** , and **UPS Ground** etc for his domestic shipments.

Being a medium-scale business owner, Steve knew that shipping costs could quickly eat into his profits if not managed well. So, he took some time to explore the settings in the [**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)—and made two smart changes:

  * First, he **added handling charges** to cover packaging and processing expenses.  

  * Then, he **switched the parcel packing method** from “Pack items individually” to “Custom box packing.”  

Soon after, Steve received an order for three different sandals. Earlier, using the individual packing method, the shipping charges were quite high. But after switching to a custom delivery box that could fit all three items, he noticed a **significant drop in shipping costs**.

So when generally the order comes for a single product, the delivery charges are shown as:

* * *

Steve had chosen to ship each item individually. When he checked rates for 3 quantity using this method, here’s what he got:

But Steve had one more way to decrease the shipping charges for his customers. **Box Packaging** saves a lot of money when it comes to multiple products. So all Steve had to do was configure the [WooCommerce UPS Shipping plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) and add a **Custom Delivery Box** which can contain three products.

This is what happened after adding a Custom Delivery Box:

* * *

So as you can see, the delivery charges are almost half and in some cases one-third of the earlier charges. This can be a game-changer, especially for small and medium business owners. If they know how the delivery charges are calculated and how they can configure UPS packaging to decrease the shipping charges drastically.

This was all about how the charges are calculated and how smartly you can optimize the shipping charges using the [WooCommerce UPS Shipping plugin.](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)

* * *

## Conclusion

The WooCommerce UPS Shipping plugin helps store owners reduce shipping costs by offering smart packaging options, accurate rate calculations, and the ability to add handling charges. By selecting the appropriate packaging type based on your business needs, you can significantly lower shipping rates. With the right setup, store owners can ship more efficiently and provide better value to their customers.  

  

## 

[ Previous  UPS Boxes for WooCommerce Shipping  ](https://www.pluginhive.com/knowledge-base/woocommerce-ups-shipping-boxes/)

[ Next  Auto-Print WooCommerce Shipping Labels for UPS Shipments  ](https://www.pluginhive.com/knowledge-base/automatic-print-shipping-label-woocommerce-ups-plugin/)
