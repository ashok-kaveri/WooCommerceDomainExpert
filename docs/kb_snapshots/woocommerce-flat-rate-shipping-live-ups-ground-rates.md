# Set Up WooCommerce Flat Rate Shipping with UPS Ground Rates

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-flat-rate-shipping-live-ups-ground-rates/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Set Up WooCommerce Flat Rate Shipping with UPS Ground Rates

In this article, we will check out how you can set up a flat rate shipping cost based on the product quantity, for some of your products, and still ship your other products via a shipping carrier by providing a live rate on your WooCommerce store. This article will feature the [**WooCommerce Multi-Carrier Shipping plugin**](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/) and how it handles complex shipping scenarios where you are required to ship different types of products differently.

* * *

## Business Case…

Cody runs an online store where he is required to ship and sell different types of products within the US. However, there are mainly two ways Cody is planning to ship from his store.

According to Cody, “ _**…I am setting up a whole new product line that I need to be able to set a flat rate shipping price for based on quantity.**_  
_**This way, if the customers order only 1 then display $149 for shipping, if they order 2 then show $298, and so on.**_

_**How can I do this..?**_

_**Also, I need to have it set up where if the customers add any of the normal shop items which I ship using UPS Ground, it will still show the flat rate option mentioned above but add the UPS shipping costs from the other products in the cart to the flat rate.  
**__**How can I set this up? I’m getting desperate here..!**_ “

* * *

## Solution…

Cody can easily set this up and provide his customers with a great shipping experience. WooCommerce Multi-Carrier Shipping plugin allows you to set up live shipping rates and display it on your website from the top shipping carriers like UPS, FedEx, USPS, Stamps.com, and DHL. Not only that, but it also allows different shipping methods for your products.

* * *

### Setting Up Shipping Classes

Since Cody knows he can divide his products into two different types, creating different shipping classes would be the perfect solution for his scenario. All he needs to do is [**set up WooCommerce shipping classes**](https://www.pluginhive.com/ultimate-guide-set-up-woocommerce-shipping-class/) for his store, as shown below.

  * **Flat Rate Products** – shipped for a flat rate fee
  * **Normal Products** – shipped as per the live UPS Ground rates

* * *

## How to Set Up Flat Rate Shipping along with Live UPS Shipping Rates for your WooCommerce store?

Based on Cody’s business case, he just needs to follow the steps below in order to get display the shipping rates on the cart page.

  * After successful [**installation and activation**](https://www.pluginhive.com/knowledge-base/how-to-download-install-update-woocommerce-plugin/) of the WooCommerce Multi-Carrier Shipping plugin, visit the plugin settings by clicking the **Settings** option on the plugins page or by visiting the **WooCommerce = > Settings => Shipping => Multi-Carrier Shipping** in order to set up the plugin.  

  * You can also follow the [**guide to setting up the WooCommerce Multi-Carrier Shipping plugin**](https://www.pluginhive.com/knowledge-base/setting-multi-carrier-shipping-plugin-woocommerce/) in order to set up the basic requirements like **Area Management**.  

  * Once you are done with the setup, make sure you enter the **UPS Account Credentials** in the plugin settings under the **UPS Settings.**  

  * Now enable the **Show Methods Groups** option on the settings page. This will allow you to create a shipping method group and specify shipping methods in that group. The plugin will make sure **only one of the shipping methods from a single group is displayed on the cart page**. If there are multiple methods, the **plugin will add the shipping costs together and display a single shipping cost at the cart page.**  

  * Save the settings.  

  * Now you can create the shipping rules for both the shipping classes created in the above section. As displayed in the image below, we have created two shipping rules as:
    * **Rule 1 – For all the products in the shipping class Flat Rate, the shipping cost will be calculated as a flat rate shipping fee of $149 per item**
    * **Rule 2 – For all the products in the shipping class UPS, the shipping cost would be based on the live shipping rates returned by USP for the UPS Ground service  
**
  * Save the settings and visit the shop page to enter different products on the cart page.
  * So, you can see the following rates on the cart page:
    * **If the customer selects the product which you want to ship via UPS Ground, he will get the live shipping rates on the cart page.**  

    * **If the customer selects the product which you want to ship with a flat rate fee, he will get the flat rate shipping rates on the cart page.**  

* * *

## What If a Customer Selects Both Types of Products – one Which Ships via UPS Ground and the other With a Flat Rate Shipping?

In Cody’s case, he requires the **shipping rates to be added together if his customers are purchasing both the types of products**. Hence, with the WooCommerce Multi-Carrier and the steps mentioned above, his customers will get the shipping rates on the cart page as shown in the image below.

* * *

## Final Thoughts…

This article covers the [**WooCommerce Multi-Carrier Shipping plugin’s**](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/) ability to combine the real-time shipping rates and flat rate shipping with the flexibility of calculating shipping rates based on product quantity, weight, as well as the total price. This is what makes this plugin a must for the WooCommerce store owners who want an advanced and flexible shipping solution for their online store.

In case you are facing trouble in setting up shipping for your WooCommerce store or having trouble setting up the WooCommerce Multi-Carrier Shipping plugin, please contact our [**shipping experts**](https://www.pluginhive.com/support/). We will surely help you out.

[ Previous  How to allow Customers to Download UPS labels from an Online Repair Shop  ](https://www.pluginhive.com/knowledge-base/how-to-allow-customers-to-download-ups-labels-repair-shop/)

[ Next  Are the dimensions of the boxes taken into account or is it going by volume when calculating how many products fit in one box using WooCommerce UPS Shipping Plugin?  ](https://www.pluginhive.com/knowledge-base/dimensions-boxes-taken-account-going-volume-calculating-many-products-fit-one-box-using-woocommerce-ups-shipping-plugin/)
