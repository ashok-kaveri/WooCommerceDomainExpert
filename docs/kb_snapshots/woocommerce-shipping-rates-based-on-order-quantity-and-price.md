# WooCommerce Table Rate Shipping: Set up Shipping Rates Based On Order Quantity and Price

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-shipping-rates-based-on-order-quantity-and-price/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce Table Rate Shipping: Set up Shipping Rates Based On Order Quantity and Price

In this guide, we are going to see how to set up WooCommerce Shipping rates based on order quantity and price. You will learn how to change shipping costs based on the order quantity and set free shipping whenever an order exceeds a certain amount, all by using [**WooCommerce Table Rate Shipping Plugin**](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/). We will set up the Shipping conditions based on a real-life business case.

* * *

## The Business Case – Shipping Rates Based On Order Quantity and Price

The WooCommerce Table Rate Shipping is the best plugin in the market. It can handle most complex business scenarios. You can set up rules to display shipping rates based on Order Quantity and Price. Let’s check out the unique business of one of our customers and see how this plugin can fulfill it.

* * *

> _Hi, I want to set the Shipping Rates based on the order quantity (e.g. $6 for less than 6 items, $10 for 7-12 items, and for more than 12 items shipping cost is $15). What am I supposed to do? And also, I would like to offer Free Shipping to customers whose order value is more than $200. How do I achieve this?_

Now let us transform his business case into a table and try implementing the above Shipping Rules into [**WooCommerce Table Rate Shipping Pro**](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/). Have a look below!

**Shipping Name**| **Zones**| **Items**| **Price**| **Cost Based on**| **Base Cost**  
---|---|---|---|---|---  
Below 6 items Per Order| USA| 0-6| –| items|  $6  
7-12 Items Per Order| USA| 7-12| –| items| $10  
More than 12 items Per Order| USA| more then 12| –| items| $15  
Free Shipping| USA| –| More than 200| Price| $0  
  
* * *

## Solution using WooCommerce Table Rate Shipping Pro Plugin

As mentioned before, the [**WooCommerce Table Rate Shipping Pro Plugin**](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/) good plugin. You can set the shipping rates based on the different shipping rules.

You need to first set up the shipping rules under plugin settings. Follow these steps, **WooCommerce** —> **Settings** —> **Shipping** —> **Shipping Pro**.

Now, before we add the Shipping Rules let us select the columns that are to be used for the rule matrix. For our business case above, we would need the following matrix columns:

**Method Title, a****Zone list,****Item,****Price, Rate****Based On,****Base Cost**

Also for the **Minimum cost or Maximum cost** option, select **Choose minimum rate in case of multiple rules** and then click on **Save Changes**. You can refer to the below image:

* * *

Once you’re done with the above steps. You must now add the Shipping Rules based on the conditions mentioned before. You can refer to the image below.

* * *

Now, let’s check whether the Shipping Rates are reflected on a Cart/Checkout page or not. Keep in mind that these Shipping Rates are based on the Shipping Rules we had set before. Thereafter, you can go ahead and place the orders to match all four of your shipping conditions:

  1. Place the orders with less than 6 items
  2. Place the orders with items between 7-12
  3. Then place an order with more than 12 items
  4. Finally, place an order where the total product price is more than 200

The below images show the changes in Shipping Rates on the Cart page.

**Below 6 items Per Order**| **7-12 Items Per Order**  
---|---  
|   
**More than 12 items Per Order**| **Order amount More than 200**  
|   
  
* * *

## Conclusion

And that’s how you set the shipping cost based on the order quantity and price using the [**WooCommerce Table Rate Shipping Pro Plugin**](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/). We hope this guide will help you configure your business case as well. 

If you have any doubts or need help setting up Tabel rate shipping on your WooCommerce-based website, feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**.

_**Good luck!**_

[ Previous  WPML Compatibility with WooCommerce Table Rate Shipping  ](https://www.pluginhive.com/knowledge-base/wpml-compatibility-woocommerce-table-rate-shipping-plugin/)

[ Next  WooCommerce UPS Shipping – Provide Live Rates and Free Shipping for Some Products based on Cart Subtotal  ](https://www.pluginhive.com/knowledge-base/woocommerce-live-ups-shipping-rates-free-shipping-cart-subtotal/)
