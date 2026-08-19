# It always seems to overlook the FedEx Ground and not include it as an option at checkout

**Source:** https://www.pluginhive.com/knowledge-base/always-seems-overlook-fedex-ground-not-include-option-checkout/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# It always seems to overlook the FedEx Ground and not include it as an option at checkout

In this guide, we will help you solve the issue where **[WooCommerce shipping plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** seems to overlook **[FedEx Ground](https://www.pluginhive.com/fedex-ground-shipping-for-woocommerce-users/)** and not include it as a shipping option at the Checkout. We will also show you how **[Shopify shipping App for FedEx](https://apps.shopify.com/fedex-shipping)** can help you display FedEx Ground on the Checkout page.

FedEx Ground delivers items within the U.S., and from the U.S. to Canada and back. Making it a viable option for store owners looking to ship their products at a cheaper shipping rate. Surprisingly, many users prefer using this service over **[FedEx Express Saver](https://www.pluginhive.com/fedex-express-saver-guide-for-woocommerce-users/)** , which is considered as the value-for-money service.

* * *

## Display FedEx Ground on WooCommerce Cart/Checkout pages

WooCommerce users who would want to provide FedEx Ground could use the WooCommerce shipping plugin for FedEx. It shows **[live FedEx shipping estimate](https://www.pluginhive.com/determine-fedex-shipping-estimate-for-your-woocommerce/)** , allows you to print generate and shipping labels, offers shipment/order tracking, schedules FedEx Pickups for you, and much more.

But many new users find it difficult to show FedEx Ground on their Cart/Checkout page. Let’s take a real-life example of one of our customers facing a similar issue.

* * *

### A real-life example

#### **Customer**

I have FedEx Ground, FedEx Express Saver, and FedEx Priority Overnight all enabled, but it always seems to overlook FedEx Ground and not include it as an option at checkout. Do you know why?

#### **PluginHive Support**

The WooCommerce shipping plugin for FedEx**[determines FedEx shipping rates](https://www.pluginhive.com/determine-fedex-shipping-estimate-for-your-woocommerce/)** based on the following basic metrics.

  * Sender address
  * Recipient address
  * Product weight and dimensions

Moreover, the FedEx shipping plugin shows only those services which are returned by the FedEx API. So we request you to kindly check whether you are getting FedEx ground on official **[FedEx Rate Finder](https://www.fedex.com/ratefinder/home)** or not.

If you are able to see the service there then kindly provide us with the following information.

  * Screenshot of the FedEx Rate Finder page
  * And, the Debug Request and Response

#### **Customer**

Thanks for the info. I’ve attached the FedEx Rate Finder screenshot. I guess the difference in price is explained by them using dimensional weight and by entering the actual weight. Either way, it shows up in their calculator. Have a look.

#### **PluginHive Support**

The FedEx Rate Finder screenshot states that you are shipping domestically. However, in the debug request, we can see that you are shipping internationally. This is the reason for the different service returned by our plugin and the FedEx Rate Finder. We would request you to check the same details in both FedEx Rate Finder and in the plugin.

#### **Customer**

My browser starts off with Belgium, yes. So I’m not sure why the Debug isn’t updating. I change the address to Georgia, and Atlanta, and the shipping box updates, but it doesn’t include FedEx Ground.

#### **PluginHive Support**

You have selected the residential option in the FedEx plugin settings. Doing this will allow FedEx to consider every ship to address as residential. And This is why you were not able to see FedEx Ground.

When we uncheck the residential option, we were able to see the FedEx Ground service on your Cart/Checkout page. Also, we are assuming that you want to set FedEx Ground service as free, then in that case (-100%) price adjustment should be made in the plugin settings.

**Note:** FedEx Ground service generally comes up for the commercial address. You have the **[FedEx Home Delivery for residential deliveries](https://www.pluginhive.com/fedex-ground-shipping-for-woocommerce-users/). **

* * *

### **Bonus Tip**

**For Address Validation Request and Response**

We notice that you are getting an **authentication failed** error for address validation. The Address Validation service identifies whether the address is commercial or residential. To get accurate rates it’s a good practice to have the Address Validation service.

Address validation is an advanced FedEx service, that requires authorization from FedEx. You need to contact FedEx support and kindly check the following link for the **[FedEx guidelines for advanced services](https://www.fedex.com/us/developer/downloads/pdf/CertificationGuidelines2016.pdf). **You may also follow the guide and get yourself a working **[FedEx Production credential](https://www.pluginhive.com/get-fedex-production-credentials-enable-shipping-labels/).**

* * *

## Display FedEx Ground on the Shopify Checkout page

If you’re a Shopify user, you can display real-time FedEx Ground rates with **[Shopify shipping app for FedEx](https://www.pluginhive.com/product/shopify-fedex-shipping-app-with-print-label-tracking/). **It’s a wonderful App that helps in providing a complete FedEx shipping experience. You can print FedEx shipping labels in bulk, enable order tracking your orders, automate **[FedEx international shipping](https://www.pluginhive.com/fedex-international-shipping-guide-for-woocommerce-users/)** , and a lot more.

Once you have set up the Shopify shipping App for FedEx, you should be able to select **FedEx Ground** under the Rates option. Refer to the image above. Now if you go to your store page and move an item into the Cart then you should be able to see the rates.

The Shopify shipping App for FedEx lets you enjoy all benefits FedEx has to provide based on your FedEx account. It supports FedEx Negotiated Rates, **[FedEx One Rates](https://www.pluginhive.com/knowledge-base/save-shipping-cost-using-fedex-one-rate/)** , **[FedEx Pickup, FedEx Saturday services](https://www.pluginhive.com/fedex-pickup-and-special-delivery-options-for-your-woocommerce-shipments/),** and more. To know more, check out the Shopify shipping App for FedEx at Shopify Store.

* * *

## Conclusion

In this guide, we showed you how to solve the issue where **[WooCommerce shipping plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** seems to overlook **[FedEx Ground](https://www.pluginhive.com/fedex-ground-shipping-for-woocommerce-users/)** and not include it as a shipping option at the Checkout. We also saw how **[Shopify shipping app for FedEx](https://www.pluginhive.com/product/shopify-fedex-shipping-app-with-print-label-tracking/)** offers real-time FedEx Ground shipping rates on the Checkout page.

If you have any queries regarding this guide or FedEx shipping then feel free to **[contact us](https://www.pluginhive.com/support/)**. Our support team will help you solve any issue in no time.

**_Happy selling!_**

[ Previous  How to Resolve Authentication Error with FedEx Production Keys  ](https://www.pluginhive.com/knowledge-base/keep-getting-authentication-error-trying-3-different-fedex-production-keys-site/)

[ Next  Debug Error: [HighestSeverity] => ERROR  ](https://www.pluginhive.com/knowledge-base/shipping-method-doesnt-show-can-see-error-highestseverity-error-notifications-stdclass-object/)
