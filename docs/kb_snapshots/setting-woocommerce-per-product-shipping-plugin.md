# Setting Up WooCommerce Per Product Shipping Add-on

**Source:** https://www.pluginhive.com/knowledge-base/setting-woocommerce-per-product-shipping-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Setting Up WooCommerce Per Product Shipping Add-on

This tutorial explains how to set up per product shipping add-on with **[WooCommerce Table Rate Shipping Pro Plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)**. Please refer to the product page to know more about the plugin features.

## Overview

Heavy or large products may require special shipping. You may want to have a different shipping fee for a particular product. To handle such cases, Per Product Shipping plugin allows you to define shipping rates for individual products. This plugin is built on top of the WooCommerce Shipping Pro plugin. So along with the per-product shipping calculation feature, you also get the rule defining the ability of Shipping Pro which helps you to handle the most complex and unique WooCommerce shipping rate calculations.  
It gives you more control over your shipping rates. It provides you with the maximum flexibility to make your shipping rates work for your business. It enables you to customize or restrict your rates according to any combination of destination(country, state, and postal code), product category, shipping class, price, number of items, weight, and Method group by defining the rule(criteria). You can still offer multiple shipping options to customers. This plugin simplifies your administrative work to define, maintain and modify your shipping rates.  
This tutorial will give you an excellent launch pad to kick-start the Usage of **[Per Product Shipping WooCommerce plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/#:~:text=Per%20Product%20Shipping%3A%20Per%20product%20shipping%20allows%20you%20to%20define%20different%20shipping%20costs%20for%20products%20based%20on%20shipping%20destination%2C%20product%20category%2C%20shipping%20class%20etc.%C2%A0WooCommerce%20Per%20Product%20Free%20Add%2Don%C2%A0will%20enable%20per%2Dproduct%20capabilities%20for%20Shipping%20Pro.)**. It will give you all the essential knowledge and step-by-step instructions.

* * *

## Installation

After purchasing the WooCommerce Table Rate Shipping Pro Plugin, the plugin Zip file is available in MY ACCOUNT.

  1. Download .zip file from MY ACCOUNT.
  2. Log in as the WordPress Admin of your online store.
  3. Navigate to **Plugins** > **Add New** to upload the downloaded PluginHive WooCommerce Per Product Shipping plugin.
  4. Activate the WooCommerce Per Product Shipping plugin.

* * *

## Setting Up Per Product Shipping Plugin

After installing the plugin, a new shipping method ‘Per Product Shipping’ is added to WooCommerce. Now you can configure this Per Product Shipping method as per your requirement. You can navigate to settings in two ways as given below:

  * Navigate to WooCommerce > Settings > Shipping > Per Product Shipping ( under the Menu tabs )

### General Settings

The general setting fields are as shown below:

General Settings

  1. **Enable/Disable** :**** Select **Enable/Disable** check box to enable the Per Product Shipping method.
  2. **Method Title** : The method Title is visible on the Cart/Checkout page under **Shipping** options. Specify the **Method Title** as required(defined by you).

### Simple Shipping Example

Suppose you want to charge $30 for the United States to ship a particular product and $50 for all other countries except the United States for the same product. The Rate Matrix setting is as shown below:

Rate Matrix Settings

For the address of the United States, the cart is as shown below:

Cart

For the address of Canada which is other than the United States, the cart is as shown below:

Cart

### Rate Matrix Settings

Rate Matrix gives you control over customizing and restricting the rates for shipment. It provides you the flexibility to set shipping rates that are best for your business. The plugin enables you to customize your rates according to any combination of destination(country, state, and postal code), product category, shipping class, price, the number of items, weight, and Method group by defining the rule. You can still offer**[multiple shipping options](https://www.pluginhive.com/knowledge-base/allow-customers-choose-among-multiple-shipping-options-using-woocommerce-table-rate-shipping-pro/) **to customers. You can also specify the Method title which is visible in cart/checkout if the rates are calculated by using the rule under that method title.  
In some business cases, you may wish to add either an additional cost to a base shipping price based on how many items are added or a surcharge based on the weight of the cart. This can be achieved by using the combination of Base cost, cost/unit, and Round fields. The Rate Matrix settings are as shown below:

Rate Matrix

Here, you need to define the rules to get the shipping rates at cart/checkout. Shipping rate(s) depends on the rules which are defined by you. The rate matrix can include the columns like Method title, Country list, Weight, Rate Based on, Base cost, cost/unit, Round, Method Group, State list, Postal Code, Shipping class, Product Category, Item, and Price. To define your desired criteria(rule) for getting shipping rates, you can add or remove columns by using the field **Display/Hide matrix columns**. All these fields are described in the next section **Display/Hide matrix columns setting**.

You can add the rule by clicking on Add button which gets you the new row to enter your rule. Otherwise, you can import the rule CSV file by clicking on the Import CSV button. This PluginHive plugin also allows you to export the CSV file for rules which are present in the Rate Matrix. As per your requirement, you can also remove the undesired rule from the rate Matrix. With Duplicate Rule(s) button, you can duplicate the selected row of the matrix and do the changes as per your requirement. You can read the defined rule through the sentence (just above the rule) in plain English.

**Note** : Currency, Weight, and Dimension Units will be taken the same as your WooCommerce settings.

#### Rate Matrix Settings for per-product shipping

Here, you can customize the number of items using the product-level shipping unit. You can count product units as multiple shipping units or fractional shipping units.  
Assign shipping unit at a product level based on the shipping complexity on Product page as shown below:

Product Page

Configure Rate Matrix using Shipping pro rules which are based on a number of items. This is as shown below:

Rate Matrix

For the address of the United States, the cart is as shown below:

Cart

For the address of Canada which is other than the United States, the cart is as shown below:

Cart

For more information on setting the Rate matrix and shipping units, _See_ **[WooCommerce Table Rate Shipping Plugin setting up guide](https://www.pluginhive.com/knowledge-base/woocommerce-shipping-pro-chapter-7-extend-using-add-ons/)**.

Click **Save Changes** to set/update configuration settings.

**Check out our[WooCommerce Table Rate Shipping Pro Plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)**.

[ Previous  WooCommerce Shipping Pro – Chapter 2: Solving Business Case  ](https://www.pluginhive.com/knowledge-base/woocommerce-shipping-pro-chapter-2-solving-business-case/)

[ Next  WooCommerce Weight-Based Shipping with Table Rate Shipping Plugin  ](https://www.pluginhive.com/knowledge-base/woocommerce-shipping-pro-chapter-9-woocommerce-weight-based-shipping-simplified/)
