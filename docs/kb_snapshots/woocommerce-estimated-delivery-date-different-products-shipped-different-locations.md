# Set Up the Estimated Delivery Date for Products  Shiping from Different Locations

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-estimated-delivery-date-different-products-shipped-different-locations/
**Platform:** WooCommerce (WordPress)
**Plugin:** estimated-delivery
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Set Up the Estimated Delivery Date for Products Shiping from Different Locations

We will check out how to **[set up an estimated delivery date](https://www.pluginhive.com/knowledge-base/ups-deliver-saturday-provide-accurate-woocommerce-estimated-delivery-date/)** for different products which are shipped from different locations. This article will cover how the **[WooCommerce Estimated Delivery Date plugin](https://www.pluginhive.com/product/estimated-delivery-date-plugin-woocommerce/)** works with the combination of WooCommerce Shipping Classes and Shipping Zones, together.

## Business Case

Brent is a WooCommerce store owner who sells phone cases from two different suppliers. One in the US and one from China. According to Brent,

“ _**I sell phone cases which ship from China and the US. The cases from China will take around 1-2 weeks to the US and 2-3 weeks to ship internationally.**__**However, the phone cases from the US will take 1 week to ship to the US and about 2 weeks to ship Internationally.**__**So as you can see I need a combination of both, is that possible?”**_

## Solution

It is possible to accomplish Brent’s business case using the WooCommerce Estimated Delivery Date plugin. In order to do so, he would require the following to be set up on his website.

### Shipping Classes

Brent’s scenario requires two types of products for which he would require two different shipping classes, as displayed below.

  * **Products Shipped from the US**
  * **Products Shipped from China**

Hence, he just needs to create these shipping classes and assign products to the shipping classes.

### Shipping Zones

Now, since Brent has mainly two destinations for which he is required to create two shipping zones, as shown below.

  * **The US**
  * **Rest of the World**

**NOTE:**  
****Provide the US zone above the other zone**  
****DO NOT provide any location in the second zone so it will take every location**

## How to Set Up the Estimated Delivery Date for Different Products that ship from Different Locations?

In order for Brent to create a shipping scenario, where he requires to display estimated delivery dates for different products from different locations, he just needs to follow the steps below:

  * After successful i**nstallation and activation** of the WooCommerce Estimated Delivery Date plugin, click on the Settings option in the plugins page or visit **WooCommerce = > Settings => Estimated Delivery.**
  * Click on **Shipping Classes** and set the delivery days based on the requirements, as shown in the image below.  
**NOTE:**  
****China – The minimum delivery days in case of products shipped from China is 2 weeks, so set up 14 days in the settings**  
****The US – The minimum delivery days in case of products shipped from the US is 1 week, so set up 7 days in the settings**
  * Now, click on **Shipping Zones** and set up the delivery days as shown in the image below.  
**NOTE:**  
****For Shipping to the US, the minimum number of additional days required from any one of the store locations is 0, so set up 0 in the number of days**  
****For Shipping to the International Locations (anywhere except the US), the minimum number of additional days required from any one of the store locations is 7, so set up 7 in the number of days**
  * Save the settings, and visit the shop page to enter a product to the cart. You will be able to see the following estimated delivery dates on the cart page.
    * Upon adding a product that ships from China to the cart and shipping it to the US address, you see that the estimated delivery is 7-14 days  

    * Upon adding a product that ships from the US to the US (California) address, you see that the estimated delivery is 0-7 days  

    * Upon adding the same products and changing the ship to address to an international address (India), the delivery dates change based on the settings that we have provided  
  

## What If Both the Products are in Cart at the Same Time?

One of the frequently asked question regarding the scenarios like this is, “ _**…What if both the products of type A as well as type B, are in the cart at the same time..? How will the estimated delivery date plugin work in that case..?**_ “

WooCommerce Estimated Delivery Date plugin will work seamlessly and will calculate the accurate delivery date in case both the products from shipping classes, US, as well as China, are in the cart.

  * **Both the products are in the cart (shipping to the US address)**  

  * **Both the products are in the cart (shipping to an International address)**  

We hope this guide would have helped you. Feel free to **[contact our customer support](https://www.pluginhive.com/support/)** in case you have any query or need help setting up shipping on your WooCommerce store.

[ Previous  Display Delivery Estimates on your WooCommerce Store  ](https://www.pluginhive.com/knowledge-base/improve-customer-experience-showing-delivery-estimates/)

[ Next  Show WooCommerce Estimated Delivery Date on the Product Page  ](https://www.pluginhive.com/knowledge-base/show-estimated-shipping-date-product-page-using-woocommerce-estimated-delivery-date-plugin/)
