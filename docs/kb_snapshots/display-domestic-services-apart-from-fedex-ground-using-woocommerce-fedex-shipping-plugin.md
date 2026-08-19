# How to Display other Domestic Services apart from FedEx Ground using WooCommerce Shipping plugin for FedEx

**Source:** https://www.pluginhive.com/knowledge-base/display-domestic-services-apart-from-fedex-ground-using-woocommerce-fedex-shipping-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# How to Display other Domestic Services apart from FedEx Ground using WooCommerce Shipping plugin for FedEx

In this guide, we’ll help you display other domestic services apart from FedEx Ground when using **[WooCommerce Shipping plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)**. We will use a real-life business case as an example to explain to you the situation better.

## The Business Case – Displaying other Domestic services apart from FedEx Ground

The **[WooCommerce Shipping plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** is the only WooCommerce solution that provides end-to-end FedEx shipping experience. The extensibility of this plugin translates to seamless user experience for both you and your customers. This includes displaying real-time shipping rates from FedEx on the Cart/Checkout page.

Some users, however, especially the ones who are new to the plugin, often find it difficult to set up and fail to display the correct shipping method. This usually happens during the first installation process and is absolutely okay. After all, getting along with a new setup and learning the process takes time. 🙂

One of our recent customers was facing a similar issue and wanted our help. Let’s check out her query.

> _Hello. How would the user know which shipping option is being displayed? I’m able to see FedEx Ground on the cart page but no other domestic services. Also, how would we set the shipping options so that the default shipping options is always FedEx Ground?_

## Solution using WooCommerce Shipping plugin for FedEx

The **[WooCommerce Shipping plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** allows you to display shipping services based on your choice. So if your business demands overnight deliveries then you may select the FedEx Overnight services. Following are steps to ensure you’re providing correct shipping services.

#### Make sure you’re displaying all the returned rates/services

Under the plugin settings, you will find the option called **Offer Rates.** Here you must ensure you have selected ‘Offer the customer all returned rates’ instead of ‘offer the customer the cheapest rates only, anonymously’. Please refer to the image attached below.

Another way to ensure the services listed on the Cart page are exhaustive is to check the XML Request and Response. Usually, for domestic services in the United States of America, you should look for the following set of services under the XML Response.

**– GROUND_HOME_DELIVERY**  
**– FEDEX_2_DAY_AM**  
**– FEDEX_2_DAY**  
**– STANDARD_OVERNIGHT**  
**– PRIORITY_OVERNIGHT**  
**– FIRST_OVERNIGHT**  
**– STANDARD_OVERNIGHT**

#### Set the preferred shipping method as default

The shipping methods will be displayed in the order you arrange them in your plugin settings. You can place the FedEx Ground service as the first method in the plugin settings by drag & drop feature. Take a look at the image below for reference.

#### Choosing between FedEx Ground and FedEx Home Delivery

By default, FedEx provides the **FedEx Ground** service only for Commercial addresses and **FedEx Home delivery** for Residential address.

Once you decide which address type you’re delivering to, you can choose between Commercial or Residential in the plugin settings. For that, you can enter the plugin settings check. If the address is Commercial, then check if you have enabled ‘Default to Residential address’ option. If yes, then all address will be considered as Residential and only FedEx Home Delivery method will be returned by the FedEx API.

Read more about **[FedEx Ground](https://www.pluginhive.com/fedex-ground-shipping-for-woocommerce-users/)** and **[FedEx Home Delivery](https://www.pluginhive.com/what-is-fedex-home-delivery-a-guide-for-woocommerce-shopify-users/)** to understand the difference better.

## Conclusion

That’s it! We hope this guide would have helped you display domestic services apart from FedEx Ground on your Cart/Checkout page when using **[WooCommerce Shipping Plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)**. Please check out the product page to know more about other cool features.

If you have any doubts or need help setting up FedEx shipping on your WooCommerce-based website then feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**. Our support team should be able to help you out.

_**Good luck! 😊**_

[ Previous  How to Generate FedEx B13A Document for Canada Exports using WooCommerce Shipping FedEx Plugin  ](https://www.pluginhive.com/knowledge-base/generate-fedex-b13a-document-for-canada-exports-using-woocommerce-fedex-shipping/)

[ Next  Ship Certain Items with FedEx and Provide Flat-Rate Shipping for others with WooCommerce FedEx Shipping Plugin  ](https://www.pluginhive.com/knowledge-base/ship-certain-items-with-fedex-and-provide-flat-rate-shipping-for-others-using-woocommerce-fedex-shipping-plugin/)
