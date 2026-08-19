# Troubleshooting WooCommerce UPS Plugin

**Source:** https://www.pluginhive.com/knowledge-base/troubleshooting-woocommerce-ups-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Troubleshooting WooCommerce UPS Plugin

In this guide, we will show you how you can troubleshoot your **[WooCommerce UPS Shipping Plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)** and resolve a few common issues regarding real-time UPS shipping rates, shipping labels, and live UPS tracking. This document contains all the steps to debug and resolve all the issues which you may come across while using the plugin.

## Troubleshooting for not getting UPS rates at all

If you are not getting **rates** at all, there might be some reasons for not fetching real-time shipping rates from UPS APIs. The list of reasons is as given below:

**Enable Shipping:** That sounds a bit trivial. But sometimes we forget to select the **Enable Real-time Rates** checkbox. By default, it is disabled. So this should be your first check. You should select the checkbox in the Admin WooCommerce Settings as shown below:

**Weight and Dimensions:** UPS shipping carrier uses the weight and the dimensions of your product (Length, Width & Height) to calculate the shipping cost (besides using the origin and destination address). So, make sure you enter the Weight and the Dimension of your product in the Product Settings as shown below:

**Fallback Field Check:** Make sure you enter the numeric value in the field or Keep the Fallback field empty. The Fallback field is as shown below:

**Note:** Do not enter text in the Fallback field.

If you have done the above basic checks and still not getting rates, then you must enable debug mode to get exact reason for not getting rates.

### **Debug Mode**

If you are not getting proper rates (lesser or higher than expected), not getting all the available shipping options, not getting rates at all or not getting Print Labels, then you need to enable **Debug** option to find the error(s). You can also see the warning(s) through the UPS plugin.

By enabling the debug mode, you can trace the issue using the log. You can see information about debugging at the top of the Cart and Checkout page. Select the **Debug** checkbox in the UPS Plugin Settings to enable debug mode as shown below:

**Note:** To enable the debug mode, you need to first enable the **Shipping Debug Mode** by navigating to **WooCommerce** > **System Status** as shown below:

After enabling the debug mode, add a product to cart. Go to the checkout page to see the debugging information. Ensure that you have entered a proper shipping address. If you are not getting rates at all, then you need to check the response sent by the UPS to know the exact reason for not showing the rates. The cases are explained in the section below.

**Shipping Address Error:** In case, the customer does not enter the correct postal code, then the UPS will not display the rates. The customer gets a message as shown below:

To know the reason, you need to check the response sent by the UPS as shown below:

From the above response, you can clearly see that the postal code is incorrect. So fix it by clicking on **Calculate Shipping** on the Cart/Checkout page as shown below:

**Authentication Error:** In Case, the credentials of the UPS are incorrect, then the UPS will not display the rates. You will get a message as shown below:

From this response, you can clearly see that there is a problem with the authorization. Hence, you can enter the correct credentials in the UPS Plugin Settings page as shown below:

## Troubleshooting for Correct UPS Rates

The Request is sent to the UPS by the plugin with an Address of source, destination, dimensions of the product, etc. The sample Request to the UPS is as shown below:

Recheck the**ShipTo** node (at location 1 in the UPS Request screenshot). According to your requirement, if the recipient address is not correct, you can fix it by navigating to the Cart/Checkout page as mentioned below:

Recheck**** the**ShipFrom** node. According to your requirement, if the Shipper address is not correct, you can fix it by navigating to the UPS Plugin Settings as shown below:

You can see the service code for this particular request. According to your requirement, you can enable or disable the service by navigating to the UPS Plugin Settings as shown below:

Similarly, you get the request and response for all the enabled services in the debug mode.

Recheck the**Dimensions** of the product with units(under **Code** node). If the product dimensions are not correct according to you, correct it by navigating to the **Admin** Product settings as shown below:

Recheck**** the weight of the product with units (under **Code** node). You can change the weight of the product according to a requirement by navigating to the **Admin** Product settings as shown below:

Recheck if the product is insured or not. In case it is not correct as per your requirement, change it by navigating to the UPS Plugin Settings of the plugin as shown below:

Recheck for if the Negotiated rates are enabled or not. According to your requirement, enable/disable it by navigating to the UPS plugin settings and correct it as shown below:

**Note:** If all the information sent to the UPS is valid, you can contact the UPS or go to the UPS site and log in with your credentials. After logging in, enter the same information in the UPS Calculator to get the quote.

  * **UPS Response** : You get the Response sent by the UPS with rates for different services. You can see the response to analyze the information sent from the UPS.

### Troubleshooting for Print Labels

If you are not able to **print labels** , it could be because of a reason listed below:

  * **Product Existence:** Sometimes, we try to print the label for the product that is removed from the shop. So check if the product still exists in your shop.
  * **Weight and Dimensions:** While printing labels, the weight and dimensions are needed to calculate the shipping cost. So make sure you have set the Weight and Dimensions of your products correctly.
  * **Service Eligibility:** If the selected service in the Admin Order page (shown in the below screenshot) is not available for the particular location/product, you will get the error about service eligibility.

To know details about the available services for the required location/product contact the UPS.

  * **Authentication Error:** If the authentication information incorrect, you get the error as shown below:

From the above screenshot, you can clearly see that there is a problem with the authorization. Correct it in the settings page as shown below:

## How to see the boxes seleted for an order?

With **[WooCommerce UPS Shipping Plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)** , you can see the boxes/packages selected in an order before the money is deducted from your UPS account for postage. You can even check parameters like the package weight, dimensions, shipping rates , shipping service name, surcharges, address, etc., for that particular order.

Follow the following steps to see the boxes selected for a particular order.

  1. Enable Debug Mode in the plugin settings
  2. Add the item(s) in the Cart
  3. Move to the Cart or Checkout page to view the Package, UPS Request, and UPS Response

Let us take an example to understand the steps better.

Assume that we have placed an order for 2 products that are packed inside a single box. With the help of the Debug option, you can see 3 code blocks on the front end(cart page/checkout page). By analyzing these 3 code blocks, you can come to know about the boxes selected in an order.

  * **Package:** This section provides information about the item(s) including product dimensions and box dimensions(if the custom box is selected).
  * **UPS Request:** This section provides the information regarding the request sent to UPS from our plugin which includes the box dimensions.
  * **UPS Response:** This section provides the information regarding the Response that has come from the UPS. Please note that the information included in this section is directly from UPS servers and not from within the plugin.

### Package

This section shows the dimensions of the 2 products marked by points 1 & 2 in the screenshot and also dimensions of the box in which packing will be done(marked by point 3 in the screenshot below).

### UPS Request

This section shows the request sent from plugin side to UPS. We can see the final box dimensions and weight of the total package as shown below.

### UPS Response

The response that comes from the UPS side shows the total shipping price charged and also the total billable weight as shown in screenshot.

## Conclusion

Check out the product page to know more about the **[WooCommerce UPS Shipping Plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) **and the features this plugin offers.

If you have any concerns or need help setting up UPS Shipping on your WooCommerce then **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**. Our support team will help you out.

**_Good luck!_ 🙂**

[ Previous  How to Connect UPS with WooCommerce  ](https://www.pluginhive.com/knowledge-base/connect-ups-with-woocommerce/)

[ Next  Fixing Ä, Ö, Ü & ß on UPS Shipping Labels in WooCommerce  ](https://www.pluginhive.com/knowledge-base/generating-ups-label-aou-s-appears-label-special-type-way-correct/)
