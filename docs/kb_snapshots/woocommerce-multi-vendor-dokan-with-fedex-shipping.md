# FedEx Shipping Guide for WooCommerce Multi-Vendor with Dokan

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-multi-vendor-dokan-with-fedex-shipping/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# FedEx Shipping Guide for WooCommerce Multi-Vendor with Dokan

In this guide, we will show you how to fulfill orders on a Multi-Vendor marketplace website with FedEx as the shipping option. We will use Dokan to set up the multi-vendor store and [**WooCommerce FedEx Shipping Plugin**](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/) to fulfill orders.

Order fulfillment can be a complicated process, especially for a Multi-Vendor marketplace. When an online shopper places an order containing products from multiple vendors, he or she has to pay the shipping cost provided by both vendors. The two vendors, on the other side, have to process the order, pack the items into boxes, print the labels, and update the tracking statuses.

Challenges such as these can be easily handled by an end-to-end WooCommerce shipping solution. The following plugin is the best option to streamline the shipping process on your multi-vendor store. Read along to know how the WooCommerce FedEx Shipping plugin works together with Dokan to provide a great multi-vendor shipping experience.

#### WooCommerce FedEx Shipping Plugin

The [**WooCommerce FedEx Shipping Plugin**](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/) is a type of plugin that will help you completely automate FedEx shipping on your WooCommerce store. It helps you display real-time rates from FedEx on the Cart/Checkout page, pay postage, and print labels. You can also choose the preferred box packing method for your packages and automatically share the tracking information with your customers.

#### Dokan Multi-Vendor Plugin

As mentioned earlier, Dokan is possibly one of the best multi-vendor plugins out there. It offers some amazing multi-vendor features that could help you build the perfect marketplace.

#### Multi-Vendor Add-On Plugin

[**Advanced Shipping for WooCommerce Multi-Vendor plugin**](https://www.pluginhive.com/product/woocommerce-multi-vendor-shipping-addon/) acts as a bridge and allows your vendors to set up their FedEx shipping accounts. You can also change the way the Cart behaves when two products from two different vendors fall into the cart. To be specific, the plugin has two options – ‘Split and sum’ and ‘Split and separate’. We will talk about this later in this guide.

## Setting up vendors on your WooCommerce

The complete installation and plugin configuration process are quite simple. You just need to download and install the Dokan Multi-Vendor plugin after which the setup wizard guides you through.

Once you are done installing the plugin, you would have to set up the rules for the vendors. To do that, you need to go to **WooCommerce > Dokan > Settings**. You can choose the Dashboard appearance, define the commission percentage, set up withdrawal methods, etc.

### How to Add vendors?

There are two ways to add vendors—you can add vendors all by yourself in the WordPress backend or allow vendors to register on your website like any typical application form.

#### Adding vendors from WordPress Backend

Add a user on **WordPress > Users > Add New** and assign him/her the role o ‘**Vendor’** as displayed in the image below.

#### Register from Website

As mentioned before, vendors can register from the front end of your WooCommerce store. Prospective vendors can go to the My Account page of your website and fill up the form shown in the image below.

### How to Configure Vendors’ Addresses?

The vendor should add his or her warehouse address which will be used as the Pickup location by FedEx. This step is essential as the real-time FedEx rates would be calculated based on this address.

To add a vendor address, you would have to go to **My Account > Addresses, **where you would find the area to enter the address.

### How can Vendors add and manage their products?

Vendors can add their products. To add and manage the products, vendors have to go to the **Vendor’s dashboard > Products. **Here they can click on **Add New Product** to add products.

### Install the Advanced Shipping for WooCommerce Multi-Vendor plugin

After you have set up the Dokan plugin, you need to install another plugin called the [**Advanced Shipping For WooCommerce Multi-Vendor Plugin**](https://www.pluginhive.com/product/woocommerce-multi-vendor-shipping-addon/). As discussed earlier this acts as the bridge and lets vendors add their carrier account details.

#### Vendor FedEx Account Details

To add FedEx Account details go to **Vendors Dashboard > Edit Account Details > Add FedEx Account details. **

#### Display FedEx Shipping Rates on the Cart/Checkout

Go to **WooCommerce > Settings > PlugiHive Multi-Vendor.** You will find **Split and Sum** , and **Split and Separate** options on the plugin settings page.

If you choose the first option, i.e Split and Sum, then the rate would be shown as the sum of the individual shipping costs of the products. And to show the shipping prices of both vendors separately select split and separate options. You can refer to the following image to see how it looks on the Cart page.

**Split and Sum**| **Split and Separate**  
---|---  
|   
  
This Feature provides the WooCommece admin options with the shipping methods. You can also [refer to this article that explains more about this plugin](https://www.pluginhive.com/knowledge-base/send-shipping-labels-multiple-vendors-woocommerce-fedex-shipping/).

## Setting up FedEx Shipping on your WooCommerce

Once you are done the setting up Dokan plugin, you can start with the setup of the FedEx Shipping Plugin. It is very easy to set up this plugin you need to enter the FedEx credentials, and your address, choose the packing method, enable the shipment tracking feature, etc.

You can follow the documentation on **[Setting Up WooCommerce FedEx Shipping Plugin](https://www.pluginhive.com/knowledge-base/setting-woocommerce-fedex-shipping-plugin/)**.

  1. Within the FedEx plugin, we need to make some changes for Multi-Vendor shipping.

2\. Under Shipping Label settings, Set **Send Shipping Label via Email** to **Vendor**

### Order Fulfillment using FedEx

Now, let us assume that a customer is going to purchase two products from two different vendors. The customer will add the items to the cart and would proceed to the Cart page to see the shipping rates and fulfill the order.

You can see that the real-time FedEx shipping rates appear on the cart page. These rates are calculated by FedEx and are returned from their API. Now WooCommerce store admin can process the orders and generate the shipping label.

### Vendor’s FedEx Label via Email

As soon as the WooCommerce store admin generates the shipping labels Vendors will receive an email containing the FedEx label.

#### Vendor 1:

Download the label from the email:

#### Vendor 2:

Download the label from the email:

### Conclusion:

The combination of these plugins can help you achieve almost all multivendor business ideas. It provides a lot of advantages and benefits of the online model without any hassle. This article has acquainted you with some of the efficient WordPress marketplace solutions. These include a range of plugins and themes designed to produce optimum results for a marketplace model.

If you have any doubts or need help setting up UPS shipping on your WooCommerce-based website then feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**. Our support team should be able to help you out.

[ Previous  UPS Shipping Guide for Multi Vendor using WooCommerce Product Vendors  ](https://www.pluginhive.com/knowledge-base/ups-shipping-guide-multi-vendor-with-woocommerce-product-vendors/)

[ Next  WooCommerce Multi Vendor Shipping with Dokan  ](https://www.pluginhive.com/knowledge-base/empower-multi-vendor-store-using-woocommerce-multi-carrier-shipping-plugin/)
