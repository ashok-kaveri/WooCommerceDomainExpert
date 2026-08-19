# Ship Physical Products along with WooCommerce Subscription Products with the WooCommerce UPS plugin

**Source:** https://www.pluginhive.com/knowledge-base/handle-shipping-standard-subscription-products-ease-using-woocommerce-ups-shipping-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Ship Physical Products along with WooCommerce Subscription Products with the WooCommerce UPS plugin

With this article, we’ll tell you how to ship Physical products along with WooCommerce Subscription products using the **[WooCommerce UPS Shipping plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)**.

## What are WooCommerce Subscription Products?

WooCommerce lets you create a variety of products including products that aren’t your normal physical products. The Subscription Products sold on a WooCommerce store usually come with a monthly or yearly subscription.

These products are usually digital and are even eligible for normal delivery. However, handling the shipping of such products together with normal products is a complex task. Let’s take an example to understand this better.

According to Mark, a WooCommerce store owner,

“ _**I am building a website for a client where I have two kinds of products: Physical products and WooCommerce Subscription Products.**_

_**Please consider the following scenario where t**_ _**he shipping charges for standard products based on the total weight of the Physical products in the cart and will be given by UPS. Shipping is free for WooCommerce Subscription Products.**__**I want to know if there is any plugin that can do the following:**_

  1. _**If there are only subscription products in the cart, shipping would be free.**_
  2. _**If there are Physical Products + Subscription Products in the cart, then shipping should be charged for the standard products only – based on the weight of all Physical products in the cart. It should not consider the weight of the Subscription Products while calculating the shipping charges. Is there any way to do this?**_ “

* * *

### Creating WooCommerce Shipping Classes for the two product types

WooComemrce store owners can divide the products based on the way they are shipped using different **[WooCommerce Shipping Classes](https://www.pluginhive.com/ultimate-guide-set-up-woocommerce-shipping-class/)**. In the case of Mark, since he is using both physical and subscription products, he requires two separate WooCommerce Shipping Classes.

  * **Physical Products**
  * **Subscription Products**

The image below shows Mark’s WooCommerce Shipping Classes.

Once the shipping classes are created, Mark needs to add the shipping classes to each product under the product edit page. After this, since he requires the subscription products to be provided Free Shipping, he can configure it in the shipping zones and provide free shipping to the shipping class subscription products.

* * *

### Skipping WooCommerce Subscription Products from shipping rate calculation

Once the shipping classes are successfully created, the main objective is to make the shipping rates calculation accurate. Since the WooCommerce Subscription Products will be shipping free of cost, nothing seems to be worrying here.

However, when the products are in the shipping class WooCommerce Subscription as well as Physical products, they are added together in the cart, things seem to be a bit different.

In such a case, the shipping rates must be calculated based on the weight of the products of Physical Products shipping class. Hence, we would be skipping the subscription products from the process of the shipping rate calculation.

Mark can easily achieve this by going into the Plugin settings page and selecting the Subscription shipping class as shown in the image below.

And once that is done, he could easily see the plugin skipping the Subscription Product without having to calculate the shipping cost for it.

* * *

## Summary

So in this article, we discussed how the **[WooCommerce UPS Shipping plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)** can easily help you ship both Physical and Subscription Products. Since both the products will have a different shipping charge, an order with both types of products in the cart can create problems for the store owners.

If you have any suggestions regarding the article, feel free to share your views in the comment section below. We have also attached some details about the plugin that we discussed in this article. You can even **[contact PluginHive Customer Support](https://www.pluginhive.com/support/)** if you have any technical issues.

**_Happy selling!_**

[ Previous  Set Up Freight Shipping with WooCommerce UPS  ](https://www.pluginhive.com/knowledge-base/handle-freight-shipping-tariffs-ease-using-woocommerce-ups-shipping-plugin/)

[ Next  Adjust WooCommerce UPS Rates based on Destination Country  ](https://www.pluginhive.com/knowledge-base/ups-shipping-rate-adjustment-based-destination-country/)
