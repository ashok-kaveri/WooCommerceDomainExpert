# How to Add Custom Text in Delivery Estimates Format using PluginHive Plugin for FedEx Shipping?

**Source:** https://www.pluginhive.com/knowledge-base/add-custom-text-delivery-estimates-format-fedex-shipping-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** estimated-delivery
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# How to Add Custom Text in Delivery Estimates Format using PluginHive Plugin for FedEx Shipping?

In this article, we will tell you how you can add a custom text in the delivery estimates format when using the [**WooCommerce Shipping Plugin for FedEx with Print Label**](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/).

The WooCommerce Shipping plugin for FedEx with Print Label is an excellent plugin that allows store owners to show accurate delivery estimates. The delivery estimates that appear on the Cart/Checkout page are shown in real-time. So, depending on the address entered by the customer, the estimated dates would change accordingly. This feature is one of the most important and useful features of this plugin.

However, at times some of our customers need to modify this feature according to their business case. This can be done by adding a code snippet into their WooCommerce. Following is one of our customer’s requests which prove to be quite common.

> Customer: Currently the plugin displays the shipping rates and the delivery format as shown below,
> 
> FedEx Ground: $33.55  
> Est delivery: February 3, 2018
> 
> Is it possible to have it come back as:
> 
> FedEx Ground: $33.55  
> Est delivery: February 3, 2018 (1 Day in transit)
> 
> or
> 
> FedEx Ground: $33.55  
> Est delivery: February 3, 2018 (1)
> 
> or
> 
> FedEx Ground: $33.55  
> 1 Day in transit
> 
> We make use of this information in order to determine the amount of Dry Ice required inside the cooler as we pack the orders. We want this because having the date will make it more difficult for the staff members to calculate this.

In this article, we will show you how to add a custom text by the end of the Estimated Delivery date. We will also show you how to customize the code in order to change it according to your need.

The above code is necessary in order to add the custom text. You need to copy and then paste the code snippet in, **Appearance-- > Editor--> Theme functions(functions.php) **and then click on Update File**.** If you look carefully at the line number 6, then you would find the following line of code:

$postfix_text = ‘ ( 1 Day in Transit )’; //Modify the text as per your requirement

In the above line of code, you can define your own message. So, if you want to show the text as “One day in Transit”, then you just have to replace it with the content inside the brackets ( ). This way the line of code would look something like the following:

$postfix_text = ‘ ( One day in Transit )’; //Modify the text as per your requirement.

Doing this will display the page as shown below in the image:

* * *

If you have any query regarding this article or the integration of WooCommerce Shipping plugin for FedEx with Print Label then feel free to share your views in the comment section below. We will be more than happy to help you understand how this plugin can work together in fulfilling your shipping requirements.

Or in case you are wondering what more does the WooCommerce FedEx Shipping plugin serve, I would request you to kindly [**visit the official product page here**](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)**.** If you need assistance regarding our plugins, you can also [**contact our support team.**](https://www.pluginhive.com/support/) We are always happy to help.

### **About the plugin…**

#### **WooCommerce Shipping Plugin for FedEx with Print Label**

#### Cost: $69.00

  * WooCommerce requires at least 2.6 up to 3.2.
  * The license entitles 1 year of support & updates.
  * No monthly fees or yearly subscription.
  * Extend support & updates after 1 year at 50% discount.
  * Protected by 30 Day Money Back Guarantee.

[ Previous  WooCommerce Shipping for FedEx – Change Customs Duty Payer based on the Destination country  ](https://www.pluginhive.com/knowledge-base/change-customs-duty-payer-based-destination-country/)

[ Next  How to Download, Install, Activate, and Update PluginHive WooCommerce Plugins  ](https://www.pluginhive.com/knowledge-base/how-to-download-install-update-woocommerce-plugin/)
