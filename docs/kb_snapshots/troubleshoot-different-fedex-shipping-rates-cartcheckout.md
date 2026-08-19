# Troubleshoot – Different FedEx Shipping Rates in Cart/Checkout

**Source:** https://www.pluginhive.com/knowledge-base/troubleshoot-different-fedex-shipping-rates-cartcheckout/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Troubleshoot – Different FedEx Shipping Rates in Cart/Checkout

Getting incorrect or different FedEx shipping rates on your Cart/Checkout page when using the WooCommerce Shipping Plugin for FedEx with Print Label? Don’t worry. This guide should help you troubleshoot it.

The [WooCommerce Shipping Plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/) is an amazing plugin that fetches the live rates directly from the FedEx Servers. It shows these rates based on the weight & dimensions of the shipment, destination address, taxes, and many other factors. It offers these rates based on the service that you have offered to your customers. For example, if the store owner has limited the FedEx services to domestic, then the international buyers won’t be able to buy the items from the store.

However, there are many real-life cases where our customers fail to get those rates. Let us look at one of the similar issues faced by our customers.

> Jean: I’m having some problems with the rate calculations with this FedEx shipping plugin for WooCommerce. These are the settings that I’m testing on my site:
> 
> Item price: 34.99 (Fedex rounds it to 35.00)  
>  Weight: 6 lbs  
>  Quantity: 1
> 
> The rates that I’m getting using the plugin is **FedEx First Overnight** : $108.05, but while checking on the FedEx Rate Calculator the rate is coming up to be **FedEx First Overnight** : $120.98.

There are a few things that a store owner should be checking first. One of them is to check whether the Request Type is selected as Account Rates as shown in the screenshot below.

Another case is when the user finds the rates to be different is when he or she is the test mode. Let us check out an example to understand this issue in a better way.

> Shirley: The rates I am getting on my website do not match the rates FedEx is providing. The plugin should be linked to the account and should be giving me the same rate I get when calculating on the FedEx website. The rates I am getting on my website is significantly higher than the rates FedEx gives.

This happens because the test servers do not return accurate rates. As it is a development server, it is unfortunately not updated to reflect the rates and/or discounts each specified by each customer. Customers primarily use the test server to ensure functionality of their application, but not the accuracy of rates returned. Accurate rates can only be retrieved from the production environment. To put it simply, you need to be in the production mode in order to show the correct rates.

* * *

We hope this article was useful to you in some way. Let us know in the comment section below if you have any query. You can [contact our customer support](https://www.pluginhive.com/support/) to get more assistance.

[ Previous  Extend the Estimated Delivery Day in WooCommerce FedEx Plugin  ](https://www.pluginhive.com/knowledge-base/extend-estimated-delivery-day-woocommerce-fedex-shipping-plugin/)

[ Next  Convert WooCommerce FedEx Shipping Rates to Base Currency  ](https://www.pluginhive.com/knowledge-base/convert-fedex-shipping-rates-base-currency/)
