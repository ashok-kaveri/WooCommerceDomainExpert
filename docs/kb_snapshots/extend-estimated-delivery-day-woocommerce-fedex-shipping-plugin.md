# Extend the Estimated Delivery Day in WooCommerce FedEx Plugin

**Source:** https://www.pluginhive.com/knowledge-base/extend-estimated-delivery-day-woocommerce-fedex-shipping-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** estimated-delivery
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Extend the Estimated Delivery Day in WooCommerce FedEx Plugin

To know the whereabouts of your package is very important. And since the delivery dates is one of the most influential factors that compel them to buy your products, it’s very important to make sure that the dates are correct.

So, if you are a WooCommerce store owner who uses FedEx as the shipping service, then you should configure the Estimated delivery date according to your business scenario.

The necessity of configuring the delivery date increases when your store needs a few extra days to process the orders. And in this article, we will come across a similar real-life scenario where a customer needs to make some special changes in order to show the delivery date as a day extra. We will also see how he can achieve this by combining a code snippet with our [WooCommerce Shipping plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/).

But, before going into the article let us check out the customer’s business case and requirements.

## Real-Life Scenario

> Customer: How can I increase the “Estimated Delivery Date” to +1 day? We want to show a more accurate time that takes into account our processing time. Since we might not get to an order the day it comes in, we want to give a 1-day buffer to not mislead the customer. Moreover, we want to implement this by adding it together with a previous Code Snippet that I used to change the formatting of the date.

In this case, the customer is already using a Code Snippet that changes the format of the estimated delivery date. You can see the default format of the estimated delivery date shown by FedEx plugin in the following image.

Following is the result of using the code snippet. Follow this link to get the **code snippet**.

Now, coming back to the customer’s case, let us quickly go to the file called **function.php**. You can find this file by going to the Dashboard of your WordPress and then by clicking on the **Appearance** -> **Editor.** Here, you have to look on the right side of the screen and you will find the function.php file. Click on that file and you would be able to see the **Selected file content:** section.

To change the estimated delivery date you would have to copy the code snippet in the [following link](https://gist.github.com/xadapter/c836240ba54a1172d3deab0727620542). After copying the code you would have to paste in the Selected file content section something like shown in the following screenshot.

Here, we have added the code snippet for the estimated delivery date in the end. After adding the code snippet you would have to click on the **Update File** button in order to save the changes that you have made. Now, if you go to the cart page and add an item, you would be able to see something like in the following image:

In the screenshot of the code snippet above, you can see that a red arrow points to the variable **$days_to_add = 1** ;. The value ‘1’ represents the number of days that you would want to extend the estimated delivery date to. So, for example, if you want to extend the date up to 6 days, then simply enter ‘6’ instead of ‘1’. You can refer the following image below.

* * *

We hope that this article was helpful to you. Do let us know how you feel about it. You can post your query in the comment section below or [**Contact PluginHive Customer Support**](https://www.pluginhive.com/support/) for further assistance.

Learn more about the **[WooCommerce Shipping Plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** features on the product page.

_**Happy selling!**_

[ Previous  WPML & FedEx shipping – WooCommerce store translation  ](https://www.pluginhive.com/knowledge-base/using-wpml-woocommerce-fedex-shipping-plugin-multilingual-sites/)

[ Next  Troubleshoot – Different FedEx Shipping Rates in Cart/Checkout  ](https://www.pluginhive.com/knowledge-base/troubleshoot-different-fedex-shipping-rates-cartcheckout/)
