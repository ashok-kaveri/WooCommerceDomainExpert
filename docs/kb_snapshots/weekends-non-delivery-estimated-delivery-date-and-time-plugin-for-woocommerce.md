# How to Show Weekends as Non-Delivery Days using Estimated Delivery Date and Time Plugin for WooCommerce

**Source:** https://www.pluginhive.com/knowledge-base/weekends-non-delivery-estimated-delivery-date-and-time-plugin-for-woocommerce/
**Platform:** WooCommerce (WordPress)
**Plugin:** estimated-delivery
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# How to Show Weekends as Non-Delivery Days using Estimated Delivery Date and Time Plugin for WooCommerce

If you are dealing with potential customers who are likely to purchase your products, then you should ensure that they are well informed about the shipping details. You should show them the correct delivery dates as it is one of the most important factors that influence them to make the purchase. However, many WooCommerce store owners fail to ship the products promptly and miss the delivery dates for a variety of reasons.

The [Estimated Delivery Date and Time plugin for WooCommerce](https://www.pluginhive.com/product/estimated-delivery-date-plugin-woocommerce/) is a simple and beautiful plugin that allows store owners to show the correct delivery date to their customers. This plugin gives complete control to the store owners and helps them to set the delivery date based on their unique business scenario.

In this article, we would be covering a business case where one of our customers wanted to implement some changes to his online store. We would also see how this plugin helped him achieve his business case.

Let us quickly see his case first.

## Live Scenario…

Osimon is one our customers and he wants to show the delivery date as one day extra. Moreover, his working days are from Monday to Friday. Now, when a customer orders a product on a holiday (Nov 24th, Friday), he cannot initiate the shipping process on the same day. Rather, he can only start the process on the next working day. But the customer does not know about this and all he or she sees is that the delivery day is Nov 25th, Saturday. Thus, he is only able to deliver the product on Monday(Nov 27th, Monday) which is not favorable.

To solve this issue, Osimon can make some small tweaks to the plugin settings in order to show the correct delivery date to the customer. Let us see how.

## Role of the Estimated Delivery Date and Time plugin

To make things simple we will go ahead and order a sample item from the WooCommerce cart. Consider the following product.

Now, we need to configure the plugin. So, let us go to the plugin settings and set the **Minimum Delivery Days** as **1.** Refer the screenshot below.

As you can see, you can select the working days for your WooCommerce store. The **Working Days** define the days when the store functional and can initiate the shipping process. Here, we have defined Monday-Friday as the working days and Saturday-Sunday as holidays.

Further, we have chosen the **Consider holiday for Shipper and Recipient** option as the **Calculation Mode** for the shipment calculation. This option considers the holiday for both the shipper and the customers. Meaning, the shipper would not initiate the shipping process if the order date or the next day is a holiday (even Saturday and Sunday). and there would be no delivery to the customer’s address if the estimated delivery day is a holiday. Rather, in both cases, the plugin would consider the next working day as the estimated delivery date and show the same date in the Checkout/Cart.

This is a very important feature that contributes a major role in determining the shipping and delivery dates. After doing the above steps you can further go and save the settings. Now in order to check the delivery date lets go to the cart page and check it out.

Now, let us check out another case where Friday is considered as a holiday. To make this change, you just need to go to the plugin settings and unselect the Friday option. You can refer to the following image for the same.

Ideally, it should show the delivery day as of Nov 28th, Tuesday. Let us check out the Cart and see the delivery date.

## Conclusion…

Thus, if you do the above steps correctly, you should be able to show the correct and required the estimated delivery date to your customers. Moreover, you would be able to show weekends as non-delivery days which is a highly demanding business case.

We hope this article has helped you using the plugin better. Do let us know if you have any query. You can contact our [Customer Support](https://www.pluginhive.com/support/) if you face any issue.

[ Previous  Using WPML with WooCommerce Estimated Delivery Date plugin for Multilingual Sites  ](https://www.pluginhive.com/knowledge-base/using-wpml-woocommerce-estimated-delivery-date-plugin-multilingual-sites/)

[ Next  Set Estimated Delivery Dates for Different WooCommerce Shipping Zones  ](https://www.pluginhive.com/knowledge-base/specify-estimated-delivery-dates-different-shipping-zones/)
