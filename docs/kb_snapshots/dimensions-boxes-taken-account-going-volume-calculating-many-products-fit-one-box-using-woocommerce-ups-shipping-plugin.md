# Are the dimensions of the boxes taken into account or is it going by volume when calculating how many products fit in one box using WooCommerce UPS Shipping Plugin?

**Source:** https://www.pluginhive.com/knowledge-base/dimensions-boxes-taken-account-going-volume-calculating-many-products-fit-one-box-using-woocommerce-ups-shipping-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Are the dimensions of the boxes taken into account or is it going by volume when calculating how many products fit in one box using WooCommerce UPS Shipping Plugin?

Parcel packing has always been confusing for WooCommerce store owners. Many store owners have had a hard time packing their products in an efficient way. One of the WooCommerce store owners even had his package repacked, as it was not the most efficient in terms of space management.

According to Jack, a WooCommerce store owner,” _**We have a product with dimensions 10 x 10 x 10 inches = 1000. We have 2 boxes with dimensions 11 x 11 x 11 inches = 1,331 and 12 x 12 x 15 inches = 2,160.**_  
_**When ordering 2 of the 10 x 10 x 10 product the UPS plugin will pack them into 1 of the 12 x 12 x 15 boxes as the volume fits. But 2 of the 10 x 10 x 10 products do not fit dimensionally.**__**The problem is the shipping rates are too low and not covering the cost of shipping, especially on overnight orders we can be about $70 short. Is there any way to change the way products will be packed more efficiently?**_ “

In this article, we will be covering how to pack the products in a more efficient way using [**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/).

## Packing Algorithms

WooCommerce UPS Shipping plugin allows store owners to pack their products based on these algorithms.

  * **Volume Based Packing**
  * **Stack First Packing**

### Volume-based Packing

Under this packing algorithm, the plugin checks the volume of the products that are in the cart. Then it checks which box can accommodate this volume inside it. In other words, if the volume of the products is less than the volume of the box, those products will be packed inside that box. Only the dimensions are taken into consideration in this algorithm.

### Stack First Packing

Stack first packing algorithm is different than the volume-based packing algorithm. Under this algorithm, the products are just piled/stacked either on top of each other or side by side. In other words, if two products are packed based on this algorithm, they will be packed on top of each other and hence their heights will be added together and the maximum width and length will be taken into consideration. You can [**get more information in detail about the stack first packing algorithm here**](https://www.pluginhive.com/knowledge-base/packing-options-available-woocommerce-ups-shipping-plugin/).

## Best Algorithm for Jack

Based on Jack’s requirements, he must use the**Stacked First Packing Algorithm**. Using this algorithm, if he selects two products with dimensions, 10x10x10 inches, then two packages will be created with dimensions 11x11x11 inches. And the box with dimensions 12x12x15 inches won’t get selected. Hence, his shipping rates will be calculated for two packages. This way Jack will be able to cover the shipping charges for his **Overnight Shipments**.

## Summary

So this article covers the method of product packing in **[WooCommerce UPS Shipping plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)**. The plugin has some of the most advanced packing methods which allow store owners to pack their items efficiently. This article covers how you can pack your products more efficiently using WooCommerce UPS Shipping plugin’s parcel packing methods.

* * *

If you have any suggestion regarding the article, feel free to share your views in the comment section below. We have also attached some details about the plugin that we had discussed in this article.

[ Previous  Set Up WooCommerce Flat Rate Shipping with UPS Ground Rates  ](https://www.pluginhive.com/knowledge-base/woocommerce-flat-rate-shipping-live-ups-ground-rates/)

[ Next  WooCommerce UPS Tracking Number for Free Shipping Orders  ](https://www.pluginhive.com/knowledge-base/populate-ups-tracking-number-orders-free-shipping-woocommerce/)
