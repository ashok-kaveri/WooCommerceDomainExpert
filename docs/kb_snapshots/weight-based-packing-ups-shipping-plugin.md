# Weight-based Packing with WooCommerce UPS Shipping plugin

**Source:** https://www.pluginhive.com/knowledge-base/weight-based-packing-ups-shipping-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Weight-based Packing with WooCommerce UPS Shipping plugin

In this article, we will discuss one of the most important features of the **[WooCommerce UPS Shipping Plugin with Print Label](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)** , which is, the weight-based parcel packing method. Read below to know more about it.

Sometimes, **[WooCommerce store](https://www.pluginhive.com/woocommerce-tutorial-for-novice/)** owners come up with a special scenario that needs something different from the usual. Such was the case with one of our customers, who wanted the plugin to calculate the shipping rates based on the billable weight of the package.

According to the customer,

> _**I want the plugin to calculate the rates based on the billable weight of the package ONLY. As most of the time my products don’t have dimensions, so I would prefer a method where charges will be calculated based on the total weight of the package instead of the dimensions like height, length and breadth.**_

[**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) is the most suitable option in cases like these. But before we discuss the weight-based packing, let’s get to know about the plugin in brief.

* * *

## WooCommerce UPS Shipping Plugin

**[WooCommerce UPS Shipping plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)** is the #1 UPS shipping plugin that has the capability to automate the whole shipping process. This plugin offers WooComerce store owners to get real-time UPS shipping rates for domestic as well as international shipments. Besides this, the plugin offers advanced features such as bulk shipping label creation, shipment tracking across the globe, the ability to adjust shipping rates, etc. If you want to check out the whole list of features this plugin provides, kindly visit the [****](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)**[**UPS Plugin and Its Features**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)**.

In this article, we will be discussing the UPS **Weight Based** parcel packing method in detail.

* * *

## Weight-Based Parcel Packing

[**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) allows store owners to pack their products based on weight. This way, the products that do not have dimensions can be packed easily.

To set up weight-based shipping, go to **UPS Plugin Settings > Packaging**, then select **“Weight based: Calculate shipping on the basis of order weight”** from the Parcel Packing dropdown. 

On selecting the weight-based packing, you will be required to select among the following options for optimized packing.

* * *

### **Box Weight:**

Enter the weight of an empty box to include it in the total shipping weight.

* * *

### **Max Package Weight**

The plugin allows you to set up a Max Package Weight value. This allows store owners to pack up to that value in a single package. The image below shows the option to add a Max Package Weight value in the plugin settings.

The image above shows the Max Package Weight set at 10 lbs. Hence, all the products up to 10 lbs, you can pack in one package. If the total weight of all the products increases beyond 10 lbs, the additional products will be added to the new package.

* * *

### **Max Package Quantity:**

Limit the number of items per package if needed. Leave blank to pack based only on weight.

The image above shows that the Max Package Quantity is set to be 2. This will make sure that only 2 quantities of the product can be packed into a single box.

For Example, if **Max Package Weight** is set to **10 lbs** and **Max Package Quantity** is set to **2** , and a customer orders:

  * Product A – 2 lbs
  * Product B – 3 lbs
  * Product C – 4 lbs

Even though the total weight is just **9 lbs** , the plugin will create **two packages** :

  * **Package 1** : Product A + Product B
  * **Package 2** : Product C

This happens because only **2 items are allowed per package** , regardless of weight.

* * *

### **Packing Process**

**[WooCommerce UPS Shipping Plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)** also supports some of the predefined packing processes which you can select in the plugin settings. The image below will show you where you can select one of the processes to help you pack your products.

Now, let us discuss these processes in brief.

#### **Pack Heavier Items First**

To understand these packing processes, let us take a real-life example. There are three types of products in a shop. **Product A (3 lbs), Product B (2 lbs), Product C (6 lbs).** Now, based on the weight-based packing, we have set the Max Weight as 10 lbs. So based on this packing process, the products will be packed as shown in the following image.

  * **Box A – Product C (6 lbs) + Product A (3 lbs) = Total of 9 lbs**
  * **Box B – Product B (2 lbs) = Total of 2 lbs**

You can easily make out that this process packs the heavy products in the box until the box is either filled or the remaining products can no longer fit into the box. And once the Max Weight is reached, it packs the remaining products into another box.

#### **Pack Lighter Item First**

In contrast to the previous packing process, this way the lighter products are packed first till the Max Weight is reached or a product can no longer fit into the box. And once the Max Weight is reached, it takes another box to pack the remaining products. So the same scenario will be different while using this packing process. The image below shows the packages created using this process.

  * **Box A – Product B (2 lbs) + Product A (3 lbs) = Total of 5 lbs**
  * **Box B – Product C (6 lbs) = Total of 6 lbs**

#### **Purely Divided By Weight**

This packing process is different from the other two processes. Packing using this process involves separating and then packing different products having the same weight together. In simple words, all the products with the same weight will be packed in one box until the weight limit reaches.

For example, consider there are 2 of Product A (2 lbs), 3 of Product B (3 lbs) and 1 Product C (6 lbs) in one orders. Using this process, all the products with similar weight will be packed in one box. The image shows the products packed based on their weight.

  * Box A – 2 x Product A (2 lbs) = Total 4 lbs

But since the package can still contain an additional 6 lbs, the other product with 6 lbs weight can be added to this box.

  * **Box A – 2 x Product A (2 lbs) + 1 x Product C (6 lbs) = Total 10 lbs**
  * **Box B – 3 x Product B (3 lbs) = Total 9 lbs**

* * *

### Packing based on Volumetric Weight

WooCommerce provides an option to add weight to the products based on the fact that the products will be shipped based on the weight of the products. However, this is not true in every scenario.

_**Does it ever happen to you that you may be shipping a product that may not weigh much but it requires more space?** _

Products such as cotton balls, pillows, etc. do not have much weight. However, the space they require for packing is comparatively greater than their weight. In such scenarios, actual weight is not considered for calculating the shipping rates. It is because the volumetric weight of the product exceeds the actual weight of the product.

Let us take an example of such a product in order to understand the concept of volumetric weight in a better way.

* * *

* * *

Here is a product that has a higher volumetric weight than the actual weight of the products. Now, let us see how you can compare the volumetric weight and the actual weight of the products.

#### **How To Calculate Volumetric Weight Of Your Products?**

So, now we have the actual weight and the dimensions of our product, let us see how you can calculate the volumetric weight of your products easily.

**Dimensions of the product  
** 20 x 07 x 02 in = 50.8 x 17.78 x 5.08 cm

**The volume of the products  
** 280 cu. in = 4588.37792 cu. cm = 4588.4 cu. cm

**Volumetric Weight = Volume / 5000 kg  
** 4588.4 / 5000 kg = 0.91768 kg

**Volumetric Weight (in lbs)  
** 2.023138088 lbs = 2 lbs

**Actual Weight of the Product – 1 lb**  
**Volumetric Weight of the Product – 2 lbs**

Now, since you already have the actual weight of the product, you can easily compare and see which one is greater. You can see the volumetric weight is reflected in the order page.

* * *

Now, let us check out how UPS returns the shipping rates for this product.

* * *

You can clearly see that the billable weight is not the actual weight of the product, but the volumetric weight. In the same way, if you enable the volumetric weight in the plugin settings, as shown in the image below, you will get the shipping rates based on the volumetric weight of the product.

* * *

**Note:**   
The plugin will only return the shipping rates based on Volumetric Weight when, The Volumetric Weight is greater than The Actual Weight. 

* * *

## Summary…

This article covers one of the most important features of the **[WooCommerce UPS Shipping plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)**. Most of the WooCommerce store owners who prefer automated shipping rates directly from the shipping carrier would like to get the shipping rates based on the weight of the products. In this article, we discussed how using the WooCommerce UPS Shipping plugin and its weight-based packing method, store owners can easily select how many products they want to pack into a single package. This will allow them to pack their products based on their own requirements and make it more convenient for them to ship products.

[ Previous  How to Show/Hide UPS Negotiated Rates?  ](https://www.pluginhive.com/knowledge-base/show-hide-ups-negotiated-rates/)

[ Next  Troubleshoot- Getting Higher Rates in UPS Shipping Plugin..!  ](https://www.pluginhive.com/knowledge-base/troubleshoot-higher-rates-ups-shipping-plugin/)
