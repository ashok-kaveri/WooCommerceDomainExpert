# UPS Shipping Guide for WooCommerce Multi Vendor with WC Vendors

**Source:** https://www.pluginhive.com/knowledge-base/ups-shipping-guide-for-woocommerce-multi-vendor-with-wc-vendors/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# UPS Shipping Guide for WooCommerce Multi Vendor with WC Vendors

In this guide, we will discuss how to fulfill Multi-Vendor orders using UPS on a WooCommerce multi-vendor store. For the Multi-Vendor setup, we will be using the WC Vendors plugin and fulfill orders using the [WooCommerce UPS Shipping Plugin with Print Label](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/).

Multi-Vendor stores have more than one vendor selling their products on your WooCommrce store which adds complications to order fulfillment, especially when a customer places an order from different vendors. That’s why it is important to use shipping solutions that will enable you to show the combined shipping rates of vendors at a cart page and also vendors should be able to print a shipping label.

There are a bunch of plugins out there that help you set up a marketplace with multiple vendors. What’s even great is when you combine these plugins with a robust shipping plugin like the **UPS Shipping plugin** which offers a great order fulfillment experience to you as well as your vendors.

* * *

## WordPress Plugins Necessary to Streamline Shipping on Your Multi-Vendor Marketplace

The following plugins are required to streamline the shipping process on your multi-vendor store. Please read along to know how they work together and provide a great multi-vendor shipping experience.

### WooCommerce UPS Shipping Plugin with Print Label:

The [WooCommerce UPS Shipping Plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) is a type of plugin that will help you completely automate UPS shipping. It displays the real-time rate on the Cart/Checkout page and allows you to directly pay the postage and print the shipping labels. You can also choose the box packing method and automatically share the tracking information with your customers.

Please note that the choice of the shipping plugin entirely depends on your business needs. So, if you find FedEx to be a better choice then you can choose the [WooCommerce FedEx Shipping plugin](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/). And if your store is using multiple carriers you can choose [Multi-Carrier Shipping Plugin for WooCommerce](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/).

### WC Vendors Plugin:

