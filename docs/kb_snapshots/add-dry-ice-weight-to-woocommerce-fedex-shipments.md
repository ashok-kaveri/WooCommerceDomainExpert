# How to Ship Frozen Food With WooCommerce FedEx Plugin

**Source:** https://www.pluginhive.com/knowledge-base/add-dry-ice-weight-to-woocommerce-fedex-shipments/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# How to Ship Frozen Food With WooCommerce FedEx Plugin

When shipping perishable goods like frozen food or medicine, dry ice is a popular choice. With the [**WooCommerce Shipping plugin for FedEx with Print Label**](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/), users can seamlessly ship frozen food with dry ice directly from their WooCommerce store.

In this guide, we will discuss how to set up dry ice weight and attach it to FedEx shipments with the WooCommerce plugin. To get started, let’s examine a straightforward business scenario. 

* * *

## WooCommerce Dry Ice Shipping with FedEx

Online store owners, nowadays, sell all kinds of products thanks to WooCommerce. But certain products/items are shipped frozen and are perishable by nature. These types of products require **Dry Ice** for shipping and thus need special care. According to John, a WooCommerce store owner,

> _“Hello. I have a meat shop and these are frozen and perishable products. The problem is if the product quantity changes then the amount of dry ice weight needed will change. For example, if someone orders 6 pound of meat then 1 pounds of dry ice is needed. 30 pounds requires about 5 pound of dry ice. If there were a way to add 5 lbs dry ice weight then that would solve the problem. Is there a way to get the dry ice weight added in your WooCommerce Shipping plugin for FedEx with Print Label?”_

* * *

The**[WooCommerce Shipping plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/) **offers an in-built feature to let users ship their items via dry ice. You can find this option right in the plugin settings under **Special Services**. You need to enable the **Ship Dry Ice** option as shown in the screenshot below:

* * *

* * *

Now provide the exact Dry Ice weight for your products. First, include the product weight with the dry ice weight. Visit and edit the product page and enter the **Actual Weight** \+ **Dry Ice Weight**. See the screenshot below for reference:

* * *

* * *

Now under the FedEx Shipping Details add **Dry Ice Weight** as shown below:

* * *

Once done, you will see the following results:

  * **Rate Calculation** : FedEx API will calculate the shipping rates based on the weight value that is configured under the **Product edit page→** **Shipping→ Weight.**
  * **Shipping Label** : Now, on the FedEx label, you will see two weight values displayed, one of which is the **ACTWGT** (actual weight) value and the other is the **Dry Ice** weight value in KG.

Now coming back to the business case where John wants to add one-third(0.33) of the total weight of his products as Dry Ice weight to his shipments. So he can calculate one-third of the weight of his product, and add it to the actual weight.

Now let’s say, 30 packs of meat weigh 30 pounds. So he has to set:

  * Product weight as 35 under the **Product edit page → Shipping → Weight**
  * Dry Ice weight as 0.33 under **FedEx Shipping Details → Dry Ice (FedEx)**

After the configuration you will be able to see the rates at the WooCommerce Checkout as shown below:

* * *

* * *

Now, on the FedEx label, the “Actual weight” will be displayed as 35 LB and Dry Ice weight as 2.27 KG (which is 5 LB). Here have a look at the sample FedEx Shipping label:

* * *

* * *

To track your shipped orders, click on the **Shipment Tracking ID** under FedEx Shipment Label as shown below:

* * *

* * *

Now you can track your orders in real-time on the FedEx website:

* * *

## Summary

So in this article, we discussed how to include Dry Ice weight for your perishable products using the **[WooCommerce Shipping plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)**. 

If you have any doubts or need help setting up FedEx Shipping on your WooCommerce-based website then feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**. Our support team should be able to help you out. 

**Good Luck!**

[ Previous  Ship Certain Items with FedEx and Provide Flat-Rate Shipping for others with WooCommerce FedEx Shipping Plugin  ](https://www.pluginhive.com/knowledge-base/ship-certain-items-with-fedex-and-provide-flat-rate-shipping-for-others-using-woocommerce-fedex-shipping-plugin/)

[ Next  WooCommerce FedEx Shipping Rates in Multiple Currencies  ](https://www.pluginhive.com/knowledge-base/provide-woocommerce-fedex-shipping-rates-in-multiple-currencies/)
