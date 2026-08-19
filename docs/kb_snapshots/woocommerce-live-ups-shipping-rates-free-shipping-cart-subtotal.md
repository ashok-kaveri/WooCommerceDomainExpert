# WooCommerce UPS Shipping – Provide Live Rates and Free Shipping for Some Products based on Cart Subtotal

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-live-ups-shipping-rates-free-shipping-cart-subtotal/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce UPS Shipping – Provide Live Rates and Free Shipping for Some Products based on Cart Subtotal

In this guide, we are going to see how to provide UPS rates and free shipping for some products using **[WooCommerce Table Rate Shipping Plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)** along with the WooCommerce UPS Shipping Plugin. We will set up the Shipping conditions based on a real-life business case.

## Understanding the Business Case

The WooCommerce Table Rate Shipping Pro along with the WooCommerce UPS Shipping Plugin is the best option in the market to handle both easy and complex business scenarios. You can easily set up rules to display shipping rates based on Order Quantity and Price. Let’s check out a unique business of one of our customers and see how this plugin can fulfill it.

> _Hi there,_  
>  _I would like to implement UPS rates for our site however not all orders ship UPS._  
>  _1\. Some orders ship via UPS. But we provide free shipping based on an order total of $300 and above_  
>  _2\. Some orders ship freight and we don’t use UPS Freight. For orders with freight items (pallets of goods) we’d like to assign a flat rate cost, say $100._
> 
> _Does your plugin support this?_

## Solution

We can easily solve the above scenario using the following three plugins:

  1. [W](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)[ooCommerce UPS Shipping](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)[ plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)
  2. [WooCommerce Table Rate Shipping Plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)
  3. Hide Shipping Methods free addon

### WooCommerce UPS Shipping Plugin

Set up the WooCommerce UPS Shipping Plugin. You can refer to the **[WooCommerce UPS setting up documentation](https://www.pluginhive.com/knowledge-base/setting-woocommerce-ups-shipping-plugin/)** to easily do that. Once you have set up the UPS plugin completely, disable the **Freight service** from the plugin.

### WooCommerce Table Rate Shipping Pro Plugin

As mentioned before, the **[WooCommerce Table Rate Shipping Pro Plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)** is an excellent plugin to set shipping rates based on the different shipping rules that match the user’s cart page.

You need to first set up the shipping rules under plugin settings. Follow these steps, **WooCommerce <** **Settings** < **Shipping** < **Shipping Pro**.

Now, before we add the Shipping Rules let us select the columns that are to be used for the rule matrix. For our business case above, we would be needing the following matrix columns:

  * **Method Title**
  * **Zone list**
  * **Item**
  * **Price**
  * **Rate****Based On**
  * **Base Cost**
  * **Shipping Class**

Now, head to **Shipping rules** under Shipping Pro. Set up two rules as shown in the below image. Save the changes.

### Hide Shipping Methods Free Addon

Specify the shipping class for each of your products as Normal and Freight. You have to create two shipping classes as it has been mentioned in the query that for orders with freight items, a flat rate has to be assigned.

Now, download and install the **[Hide Shipping Methods& Rate Adjustment Plugin. ](https://www.pluginhive.com/product/hide-woocommerce-shipping-methods-and-rate-adjustment/)**Add a product to the cart and check out. Now, inspect each UPS shipping method and copy all the values.

Create two Rate options as shown in the below image. Enter the values of all the UPS shipping methods that you had copied in both the Rate options. In the first option, the UPS shipping methods are to be hidden for a total cost of more than $300. In the second option, you have to hide the UPS Shipping methods for freight shipments since for freight shipments, a flat rate has to be added.

Now, add the product to cart and checkout.

For a normal product whose total cost is less than $300, you can see that all the UPS Shipping methods are displayed.

For Freight shipments, you can see that a flat rate of $100 is shown at the checkout.

For normal items whose total value is more than $300, you can see that the option for Free Shipping is enabled and other UPS Shipping methods are disabled.

## Conclusion

And that’s the way to provide UPS rates and free shipping for some products using WooCommerce Table Rate Shipping Pro along with the WooCommerce UPS Shipping Plugin and the Hide Shipping methods addon. We hope this guide would have helped you configure your business case as well. Check out WooCommerce Table Rate Shipping Pro for more information and features.

If you have any doubts or need help setting up Tabel rate shipping on your WooCommerce-based website then feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**. Our support team should be able to help you out.

[ Previous  WooCommerce Table Rate Shipping: Set up Shipping Rates Based On Order Quantity and Price  ](https://www.pluginhive.com/knowledge-base/woocommerce-shipping-rates-based-on-order-quantity-and-price/)

[ Next  Set up WooCommerce Shipping by State and Shipping Class using Table Rate Shipping plugin  ](https://www.pluginhive.com/knowledge-base/woocommerce-table-rate-shipping-based-on-state-and-shipping-class/)
