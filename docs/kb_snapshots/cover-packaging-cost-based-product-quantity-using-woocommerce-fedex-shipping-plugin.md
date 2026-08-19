# Packaging Cost by Product Quantity for Shopify & WooCommerce

**Source:** https://www.pluginhive.com/knowledge-base/cover-packaging-cost-based-product-quantity-using-woocommerce-fedex-shipping-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Packaging Cost by Product Quantity for Shopify & WooCommerce

In this article, we will be discussing how you can cover the packaging cost based on the quantity of product that you are shipping, using **[WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)**. We will also show you how **[Shopify Ship, Rate and Track for FedEx](https://apps.shopify.com/fedex-shipping)** helps you adjust the returned FedEx shipping rates.

* * *

### Packaging cost based on Product quantity

WooCommerce store owners have the option to provide shipping options to their customers using a lot of **[shipping plugins](https://www.pluginhive.com/product-category/woocommerce-plugin/woocommerce-shipping/)**. However, the most common problem they face is the shipping cost. Ideally, the shipping cost includes the cost to ship a product from one place to another.

However, there are a lot of hidden charges to it. Before shipping, the products need to be packed properly into single or multiple boxes. This is a really important task as while shipping, there are high chances that the products might get damaged.

So to prevent that the store owners are required to pack them into reinforced boxes with an adequate amount of padding material inside the box. This, however, adds up to the shipping cost. And in the case of multiple boxes, this cost adds up to a significant amount.

* * *

#### **A real-life business scenario**

To understand the complete scenario, we should first take an example. Let’s hear what one of our customers has to say.

**Steve:** I need to add an additional cost to the shipping service based on quantity. 1 product, gets charged X amount extra shipping, and 2 products get charged a different account.

Basically, we are trying to add our box cost to the FedEx shipping calculation. Since you have a price adjustment available per shipment method, what code can we use for an additional shipping price adjustment based on the quantity in the cart?

* * *

Now let’s see how **[WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** solves his query.

### Adding Packaging Cost per Item to the Shipping Cost

**[WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** provides an easy way to adjust the shipping cost by adding the integer or the percentage value to the shipping cost. However, using this method the cost can be increased or decreased based on the shipping method.

Since Steve’s case is based on the packaging cost per item, he can achieve the same[**using the code in this link**](https://gist.github.com/xadapter/7e9aec09261e5ce77bbaca7093aba4ea).

Steve just needs to add the code to the **_functions.php_** file and specify the additional cost of packing. This way the cost of packing will be added to the shipping rates returned by the plugin and the customers will be paying the cost of packaging as well as the cost of shipping.

* * *

## Can you adjust the shipping cost in Shopify Ship, Rate and Track for FedEx?

**Yes, you can.** But you can only alter the prices by an integer value or a percentage.

As you already know, you can display real-time FedEx shipping rates on the Checkout page with **[Shopify Ship, Rate and Track for FedEx](https://apps.shopify.com/fedex-shipping)**. These rates are returned by FedEx APIs based on the request the App sends.

You can find all the **[FedEx shipping services](https://www.pluginhive.com/knowledge-base/display-fedex-shipping-methods-on-shopify-store/)** right under the Rates settings. The App allows you to change the Display name of the service as well as change the shipping cost. Refer to the following image.

* * *

Now let’s say you want to reduce $5 from the returned **[FedEx International Economy shipping](https://www.pluginhive.com/fedex-international-shipping-guide-for-woocommerce-users/)** price. You then have to enter in -5 under the Adjustment Value option as shown below in the image.

* * *

Now let us move an item into the Cart and see the price difference before and after adjusting the shipping price.

#### **Before Price Adjustment**

As you can see the shipping rate for FedEx International Economy is $85.49.

* * *

#### **After Price Adjustment**

And here’s the shipping price after the adjustment.

In a similar way, you can adjust the shipping prices based on a percentage value.

* * *

## Summary…

In this article, we discussed the **[WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** and how using this plugin, store owners can accommodate the cost of packaging to the shipping cost. So WooCommerce store owners can now add the packaging cost per quantity to the shipping cost. We also saw how the **[Shopify Ship, Rate and Track for FedEx](https://www.pluginhive.com/product/shopify-fedex-shipping-app-with-print-label-tracking/)** helps you adjust the shipping price.

If you have any suggestions regarding the article, feel free to contact our customer support. They can also help you set up FedEx shipping on your online store.

_**Happy selling!**_

[ Previous  Shipping Cost Optimization: WooCommerce FedEx Shipping Plugin  ](https://www.pluginhive.com/knowledge-base/earn-extra-profits-adjusting-shipping-cost-using-woocommerce-fedex-shipping-plugin/)

[ Next  Send Prepaid FedEx Labels to WooCommerce Customers  ](https://www.pluginhive.com/knowledge-base/send-prepaid-fedex-shipping-label-customers-can-send-products-service/)
