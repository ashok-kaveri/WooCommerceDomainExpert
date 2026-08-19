# FedEx Address Validation & Residential Shipping for WooCommerce

**Source:** https://www.pluginhive.com/knowledge-base/fedex-plugin-woocommerce-button-switch-residential-shipping/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# FedEx Address Validation & Residential Shipping for WooCommerce

In this guide, we will help you understand how Address Validation and Residential Shipping work inside the **[WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** and **[Shopify Ship, Rate and Track for FedEx](https://apps.shopify.com/fedex-shipping)**. Read along to learn about it.

## Difference between a Commercial and Residential address

FedEx ships items to two types of locations—**Commercial/Business** and **Residential**. Commercial addresses are generally the locations that are considered commercial real estate. These locations are usually classified as a warehouse that has tractor-trailer access and a loading dock.

Residential addresses, on the other hand, are any business location that is operated from a home, apartment, or any other similar area where people live. Delivery trucks usually enter these areas to perform the final delivery. In addition, the overall shipping charges are slightly higher than that of commercial addresses.

For instance, **[FedEx Ground](https://www.pluginhive.com/fedex-ground-shipping-for-woocommerce-users/)** **charges $10 to deliver a package** while **[FedEx Home Delivery](https://www.pluginhive.com/fedex-ground-shipping-for-woocommerce-users/)** **charges $13 for the same address (residential) and package**.

To better understand this concept, let us take a real-life example. Here’s a business case by one of the WooCommerce store owners who use FedEx for residential delivery.

> Your WooCommerce Shipping Plugin for FedEx with Print Label provides an option for FedEx residential shipping. The documentation says that “If your account has address validation enabled, this will be turned off/on automatically.” But I have the following queries:
> 
>   * We have a FedEx account. How do we know if address validation is enabled for our account? I searched the website and could not determine if we have the service enabled.
>   * We ship to business and residential addresses. If we have FedEx address validation enabled and the checkbox in the settings is unchecked, depending on the address, will the shipping cost that is passed from FedEx be the residential or commercial delivery rate?
> 

* * *

## How does FedEx Address Validation work in WooCommerce

FedEx address validation service identifies whether the address is commercial or residential. To get accurate rates, it is a good practice to have the address validation service enabled for your account.

Address validation is an advanced FedEx service that requires authorization from FedEx. You need to contact FedEx support so that they can guide you through the entire process.

If you have FedEx address validation enabled, it does not matter whether you marked the address residential. FedEx API will validate the address on its own and return the rates for the address accordingly.

In case the FedEx API is under maintenance or facing downtime, we recommend enabling the ‘**Default to residential delivery’** option within the plugin settings to force the shipping address as Residential.

* * *

* * *

You can read more about **[FedEx residential delivery and FedEx Home Delivery](https://www.pluginhive.com/knowledge-base/use-fedex-home-delivery-residential-addresses/)**.

* * *

**_Read More_**   
  
  
[Use the FedEx Home Delivery service for your residential addresses](https://www.pluginhive.com/knowledge-base/use-fedex-home-delivery-residential-addresses/)   

* * *

## How does FedEx Address Validation work in Shopify

You can provide real-time FedEx shipping rates on your Checkout page using the **[Shopify Ship, Rate and Track for FedEx](https://apps.shopify.com/fedex-shipping)**. This intuitive shipping App provides end-to-end shipping by **[providing FedEx shipping labels](https://www.pluginhive.com/knowledge-base/bulk-shipping-label-generation-made-easy-with-shopify-fedex-app/)** , shipment tracking, FedEx pickup, and more. Check here to know more about it.

Coming back to the point, this App sends the request for a residential address check to FedEx API every time a customer enters an address in the Cart page. FedEx then checks for the address and validates the request if correct. It sends the valid shipping service along with rates back to the App which then displays on the Checkout page.

* * *

## Conclusion

In this article, we discussed how the FedEx Address validation works in FedEx and how it identifies a residential address. We also saw how the **[WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** and **[Shopify Ship, Rate and Track for FedEx](https://www.pluginhive.com/product/shopify-fedex-shipping-app-with-print-label-tracking/)** helps you do that on your store.

If you have any queries regarding this article then feel free to **[contact our customer support](https://www.pluginhive.com/support/)**. They would be more than happy to help you out and set up shipping on your online store.

_**Happy selling!**_

[ Previous  Debug Error: “Authentication Failed”  ](https://www.pluginhive.com/knowledge-base/debug-turned-fedex-response-says-authentication-failed/)

[ Next  Why does FedEx overnight deliveries shows Delivery – TUE instead of next business day, Monday?  ](https://www.pluginhive.com/knowledge-base/fedex-overnight-deliveries-showdelivery-tue/)
