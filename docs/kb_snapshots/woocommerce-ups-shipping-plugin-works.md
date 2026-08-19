# WooCommerce UPS Shipping Plugin and How it works?

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-ups-shipping-plugin-works/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce UPS Shipping Plugin and How it works?

In this article, we will show you how [**WooCommerce UPS Shipping plugin with Print Label**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) works. It covers the functionalities like UPS real-time shipping rates, shipping labels, **[live UPS tracking](https://www.pluginhive.com/live-tracking-updates-and-ups-freight-rate-calculation-woocommerce-ups-shipping/)** , and much more.

It is expected that the reader knows how to install the plugin. For more information on “How to install and set up the plugin,” kindly browse through our **[Setting Up WooCommerce UPS Shipping Plugin](https://www.pluginhive.com/knowledge-base/setting-woocommerce-ups-shipping-plugin/).**

Assuming that the plugin has been installed, let us understand it point by point.

  1. **Fetches Real Time Shipping Rates:  
**Woocommerce UPS shipping plugin enables one to fetch shipping rates directly from UPS so that there is no need to manually go to the website and check every shipment’s shipping rate. Suppose we go to the WooCommerce UPS plugin-enabled website, let us select a product and then place an order. On placing an order, we get to the cart page, where we can see the “Calculate Shipping” button. On giving address details, the plugin sends this information to the UPS. And for a particular sender and recipient address, the UPS returns the possible shipping services with their rates. The flow can be explained as follows:  
Place an order with valid recipient address --> the plugin requests the UPS for appropriate rates --> the UPS responds with various services and rates applicable for this order --> customer can see these services & rates on the cart page. This whole process is referred to as – **Fetching of real-time rates**. In the snapshot below, we can see that, based on the address, the UPS has returned the shipping rates and services.Cart
  2. **Prints Labels :**  
This plugin has a feature through which one can print labels for each order as an automatic process. The shop owner does not have to go to the UPS website and manually type in the details for generating labels. The address details will automatically be fetched from the order details on printing a label. This step can be explained as follows:  
Once the order is made, we can go to that particular order and select a button at the top right-hand corner called “Confirm Shipment”.

On pressing the “Confirm Shipment” button, the plugin will generate the shipping labels and invoice (for international orders only) as shown below:

Now, we see every other detail is taken care of by the plugin. We only have to generate packages and confirm shipment. We have printed the sample label for you by clicking on the “Print Label” button.

Shipping Label
  3. **Shipment Tracking:  
** Tracking of shipment is a very simple process. The tracking ID generated during print label is provided in the UPS Shipment tracking box. We get tracking information as soon as we press the “Save/Show Tracking info,” as shown below:UPS Shipment Tracking

**Note :**

     * Tracking information is displayed in the Live environment only. In the test environment, UPS shipment tracking will not display any tracking details as it would require a live tracking ID for a genuine order.

Once the rates are fetched from the UPS, the order is placed and print label generated, the shop owner has to complete the order so that the order completion e-mail can be sent. This can be done by going to the admin section --> Selecting WooCommerce --> Selecting orders and then selecting the order number. The snapshot below shows the path:

  4. Once the order page opens, we see a drop-down menu called ‘Order Status”. To complete the order, the shop owner has to mark it as “Completed order” in “Order Actions” tab towards the top right-hand corner.
  5. This will change the “Order Status” to “Completed”. As soon as you mark the order as completed, the plugin will send the tracking details attached to the order completion email.
  6. Now, we have covered a high-level end-to-end working of the product!

Also, check out our **[UPS Shipping plugin review at Cloudways](https://www.cloudways.com/blog/woocommerce-ups-shipping-plugin/)**.

[ Previous  Setting Up WooCommerce UPS Shipping Plugin  ](https://www.pluginhive.com/knowledge-base/setting-woocommerce-ups-shipping-plugin/)

[ Next  Advanced Add-Ons to Extend WooCommerce UPS Shipping Plugin’s Functionality  ](https://www.pluginhive.com/knowledge-base/advanced-add-ons-to-extend-woocommerce-ups-shipping-plugins-functionality/)
