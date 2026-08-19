# Add an Additional Cost to the Shipping Service based on WooCommerce Shipping Class

**Source:** https://www.pluginhive.com/knowledge-base/add-additional-cost-shipping-service-based-shipping-class/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Add an Additional Cost to the Shipping Service based on WooCommerce Shipping Class

In this article, we will check out how you can add an additional cost to a particular shipping service for a particular product. We will cover a customized solution based on the **[WooCommerce shipping classes](https://www.pluginhive.com/ultimate-guide-set-up-woocommerce-shipping-class/)** which will add an amount to the live shipping rates if the cart contains any product related to a particular shipping class.

## Business Case

Mark is a WooCommerce store owner who deals with Hazardous Products and ships them to his customers.

According to Mark, “ _**Can you give me a way to add a fee based on the product’s Shipping Class in addition to the FedEx Ground or FedEx Home Delivery charges?**_

_**Is this possible? For example, if I have a product with the Shipping Class “HAZMAT” I want to add $10 to the actual shipping rate returned by FedEx**_ “

## Solution

Add the [**customized solution**](https://gist.githubusercontent.com/Karthik-Naik/dfcbdf4dbc2f1e479117cab12943ca01/raw/c14610576a79744c523abab01178eb2a708509d0/functions.php) to your functions.php or anywhere relevant.

In the code given in the link:

  * **_$shipping_class_** contains the slug of shipping class(es) for which you want to add an additional cost for shipping.
  * **_$extra_cost_** contains an additional cost that is to be added to shipping.
  * **_$shipping_services_** contains IDs of services for which you want to add an additional cost for shipping.

If  _$shipping_class_ matches with the shipping class of the cart product, then _$shipping_class_exists_ becomes **true**. If  _$shipping_class_exists_ exists, then the cost of all the listed services is added with _$extra_cost_ and saved in  _$available_shipping_methods_. The Function returns _$available_shipping_methods_ which contains an additional cost of shipping.

  * To locate the shipping class slug, please visit the shipping class section **WooCommerce = > Settings => Shipping => Shipping class**

Shipping Class Slug

* * *

  * Assign the value of slug to the array

  * To add the extra charges you need to enter the additional amount under the **$extra_cost**
  * Then replace ‘wf_shipping_ups:01’ in the code snippet with the value of the appropriate shipping method as shown in the screenshot below. (for example, I have added $10 extra to FedEx Ground)

​​

* * *

  * To find the value for FedEx Ground, inspect it and provide exactly what is assigned to the variable “value” as shown in the screenshot below :

​

* * *

  * Once done, you will now be able to see additional charges that will be added on top of the normal shipping rates on the cart page as shown in the screenshots below:
    * Without adding extra charges

  * After adding $10 extra for the shipping class “HAZMAT”

## Plugin Compatibility

The abovementioned solution is compatible with the following shipping plugins.

  * [**WooCommerce UPS Shipping plugin with Print Label**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)
  * [**WooCommerce FedEx Shipping plugin with Print Label**](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)
  * [**WooCommerce Canada Post Shipping plugin with Print Label**](https://www.pluginhive.com/product/woocommerce-canada-post-shipping-plugin-with-print-label/)
  * [**WooCommerce Multi-Carrier Shipping plugin**](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/)
  * [**WooCommerce Royal Mail Shipping plugin with Tracking**](https://www.pluginhive.com/product/woocommerce-royal-mail-shipping-with-tracking/)

[ Previous  Adjust WooCommerce UPS Rates based on Destination Country  ](https://www.pluginhive.com/knowledge-base/ups-shipping-rate-adjustment-based-destination-country/?seq_no=2)

[ Next  How to Download, Install, Activate, and Update PluginHive WooCommerce Plugins  ](https://www.pluginhive.com/knowledge-base/how-to-download-install-update-woocommerce-plugin/)