[WC Vendors](https://www.wcvendors.com/) is one of the best Multi-vendor plugins for WooCommerce out there. It has some of the best features like the frontend dashboard for Vendor management and gives the vendor flexibility to create product coupons, view reports, and configure their own shipping rates. It has the best admin interface and lets the store admin restrict access to features and functions.

Using WC Vendor store admin can set the commission at a global, Vendor, or product level. It has also got a very good approval process, store admin can approve at a product or vendor level.

### Multi-Vendor Add-On Plugin:

[WooCommerce Multi-Vendor Add-On plugin](https://www.pluginhive.com/product/woocommerce-multi-vendor-shipping-addon/) will act as a bridge and lets your vendors set up their UPS shipping accounts. You can also change the way the Cart behaves when two products from two different vendors fall into the cart. To be specific, the plugin has two options – Split and sum, and Split and separates will explain to you in detail later.

* * *

## How do these plugins work together?

The WooCommerce UPS Shipping Plugin has been made compatible with the WC Vendor plugin. This means that the plugins operate together seamlessly. Let us set up these three plugins and place an order to see how it works.

### Setting up vendors on your WooCommerce

Let us download the WC Vendor plugin and install it on our WooCommerce store. After installing the plugin activate it, the plugin then guides you through the setup process and allows you to configure it on the way.

You can follow the steps given in the following [document in order to set up vendors for your store](https://docs.wcvendors.com/article-categories/getting-started/).

You can set up the rules for vendors and other settings. To do that, you need to go to **WooCommerce Dashboard** > **WC Vendors** > **Settings.** Here you have multiple settings that you would need to choose and configure. You define the commission percentage, set up withdrawal methods, etc.

### How to Add Vendors?

You can add vendors yourself on the WordPress backend or vendors can request from the frontend of the website.

To add vendors from the backend you need to go to **WooCommerce > Users > Add New. **Add the user and assign him the role of the **vendor** as shown in the image below:

Or Vendors can Register from the front end of the WooCommerce store. Do they have to go to the **My Account page** and **Apply to become a Vendor?**

### Vendor’s address configuration

The vendor should add his Warehouse address, these will be the pickup location for UPS. Real-time rates will also be calculated on this basis. To add the vendor address you have to go to **My Account > Addresses **and add a shipping address.****

### How can Vendors add and manage the product?

To add and manage the products go to WordPress backend (store URL/wp-admin) **WordPress backend** > **Products** > **All Products.** Here you can see all your products and also **Add New** products as shown in the image.

Now you can install the Multi-Vendor Ad-On.

### Install the Multi-Vendor Add-On plugin along with WC Vendors

After you have set up the WC Vendors plugin, you need to install another plugin called the Advanced Shipping For WooCommerce Multi-Vendor Plugin. As discussed earlier this acts as the bridge and lets vendors add their carrier account details.

#### Vendor’s UPS Account Details.

To add UPS Account details go to **My Account > Account Details > UPS Account details. **

#### Shipping rates on cart

Go to **WooCommerce > Settings > PlugiHive Multi-Vendor.** You will find **Split and Sum** , and **Split and Separate** options in the plugin settings page.

If you choose the first option, i.e Split and sum, then the rate would be shown as the sum of the individual shipping costs of the products. And if you choose the Split and separate option then the prices would be shown separately. You can refer the following image to see how it looks on the Cart page.

**Split and Sum**| **Split and Separate**  
---|---  
|   
  
In the above image, the Cart page includes two different items from two separate vendors. This is a nice feature as it allows your customers to have options over the shipping methods. You can also [refer to this article that explains more about this plugin](https://www.pluginhive.com/knowledge-base/send-shipping-labels-multiple-vendors-woocommerce-fedex-shipping/).

* * *

## Setting up UPS Shipping on your WooCommerce

Once you are done setting up the WC Vendors plugin, you need to set up the UPS Shipping Plugin. This is fairly easy to set it up and start using the plugin. You just need to keep a few things in mind. For instance, if you are going to allow your vendors to pack their items into boxes based on weight then you have to choose the Weight-based packing method. You need to enter the UPS credentials, and your address, choose the packing method, enable the shipment tracking feature, etc.

You can follow the [Setting Up WooCommerce UPS Shipping Plugin](https://www.pluginhive.com/knowledge-base/setting-woocommerce-ups-shipping-plugin/) article to know more. You need to change a couple of settings within UPS for multi-vendor shipping.

  1.   

Set **Ship From Address Preference** to **vendor address**

  

  2. Set **Send Shipping Label via Email** to **Vendor**

### Order Fulfillment using UPS

Now, let us assume that a customer is going to purchase two products from two different vendors. The customer will add the items to the cart and would proceed to the Cart page in order to see the shipping rates and fulfill the order.

You can see that the real-time UPS shipping rates appear on the cart page. These rates are calculated by UPS and are returned from their API.

Now WooCommerce store admin can process the orders and generate the shipping label.

As soon as the WooCommerce store admin generates the shipping labels Vendors will receive an email containing the shipping label.

**Vendor 1**| **Vendor 2**  
---|---  
|   
  
* * *

## Final Words

The combination of these plugins will help you to go online with a Multi-Vendor marketplace and ship seamlessly using shipping WooCommerce UPS shipping plugin. In this article, we have shown you how to add vendors, how a vendor can add products, how to store admin and vendors can fulfill their orders seamlessly.

If you have any doubts or need help setting up UPS shipping on your WooCommerce-based website then feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**. Our support team should be able to help you out.

_**Good luck!**_

[ Previous  Set up a Multi-Vendor store with WooCommerce DHL Express & Dokan  ](https://www.pluginhive.com/knowledge-base/setup-woocommerce-multi-vendor-add-on-dhl-express-plugin-print-label-dokan/)

[ Next  FedEx Shipping with WC Vendors Marketplace for WooCommerce  ](https://www.pluginhive.com/knowledge-base/woocommerce-marketplace-with-fedex-shipping-and-wc-vendors/)
