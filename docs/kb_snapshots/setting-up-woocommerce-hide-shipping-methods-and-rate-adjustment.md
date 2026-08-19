# Setting up PH WooCommerce Hide Shipping Methods & Rate Adjustment

**Source:** https://www.pluginhive.com/knowledge-base/setting-up-woocommerce-hide-shipping-methods-and-rate-adjustment/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Setting up PH WooCommerce Hide Shipping Methods & Rate Adjustment

Use this quick guide to set up your **[PH Hide WooCommerce Shipping Methods& Rate Adjustment](https://www.pluginhive.com/product/hide-woocommerce-shipping-methods-and-rate-adjustment/)** plugin. We’ve shown necessary settings, steps, and images along the way to help you configure features available in the plugin.

* * *

## On this page

  * **Plugin Installation& Activation**
  * **General Settings**
  * **Hide WooCommerce Sipping Methods**
  * **Rate Adjustment for WooCommerce Shipping Methods**

* * *

**[PH Hide WooCommerce Shipping Methods& Rate Adjustment](https://www.pluginhive.com/product/hide-woocommerce-shipping-methods-and-rate-adjustment/)** plugin lets you conditionally show/hide shipping methods and adjust the shipping cost using different control options. Plugin Conditionally hides the shipping method and adjusts the shipping cost with respect to the fixed value or percentage value.

Multiple options can be provided as a parameter to set rules for hiding/showing shipping methods and adjust the cost of shipment.

Let’s get into the specifics of how it lets you do that and how can we use multiple parameters to create rules. 

* * *

### Plugin Installation and Activation

  * Log in as the WordPress Admin of your WooCommerce online store
  * Navigate to **Plugins > Add New** to upload PH Hide WooCommerce Shipping Methods & Rate Adjustment plugin
  * **Activate** the PH Hide WooCommerce Shipping Methods & Rate Adjustment plugin
  * A new **Hide Shipping** tab will appear in the left sidebar as shown in the image below

* * *

The **[WooCommerce Hide Shipping Methods plugin](https://www.pluginhive.com/product/hide-woocommerce-shipping-methods-and-rate-adjustment/)** functionality can be divided into two sections, 

  * Displaying and Hiding the WooCommerce Shipping Methods based on certain parameters
  * Modifying the Shipping Rates based on certain parameters

* * *

### General Plugin Settings

The plugin General settings include the following options.

  * **Enable:** Tick the checkbox to enable hiding shipping rules.
  * **Debug Mode:** If you are not getting proper rates (lesser or higher than expected), all the available shipping options, or no rates at all, enable Debug option to find the error(s). You can also see the warning(s) from the plugin.

By enabling debug mode, you can trace issues using log. See information about debugging at the top of the Cart and Checkout page. After enabling debug mode, add a product to the cart. Go to the cart or checkout page to see the debugging information.

* * *

## Hide WooCommerce Shipping Methods

PH Hide WooCommerce Shipping Methods & Rate Adjustment allows you to hide/show WooCommerce default shipping methods as well as a third-party shipping plugin in your WordPress store. This plugin conditionally hides shipping methods on the cart page and specific shipping options. The plugin offers some useful parameters, using which you can hide/show shipping methods on the cart page. Based on the parameters configured, the shipping methods will be hidden/shown on the cart and checkout pages.

To set up a rule follow the instructions below,

  * Click on the add rule button on the settings page

* * *

  * In the ‘add rule’ page set the following options,

* * *

  1. **Rule name**  
You can set the name for the shipping rule in this option. It is completely optional.
  2. **Activate rule**  
Enable this option to hide/show WooCommerce shipping methods based on various parameters.
  3. **Break on the first occurrence**  
Suppose you have created multiple rules in the plugin. Now, if the first rule is satisfied, then the plugin will no longer check the other rules. So if you have framed 3 rules that hide shipping methods “FedEx Ground”, ” FedEx 2 Day”, “FedEx Express”, then in this case only “FedEx Ground” will be hidden as this rule is satisfied first.

* * *

  * Enable the parameters you want to set up under the option ‘**Parameters** ’ 

* * *

  * After enabling the filters you can add **Conditions** to hide/show the shipping method.
  * The parameters settings are as shown below.

* * *

The plugin supports the following Parameters based on which you can display or hide the shipping methods on WooCommerce cart and checkout page.

  * **Locations**  
Based on the shipping zone created in the WooCommerce you can hide/show the shipping services on the checkout page

* * *

  * **Products**  
Based on the shipping class and product categories you can hide or show shipping method on the cart page 

* * *

  * **Cart value**  
You can create a rule to hide/show the shipping method on the checkout page based on the subtotal, total quantity, and total weight of the product on the cart page 

* * *

  * **User**  
Select the desired WordPress User Roles from whom you want to hide shipping methods. You can select one or more user roles

* * *

  * **Shipping**

  1. **Shipping method**  
If you want to filter a specific shipping method from your premium shipping method(s), you can add the HTML value of the desired shipping method. You can add multiple methods by separating them with semicolons (;).
  2. **Shipping Service**  
Here you can add specific shipping carrier / free shipping/Local pickup as a parameter.

* * *

  * **AND logic**  
After enabling this option, the shipping rule with one or more shipping services/ shipping methods can be created. And the rule gets applied only when both shipping services/shipping methods are available on the cart page. 

  * **Day & Time**  
This option allows you to hide shipping method based on different time measures like,

  1. **Days  
** Here, you can select a specific day or multiple days
  2. **Time zone  
** Here you can choose between UTC or WordPress time zone
  3. **Time  
** Here you can set start time and end time

* * *

  * **Coupons**  
Using this option you can hide/ show shipping methods based on coupons code. You can select a coupon code from the drop-down list.

After setting up the parameters you can add the action to be taken based on the parameters. This option includes,

  * **Action Type**  
You can select hide method or show method as the action type 
  * **Shipping service**  
You can select shipping services from the drop-down list here
  * **Shipping Method**  
If you want to set rules for a specific shipping method , you can add a HTML value of that shipping method here

* * *

## Rate Adjustment for WooCommerce Shipping Methods

This Plugin will allow you to adjust shipping costs based on different parameters. The **[PH WooCommerce Hide Shipping Methods and Rate Adjustment plugin](https://www.pluginhive.com/product/hide-woocommerce-shipping-methods-and-rate-adjustment/)** offers some useful parameters , using which you can adjust the shipping cost. Based on the parameters configured, shipping costs can be adjusted with a fixed or a percentage value. To set up a rule follow the instructions below,

  * Click on the **Add rule** button on the settings page.

* * *

  * In the ‘**Add Rule** ’ page set the following options,

  1. **Rule name**  
You can set the name for the rate adjustment rule using this option. It is completely optional.
  2. **Activate rule**  
Enable this option to adjust the rates of WooCommerce shipping methods based on various parameters.
  3. **Break on the first occurrence**  
Suppose you have created multiple rules in the plugin and enabled this option. Then, if the first rule is satisfied, then the plugin will no longer check the other rules. 

* * *

  * Enable the parameters you want to set up under the option ‘**Parameters** ’. 

* * *

  * After enabling the filters you can add Conditions to adjust rates. The parameters settings are as shown below.

* * *

The plugin supports the following Parameters based on which you can adjust the shipping methods and either increase the cost or decrease it on WooCommerce cart and checkout page.

  * **Locations**  
Based on the shipping zone created in the WooCommerce shipping setting you can adjust the shipping cost shown on the checkout.

* * *

  * **Products**  
Based on the shipping class and product categories you can adjust the shipping cost shown on the checkout.

* * *

  * **Cart Value**  
You can create a rule to adjust the shipping cost shown on the checkout page based on the subtotal, total quantity, and total weight of the product on the cart page

* * *

  * **User**  
Select the desired WordPress User Roles from whom you want to set rules to adjust shipping rate. You can select one or more user roles

* * *

  * **Shipping**

  1. Shipping method  
If you want to filter a specific shipping method from your premium shipping method(s), you can add the HTML value of the desired shipping method. You can add multiple methods by separating them with semicolons (;).
  2. Shipping Service  
Here you can add a specific shipping carrier / free shipping/Local pickup as a parameter.

* * *

  * **AND Logic**  
After enabling this option, the shipping rule with one or more shipping services/ shipping methods can be created. And the rate adjustment rule gets applied only when both shipping services/shipping methods are available on the cart page.   

  * **Day & Time**  
This method allow you to adjust shipping cost based on different time measures like,

  1. Days  
Here , You can select a specific day or multiple days 
  2. Time zone  
Here you can choose between UTC or WordPress time zone
  3. Time  
Here you can set start time and end time

* * *

  * **Coupons**  
Using this option you can adjust shipping costs based on coupons code. You can select a coupon code from the drop-down list.

* * *

After setting up the parameters you can add the action to be taken based on the parameters

This option includes,

  * **Shipping service**  
You can select shipping services from the drop-down list here. Then You can adjust the shipping cost with respect to the percentage value or fixed value. If you want to decrease the shipping cost add the ‘-’ sign along with the value you are given to adjust.  

  * **Shipping Method**  
If you want to set rules for a specific shipping method, you can add an HTML value of that shipping method here. Then adjust the shipping cost with respect to the percentage value or fixed value. If you want to decrease the shipping cost add the ‘-’ sign along with the value you are given to adjust.

* * *

[ Previous  Setting Up WooCommerce TForce Freight Shipping Plugin  ](https://www.pluginhive.com/knowledge-base/setting-woocommerce-tforce-freight-shipping-plugin/)

[ Next  Set up & use Multi-Carrier Shipping Label App for BigCommerce  ](https://www.pluginhive.com/knowledge-base/set-up-bigcommerce-multi-carrier-shipping-label-app/)
