# Troubleshoot – Getting Multiple Shipping Options with No Price!

**Source:** https://www.pluginhive.com/knowledge-base/troubleshoot-getting-multiple-shipping-options-no-price/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Troubleshoot – Getting Multiple Shipping Options with No Price!

In this article, we will help you understand how you can troubleshoot the issue when you get shipping services without the rates when using the WooCommerce Table Rate Shipping Pro. Read more below.

The online store owners want their customers to have a nice experience while shopping at their store. That experience not only counts the ease customers face while shopping but it also includes the post-shopping experience. The shipping options and the whole shipping process play an important part in the post-shopping experience of the customers.

One of our customers, Gerry, who owns an online shopping store in Ontario, Canada, also wanted his customers to be satisfied after shopping from his store. But Gerry had some issues with the shipping rates being shown to his customers on his website.  
According to Gerry,

> There is an issue with the cart page on my site.  
> It’s showing two shipping options… one calculated accurately, and another one that has NO price.  
> How do I get rid of this second, no-price option?

Now let’s see what made Gerry’s cart page display more than one shipping option and that too without any price.

## Understanding Gerry’s Issue…

Let’s try to understand the issue a bit. There are two aspects to the issue,

  * Multiple Shipping options
  * No Shipping Rates

Based on the working of WooCommerce Table Rates Shipping Pro, there are two scenarios when this situation may arise.

  * **Multiple Shipping options**

The cart and checkout page shows those shipping options that are set up in the settings of the plugin. If there are multiple shipping options created and grouped separately in the settings they will appear on the cart page.

  * **No Shipping Rates**

Shipping Rates are calculated based on the rates and the calculation methods specified in the settings of the plugin.

## Solution…

The solution in the case of Gerry was that he had configured multiple shipping methods for his store and had grouped them separately. Besides, in one of the shipping methods, he had not given any price, neither a base cost nor the cost per unit.  
Hence more than one shipping method was showing on his cart page, along with a shipping option with no cost associated with it.  
Below is the image showing Gerry’s configuration and his cart page:

The above image clearly shows the reason behind Gerry’s misery. His issues can be easily solved by either correctly grouping the shipping option as per the business case, and by removing the shipping method that doesn’t have rates associated with it. While configuring the rates with Shipping Pro, if you have specified multiple shipping methods and you want only one of them to be selected on the cart page, then all of them need to be in the same group. Also, every shipping method has to have a price associated with it. Be it the **Base Cost** , or the **Cost per Unit** , either one is needed to calculate the shipping cost.

The image below shows the correct configuration that will not show an empty shipping option on the cart page.

Now based on the above settings, let us check how the customers will see the shipping options in the cart as well as the checkout page.

  * Cart page
  * Checkout page

* * *

So this is how you can configure **[WooCommerce Table Rates Shipping Pro](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)** accurately so that no additional shipping options would show. And all the shipping options that are shown to the customers would have a shipping cost associated with it.

[ Previous  Setting up Weight Based Shipping Rates using Shipping Pro  ](https://www.pluginhive.com/knowledge-base/setting-weight-based-rates-using-shipping-pro/)

[ Next  I added 36 line and when I try to add more rows I’m faced with this error "action failed  ](https://www.pluginhive.com/knowledge-base/added-36-line-try-add-rows-im-faced-error-action-failed/)
