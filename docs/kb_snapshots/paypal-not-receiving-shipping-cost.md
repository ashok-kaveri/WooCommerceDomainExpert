# Why is My Paypal not Receiving Shipping Cost ?

**Source:** https://www.pluginhive.com/knowledge-base/paypal-not-receiving-shipping-cost/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Why is My Paypal not Receiving Shipping Cost ?

This article will cover the common issues faced by users who aren’t getting the shipping rates to show on their PayPal account while using the **[WooCommerce UPS Shipping plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)**. Read more below.

WooCommerce store owners require constant support and assistance in terms of the plugins and functionalities they are using. In recent times, there have been cases where WooCommerce store owners have come up with an issue regarding Paypal.

One of our customers had been using [**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) to handle his shipping requirement. According to the customer,

“** _Over the past three months, we have had three orders where the shipping cost was not sent to Paypal. We got the email from WooCommerce with the product and shipping cost correct, but just the product cost was sent to PayPal and so we were not paid the money for the shipping by the customer. What’s weird is that it has only happened three times and we have many other orders that have gone through fine_** “

PayPal

## Product Cost & Shipping Cost

Ideally, the process of calculation of total cost has two phases.

  * **Calculation of Product Cost**
  * **Calculation of Shipping Cost**

Product Cost is based on the cost of the product that store owners have to add on the Edit Product page. Also, if there are multiple products added to the cart, the product cost is multiplied by the product quantity. However, the shipping cost is calculated in a different manner. It is based on various factors defined by different carriers. Some of the factors include the weight of the package, source and destination address, package dimensions, etc.

Once the shipping cost is calculated, the total cost is shown on the cart page. This is the cost that the customer has to pay while placing an order.

## No Shipping Cost transferring to PayPal Account

WooCommerce actually sends the shipping cost and the product cost separately to PayPal. It is then updated to PayPal. However, the issue seems to be with the updated versions of WooCommerce (v.2.6 and above).

Since the shipping cost is sent to PayPal exclusively, there is an option to configure shipping rules in PayPal. So,**if the store owners have configured shipping rules in PayPal, there is already a mechanism that does not transfer the shipping rates from WooCommerce to PayPal.**

As a preventive measure against this issue, store owners can either remove all the shipping methods configured in PapPal or disable those shipping rules. This way, the shipping rates will be transferred to PayPal by WooCommerce and will be included in the payment.

## Summary

So this article is about the issues faced by **[WooCommerce UPS Shipping plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)** users, who are not getting the **[WooCommerce shipping](https://www.pluginhive.com/product-category/woocommerce-plugin/woocommerce-shipping/)** rates to show on their PayPal account.

This article will help you to understand the process of total cost calculation in WooCommerce and how to transfer the shipping cost successfully to PayPal. If you have any queries or need help with your WooCommerce, feel free to **[contact our customer support](https://www.pluginhive.com/support/)**.

[ Previous  WPML WooCommerce Shipping Solutions for Multilingual Sites  ](https://www.pluginhive.com/knowledge-base/using-wpml-woocommerce-ups-shipping-plugin-multilingual-sites/)

[ Next  Add Handling Charges to WooCommerce UPS Shipment  ](https://www.pluginhive.com/knowledge-base/how-to-add-handling-charges-ups-shipment/)
