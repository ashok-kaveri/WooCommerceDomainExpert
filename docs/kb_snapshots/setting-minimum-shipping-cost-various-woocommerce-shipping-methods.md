# Set Minimum Shipping Cost for WooCommerce Shipping Methods

**Source:** https://www.pluginhive.com/knowledge-base/setting-minimum-shipping-cost-various-woocommerce-shipping-methods/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Set Minimum Shipping Cost for WooCommerce Shipping Methods

WooCommerce store owners have a lot of options when it comes to WooCommerce shipping methods. WooCommerce by default provides Free Shipping and Flat Rate Shipping methods. On the other hand, if you want to provide real-time shipping rates from shipping carriers like UPS, FedEx, Canada Post, etc. you can go with the following shipping plugins for WooCommerce.

  * [**WooCommerce UPS Shipping Plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)
  * [**WooCommerce Shipping Plugin for FedEx**](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)
  * [**WooCommerce Canada Post Shipping Plugin**](https://www.pluginhive.com/product/woocommerce-canada-post-shipping-plugin-with-print-label/)
  * [**WooCommerce Multi-Carrier Shipping plugin**](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/)

Also, there are cases which require advanced shipping calculations based on factors like weight, quantity, and price of the products. In such cases, plugins like [**WooCommerce Table Rate Shipping Pro**](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/) is the best bet for WooCommerce store owners. However, in some cases, store owners require their customers to pay at least a minimum amount for shipping. This way the store owners can make sure they cover all the handling charges and can deliver products to their customers easily. Yet, there is no way to achieve this. This article will focus on how you can set a minimum amount of shipping cost to every shipping method.

## Set A Minimum Shipping Cost For Different Shipping Methods

Before starting, let take a look at the image below.

Now as you can see, the shipping rates from UPS are accurate for all the domestic shipping services. **However, what if we require the minimum shipping rates to be $20 for say, UPS Ground service..?** To set the minimum shipping cost for your shipping methods, you need to add the code from [**this link**](https://gist.github.com/xadapter/c91282b9e1df7623085745fd9008bf1c). Just copy the code and paste it into the functions.php file on your website. You can access the file by clicking,

**Appearance > Editor > Functions.php**

Once you have pasted the code, you can easily set the minimum shipping cost by editing the code. All you need to do is change the value in the code.

> $shipping_method_min_cost = array(  
> ‘**flat_rate:5** ‘ => 60, // **Shipping id** => **min_cost**  
>  ‘**flat_rate:3** ‘ => 80,  
> ‘**wf_fedex_woocommerce_shipping:FIRST_OVERNIGHT** ‘ => 99,  
> );

As you can clearly see, the ‘**flat_rate:5** ‘ is the **shipping method value** and ‘**60** ‘ is the minimum value for that shipping method. For the shipping method ID, you can visit the cart page and right click on the shipping method and select **Inspect.** There you will get the shipping method ID. The image below will show you how to get the shipping method value for the code.

So based on our requirement, the changes required in the code will be similar to the one below.

> $shipping_method_min_cost = array(  
> ‘**wf_shipping_ups:03** ‘ => 20,  
> );

On saving this code, the shipping rates for the UPS Ground would remain a minimum $20 unless it reaches beyond that. The image shows the shipping rates on the same product which was used to fetch the rates earlier.

So, as you can see, the code lets you add a minimum value for all the shipping methods in a similar way.

[ Previous  I need $5 for shipping the first item and $1 per additional item. How to setup WooCommerce Shipping?  ](https://www.pluginhive.com/knowledge-base/need-5-shipping-first-item-1-per-additional-item-setup-woocommerce-shipping/)

[ Next  Set up WooCommerce Shipping by Product Weight and Size  ](https://www.pluginhive.com/knowledge-base/setting-default-product-weight-dimensions-ship-products-using-woocommerce-shipping-plugins/?seq_no=5)
