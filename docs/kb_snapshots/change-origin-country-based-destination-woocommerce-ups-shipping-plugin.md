# WooCommerce UPS Shipping Rate for US-US & Europe-Europe

**Source:** https://www.pluginhive.com/knowledge-base/change-origin-country-based-destination-woocommerce-ups-shipping-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce UPS Shipping Rate for US-US & Europe-Europe

[**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) is one of the best shipping plugins. It provides advanced features such as real-time shipping rates, UPS domestic and international shipping labels, shipment tracking, and much more. However, no matter the features that it provides, WooCommerce store owners can come up with some really interesting scenarios that can challenge the functionality of the plugin. A similar thing happened when one of our customers requested to add functionality to the plugin.

According to Jesper, “… _**I have a shipping location in the USA and one in Europe. Can your UPS plugin add-on calculate ups rates from each origin, and only show shipping rates from the****US to the US****, and only Europe to Europe..?**_ ” Before getting to the end result, let us first try to understand what exactly needs to be done here.

## Jasper’s Request…

According to Jasper, he needs to be able to switch his origin address based on the address entered by his customer. This scenario can be achieved using the WooCommerce UPS Shipping plugin simply with the help of [**a code snippet published here.**](https://gist.github.com/xadapter/29ad029a778a5ee898ef76e050be45dc)

However, before placing the code, there is something that you need to take into consideration. The store owners may be using a **single or multiple UPS accounts** while shipping from separate origin addresses. The code provides a way to switch the UPS accounts as well as the Origin address based on the address provided by the customer on the checkout page.

Besides the UPS account and the origin address, there is one more thing that the store owners need to take care of. Different countries can have **different measurement units**. Hence, while changing the origin address, store owners will also have to update the measurement units in the code.

## Before the Code

The following image shows the Origin address that was set up by default in the plugin settings.

## After the Code

Once we provided the Canadian store’s address in the code, the updated Canadian Origin address is shown based on the destination address.

## Summary…

This article covers the process of changing the origin address based on the destination address provided by the customers. Using the WooCommerce UPS Shipping plugin and the code provided in the article, store owners will be able to switch between two UPS accounts and different origin addresses at the same time. This way they can optimize the shipping cost based on the address provided by their customers.

### About the Plugin

[**WooCommerce UPS Shipping Plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)

  * Official real-time UPS shipping rates.
  * Shipping rate Adjustment
  * Advanced packing methods
  * Print UPS Shipping Labels
  * UPS Shipment Tracking
  * Premium Version Cost – **$69**

[ Previous  Hide UPS Services for Shipments Weighing more than 10lbs and Show only FedEx  ](https://www.pluginhive.com/knowledge-base/hide-shipping-methods-based-total-order-weight/?seq_no=2)

[ Next  Adjust WooCommerce UPS Rates based on Destination Country  ](https://www.pluginhive.com/knowledge-base/ups-shipping-rate-adjustment-based-destination-country/?seq_no=2)
