# “There are no shipping methods available” on WooCommerce

**Source:** https://www.pluginhive.com/knowledge-base/problem-plugin-always-no-shipping-methods-available/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# “There are no shipping methods available” on WooCommerce

With this guide, we’ll tell you how to troubleshoot the error message ‘There are no shipping methods available’ that appears on the WooCommerce cart or checkout page. We will specifically look into some of the most common reasons you might get this message while using the **[WooCommerce FedEx Shipping plugin](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)**.

* * *

## On this page

  * **Reasons for the “There are no shipping methods available” message on the WooCommerce cart& checkout page**
    * **Incorrect shipper’s FedEx account details**
    * **Incorrect Shipper’s Address**
    * **FedEx Real-time rates are disabled under the Rates and Services tab**
    * **WooCommerce product weight& dimensions are not configured**
    * **Shipping service availability for specific countries**
    * **Appropriate FedEx shipping services not selected in the Services Table under “Rates and Services”**
    * **Conditional shipping – Minimum Order Amount configured within the plugin settings**
    * **Incorrect destination address entered by the customer**
    * **Inaccurate combination of FedEx Special Services**

* * *

## Reasons for the ‘There are no shipping methods available’ message on the WooCommerce Cart/Checkout page

WooCommerce is a WordPress plugin capable of letting you set up the desired online store. And with its features, you can sell and deliver all kinds of products to your customers with no problem whatsoever. You may have a few hiccups in the midst of setting up the store. But that’s completely normal for someone new to WooCommerce or e-commerce, in general.

One of the most common issues is the message that appears on the cart/checkout page – There are no shipping methods available. This message can appear due to many reasons and can have serious repercussions if not addressed quickly.

Let’s discuss some of the reasons why you are getting the “There are no shipping methods available” message on the WooCommerce cart or checkout page.

* * *

### Incorrect shipper’s FedEx account details

