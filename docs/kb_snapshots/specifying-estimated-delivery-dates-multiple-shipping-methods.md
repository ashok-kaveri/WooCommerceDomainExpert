# WooCommerce: Set Estimated Delivery Dates for Multiple Methods

**Source:** https://www.pluginhive.com/knowledge-base/specifying-estimated-delivery-dates-multiple-shipping-methods/
**Platform:** WooCommerce (WordPress)
**Plugin:** estimated-delivery
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce: Set Estimated Delivery Dates for Multiple Methods

As we all know that WooCommerce is one of the best platforms to sell your products online. This has been possible because of various useful plugins that add extra features to WooCommerce. One of those amazing plugins is the Estimated Delivery Date and Time for WooCommerce. This plugin helps store owners to show the estimated delivery dates of their products which helps customers to purchase the products accordingly.

It gives the ability to show delivery dates for all types of shipping methods. For example, if you are offering FedEx as the shipment service then you can even display the delivery dates for the same. But, some of our customers find it difficult to set up the dates. Let us try to understand an issue of one of our customers and see how this plugin can help him.

> Frederic: I just bought your plugin but I’m not able to set a différent delivery date according to the shipping method. I don’t really know what I should put in the field “Shipping method” in your shipping method page. As there is no dropdown menu allowing me to choose my current shipping methods it’s not easy to find the good one.

If you look closely in the Shipping Methods section of the plugin settings page, you would find the **Add Method** button. This option will help you add the various shipping methods and specify the delivery dates for each of them. To understand this clearly let us assume the following situation.

Imagine you are offering the Flat Rate and FedEx as the shipping services to your customers. You would want to add the value 3 as the delivery days for Flat Rate. For the FedEx shipments, you are offering the **FedEx Overnight** and the **FedEx Priority Overnight,** and you want to show the delivery day value as 1. Moreover, let us assume that the Minimum Delivery Days is set as 1 as shown in the image below.

**Note:** We are assuming Saturday and Sunday as holidays.

Now, in order to specify the shipping methods, you would need to go to the cart and select the shipping methods one by one and click on the right mouse button.

Click on the inspect option and you would see the following section on your screen.

Here, just for this explanation, we have chosen the **FedEx Priority Overnight.**

Now, in the inspect section you have to copy the shipping method ID as pointed by the red arrow (here, wf_fedex_woocommerce_shipping: PRIORITY_OVERNIGHT). After copying this text you will have to paste it in the Shipping Method box as shown in the image below.

Here, we have already performed the similar steps for the Flat Rate and FedEx Overnight. You can now enter the shipment delivery dates based on your need (here, we have entered 3, 1 and 1 respectively) and save the changes that you have made.

Now to try out the settings, we can go to the cart and select each shipping methods to check the delivery dates. You can refer to the following calendar for reference.

So, based on the above calendar the order was received on the 17th of November and thus, the Flat Rate option should display 23rd November as the estimated delivery date. You can confirm that in the image shown below.

Now, if we choose the FedEx Priority Overnight, then the delivery date should come up to be 21st of November.

Based on the above procedures, you can even set the delivery date for various third-party shipping services like UPS and USPS.

* * *

We hope that this article was useful to you in some way. Do let us know if you have any query in the comments section below. If you are facing some technical difficulties, you can contact our [customer support](https://www.pluginhive.com/support/) for further assistance.

[ Previous  Set Estimated Delivery Dates for Different WooCommerce Shipping Zones  ](https://www.pluginhive.com/knowledge-base/specify-estimated-delivery-dates-different-shipping-zones/)

[ Next  Provide Standard or Priority Shipping with Different Shipping Cost and Delivery Time on your WooCommerce store  ](https://www.pluginhive.com/knowledge-base/provide-woocommerce-standard-or-priority-shipping-different-delivery-time/)
