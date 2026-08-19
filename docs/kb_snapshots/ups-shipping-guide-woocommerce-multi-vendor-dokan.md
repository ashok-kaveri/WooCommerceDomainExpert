# UPS Shipping Guide for WooCommerce Multi Vendor with Dokan

**Source:** https://www.pluginhive.com/knowledge-base/ups-shipping-guide-woocommerce-multi-vendor-dokan/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# UPS Shipping Guide for WooCommerce Multi Vendor with Dokan

In this article, we will show you how to fulfill orders using UPS on a WooCommerce Multi-Vendor store. We will be using Dokan to set up a multi-vendor store and use the [WooCommerce UPS Shipping Plugin with Print Label](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) to fulfill the orders.

Order fulfillment gets complicated when it comes to multiple vendors selling multiple products in a single online store because each vendor has to fulfill orders on their own. So it becomes essential to have a good shipping solution that can seamlessly automate live shipping rates from each vendor, and help you generate shipping labels based on the vendor’s address.

There are a bunch of plugins out there that help you set up a marketplace with multiple vendors. What’s even great is when you combine these plugins with a robust shipping plugin like the **UPS Shipping plugin** which offers a great order fulfillment experience to you as well as your vendors.

* * *

## Prerequisite to streamline shipping on your WooCommerce Multi-Vendor Marketplace

The following plugins are required to streamline the shipping process on your multi-vendor store. Please read along to know how they work together and provide a great multi-vendor shipping experience.

* * *

### WooCommerce UPS Shipping Plugin with Print Label

The [WooCommerce UPS Shipping Plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) helps you integrate UPS shipping on your WooCommerce store. It displays the real-time UPS shipping rates on the WooCommerce cart & checkout page and allows you to directly pay the postage and print UPS shipping labels from within the WooCommerce dashboard. You also get the tracking details for your order updated within the WooCommerce orders and the plugin automatically sends the UPS tracking information to your customers via email.

Please note that the choice of the shipping plugin entirely depends on your business needs. So, if you find FedEx to be a better choice then you can choose the [WooCommerce FedEx Shipping plugin](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/). And if your store is using multiple carriers you can choose [Multi-Carrier Shipping Plugin for WooCommerce](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/).

* * *

### Dokan Multi-vendor Plugin

No matter what type of multivendor store or marketplace you are trying to build, Dokan is the most suitable solution that you will find inside WordPress. Dokan extends the capabilities of the most popular eCommerce plugin, WooCommerce, providing the best **front-end** experience combined with the exceptional features that every marketplace needs. It is the must-have multivendor plugin on the market right now. 

Whether you are trying to build a marketplace for digital products, physical products, an auction site, or a site to sell bookings, Dokan can do it all. Dokan is trusted by more than **60,000+ marketplaces** all around the world and successfully helps people fulfill their dreams of becoming marketplace owners.

With Dokan, you can let your vendors register, upload their products, and **start earning commissions** without any hassle**.**

### Major benefits that you get with Dokan

  * Set up a fully functional online marketplace without any coding
  * Each vendor can create their own store from scratch within minutes
  * Vendors can add products and manage orders from the front end
  * Complete front-end experience for both vendors and customers alike
  * Comes with 38+ modules that make it easy for vendors to customize stores and augment customer experience
  * Beautifully designed free built-in theme with pro packages to make the setup process seamless
  * Advanced shipping calculation features for any type of delivery and zones around the world
  * All popular payment gateways are supported for transactions and orders
  * Generate detailed reports and earning statements in seconds
  * Available in English, German, Russian, Chinese, and 10+ languages
  * Owners can set commission rates to earn from vendors

### Easiest Learning Curve For A Marketplace

  1. All the documentation you will ever need to understand every bit of your marketplace
  2. Features being added with every release in accordance with user suggestion
  3. Super prompt customer support from support engineers and specialists: live chat and ticket-based.

