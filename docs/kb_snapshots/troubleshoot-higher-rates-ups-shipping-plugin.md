# Troubleshoot- Getting Higher Rates in UPS Shipping Plugin..!

**Source:** https://www.pluginhive.com/knowledge-base/troubleshoot-higher-rates-ups-shipping-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Troubleshoot- Getting Higher Rates in UPS Shipping Plugin..!

This article will help you achieve the most accurate shipping rates when using the [**WooCommerce UPS Shipping Plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/). If you are not sure about the accuracy of the shipping cost returned by the plugin, double-check them using the [**UPS shipping calculator**](https://wwwapps.ups.com/time). Enter the same package details into the calculator and compare the prices.

This will help you pinpoint any mismatches between the rates shown by the plugin and your UPS account’s actual rates.

* * *

## Reasons for UPS Shipping Rates Mismatch

Discrepancies in the shipping cost can arise due to a lot of reasons, such as:

  * UPS Negotiated Rates Enabled/Disabled Within the Plugin Settings
  * UPS Tax on Rates Enabled/Disabled Within the Plugin Settings
  * The Type of Destination Address (Residential or Commercial)
  * Different Ways to Pack Your Products
  * Shipment Insurance
  * UPS Special Services Like Cod or Delivery Confirmation
  * Opting for UPS Pickups & the Type of Pickup
  * The Difference in the APIs Used by the Plugin and UPS Rate Calculator

* * *

### **UPS Negotiated Rates Enabled/Disabled Within the Plugin Settings**

Negotiated Rates are the discounted rates provided by the UPS are based on the merchant’s shipment volume

To check the negotiated rates option in the WooCommerce UPS Shipping plugin settings, go to **Settings > Shipping > UPS > General > Negotiated Rates** as shown below:

* * *

For the most accurate rates, set **Customer Classification** to **Rates associated with Shipper Number**.

To set **Customer Classification** , go to **Settings > Shipping > UPS > Rates & Services** as shown below:

* * *

### **UPS Tax on Rates Enabled/Disabled Within the Plugin Settings**

Taxes applied to some shipments will also cause a mismatch in the rates shown on the checkout page. The nature of the product and the address of your customer determines the taxes applied to the shipment.

To make sure this doesn’t raise any issues with the rates returned by the plugin enable the **Tax on Rates** under the **Rates & Services** setting.

The image below shows how you can help with taxes for the rates returned by the plugin:

* * *

### **The type of Destination Address (Residential or Commercial)**

Since the UPS API automatically checks if the address entered is a **Residential or Commercial Address**. Shipping to a residential address costs more than shipping to a commercial address.  
However, the WooCommerce UPS Shipping plugin provides the option where, if you ship to Residential Addresses only, you can enable the “Residential” option under**Plugin** **General** settings.

* * *

Also, UPS rate mismatch can happen due to incorrect Shipper & Recipient Addresses. Hence, make sure that you configured it correctly. While checking in the official UPS rates calculator enter the correct residential address to compare the rates with the WooCommerce UPS Shipping plugin

  * [Refer to this article](https://www.pluginhive.com/knowledge-base/troubleshooting-woocommerce-ups-plugin/) for more details on how to add correct shipping addresses and other shipping details to get the correct ups rates

* * *

### **Different ways to pack your products**

The way you pack your products can easily result in a shipping cost mismatch. To help you set up a personalized packaging method, the WooCommerce UPS Shipping plugin supports parcel packing methods like:

  * **Pack Items Individually**   
If you want to pack your products separately, no matter their size, you can use this option.  
Remember, this can result in higher costs as UPS charges more based on the number of boxes. 
  * **Pack Into Boxes With Weights and Dimensions  
** If you want to pack multiple products in a single package, you can use this option. It uses the weight and the dimensions of the products to find a suitable box/package. Make sure to provide the weight and dimensions of your product, as it is essential to choose the right box.
  * **Weight-Based: Calculate Shipping based on Order’s Total Weight  
** Using Weight-based packing differs from business to business. This option uses the total weight of the package as the parameter to calculate the shipping cost. There are no restrictions on the number of items packed until the weight is under the maximum limit set by the store owner. Until the weight is under the set limit, all the items will be packed inside a single box and no other box will be used for packing.

You can select your preferred packaging method by visiting the **Plugin Packaging Settings** as shown below 

* * *

### **Shipment Insurance**

Enable the **Insured Value** option in the plugin setting to add insurance coverage for the products you ship. This will give you financial protection against the damage, loss, or theft of your shipments.

* * *

### **UPS Special Services like COD or Delivery Confirmation**

WooCommerce UPS Shipping plugin supports UPS special services like:

  * **UPS Import Control:** It allows you to import, & initiate UPS international shipments and have those shipments delivered to your business address or to an alternate location.  
**For more details** : https://www.ups.com/us/en/support/international-tools-resources/ups-import-control.page 
  * **UPS COD** : This special service enables you to collect payment in terms of cash from the customers after delivering the orders.
  * **UPS Saturday Delivery** : You can deliver your orders on weekends with UPS Saturday Delivery.
  * **UPS Delivery Confirmation:** This special service enables you to confirm your order deliveries in terms of signatures.

If you want to get the most accurate shipping rates including all the special services applicable to your business, make sure that you enable these service options under the Special Services tab in the UPS Shipping plugin as shown below.

* * *

### **Opting for UPS pickups & the type of pickup**

If you opt for UPS pickup services, you will be charged an additional fee based on the type of pickup you have opted for. Select the appropriate combination of “**Rates based on pickup type** ” and “**Customer classification** ” options based on your account, as shown below.

* * *

## Different APIs used

One thing worth noticing is that there may be a slight difference in the official quotations and the rates of the UPS Shipping plugin. This difference may range from a few cents to $1. The reason behind this is that the official website uses a different API than the UPS Shipping plugin to get real-time rates.

[ Previous  Weight-based Packing with WooCommerce UPS Shipping plugin  ](https://www.pluginhive.com/knowledge-base/weight-based-packing-ups-shipping-plugin/)

[ Next  Why UPS Shipping Methods are not listed under WooCommerce Shipping Zones?  ](https://www.pluginhive.com/knowledge-base/ups-shipping-methods-not-listed-woocommerce-shipping-zones/)
