# Calculate Shipping Rates for Pickup and Non Pickup Products

**Source:** https://www.pluginhive.com/knowledge-base/calculate-shipping-rates-pickup-products/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Calculate Shipping Rates for Pickup and Non Pickup Products

In this article, we will discuss a special shipping scenario where both shipping, as well as local pickup, can create confusion for store owners. Moreover, this article will cover how using [**WooCommerce Table Rate Shipping Pro**](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/) plugin, both local pickups and shipping charges can be accommodated together.

WooCommerce allows store owners different ways to ship packages across the globe. From domestic and international shipping to local pickup, different businesses can have different modes of sending products to buyers. While shipping has additional costs attached to it, local pickup service allows the buyer to collect the package directly from the store. In such diverse cases, there are times when it becomes difficult to manage the shipping and pickups together.

* * *

## Christy’s issue – Pickup And Shipping

Online store owners can have a lot of products in their stores. Ideally, for most of the products, store owners prefer shipping. Yet, it is very common to see store owners selling products with pickup options available. For local customers, the shipping option is both inconvenient as well as time-consuming. Until the product is too heavy or too expensive, most customers prefer the pickup option over shipping. In such cases, the store owners may face difficulties on their end. Let’s discuss one such scenario, where the store owner was having trouble with her shipping scenario.

**Christy owns an online electronic store based in Texas, USA**. In Christy’s case, she wants the buyers to pay shipping charges on the basis of the Cart Value. According to Christy, the total price of all the products in the cart will determine the shipping cost. Based on that, she created a shipping table, which you can see below.

The issue arose with the products which they sold with a **local pickup** option available. Her concern was, “** _What will happen when the Pickup eligible product will be added to the cart with another product which is Shipping eligible..?_** ” Ideally, any product will have a selling price which will be added to the cart total. The issue was since her shipping is based on the cart total, a product with zero shipping cost (pickup eligible) yet some selling price, will increase the total value of the cart. This may, in turn, increase the total shipping cost based on the above table.

Let us see how we can resolve this problem using WooCommerce Table Rate Shipping Pro.

* * *

## WooCommerce Table Rate Shipping Pro

WooCommerce Table Rate Shipping Pro is among the top WooCommerce Shipping plugins when it comes to shipping calculations. This plugin supports shipping calculations based on a number of factors, such as,

  * **Product Weight**
  * **Product Quantity**
  * **Cart Value (Price)**
  * **Shipping Class**
  * **Shipping Destination (Zones, Country, State, City, ZIP Code)**
  * **Product Category**

With its advanced shipping calculation modes, it can calculate shipping rates for almost every shipping scenario. Using WooCommerce Table Rate Shipping Pro, Christy can easily set up her shipping rules.

* * *

### Shipping Calculation using WooCommerce Table Rate Shipping Pro

Christy needs to follow the following steps in order to successfully configure her shipping scenario.

  * **Create Shipping Classes and assign products to them  
**Since we are dealing with two different types of products, the first step is to divide them into two different shipping classes. The first shipping class will be for Pickup Products, containing all the products eligible for pickup. The other will be for Standard Products. This shipping class will include all the other products which are eligible for shipping. The below image will show you the two shipping classes.

* * *

  * **Configuring the plugin’s settings**  
Once she has created the shipping classes, she has to configure the WooCommerce Table Rate Shipping Pro plugin’s settings. The Settings tab contains all the important options to **enable the plugin as a shipping method** , the shipping rules **Matrix columns** , **Calculation modes** , etc. In Christy’s case, she needs to select the Matrix Columns shown in the image below. Also, the calculation mode that will help Christy get accurate shipping rates will be ‘**Calculate Shipping Cost Per Shipping Class** ‘. The image below shows where she can select the calculation mode.

* * *

  * **Create Shipping Rules**  
Now the only thing that is left is to create shipping rules. Based on Christy’s shipping table, it is clear that she wants shipping rates as per the cart value. However, for all the products eligible for pickup, she wants the shipping cost to be zero. The image below shows WooCommerce Table Rate Shipping Pro shipping rules that will satisfy Christy’s shipping scenario.

* * *

### Cart Page

Since the shipping rules are created, let’s check the cart page with the following scenarios.

  * **With Pickup eligible product in the cart** When a product that is eligible for pickup comes in the cart, as defined in the shipping rule 1, the only shipping option that is visible is Free Shipping.

* * *

  * **With Standard (shipping eligible) product in the cart** When the product which is eligible for shipping comes in the cart, the shipping rates are calculated based on the cart value. As shown in the above image, the shipping is calculated based on Shipping Rule 4, for a cart value of $75.

* * *

  * ****With both Pickup and Shipping eligible products together in the cart  
****When both the shipping and pickup-eligible products are in the cart, the total cart value is excluding the selling price of the Pickup eligible products. And as a result, the shipping calculation is done based on only the shipping-eligible products.

* * *

For your reference and easy understanding, here is a video tutorial showing the step-by-step instructions on how to calculate shipping rates when there is a Pickup-Only product in the cart.

* * *

## Summary

So this article covered WooCommerce shipping and pickup service. This article deals with the issue store owners face while providing pickup services along with shipping services. Using the WooCommerce Table Rate Shipping Pro plugin store owners can easily differentiate between the two. By creating separate shipping classes for each product type (pickup or shipping eligible), they can easily create shipping rules for each shipping class. The result will be separate shipping rates based on shipping classes. Moreover, for pickup-eligible products only Free Shipping will only be visible on the cart page. Also, when a buyer wants to buy both the products eligible for pick up and shipping, then shipping rates for shipping-eligible products will be visible on the cart page.

* * *

If you have any queries regarding the features and pricing of the WooCommerce Table Rate Shipping Pro, I request you to[**visit the plugin’s official product page here.**](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/) There you will find all the details regarding the plugin. If you have any queries regarding the article, feel free to share your views in the comment section below. I will surely help you understand the shipping scenario discussed in this article.

[ Previous  Calculate Shipping Rates for Different Types of Products in the Cart  ](https://www.pluginhive.com/knowledge-base/calculate-shipping-rates-different-types-product-cart/)

[ Next  Configure Normal & Priority shipping rates for Swiss Post with WooCommerce Table Rate Shipping Pro  ](https://www.pluginhive.com/knowledge-base/configure-normal-priority-shipping-rates-swiss-post-using-woocommerce-tabel-rate-shipping-pro/)
