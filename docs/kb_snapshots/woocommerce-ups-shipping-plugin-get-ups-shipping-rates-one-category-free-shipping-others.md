# WooCommerce UPS Rates & Free Shipping Based on the Product Category

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-ups-shipping-plugin-get-ups-shipping-rates-one-category-free-shipping-others/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce UPS Rates & Free Shipping Based on the Product Category

In this article, we will be discussing the [**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) and how using that plugin you can easily provide UPS shipping options based on one shipping class and Free Shipping to others.

WooCommerce store owners may offer their customers more than one shipping option based on demand, shipping cost, and many other factors. However, handling the same scenario in WooCommerce is a pretty difficult task.

According to Matt, a WooCommerce store owner, “ _**Hello, I have a query regarding the WooCommerce UPS shipping plugin. Is there any way I can provide shipping options based on a shipping class? I don’t need the UPS rates for all products. Only one product category needs UPS rates. I have 2 shipping options,**_

_**1) Free Class These are assigned to all Free shipping products**_  
 _**2) UPS Class These are assigned to all products I ship via UPS.**_

_**I need UPS shipping on all products excluding chairs which will be free.**__**Is this possible with this plugin? Thanks!**_ “

* * *

## Hide UPS Shipping options

Since Matt is providing UPS shipping as well as Free Shipping, it is necessary that these shipping options don’t get mixed with each other. Hence, in order to do that, we will be using the [**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) with **[Hide WooCommerce Shipping Methods and Rate Adjustment plugin](https://www.pluginhive.com/product/hide-woocommerce-shipping-methods-and-rate-adjustment/),** Matt can easily show the dedicated shipping options based on his shipping classes. This way he can get the UPS shipping options for the shipping class UPS and Free Shipping for the Free shipping class.

* * *

## Skipping Free Shipped Products

Based on Matt’s scenario, one thing is sure in his case, in case there are two products in the cart from **both the shipping classes – UPS and Free** , there should be no extra shipping charges for the product which is under the Free shipping class. Matt can easily achieve this [**using the code snippet from this link**](https://gist.github.com/xadapter/63cbc9436939dada64972ce78c4b6c72). Using this code, whenever there are products with both shipping classes available in the cart, all the products from the Free shipping class will be skipped from the UPS shipping calculation.

In other words, the shipping rates will be calculated for the products which are in the UPS shipping class. This way Matt will be able to achieve his complex-looking shipping scenario.

* * *

## Summary…

So this article covers the [**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/). With the help of this article, you will be able to handle a shipping scenario when the store owner wants to show shipping rates based on a particular category of products. With the help of this article, you will be able to setup UPS Shipping Rates along with free shipping on your WooCommerce store.

[ Previous  Generate Return Label & Drop Package at the UPS Access Point  ](https://www.pluginhive.com/knowledge-base/generate-return-label-drop-ups-access-point/)

[ Next  How to Get the Best Shipping Rates for WooCommerce Orders  ](https://www.pluginhive.com/knowledge-base/optimize-shipping-rates-using-woocommerce-ups-plugin/)
