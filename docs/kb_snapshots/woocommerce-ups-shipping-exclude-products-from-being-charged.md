# Exclude Gift Products from being Charged for UPS Shipping on your WooCommerce Store

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-ups-shipping-exclude-products-from-being-charged/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Exclude Gift Products from being Charged for UPS Shipping on your WooCommerce Store

This guide will discuss the **[WooCommerce UPS Shipping plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)** and show the steps to exclude certain products from being charged for shipping by UPS and offer Free Shipping instead.

## Business Case: Exclude products from being charged for UPS shipping

WooCommerce store owners have a variety of products on their store, some of which don’t require an applicable shipping cost. Store owners would rather prefer shipping such products for free to execute their business requirements. Let’s take a real business case to understand this better.

According to Mark, a WooCommerce store owner,

> _We are using WooCommerce UPS Shipping plugin and want to exclude “Gift Certificate” products from being charged for shipping. How do we put/assign Free Shipping option for such products? Ideally, if there are regular (not free shipping) products in the cart, the shipping amount should be for the products that have no free shipping._

### Solution using **WooCommerce UPS Shipping plugin**

The first and foremost step is to create two different WooCommerce Shipping Classes, say ‘Free Shipping’ and ‘UPS’. Have a look at the screenshot below for your reference.

As you can see, we’ve created two separate shipping classes under the Shipping classes section available under **WooCommerce → Settings → Shipping**.

Now, you need to assign the ‘Free Shipping’ class to **Test Product 1** (the product which requires Free Shipping) and ‘UPS’ class to **Test Product 2** (the product which requires UPS rates).

After assigning the two products to their respective shipping classes, it’s now time to skip the **Test Product 1**(Free Shipping products). For that, you need to go to the plugin settings and select the ‘**Free Shipping’** class under the ‘**Skip Products** ‘ field. Check out the image below for your reference.

Now you need to create a desired shipping zone under the **WooCommerce Shipping Zone** option in order to create the **Free Shipping** option. As you can see in the image below, we’ve created a shipping zone called **‘United States’** and added the **‘Free Shipping’** method.

The above steps will help you display skip UPS rate calculation for **“Gift Certificate”** products and also show the **‘Free Shipping’** method when Gift Certificates are alone in the cart. However, the point that needs to be noted is the **‘Free Shipping’** method will still be shown as an option for UPS products as well. So if you want to hide **‘Free Shipping’** for UPS products, then you can hide the **‘Free Shipping’** method based on the UPS shipping class using the **“Hide Shipping Methods”** plugin.

So the next step is to download and install the **[PH Hide WooCommerce Shipping Methods& Rate ](https://www.pluginhive.com/product/hide-woocommerce-shipping-methods-and-rate-adjustment/)Adjustments **by PluginHive. This plugin will help you hide shipping methods based on Shipping Class and Zone. It works in conjunction with any of the shipping plugins from PluginHive like FedEx, UPS, Canada Post, etc., You can check out the following video to see how this add-on [hide shipping methods based on different Shipping Classes](https://www.youtube.com/watch?v=xTvxNKZayGM).

Once done, your requirements will be fulfilled. You can see the respective results below:

#### Scenario 1

When Free shipping products are alone in the cart.

#### Scenario 2

When UPS shipping products are alone in the cart.

#### Scenario 3

When both Free shipping and UPS shipping products are together in the cart.

## Business Case: Manage third-party fulfillment while calculating UPS rates for products shipped internally

WooCommerce store owners have a lot of options when it comes to shipping their products. In some cases, the store owners may ship the products themselves. Sometimes, the store owners may have a third-party company shipping the products on their behalf. And there are cases when the store owners may be using a combined scenario, where the products are shipped by both the store owner and the third party.

However, in the above cases, it is very common to have slight confusion while shipping. In this article, we will be focusing on how a store owner can handle third-party fulfillment while calculating shipping rates for the products shipped by them. Let’s take an example of a WooCommerce store owner.

According to Michael, “ _**I am working with a third-party fulfillment company to process some of my orders. Currently, if I order my products the UPS shipping calculates correctly. If I add their product to the same order the UPS shipping never calculates. Is there a solution to this or some way to not use those specific products in the current calculations? The 3rd party fulfillment will ship the products from their site so I would not need to worry about them.**_ ”

### Solving Michael’s Issue using the WooCommerce UPS Shipping plugin

While using a third party to ship some of the products, one of the best ways to simplify the shipping is to use **[WooCommerce Shipping Classes](https://www.pluginhive.com/ultimate-guide-set-up-woocommerce-shipping-class/)**. So, Michael will have to create two shipping classes, one for the products that he handles internally, and the other one for the products shipped by the third party.

Now, after successfully differentiating between the products, Michael needs to calculate UPS shipping rates only for his products. In that case, the best possible solution would be to **skip calculation for any product handled by the third party, that may be in the cart**.

Using the code in [**this link**](https://gist.github.com/xadapter/63cbc9436939dada64972ce78c4b6c72), Michael can easily skip shipping calculations in case of all those products that are fulfilled and shipped by a third-party company.

## Summary

So in this article, we discussed a few examples to exclude some products from being charged for UPS shipping on a WooCommerce store using the **[WooCommerce UPS Shipping plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)** in combination with the **[Hide WooCommerce Shipping Methods plugin](https://www.pluginhive.com/product/hide-woocommerce-shipping-methods-and-rate-adjustment/) **by PluginHive.

If you have any doubts or need help setting up UPS Shipping on your WooCommerce-based website then feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**. Our support team should be able to help you out.

**_Good Luck!_ **

[ Previous  Display UPS Shipping Rates Based On WooCommerce Shipping Zones  ](https://www.pluginhive.com/knowledge-base/display-ups-shipping-rates-based-on-woocommerce-shipping-zones/)

[ Next  WooCommerce UPS Shipping – Can a Third-Party’s Account Pay the Shipping Charges?  ](https://www.pluginhive.com/knowledge-base/woocommerce-ups-can-third-party-ups-account-pay-shipping-charges/)