WooCommerce doesn’t provide FedEx integration as a built-in functionality. Using the **[WooCommerce FedEx Shippin](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** g Plugin, you can integrate your own FedEx account to display live FedEx shipping rates at cart and checkout pages. However, you need to add accurate FedEx account details for the plugin to get the most accurate shipping rates from FedEx in real time.

To access the FedEx Registration,**Plugins > WooCommerce Shipping Plugin for FedEx > Settings > General**

In case you have entered incorrect FedEx account details, the message displayed on the WooCommerce cart and checkout page will be, “There are no shipping methods available.”.

**In order to fix this, make sure you enter the correct FedEx account details within the plugin.**

* * *

### Incorrect Shipper’s Address

The shipper’s address in shipping refers to the location from where a package or shipment will be picked up by the shipping carrier. It is the starting point or the place of origin for the delivery process. FedEx requires an accurate shipper’s address to calculate the correct shipping cost.

If the shipper’s address is not configured correctly in the plugin settings, it can lead to shipping options being unavailable because then **[FedEx](https://www.pluginhive.com/fedex-shipping/)** will not be able to accurately calculate the shipping rates or determine the appropriate shipping services to offer.

**To resolve this issue,** it is important to review the Woocommerce FedEx plugin settings and ensure that the origin address is entered accurately. Double-check the street address, city, state, and postal code to make sure they match the actual location from where the shipments will be originating. Once the correct origin address is added, the shipping options should be visible to the customers on the WooCommerce cart & checkout page, allowing them to proceed with their orders.

* * *

### FedEx Shipping rates are disabled under the Rates and Services tab

To provide accurate shipping options and pricing information, the plugin needs to connect with FedEx and retrieve up-to-date rates based on factors like weight, dimensions, and destination. The plugin requires WooCommerce store owners to enable the **Real-time Rates** option, to get the most current shipping rates. If the option is not enabled, the plugin will be able to print shipping labels for the orders but the shipping rates will not get displayed.

To avoid this issue, you need to visit the plugin settings and navigate to the “**Rates and Services** ” tab. Look for the option to enable Real-time rates and make sure it is turned on. Once enabled, our plugin will be able to display valid shipping services for your selection during the checkout process.

* * *

### WooCommerce product weight & dimensions are not configured

When a WooCommerce product is created without weight and dimensions, it means that the necessary physical attributes required for shipping calculations are missing. **[All shipping carriers](https://www.pluginhive.com/carriers/)** typically rely on weight and dimensions to determine shipping rates and available shipping methods.

Due to the absence of weight and dimensions, FedEx will be unable to provide valid shipping methods at the WooCommerce checkout page.

To avoid this, you need to add approximate weight and dimensions for each product in your WooCommerce store. You can do this by editing the product details and filling in the appropriate fields for weight and dimensions. Once the correct weight and dimensions are added, you will be able to display shipping costs accurately and display valid shipping methods for your customers at checkout.

* * *

### Shipping service availability for specific countries

The concept of configuring specific shipping methods under “Rates and Services” applies both to international and domestic shipping. It allows WooCommerce store owners to customize their shipping options based on the requirements, preferences, or limitations of different countries or regions, as well as within their own country.

By configuring shipping methods based on specific countries or regions, merchants can effectively manage their logistics operations, optimize shipping costs, meet customer expectations, and ensure timely and reliable delivery across international and domestic locations.

* * *

If shipping rates are set appropriately for specific countries, it can lead to the “There are no shipping options available” message during checkout. For example, if you have specified the US, UK & India under the Specific Countries, then the plugin will not display any shipping services for other countries.

* * *

### Appropriate FedEx shipping services not selected in the Services Table under “Rates and Services”

FedEx shipping services vary from location to location. Certain shipping services like FedEx Ground do not apply to the island countries across the globe. In such cases, if you have not selected an alternate FedEx Air service, your cart and checkout page will display the “There are no shipping options available” message.

In order to avoid this, make sure you have appropriate shipping services selected for all the locations where you provide shipping. This will include both FedEx Ground & Air services.

* * *

### Conditional shipping – Minimum Order Amount configured within the plugin settings

**[WooCommerce FedEx Shipping Plugin](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** for shipping provides flexible options that let you display shipping methods only if certain conditions are fulfilled on the WooCommerce cart & checkout page. these features include “**Minimum Order Amount** ” which allows you to set a minimum order value that customers must reach in their shopping cart before they can proceed with FedEx shipping. 

If your customers are not able to fulfill the criteria the plugin will be able to display the shipping rates on the WooCommerce cart & checkout page.

**In order to avoid this** , we recommend reviewing your business requirements and setting the minimum order value based on your requirements only. If your business does not require a minimum order value to calculate shipping, ideally you should keep the feature unchecked.

* * *

### Incorrect destination address entered by the customer

Shipping carriers like **[FedEx](https://www.pluginhive.com/fedex-shipping/)** require both the shipping address and the customer’s address to calculate accurate shipping rates. If a customer enters an incorrect address at the checkout, the “There are no shipping options available” message.

To avoid this, double-check the address for accuracy, including street names, numbers, city, state, and postal code. Using standardized address formats and verifying with official sources can help ensure successful delivery.

* * *

### Inaccurate combination of FedEx Special Services

FedEx provides some special shipping services that give additional control to its shippers. These special services include:

  * Shipment Liability Coverage
  * Delivery Signature
  * Dry Ice Shipping for Perishable Products
  * Wine/Alcohol shipping
  * HazMat shipping

and many more.

It often happens that WooCommerce store owners configure multiple special services that are generally not supported by FedEx.

To avoid this, we recommend you check the appropriate special services applicable to your business requirements. You can determine if a certain FedEx Special Service is applicable to your business requirements or your chosen origin and destination by visiting the official FedEx website and navigating to the Special Services page.

You can look for information regarding the supported origins and destinations. FedEx should provide details about the service coverage, including which countries or regions are supported. If your chosen origin and destination are supported, you can proceed with the appropriate Special Services option and the plugin will display accurate FedEx shipping rates to your customers.

If you cannot find the required information on the FedEx website, it’s advisable to directly contact FedEx customer support for more specific and up-to-date assistance. They will be able to provide you with accurate information regarding the support for your chosen origin and destination.

* * *

## Conclusion

We hope this article has helped you solve the ‘There are no shipping methods available’ error message. We also showed you how the **[WooCommerce FedEx Shipping plugin](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** helps you set up the desired shipping methods and prices on your WooCommerce store.

If you need any help setting up WooCommerce shipping on your store then feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**.

[ Previous  FedEx Hold At Location at WooCommerce Checkout  ](https://www.pluginhive.com/knowledge-base/fedex-hold-at-location-at-woocommerce-checkout/)

[ Next  WooCommerce Currency Conversion – FedEx Europe  ](https://www.pluginhive.com/knowledge-base/woocommerce-currency-conversion-fedex-europe/)
