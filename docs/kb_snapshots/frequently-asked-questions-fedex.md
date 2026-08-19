# WooCommerce FedEx Shipping plugin – FAQs

**Source:** https://www.pluginhive.com/knowledge-base/frequently-asked-questions-fedex/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce FedEx Shipping plugin – FAQs

With this article, we will be covering some of the most common frequently asked questions that people have about the WooCommerce Shipping Plugin for FedEx with Print Label. Read along to know more about it.

## On this page

  * **General FedEx services**
  * **Product Packaging& Boxes**
  * **FedEx Shipping Rates**
  * **FedEx API Error Codes**
  * **FedEx Shipping Labels**

* * *

### General FedEx Services

  * Does your **[WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** support the weight and dimensions of the product in Kg & cm? If yes, then how do I set up the plugin to work with Kg and cm?

Yes, product weight and dimensions are mandatory to get accurate FedEx shipping rates on your WooCommerce cart & checkout page. You can set the dimensions and weight of the product with any unit in the product settings. The WooCommerce Shipping Plugin for FedEx uses the product dimensions and weight and converts the weight and dimensions of the product into **Lbs** and **In** automatically. The plugin then displays the shipping cost based on the weight and dimensions and the customer’s shipping address.

**Note:** If the weight and dimension of the product are in Kg & cm, make sure you convert and enter the customized Box dimension in inches with box weight and maximum weight in lbs.

  * Does the WooCommerce Shipping Plugin for FedEx with Print Label work globally?

Yes, this plugin works for **ALL COUNTRIES** Where FedEx Operates. Currently, WooCommerce merchants across the following countries are successfully using the plugin:

  * United States
  * Canada
  * United Kingdom
  * France
  * Bulgaria
  * Denmark
  * Panama
  * Mexico
  * Costa Rica
  * Indonesia
  * Australia
  * Sweden
  * New Zealand
  * Netherlands
  * Germany
  * Hungary
  * Poland
  * India
  * Israel
  * Palestine
  * Philippines

* * *

### Product Packaging & Boxes

  * If my customers order multiple items, how to determine the number of items that I can fit into one box?

The total number of items that can fit into a single box, depends on the dimensions and weight of the product(s) available in the Cart. For multiple items, you need to select **Pack into boxes with weight** from the **Parcel Packing** drop-down list in plugin settings. After this, the plugin chooses the best-fitted box from the pre-defined boxes.

If the dimensions and weight of the products do not suit any pre-defined box from FedEx, you can add a customized box for your products.

For more information on box packing, _see_ **[Configure box dimensions in WooCommerce](https://www.pluginhive.com/knowledge-base/woocommerce-configure-box-dimensions/)**.

* * *

### FedEx Shipping Rates

  * Is it possible to utilize WooCommerce Shipping Plugin for FedEx with Print Label only for FedEx rate calculations? We do not need the print labels feature.

You can use the **[WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** only for calculating shipping rates during checkout. Print label and tracking features will be available only if you generate the label on the admin page of the order.

  * Even though I have configured the settings, the Cart is still showing that no available shipping option is available. Why?

After enabling the debug option, you can see the API **Request** and **Response** to find out the issue during checkout. For more information, _see_[**Troubleshooting WooCommerce Shipping Plugin for FedEx with Print Label**](https://www.pluginhive.com/knowledge-base/troubleshooting-woocommerce-fedex-shipping-plugin/).

  * Is there a way to have the plugin calculate FedEx shipping rates even with just having product weights?

No, FedEx API requires dimension and weight to calculate the shipping rates.

  * Can I get FedEx One Rate and the rate of other regular services like FedEx Ground, Standard Delivery, FedEx 2 Day, etc. in a single API request?

No, if you enable **[FedEx One Rate](https://www.pluginhive.com/knowledge-base/save-shipping-cost-using-fedex-one-rate/)** option, you only get rates for FedEx One Services and not for regular services, and vice-versa. If you disable FedEx One Rate option, you only get rates for regular services and not for FedEx One Services.

  * I would like to calculate the shipping costs for the order and bill it to the customer. However, I specifically do not want it to charge my FedEx account. Is it possible with the plugin?

You can use the plugin for displaying the live rates at the WooCommerce cart and checkout. FedEx will not charge your account for the shipping cost in this case The charges will only apply if you choose to print labels.

* * *

### FedEx API Error Codes

  * Why am I getting this error message “Authentication Failed” with Code ‘1000’ error when creating a label?

To eliminate the above error, you must enter the correct Account details in the plugin settings. For more information, _see_ the topic **[Get API Access From FedEx](https://www.pluginhive.com/knowledge-base/setting-woocommerce-fedex-shipping-plugin/).**

  * Why am I getting the FedEx API Response message “There are no valid services available” with Code ‘556’?

You can enable debug mode in plugin settings.**** Then, You can see FedEx **Request** displayed on the checkout page. For more information, see **[Troubleshooting Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/knowledge-base/troubleshooting-woocommerce-fedex-shipping-plugin/)**.

  * I received the following error message:

> Rating is temporarily unavailable for one or more services

**Ans:** This error occurs when the FedEx test servers are down. Ideally, FedEx test servers are up within 24 hours. If the problem persists, kindly communicate this issue with FedEx technical team.

  * I am getting an error code:

> 2026 – “Message: Packaging Type is invalid for Service Type.”. I am in production mode and trying to print a label.

The error code indicates that the available FedEx boxes are not available for the specified location or service.

Disable all the FedEx boxes that you have enabled in the**Pack into boxes with the weight and dimension** option in the plugin settings. Next, define a custom box and then try to ship. For more information, read our [troubleshooting document](https://www.pluginhive.com/knowledge-base/troubleshooting-woocommerce-fedex-shipping-plugin/).

Also, request you to discuss with FedEx to know the appropriate boxes and services available for your account. If you need any help setting up FedEx shipping on your WooCommerce store, feel free to [Con](https://www.pluginhive.com/support/)[tact](https://www.pluginhive.com/support/)[ PluginHive Customer Support](https://www.pluginhive.com/support/). We would be more than happy to help.

  * I am not able to create shipments from the WooCommerce order page, despite real-time rates being calculated on the front end of the website. When I click on Create Shipment option on the order page, I get the following error message:

> FedEx Create Shipment Error: Severity: ERROR  
> Source: prof  
> Code: 1000  
> Message: Authentication Failed

You need authorization from FedEx while printing shipment labels in production mode. You can contact FedEx with the sample label generated using Test Account details. Please follow the [certification guidelines](https://www.fedex.com/us/developer/downloads/pdf/CertificationGuidelines.pdf) to get advanced services for [printing FedEx shipping labels](https://www.pluginhive.com/knowledge-base/print-fedex-shipping-labels-directly-from-woocommerce-store/).

* * *

### FedEx Shipping Labels

  * Is there a way to set up the WooCommerce Shipping Plugin for FedEx with Print Label so that only one shipping label is made for the entire order?

Yes, you can use the **Parcel Packing Method** as **Box Packing** , and configure the box dimensions and weight that can hold the entire order.

  * The plugin is set up to use 4×6 size for label printing. But when the PDF is created and we try to print it, the Zebra thermal printer detects the document as an 8.5×11 paper size and the label has too large of a margin on the left. How can I print my FedEx labels accurately?

To correct the problem, you have to re-create the shipment for the particular order. But before doing that, make sure that PNG format is selected for label type in the plugin settings. Once you configure that properly, the label should be printed correctly(4×6).

* * *

You can check out the **[WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** to know more about its features. If you need help setting up FedEx shipping on your WooCommerce store, feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**.

[ Previous  WooCommerce Currency Conversion – FedEx Europe  ](https://www.pluginhive.com/knowledge-base/woocommerce-currency-conversion-fedex-europe/)

[ Next  WooCommerce Shipping: What are Freight Classes?  ](https://www.pluginhive.com/knowledge-base/shipping-freight-classes/)
