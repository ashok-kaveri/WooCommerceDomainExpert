# Troubleshoot

**Source:** https://www.pluginhive.com/knowledge-base/troubleshooting-woocommerce-royal-mail-shipping-tracking-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** royal-mail
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Troubleshoot

This article will be useful for you to troubleshoot issues when using the WooCommerce Royal Shipping Plugin. You can use this guide if you are not able to see the shipping rates on the Cart/Checkout page or want to solve any other issue. But before you go ahead, check out this guide- [how to set up the Royal Mail Shipping plugin](https://www.pluginhive.com/knowledge-base/setting-woocommerce-royal-mail-shipping-tracking-plugin/). You can refer the product page as well- [WooCommerce Royal Mail Shipping plugin.](https://www.pluginhive.com/product/woocommerce-royal-mail-shipping-with-tracking/)

### Troubleshooting for not getting shipping rates on Cart/Checkout page

This is one of the most common issues that most of the plugin users face. This can happen because of many possible reasons and some of the reasons are listed below:

  1. **Enable Rates** : This might sound a bit trivial but sometimes we forget to select **Enable Rates** checkbox. Moreover, as soon as you install the plugin, the Enable Rates checkbox is disabled by default. So this should be your first check. You must enable shipping at two places.
     1. You should first ensure that **Calculations** is enabled. You have to enable the checkbox in the WooCommerce Shipping settings page as shown below:
     2. Now, you need to make sure that the Enable Rates option is enabled in the Royal Mail Shipping plugin. You can refer to the following video for the same:
  2. **Weight and Dimensions of the products:** The Royal Mail shipping service makes use of the weight and dimensions of your product(Length, Width, and Height) in order to calculate the shipping cost. So, it is essential to ensure that the products that you are going to sell using the Royal Mail contain both physical parameters. You have to enter the Weight and the Dimension of your product in the Edit Product page as shown below:
  3. **Change the Units:** The Royal Mail follows the Metric system. So, you should set the Measurement unit of the products in the metric units only. You can change the measurements units on the WooCommerce Products page as shown below: Also, the store currency should be in Pound sterling. In order to change the currency, you would need to go to the WooCommerce General Settings page and then select the Pound sterling from the drop-down menu. You can refer the following image as shown below:
  4. **Check the zip-code and address entered:** The shipping calculation is sensitive to the address and the zip code entered on the Cart/Checkout page. This is the reason why you should also make sure that the entered address is correct.

## Using the Debug Mode

If you are not getting proper rates (lesser or higher than expected), not getting all the available shipping options, then you enable **Debug Mode** option to find the error(s). By using the Debug Mode, you can also see important warnings that will eventually help you to find and solve the issue.

As soon as you enable the Debug Mode, you would be able to see the log on the top of the Cart and Checkout page. This log will prove to be quite useful once you get used to it and understand how the log displays each parameter. For that, you need to enable the **Debug Mode** checkbox in the Royal Mail plugin Settings as shown below:

After enabling Debug Mode in the plugin settings page, add a product to the cart. Thereafter, go to the Cart or Checkout page to see the debugging information on the top section of the page. The next step is to ensure that you have entered a proper shipping address. If you are not getting rates at all, then you need to find the exact reason for that. Some of the most common cases are explained in the below section.

  1. **When the shipment weight is more than the limit:** There are certain weight limits to each order and you have to keep your orders within that limit for shipping. For example, shipments of more than 30 kgs will not be calculated for the shipping and the Debug log will show that there are no shipping methods available.
  2. **Comparing shipping rates for the mismatch:** You can use the Debug Mode to see whether the shipping rates are correct or not. For that, you can go to the official Royal Mail website and find the actual shipping price. There, you have to enter the exact weight of the package, choose the right parcel(letter or parcel) and enter the from and to address. Then you can compare the obtained rates and the shipping rates shown on the Cart/Checkout page.
  3. **Checking if the units are correct or not:** The Debug Mode has an amazing feature that displays the warnings related to shipping. As discussed above in the ‘Change the Units’ section, you have to select the correct units. For example, if you have chosen the measurements units **lbs** and **in,** then the plugin will show the warning as shown in the image below:

You can also check out the following plugin options that may result in the rates mismatch.

The Exclude Tax checkbox will allow you to exclude the tax from product price. If you are getting higher shipping rates then try disabling this option. Another option is to add the Insurance amount to an order. This can also increase or decrease the actual shipping cost.

* * *

If you have any query regarding the setting up of this plugin then kindly comment down below. If you need any further help then kindly [contact our customer support](https://www.pluginhive.com/support/). We would be more than happy to help you with anything.

[ Previous  How to Set Up PH Royal Mail Shipping with Tracking for WooCommerce  ](https://www.pluginhive.com/knowledge-base/setting-woocommerce-royal-mail-shipping-tracking-plugin/)

[ Next  How to Download, Install, Activate, and Update PluginHive WooCommerce Plugins  ](https://www.pluginhive.com/knowledge-base/how-to-download-install-update-woocommerce-plugin/)
