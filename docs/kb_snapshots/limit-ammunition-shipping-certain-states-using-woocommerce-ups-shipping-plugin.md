# Restrict WooCommerce Shipping by State for Products like Ammunition and Alcohol

**Source:** https://www.pluginhive.com/knowledge-base/limit-ammunition-shipping-certain-states-using-woocommerce-ups-shipping-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Restrict WooCommerce Shipping by State for Products like Ammunition and Alcohol

With this article, we’ll tell you how to restrict WooCommerce shipping by the state for special/restricted products like Ammunition and Alcohol. We’ll also show you a few tricks to set up the desired WooCommerce shipping rates based on various parameters.

## On This Page

  * Use the WooCommerce UPS Shipping Plugin for Ammunition delivery
  * How to Restrict WooCommerce Shipping by State Using Shipping Zones?
  * [How to Restrict WooCommerce Shipping Methods Using Shipping Classes?](http://restrict-woocomerce-shipping-methods)
  * Limit WooCommerce Shipping Methods Based on Various Conditions
  * Hide WooCommerce Shipping Methods

## Use the WooCommerce UPS Shipping Plugin for Ammunition delivery

The **[WooCommerce UPS Shipping plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)** is something you call a complete UPS shipping solution for users with a WooCommerce store. It lets you display live UPS shipping rates on the Cart/Checkout page, print UPS labels, and share live tracking updates with your customers.

* * *

[](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)

[](https://www.pluginhive.com/product/shopify-ups-shipping-app-rates-shipping-labels-tracking/)

[](https://www.pluginhive.com/magento-shipping-services/)

* * *

While shipping there will be some cases where you need to restrict your shipping based on the rules and regulations of a particular area. While handling WooCommerce shipments, and using a shipping solution, a WooCommerce store owner must be well prepared for such scenarios.

According to James, a WooCommerce store owner, “ _**We sell ammunition, and the thing with ammunition is that you****can’t****ship to certain states. Is there a way to limit which states it will ship to. The shipping zones feature in WooCommerce**_ _**appears to be ignored. Any suggestions on how to create these limitations would be appreciated.**__**Thanks**_ “

Let’s see how to achieve James’s business case using the **[Hide Shipping Methods based on Shipping Class and Zone plugin](https://www.pluginhive.com/product/hide-woocommerce-shipping-methods-and-rate-adjustment/)** and the **[WooCommerce UPS Shipping plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)**. As the name suggests, this plugin lets you control WooCommerce shipping using two parameters, i.e, **Shipping Class** and **Shipping Zone**.

* * *

## How to Restrict WooCommerce Shipping by State Using Shipping Zones?

Based on James’s query, no shipping method should be available whenever a customer tries to purchase an ammunition product from the states where ammunition shipping isn’t allowed. But whenever a customer buys from a valid/approved location, the shipping methods should be available on the cart page.

As a first step, James needs to create a **[WooCommerce Shipping Zone](https://www.pluginhive.com/woocommerce-shipping-zones-ultimate-guide/)** named**Restricted,** containing all the states where ammunition shipping is not allowed. This way he can club all the restricted states together and he can go on with the configuration. This can be easily done under the Shipping zone option provided by the WooCommerce settings page.

* * *

Next, he has to get the Value ID by inspecting the shipping method as shown in the image below. As you can see, the Value ID of the shipping service, **UPS Ground,** is ‘wf_shipping_ups:03’ and James has to copy and paste this value under the Shipping Method option shown below.

* * *

## How to Restrict WooCommerce Shipping Methods Using Shipping Classes?

One of the best ways to categorize and restrict shipping methods based on product is with the help of **[WooCommerce Shipping Class](https://www.pluginhive.com/ultimate-guide-set-up-woocommerce-shipping-class/)**. The Shipping classes help you to categorize products based on their shipping preferences.

* * *

In this case, James can create a shipping class, say, Ammunition, and then assign it under the Shipping class option in the Addon setting. After that, he can restrict shipping for any shipping method based on the desired shipping class.

With the help of this Addon, James can easily hide all the UPS shipping methods whenever a customer tries to buy ammunition from the Restricted shipping zone or state. Have a look at this video and check out the complete process in real-time.

* * *

## Limit WooCommerce Shipping Methods Based on Various Conditions

Similarly, you too can restrict WooCommerce shipping methods based on various conditions like Shipping class, Shipping zone, Product category, etc. But this requires an additional WooCommerce conditional shipping plugin that allows users to exercise table rate shipping.

### Hide WooCommerce Shipping Methods

As mentioned before, you need a **[WooCommerce Conditional Shipping plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)** if you would like to control your shipping methods even more precisely. So let’s say, you want to hide a certain shipping method over the cart value of **$20**. In that case, you need to select the shipping methods and then define the upper cart limit as **$20**.

You can learn more about such WooCommerce conditional shipping scenarios and how to **[hide WooCommerce Shipping methods](https://www.pluginhive.com/hide-woocommerce-shipping-methods-complete-tutorial/)**.

And here’s an article on **[shipping alcohol products from WooCommerce](https://www.pluginhive.com/knowledge-base/ship-alcohol-using-fedex-shipping-plugin/)** if you would like to know more about it.

* * *

## Conclusion

This article covers a very interesting WooCommerce shipping scenario that involves ammunition shipping. Since shipping ammunition products is not allowed in certain states of the U.S., it becomes all the way important to prepare your online store that obliges to the rules and regulations.

With the help of this article, you can configure the **[WooCommerce UPS Shipping plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)** in such a way that it won’t allow shipping to some states only when there is ammunition in your order.

If you need any help with shipping or need help with the article, feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**. Our support team would definitely help you out.

**_Good luck!_**

[ Previous  Package Tracking and Returns with WooCommerce UPS Plugin  ](https://www.pluginhive.com/knowledge-base/make-easy-customers-track-package-process-returns-using-woocommerce-ups-shipping-plugin/)

[ Next  Scheduling UPS Pickup for WooCommerce Shipments  ](https://www.pluginhive.com/knowledge-base/schedule-ups-pickup-woocommerce-shipment/)
