# Set up WooCommerce Shipping by State and Shipping Class using Table Rate Shipping plugin

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-table-rate-shipping-based-on-state-and-shipping-class/
**Platform:** WooCommerce (WordPress)
**Plugin:** table-rate
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Set up WooCommerce Shipping by State and Shipping Class using Table Rate Shipping plugin

With this article, we’ll show you how to set up WooCommerce Shipping by State and WooCommerce Shipping Class using the **[WooCommerce Table Rate Shipping Plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)**. We’ll also discuss a real-life business case and show you how to set up the shipping rules within the plugin.

* * *

## How to set up WooCommerce Shipping by State and Shipping Class?

WooCommerce is designed to help business owners like you accomplish basic shipping-related tasks. **[WooCommerce Shipping Zone](https://www.pluginhive.com/woocommerce-shipping-zones-ultimate-guide/)** and **[WooCommerce Shipping Class](https://www.pluginhive.com/ultimate-guide-set-up-woocommerce-shipping-class/)** , the two important tools, play important roles in doing that. However, the two have their limitations and feel insufficient when tackling modern business requirments.

One such requirement is to provide shipping rates based on desination with multiple shipping classes. But with the help of an advanced **[WooCommerce shipping plugin](https://www.pluginhive.com/product-category/woocommerce-plugin/woocommerce-shipping/)** like, **[WooCommerce Table Rate Shipping Pro](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)** , it becomes quite easy. Let’s take an example.

**Customer:** _I want to set up WooCommerce shipping rates based on the following conditions using the WooCommerce Table Rate Shipping plugin._

_Shipping Class: Hoodies for Arizona – $10, New Mexico – $25, Texas – $25_

 _Shipping Class: Belts for Arizona – $20, New Mexico – $35, Texas – $35_

 _Please tell me how to achieve this._

* * *

## Solution using the WooCommerce Table Rate Shipping Pro

The WooCommerce Table Rate Shipping Pro is one of the best plugins to set up and provide WooCommerce shipping methods. The plugin is specially made to cover all of the possible complex business scenarios and offer to ship accordingly.

In this case, you can add shipping rules based on the following parameters.

  * WooCommerce Shipping Class
  * Destination State

Based on the rules defined above, let’s transform the above business case into a table. So that it will be easy to add the above Shipping Rules into [**WooCommerce Table Rate Shipping Pro**](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/). Have a look below!

Note: The above shipping condition does not mention what happens when both products are present in the cart together. So, we’ve assumed such shipping rates in these scenarios on the table.

**Shipping Method Name**| **States**| **Shipping Class**| **Base Cost**  
---|---|---|---  
Hoodie + Arizona| Arizona| Hoodies| 10  
Hoodie + New Mexico| New Mexico| Hoodies| 25  
Hoodie + Texas| Texas| Hoodies| 25  
Belt + Arizona| Arizona| Belt| 20  
Belt + New Mexico| New Mexico| Belt| 35  
Belt + Texas| Texas| Belt| 35  
Hoodie + Belt + Arizona| Arizona| Hoodie, Belt| 15  
Hoodie + Belt + New Mexico| New Mexico| Hoodie, Belt| 40  
Hoodie + Belt + Texas| Texas| Hoodie, Belt| 40  
  
* * *

### Setting up the Table Rate shipping rules

Set the WooCOmmerce shipping rules based on the above tables using [WooCommerce Table Rate Plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/). You need to first set up the shipping rules under plugin settings. Follow these steps, **WooCommerce →****Settings** → **Shipping →** **Table Rate Shipping**.

Now, let us select the columns that we are going to use to set the shipping rules. For the above conditions, we would be needing the following matrix columns:

  1. **Method Title**
  2. **State**
  3. **Shipping Class**
  4. **Base Cost**

* * *

Also, enable **Calculation Logic (AND)** And **Strict Logic (AND)**. You can refer the below image:

* * *

After finishing the above steps, let’s now set the shipping rules based on the table above. you can refer to the image below.

After you add these shipping rules you will get desired results. You check this by adding the orders to the cart page. You can check for all 9 conditions whether you are getting the right shipping rate on a cart page. Let us show you the results for three conditions:

### 1\. WooCommerce Shipping by State: New Mexico for Hoodies

* * *

### 2\. WooCommerce Shipping by State: Texas for Belts

* * *

### 3\. WooCommerce Shipping by State: Arizona for Belts and Hoodies

* * *

## Conclusion

So that’s how you set up WooCommerce Shipping by State and WooCommerce Shipping Class. We have used **[WooCommerce Table Rate Shipping Plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)** for the above business case.

Hope this guide will help you to configure your business case. Check out WooCommerce Table Rate Shipping Plugin for more information and features.

If you have any doubts or need help setting up table rate shipping on your WooCommerce-based website then feel free to [**Contact PluginHive Customer Support**](https://www.pluginhive.com/support/).

**_Good luck!_**

[ Previous  WooCommerce UPS Shipping – Provide Live Rates and Free Shipping for Some Products based on Cart Subtotal  ](https://www.pluginhive.com/knowledge-base/woocommerce-live-ups-shipping-rates-free-shipping-cart-subtotal/)

[ Next  How to Configure State-based Rules Manually Using the WooCommerce Table Rate Shipping Plugin  ](https://www.pluginhive.com/knowledge-base/configure-state-based-rules-manually-using-the-woocommerce-table-rate-shipping-plugin/)
