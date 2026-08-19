# Ship Certain Items with FedEx and Provide Flat-Rate Shipping for others with WooCommerce FedEx Shipping Plugin

**Source:** https://www.pluginhive.com/knowledge-base/ship-certain-items-with-fedex-and-provide-flat-rate-shipping-for-others-using-woocommerce-fedex-shipping-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Ship Certain Items with FedEx and Provide Flat-Rate Shipping for others with WooCommerce FedEx Shipping Plugin

In this article, you will learn how to display FedEx’s real-time shipping rate at a cart page for most of the products. While offering a flat rate for some of the products. We will discuss a unique business case. In which store owners want to hide the shipping rate for certain shipping classes.

* * *

## Understanding the Business Case:

[WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/) is one of the best shipping plugins. This plugin helps in automating the shipping by 

  * Showing real-time shipping rates on a cart page 

  * Print shipping label within WooCommerce 

  * Enable tracking, and more

To understand this use case, let’s check out a query from one of our customers. Hope it will help you get an idea of it.

> _We will be using FedEx for shipping most of our product. but there are a couple of small products, such as small stickers that we would like to ship in a regular envelope. For these small products, we will charge a flat rate. How can I achieve this?_

In the above case, the user wants to show a flat rate when the small product (in this case “sticker” ) is on the cart page. For all other conditions, they want to show real-time FedEx rates on a cart/checkout page. So for the above case, we will have three conditions:

si no| Conditions| Required rates at a cart page  
---|---|---  
1| Only small products are added to the cart| Flat- Rate  
2| Regular products ordered without a small product| FedEx real-time rates  
3| Small and regular products ordered together| FedEx real-time rates  
  
* * *

## Solution Using WooCommerce Shipping Plugin for FedEx with Print Label

You can solve the above cases by using [WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/). The first step would involve adding two shipping class. One for small items and others for the rest of the products.

* * *

* * *

To hide shipping rates at a cart page you need to have a [**Hide Shipping Methods**](https://www.pluginhive.com/product/hide-woocommerce-shipping-methods-and-rate-adjustment/) Plugin.

For this case, we will display shipping rates from FedEx when you add the regular product to a cart. But when customers add only small products to a cart. we will hide the shipping rates from FedEx using the **[Hide WooCommerce shipping methods plugin](https://www.pluginhive.com/product/hide-woocommerce-shipping-methods-and-rate-adjustment/)**. Let us try to understand this feature with this simple example.

Now go to **Manage Shipping Methods** and add two shipping Rate Options. One to hide flat-rate for regular products and hide FedEx shipping method for Small items. Also, enable **Break on the first occurrence.** You can refer to the image below:

* * *

* * *

You can watch this [video](https://youtu.be/xTvxNKZayGM) to learn how to hide the shipping method on a cart page based on shipping class.

Now let us place test orders and check our cart page for the different cases. For testing, I have added “**Bjorn Tee SS Jack & Jones**” as the regular item and “**CAP** ” as a small item in the shipping class.

* * *

#### 1st case: Add only a small item to the cart

* * *

#### 2nd case: Add only regular items to the cart

* * *

#### 3rd case: Add both regular and small products together

* * *

## Conclusion

We hope this short guide will help you display **[FedEx shipping rates](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** based on the shipping class. Also, hide the shipping methods based on shipping class in some cases.

If you have any doubts or need help setting up FedEx shipping on your WooCommerce-based website then feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**.

**_Happy selling!_**

[ Previous  How to Display other Domestic Services apart from FedEx Ground using WooCommerce Shipping plugin for FedEx  ](https://www.pluginhive.com/knowledge-base/display-domestic-services-apart-from-fedex-ground-using-woocommerce-fedex-shipping-plugin/)

[ Next  How to Ship Frozen Food With WooCommerce FedEx Plugin  ](https://www.pluginhive.com/knowledge-base/add-dry-ice-weight-to-woocommerce-fedex-shipments/)
