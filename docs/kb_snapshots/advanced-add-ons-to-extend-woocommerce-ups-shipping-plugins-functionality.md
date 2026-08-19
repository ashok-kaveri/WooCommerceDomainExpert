# Advanced Add-Ons to Extend WooCommerce UPS Shipping Plugin’s Functionality

**Source:** https://www.pluginhive.com/knowledge-base/advanced-add-ons-to-extend-woocommerce-ups-shipping-plugins-functionality/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Advanced Add-Ons to Extend WooCommerce UPS Shipping Plugin’s Functionality

This guide provides you with the list of supported advanced add-ons plugins for the [**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/). It contains instructions on how to use these add-ons along with a real-world business scenario to help you understand the working of the plugins.

## List of Available Add-on Plugins

The add-on plugins supported for WooCommerce UPS Shipping plugin with Print Label:

  1. **Auto-Label Generation for UPS Freight add-on plugin**
  2. **Estimated Delivery Date Adjustment for UPS add-on plugin**
  3. **Disallow UPS Shipping for PO Box Addresses add-on plugin**

### 1\. Auto-Label Generation for UPS Freight

#### What does it do?

This add-on plugin allows you to generate **[UPS Freight Shipping Labels](https://www.pluginhive.com/ups-freight-a-guide-for-woocommerce-users/) **automatically for the shipments which you want to ship via UPS Freight Services. Using the plugin you can set a weight limit which will be used to differentiate the parcel shipments from the freight shipments. Based on this, the UPS Shipping plugin will generate the shipping labels automatically by identifying the shipments.

#### Pre-Requisites:

  * [**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) **[Version 3.10.13 or above]**
  * **Auto-Label Generation for UPS Freight**

#### Business Case:

**Automatically generate UPS Shipping Labels when providing Flat Rate Shipping for both UPS Freight and Parcel Shipments**

 _Most of our products are shipped as parcels and we require the shipping labels to print automatically. However, one of our products we need to ship via UPS Freight. We ship 150+ lbs using UPS Freight. Is there any way to print shipping labels automatically based on the products, i.e Parcel or Freight._

#### Solution:

Follow the steps below to set up **Auto-Label Generation for UPS Freight** :

  * Install [**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) and enable the Freight Services from the plugin settings
  * **Set the Parcel Packing Methods to Pack Items Individually**
  * Set up **Automatic Label Generation** for your Parcel Shipments. You need to select a **Default Domestic and Default International Shipping Services**
  * Install **Auto-Label Generation for UPS Freight plugin**
  * Visit the plugin settings
  * Set up a **Minimum Package Weight** in order to consider the shipments above that weight for Freight Shipment. This weight will be taken based on the store weight units (lbs or kgs).  
**For example: If your store weight limit is lbs, set the weight limit to 150.** This will allow you to automatically generate UPS Freight Shipping Labels for all packages weighing more than 150 lbs. However, all the packages below 150 lbs will still be considered for Parcel ShipmentsFreight Weight Limit
  * Set a **Default UPS Freight Service for Domestic Shipment.** This service will be used to generate a shipping label automatically for a domestic freight shipment
  * Set a **Default UPS Freight Service for International Shipment.** This service will be used to generate a shipping label automatically for an international freight shipment
  * Click on **Save Settings** to save the settingsDefault Shipping Service

* * *

### 2\. Estimated Delivery Date Adjustment for UPS

#### What does it do?

This add-on plugin allows you to set an adjustment for the UPS Estimated Delivery Date based on the number of days provided by the user. Moreover, it also allows you to set a list of holidays that should not be considered while calculating the final estimated delivery dates on the cart page.

#### Pre-Requisites:

  * [**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) **[Version 3.10.13 or above]**
  * **Estimated Delivery Date Adjustment for UPS**

#### Business Case

 _Provide 8 days adjustment for UPS Estimated Delivery Dates without taking into consideration the Weekends.__Since UPS already considers the holidays and weekends in the delivery dates that it provides, we require a way to set up an additional 8 days adjustment to the delivery dates. These 8 days must not take into consideration Saturdays and Sundays or any holiday and must be added to the delivery dates on the cart page._

#### Solution

Follow the steps below to set up **Estimated Delivery Date Adjustment for UPS** :

  * Install [**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) and enable the **Estimated Delivery Dates** from the plugin settings
  * Install **Estimated Delivery Date Adjustment for UPS** plugin
  * Click on settings
  * Set up your holidays or weekends that you want to skip from the estimated delivery date calculation by selecting the **Custom Date** **Range** or **Days Range** under the ****Range Type  
****Select Range Type
  * Choose the **Shipping Class** for which you want to provide additional delivery days and set the **Number of days**. These days will be added to the delivery date calculated by the UPS Shipping pluginSelect Shipping Class
  * Click on **Save Settings**

Rules Table

* * *

### 3\. Disallow UPS Shipping for PO Box Addresses

#### What does it do?

This add-on plugin checks for the combination of PO Box in the WooCommerce address fields, Address Line 1 and Address Line 2, and disallows the UPS Shipping methods for that order. Moreover, you can provide different combinations of PO Box addresses and the plugin will then check for that in the address fields also.

#### Pre-Requisites:

  * [**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)
  * [**Disallow UPS Shipping for PO Box Address**](https://www.pluginhive.com/tailor-made-woocommerce-shipping-solutions/#restrict_woocommerce_shipping_to_pobox_address)

#### Business Case:

**Do not want to ship to PO Boxes, hence, no need to display shipping methods on the checkout page**

 _We don’t generally ship to PO Boxes. however, some of our customers are placing orders and checking shipping options for the PO Boxes. We require some mechanism to not allow orders to the PO Boxes. Is it possible using the WooCommerce UPS Shipping plugin..?_

#### Solution:

Follow the steps below:

  * Install [**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)
  * Install [**Disallow UPS Shipping for PO Box Address add-on plugin**](https://www.pluginhive.com/tailor-made-woocommerce-shipping-solutions/#restrict_woocommerce_shipping_to_pobox_address)
  * Click on **Settings** to visit the add-on settings  

  * By default, the add-on will be set up with the following PO Box combinations that it will check and disallow the UPS Shipping method on the cart page
    * PO BOX
    * PO-BOX
    * P.O. BOX
    * P.O BOX
    * PO. BOX

  * Set up any combination of PO Box addresses in the **PO Box Name Combination** field in the settings and click on **Save Changes**
  * The plugin can also disallow other shipping methods for the PO Box addresses like **Free Shipping, Flat Rate Shipping or Local Pickup** , etc. All you need to do is add the shipping method value in the **Additional Shipping Methods** field.
  * Also, once the plugin disallows the shipping to the PO box addresses, you can set a custom message that will be displayed in the shipping tab on the checkout page, using the**Custom Checkout Message** field in the plugin settings. Here you can define any message based on your preferences that will be displayed to the customers.  
**Note:** If this field is kept empty, the default WooCommerce checkout message will be shown – No Shipping Methods found for the address.

* * *

## Final Thoughts…

[**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) is a one-stop shipping solution when it comes to UPS Shipping for your WooCommerce store. The plugin supports features like real-time UPS Shipping Rates, Automatic UPS Shipping Labels, UPS Shipment Tracking, and much more.

If you have any queries based on the plugins discussed above, or you have a complex booking scenario, feel free to contact our [**support team**](https://www.pluginhive.com/support/). We will try our best to help you find a solution and set up your online WooCommerce store.

[ Previous  WooCommerce UPS Shipping Plugin and How it works?  ](https://www.pluginhive.com/knowledge-base/woocommerce-ups-shipping-plugin-works/)

[ Next  How to Connect UPS with WooCommerce  ](https://www.pluginhive.com/knowledge-base/connect-ups-with-woocommerce/)
