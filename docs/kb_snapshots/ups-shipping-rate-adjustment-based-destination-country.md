# Adjust WooCommerce UPS Rates  based on Destination Country

**Source:** https://www.pluginhive.com/knowledge-base/ups-shipping-rate-adjustment-based-destination-country/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Adjust WooCommerce UPS Rates based on Destination Country

WooCommerce allows store owners to provide shipping rates to their customers. However, WooCommerce doesn’t provide a way to adjust shipping rates based on the destination. Generally, store owners require real-time shipping rates from the shipping giants like UPS, FedEx, Canada Post, etc. based on their preference. Still, they prefer some mechanism of shipping rate adjustment. This way they can easily provide discounts on shipping to those locations where the demand is higher. Further, it also allows them to add additional handling charges to the shipping cost.

One of the store owners also needed similar customization for his store. **Shameel owns an online auto parts store based in Sharjah, UAE**. He has prepared a customized shipping discounts list based on countries. According to Shameel, “** _I got the discounts list and it’s by country wise not state wise. I am not sure how to configure the discount on the shipping rates country-wise. Hope you can help with it. Kindly help me to configure soonest possible, your help in this regard is really appreciated._** ”

In this article, we will discuss how you can adjust WooCommerce UPS rates based on the destination country. It will cover a step-by-step guide to configuring Shameel’s business case using the [**WooCommerce UPS Shipping plugin.**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)

## Shipping Rate Adjustment

There are instances where store owners prefer to adjust shipping rates. By default, the WooCommerce UPS Shipping plugin provides a mechanism to adjust shipping rates. However, using this method, the shipping rate adjustment will be applied to all the shipping methods irrespective of the factors like destination country.

In the case of Shameel, he already has a dedicated shipping discount list where he has defined discount percentages for every country. So we need a solution that will help him adjust shipping rates based on the destination country. WooCommerce UPS Shipping plugin can help Shameel achieve his business requirements with the help of a code snippet.

### Working with the Code

Shameel can provide discounted shipping rates to his customers by adding the[**code from this link**](https://gist.github.com/xadapter/26554e4ec28f48b8599d30810b4dde58) to the following location,

**Appearance -- > Editor -->  _functions.php_ file**

However, based on his requirements he needs to do some changes to the code. To understand those changes, let’s discuss each of them separately.

  * **Shipping Method Values  
**The below image shows the field where you need to add shipping method values in the code. To get these shipping method values, you need to **Right Click** the shipping methods on the cart page and click on **Inspect**. There you will get the shipping method value for that method. You simply need to paste that value into the below field in the code.

Once you add the value(s) of all the shipping methods for which you need to adjust rates, the above code will look something like the image below.

  * **Country/State code**  
The store owners can use this code to adjust shipping rates based on both Countries as well as States. You just need to add the correct **Country or State Code**. The image below shows both cases.

Either you can specify for which state in a country you want to adjust the shipping rates or you can just simply use **‘*’** to adjust shipping rates throughout the country.

  * **Shipping Rate Adjustment values  
**One of the most important things worth noticing is that this code will help store owners add or remove a percentage of shipping costs. Hence, you need to add the **decimal values** in the code. For example, for an additional 20 percent handling charges, the amount would be **0.2** (20/100) instead of 20. Also, there are different sign conventions for discounts. The image below shows clearly that to provide a discount, you need to use the **‘-‘ sign.**

## 

## Shameel’s Shipping Scenario

To configure Shameel’s scenario, the following are the shipping rate adjustments that he wants to configure.

  * **In the US, customers should get a 40% discount across New York.**
  * **Throughout Canada, customers must pay 20% additional handling charges included in the shipping cost.**

For both the above cases, Shameel uses the following UPS International Shipping Services.

  * **UPS Worldwide Express ( with value ‘wf_shipping_ups:07’ )**
  * **UPS Worldwide Expedited ( with value ‘wf_shipping_ups:08’ )**

So based on the above information, he needs to add the shipping method values in the code. Also, he needs to change the Country and State Codes along with the shipping adjustments. The below image shows the code after configuring Shameel’s scenario.

Now let’s check shipping rates on the cart page.

### Cart Page

Once we have placed the code in the functions.php file, all we need to do is add a product to the cart and check the shipping rates. The images below show the shipping rates for both Canada (Ontario) and the USA (New York) before as well as after adding the code. It will help you to understand whether the code is working properly or not.

  * **Before adding the Code**

  * **After adding the Code**

* * *

For an easy understanding of the whole process, below is an attached tutorial video showing how store owners can make shipping rate adjustments based on destination country using the WooCommerce UPS Shipping plugin.

## Some benefits of Shipping Rate Adjustment

So far we discussed how a store owner can adjust his shipping cost in WooCommerce. Now let us discuss some scenarios where adjusting the shipping cost has really helped the store owners.

  * **Discounts on special occasions**  
It is during special occasions like Christmas and New Year, we expect online businesses to provide cheaper or free shipping to our doorsteps. For a store owner, the option to slash shipping rates on the go can definitely come in handy.
  * **Handling Charges**  
Most of the time, while shipping heavy items, the handling charges may add up to the shipping cost. In such cases, store owners can easily add those charges to the total shipping cost, so that they may not have to pay for the additional handling of the packages.
  * **Reduce Abandoned Carts**  
Almost every online store has faced the issue of abandoned carts. According to a [**study**](https://baymard.com/lists/cart-abandonment-rate), among so many reasons for the cart being abandoned by customers, high shipping rates serves as the biggest reason.

An online store facing a similar issue can make use of shipping rate adjustment to reduce, if not eliminate, customers leaving the carts empty.

##  Summary

So this article covers how store owners can make adjustments in the shipping rates based on the destination country. This way store owners can have customized shipping rates for all the UPS Shipping Services. **[WooCommerce UPS Shipping plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)** , on the other hand, provides tons of shipping services, along with real-time shipping rates and advanced features like shipping label and shipment tracking. With such a combination of personalization and accuracy, WooCommerce UPS Shipping plugin is a one-stop shipping solution for WooCommerce store owners.

* * *

If you have any queries regarding the WooCommerce UPS Shipping plugin and its features, I request you to please [**visit the official product page.**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) Or you can share your views regarding this article in the comment section below. I will surely help in clearing any doubts and queries regarding the plugin.

[ Previous  Ship Physical Products along with WooCommerce Subscription Products with the WooCommerce UPS plugin  ](https://www.pluginhive.com/knowledge-base/handle-shipping-standard-subscription-products-ease-using-woocommerce-ups-shipping-plugin/)

[ Next  WooCommerce Shipping – Managing Units of Measurement  ](https://www.pluginhive.com/knowledge-base/managing-units-measurement-shipping-woocommerce/)
