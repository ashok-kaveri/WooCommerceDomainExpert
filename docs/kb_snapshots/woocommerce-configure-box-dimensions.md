# WooCommerce: Configure Box Dimensions

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-configure-box-dimensions/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce: Configure Box Dimensions

In this guide, we are going to help you understand WooCommerce boxes and how to configure box dimensions based on your business needs.

### The Problem

There is a lot of confusion around on how to properly configure box sizes for various shipping methods including USPS. In reality, this is not as difficult as it seems to be if there is a basic understanding of how packaging works. This article is an attempt to explain the basic concept with a few examples. Below example is explained taking the USPS use case, but it is relevant even for UPS too.

### Basics.

What is the outer and inner length? Simple. Taking an example of an order for a single product, Inner length is the dimension of the product and Outer Length is the dimension of the package.

Btw, the product dimensions can be updated at admin --> products --> edit individual product --> Product Data.

Notice by default weight measurement unit is set as “Kg” and dimension as “cm”. This can be changed to “lbs” and “mm” at Woocommerce --> Settings --> Product.

We are coming back to our topic. In the case of light weighted products like envelop, inner and outer dimensions will be the same. But, when there is some filling made to protect the product as like glass, electronic items, etc, the product (inner) dimension and package (outer) dimension will differ.

For example, suppose a product has an inner dimension of 20x2x1 and need to have a light filling while packing, the outer box size can be 22x4x3. Now, what if someone buys 10 number of it as part of a single order? Obviously, we need to consider shipping it as part of one single package. So, the outer box size should be 22x4x30. Notice only height changes as length and width remains same (think about a deck of cards).

Likewise, we need to define each logical box inner and outer sizes according to the packing style being followed for different products with different quantity.

Also, in case of heavy packing, Box Weight needs to be added in the corresponding field. This is the weight of the package and it will be added with the product weight to determine the shipping rates. And if the total weight which is the sum of combined product and box weight, exceeds the entry in Max Weight, this box will not be the right one and so, another box will be chosen.

### Settings.

USPS Settings are located at WooCommerce --> Settings --> Shippings --> USPS. Few key configuration elements are explained here.

**Parcel Packing Method.**

By setting the Parcel Packing Method drop down to default, each product item from the order will be considered as a separate package. Shipping cost will be calculated for every single quantity of the products in the cart.

Rest of the options are self-explanatory. Box dimensions must be defined as explained above to make it work.

**Flat Rate Boxes.**

Flat rate boxes and envelopes are hardcoded in the USPS plugin code itself. There are a number of pre-defined box sizes and corresponding rates which will be picked up automatically according to your product dimensions and order quantities. This makes the job easier, but it may not be suitable for all businesses.

### Use Case.

I think a use case may help to get more clarity. Here is one.

Case 1: “Red Bag” single quantity. Product dimension 7x 11x .75 weight 20.  
Case 2: “Red bag” quantity 20.

In the first case, the best fit found is this predefined box (d29).

“length” => “12.5”,  
“width” => “9.5”,  
“height” => “1”,  
“weight” => “70”,  
“online price” => “5.70”

In the second case, it will get packed to two predefined boxes (d22a, d17b).

Box 1:  
“length” => “23.69”,  
“width” => “11.75”,  
“height” => “3”,  
“weight” => “70”,  
“online price” => “15.80”

Box 2:  
“length” => “11”,  
“width” => “8.5”,  
“height” => “5.5”,  
“weight” => “70”,  
“online price” => “11.30”  
So, 15.80 + 11.30 = 27.10

**Services.**

There are a number of services listed, where we can enable desired services. For more details on services provided by USPS, go through below link.

<https://www.usps.com/ship/mail-shipping-services.htm>

### Tip of the Day.

While testing, if you face the issue of updated product dimensions and rates have no impact on the cart page, you can try disabling shipping rate caching.

You can go to wooCommerce --> System Status --> Tools, and enable Shipping Debug Mode by checking it on.

All the best 🙂

Check out our plugins,

  * ****[**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)
  * ****[**WooCommerce FedEx Shipping plugin**](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)
  * ****[**WooCommerce Canada Post Shipping plugin**](https://www.pluginhive.com/product/woocommerce-canada-post-shipping-plugin-with-print-label/)
  * ****[**WooCommerce Multi-Carrier Shipping plugin**](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/)
  * ****[**WooCommerce Table Rate Shipping Pro plugin**](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)

[ Previous  How to troubleshoot WooCommerce FedEx Shipping Plugin  ](https://www.pluginhive.com/knowledge-base/troubleshooting-woocommerce-fedex-shipping-plugin/)

[ Next  How to Ship WooCommerce Custom Product Boxes via FedEx  ](https://www.pluginhive.com/knowledge-base/create-ship-woocommerce-custom-product-assortments-via-fedex/)