With such benefits, Dokan is one of the best options for a WooCommerce marketplace owner. If you are also looking to create your own multi-vendor marketplace, you can download the free version of [Dokan](https://dokan.co/wordpress/) or see the [official pricing](https://dokan.co/wordpress/pricing/).

* * *

### WooCommerce Multi Vendor Add-on Plugin

The [WooCommerce Multi Vendor Add-on plugin](https://www.pluginhive.com/product/woocommerce-multi-vendor-shipping-addon/) allows your vendors to integrate their UPS carrier account within the WooCommerce marketplace. You can also change the way the Cart behaves when two products from two different vendors fall into the cart. To be specific, the plugin has two options – Split and sum, and Split and separate will be explained to you in detail later.

* * *

## Using Dokan with WooCommerce UPS shipping plugin

The WooCommerce UPS Shipping Plugin has been made compatible with the Dokan Multivendor plugin. Which means that the plugins operate together seamlessly. Below is the flow that shows how the two plugins work together.

* * *

* * *

## Create vendors for your WooCommerce store

The process of installing the plugins and configuring them is quite simple. You just need to download and install the Dokan Multivendor plugin. The plugin then guides you through the setup process and allows you to configure it on the way.

* * *

* * *

You can follow the steps given in the [following document to set up vendors for your store](https://dokan.co/wordpress/pricing/).

Once you are done installing the plugin, you have to set up the rules for the vendors. To do that, you need to go to **WooCommerce > Dokan > Settings**. Here you have multiple settings that you would need to choose and configure. You can choose the Dashboard appearance, define the commission percentage, set up withdrawal methods, etc.

* * *

* * *

### Add vendors details

You can add vendors yourself on WordPress’s backend or vendors can request from the front end of the website.

To add vendors from the backend you need to go to **WooCommerce > Users > Add New. **Add the user and assign him the role of the **vendor** as shown in the image below:

* * *

* * *

Or Vendors can Register from the front end of the WooCommerce store. They have to go to the My Account page and register as a Vendor.

* * *

* * *

### Add vendor’s shipping address

The vendor should add his Warehouse address, these will be the pickup location for UPS. Real-time rates will also be calculated on this basis. To add the vendor address you have to go to **My Account > Addresses **and add a shipping address.****

* * *

* * *

### Add and manage vendor products

To add and manage the products vendors have to go to the **Vendor’s dashboard > Products **Here you can see all your products and also **Add New Products** as shown in the image.

* * *

* * *

Now you can install the Multi-Vendor Ad-On.

### Install the Multi-Vendor Add-On plugin along with Dokan

After you have set up the Dokan plugin, you need to install another plugin called the Advanced Shipping For WooCommerce Multi-Vendor Plugin. As discussed earlier this acts as the bridge and lets vendors add their carrier account details.

* * *

#### Add Vendor’s UPS Account Details

To add UPS Account details go to **Vendors Dashboard > Edit Account Details > Add UPS Account details. **

* * *

#### Display UPS Shipping rates on the WooCommerce cart for vendor’s products

Go to **WooCommerce > Settings > PlugiHive Multi-Vendor.** You will find **Split and sum** , and **Split and separate** options on the plugin settings page.

* * *

If you choose the first option, i.e Split and sum, then the rate would be shown as the sum of the individual shipping costs of the products. And if you choose the Split and separate option then the prices would be shown separately. You can refer to the following image to see how it looks on the Cart page.

**Split and Sum**| **Split and Separate**  
---|---  
|   
  
In the above image, the Cart page includes two different items from two separate vendors. This is a nice feature as it allows your customers to have options over the shipping methods. You can also [refer to this article that explains more about this plugin](https://www.pluginhive.com/knowledge-base/send-shipping-labels-multiple-vendors-woocommerce-fedex-shipping/).

* * *

## Setting up UPS Shipping on your WooCommerce

Once you are done setting up the Dokan plugin, you need to set up the UPS Shipping Plugin. This is fairly easy to set it up and start using the plugin. You just need to keep a few things in mind. For instance, if you are going to allow your vendors to pack their items into boxes based on weight then you have to choose the Weight-based packing method. You need to enter the UPS credentials, and your address, choose the packing method, enable the shipment tracking feature, etc.

* * *

* * *

You can follow the UPS plugin setting up articles:

  1. [Woocommerce UPS Shipping Plugin – How it works?](https://www.pluginhive.com/knowledge-base/woocommerce-ups-shipping-plugin-works/)
  2. [Setting Up WooCommerce UPS Shipping Plugin](https://www.pluginhive.com/knowledge-base/setting-woocommerce-ups-shipping-plugin/)

You need to change a couple of settings within UPS for multi-vendor shipping.

  * Set **Ship From Address Preference** to **vendor address**
  * Set **Send Shipping Label via Email** to **Vendor**

* * *

### Order Fulfillment using UPS

Now, let us assume that a customer is going to purchase two products from two different vendors. The customer will add the items to the cart and would proceed to the Cart page in order to see the shipping rates and fulfill the order.

* * *

* * *

You can see that the real-time UPS shipping rates appear on the cart page. These rates are calculated by UPS and are returned from their API. Now WooCommerce store admin can process the orders and generate the shipping label.

* * *

As soon as the WooCommerce store admin generates the shipping labels Vendors will receive an email containing the shipping label.

**Vendor 1**| **Vendor 2**  
---|---  
|   
  
* * *

## Final Words

The combination of these plugins can help you achieve almost all multivendor business ideas. It provides a lot of advantages and benefits of the online model without any hassle.

This article has acquainted you with some of the efficient WordPress marketplace solutions. These include a range of plugins and themes designed to produce optimum results for a marketplace model. Let us know if you have a suggestion or query.

[ Previous  WooCommerce Multi Vendor Shipping with Dokan  ](https://www.pluginhive.com/knowledge-base/empower-multi-vendor-store-using-woocommerce-multi-carrier-shipping-plugin/)

[ Next  Set up a Multi-Vendor store with WooCommerce DHL Express & Dokan  ](https://www.pluginhive.com/knowledge-base/setup-woocommerce-multi-vendor-add-on-dhl-express-plugin-print-label-dokan/)
