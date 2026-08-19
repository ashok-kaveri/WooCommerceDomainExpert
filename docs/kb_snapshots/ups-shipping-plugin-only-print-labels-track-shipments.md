# UPS Shipping Plugin for Label Printing & Order Tracking in WooCommerce

**Source:** https://www.pluginhive.com/knowledge-base/ups-shipping-plugin-only-print-labels-track-shipments/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# UPS Shipping Plugin for Label Printing & Order Tracking in WooCommerce

Sometimes the customers do not want to provide UPS Shipping Rates for some specific regions. There can be different reasons for doing so. Especially when your business case demands the same. In such cases the UPS Shipping plugin can be used to just Print Shipping Labels and one of the important aspects of shipping, tracking the package.

Consider the following customer scenario:

> I would like to keep my WooCommerce Flat Rate setup and only use the UPS Shipping plugin for label printing and tracking.

As the customer wants that the **Flat Rate** option should be the default for his WooCommerce Store, the UPS Shipping plugin should not be used to calculate the shipping charges. Instead, the plugin must generate the shipping label based on the packages. Also, the plugin must generate tracking numbers so that the store owner and customers can track the shipment easily.

There is another scenario where the store owner’s business case involved using custom rates but needed UPS Shipping plugin to just print shipping labels. Take a look at the scenario:

> Our woo is already configured with table rate and yes we want to use the UPS only to generate the label. I just don’t know how to setup this with your tool as everything is related to API rates each time. Basically, I don’t need your any shipment option to appear for the customer in the front end, but only for admins in the back office. And to maintain our Shipping zones set up on WooCommerce.  
> And I can’t see how to set this up.  
> Do you have guidelines for this?

These scenarios can be achieved easily by following these steps:

  * As the real-time rates are not needed by UPS, disable the **Real-Time Rates** option from UPS settings.

Disabling UPS Real-time Rates

* * *

  * As the customer only wants UPS Shipping plugin to generate labels and track shipments, enable the **Label** **Printing** and Tracking options in the plugin settings. Also, you can enable **Automatic Label Printing** option in Advanced Setting.

Enable Automatic Label Printing

* * *

Enable Shipment Tracking

  * Set up the Flat Rates in WooCommerce Shipping Zones. For more details regarding Flat Rates,[**click here.**](https://docs.woocommerce.com/document/flat-rate-shipping/)

Once these steps are performed successfully, the UPS Shipping plugin will not show UPS rates to the customers. But once the customers place the order, all you have to do is **confirm shipment.**

After confirming shipment, the UPS Shipping plugin will generate the shipping label as well as the UPS tracking number. Hence, you will be able to print the shipping label and track your package without even using the plugin to generate real-time rates.

[ Previous  Residential or Commercial Address in WooCommerce UPS Plugin  ](https://www.pluginhive.com/knowledge-base/residential-commercial-address-ups-shipping-plugin/)

[ Next  How to Adjust the Size of UPS Shipping Label?  ](https://www.pluginhive.com/knowledge-base/adjust-size-ups-shipping-label/)
