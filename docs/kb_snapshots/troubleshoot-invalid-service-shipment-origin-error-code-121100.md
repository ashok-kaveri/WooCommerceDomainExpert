# Troubleshoot – Invalid Service for Shipment Origin [ Error Code:121100]

**Source:** https://www.pluginhive.com/knowledge-base/troubleshoot-invalid-service-shipment-origin-error-code-121100/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Troubleshoot – Invalid Service for Shipment Origin [ Error Code:121100]

In this small guide, we will help you troubleshoot one of the most common issues that users face when using the WooCommerce UPS Shipping Plugin with Print Label, i.e, invalid service for shipment origin[Error Code:121100].

While using the UPS Shipping plugin with Print Label, you might have come across some sort of issues. Take a look at the issue faced by one of the customers:

> _After upgrading to the latest version of the plugin, we are getting the following error when generating our shipping labels:_
> 
> _The requested service is invalid for the shipment origin [Error Code: 121100]_

This error generally occurs when there is some mistake on the store owner’s side while configuring the plugin. As the description of the error suggests, the following can be the possible reason for this code:

  * Invalid UPS Service based on the origin address
  * Invalid UPS service selection while confirming the shipment

* * *

## Troubleshooting the Error

To find out why this error is coming you need to check for a few things first:

  * **Check origin Address**

  * **Check UPS Services available from your address (Origin Address)**

You need to check which UPS Services are available from your address before selecting the Shipping Services option in the UPS plugin. You can [**check all possible UPS Shipping services available from the origin address as well as to the place where you are shipping, here.**](https://wwwapps.ups.com/ctc/request)

Below is an image showing where you can check for UPS Services present for both your address and the customer’s address.

  * **Select the valid UPS Services in the UPS Shipping plugin**

When setting up the UPS Shipping plugin, make sure to select those options that are available from your address only. Also, make sure to check the same for the destination address too. Selecting those services which are not available between the source and destination address can cause an error.

Below is an image showing where you can select the UPS Shipping services:

  * **Make sure not to select invalid UPS Services while confirming shipment on the WooCommerce Orders page.**

One of the mistakes that some store owners commit is that while confirming the shipment in the WooCommerce Orders page, they select invalid UPS Service. This doesn’t let the shipment being confirmed and the error is shown. The image below shows where the store owners might select the invalid shipping service:

Hence these were some of the things to keep in mind when the above-mentioned error message is displayed.

[ Previous  Add Handling Charges to WooCommerce UPS Shipment  ](https://www.pluginhive.com/knowledge-base/how-to-add-handling-charges-ups-shipment/)

[ Next  Print UPS Shipping Label for WooCommerce Orders  ](https://www.pluginhive.com/knowledge-base/print-ups-shipping-label-for-your-woocommerce-orders/)
