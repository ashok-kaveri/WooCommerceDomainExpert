# WooCommerce Table Rate Shipping: Pickup & Shipping Choices

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-table-rate-shipping-pro-allow-customer-choose-between-pickup-option-shipping/
**Platform:** WooCommerce (WordPress)
**Plugin:** table-rate
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce Table Rate Shipping: Pickup & Shipping Choices

In this article, we will guide you on enabling customers to conveniently choose between the Pickup and shipping choices while utilizing the powerful features of WooCommerce Table Rate Shipping Pro. Explore below to discover how you can enhance your store’s shipping flexibility and cater to diverse customer preferences.

While shopping online, who doesn’t like to have multiple options for delivery? One of the most popular ways to attract more customers is by providing them the option of Free Shipping. However, some customers may not worry too much about the shipping expenses. The only thing such customers require is a fast and reliable method of delivery. Something like an Express Delivery or Guaranteed 1 or 2 days delivery may be great even though it may cost a little more. Lastly, for local customers, all this hassle for delivery and additional charges may seem a bit too much. Having a Pickup option for such customers always comes in handy. Well, we have covered some of the most common and widely used delivery methods that are necessary, if not mandatory, to run an online business smoothly.

One of the biggest challenges that still remain is how can store owners integrate all these delivery options for a better customer experience. To achieve this, WooCommerce store owners require a flexible way to set up a shipping scenario which must involve all the following delivery options together,

  * **Local Pickups**
  * **Standard Shipping option**
  * **Express Shipping option**
  * **Guaranteed Shipping option**

* * *

## WooCommerce Table Rate Shipping Pro

WooCommerce Table Rate Shipping Pro is one of the best bets for WooCommerce store owners who want flexibility in providing delivery options. The plugin offers store owners to create their own shipping rules. Using these rules, WooCommerce store owners can calculate shipping rates based on factors like the weight, quantity, and price of the products. Not only that the plugin offers calculation modes to calculate shipping rates per order, per item, or per shipping class and product category. No doubt, it is one of the best WooCommerce table rate plugins available in the official WordPress repository, with some of the coolest features. If you want to check out all the features or you want to have a look at the interface, feel free to [**visit the link here**](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/).

In this article, we will be focusing on the need for WooCommerce store owners to provide a pickup option for the customers along with different delivery options. For this, we will be using the WooCommerce Table Rate Shipping Pro plugin to divide different delivery options and to provide these options to the customers on the cart and checkout page.

* * *

### Adding the Option for Pickups along with Shipping Rates

As discussed, WooComerce Table Rate Shipping Pro lets you calculate shipping rates based on the shipping rules. If the conditions for any shipping rule match, the shipping rates are calculated and then displayed on the cart page. Take a look at the following image showing how you can add a pickup option with the help of shipping rules configured in the plugin settings.

The above shipping rules indicate that,

  * **Rule 1** – If the order weight is less than or equal to 50 lbs inside Zone 1, Local Pickup must be displayed on the cart page.
  * **Rule 2** – If the order weight is less than or equal to 20 lbs inside Zone 1 and Zone 2, a Standard Shipping charge of $5 with $0.2 per lbs will be displayed on the cart page.
  * **Rule 3** – If the order weight is less than or equal to 50 lbs but more than 20 lbs inside Zone 1 and Zone 2, an Express Shipping charge of $18 will be displayed on the cart page.
  * **Rule 4** – If the order weight is less than or equal to 50 lbs inside Zone 1 and Zone 2, a Guaranteed 1 Day Shipping charge of $25 will be displayed on the cart page.

The following image shows the areas under both Shipping Zones.

However on the cart page when we add a product and the address within Zone 1 or Zone 2, **only one delivery option is displayed.** This happens because the plugin requires a **Method Group Name** for the shipping options that must be displayed on the cart page. It must be noted that the plugin calculates a shipping rate and displays it on the cart page. However, in this case, if you want to display the pickup option along with shipping rates, you need to specify different Method Group Names for the shipping rules.

* * *

#### The following things you need to keep in mind while using Method Groups.

  * If there are no groups assigned to the rules, then one which satisfies the conditions will be selected and the shipping rates from that rule will be displayed on the cart page.
  * If you assign the same group name to all the shipping rules, only 1 rule will be selected and the rates from that rule will be displayed on the cart page.
  * In order to display all the shipping rates from all shipping rules, a unique Method Group Name must be given to each rule. Then only all the shipping rates will be displayed on the cart page.

Once we provide the Method Group name to the shipping rules, the shipping rules will look similar to the image below.

Now, since we have successfully created the shipping rules and added a unique Method Group Name for each shipping rule, let’s see what happens when a customer adds a product to the cart.

* * *

### Outcome…

Once the customer adds a product to the cart and calculates the shipping, the following shipping rates will be displayed for Los Angeles, California ( inside Shipping Zone 1).

You can clearly see that all the shipping options are displayed on the cart page, except Express Shipping. This is due to the fact that according to our shipping rules, express shipping is only eligible for products weighing more than 20 lbs up to 50 lbs. Once we increase the product weight to more than 20 lbs, the following shipping rates are shown on the cart page.

Also, in the case of Zone 2, our shipping rules state that there is no option of Pickups for a customer. Once a customer adds the products to the cart page, the following shipping options will be displayed on the cart page.

As you can clearly see the plugin can create a number of shipping rules based on your business requirements. And this way you can display all those shipping options on the cart page. Not only that the same shipping options will be displayed on the checkout page as shown in the image below.

WooCommerce Tabel Rate Shipping Pro is one of the best shipping plugins when it comes to calculating multiple shipping rates and displaying them for customers. Not only the shipping rates, but the options like Free Shipping or Local Pickups, etc. can also be configured based on a number of factors. This way the store owners can completely customize the way the shipping is calculated.

* * *

## Final Thoughts…

This article shows how different delivery options can be easily implemented together at the same time on a WooCommerce store’s cart page. Using the WooCommerce Table Rate Shipping Pro plugin WooCommerce store owners can easily create shipping rules based on which the options will be visible on the cart page. This way the customers can select the option that suits them the most. I hope this article gives you enough idea about the ease with which the plugin achieves such an important business scenario for WooCommerce store owners.

* * *

### About the plugin

[**WooCommerce Table Rate Shipping Pro plugin**](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)

  * Calculate shipping rates based on factors like,
    * Product Cost
    * Product Weight
    * Number of Items in the cart
    * Shipping Classes
    * Product Category
    * Destination Address

[ Previous  WooCommerce Measurement Price Calculator with Table Rate Shipping  ](https://www.pluginhive.com/knowledge-base/easily-ship-products-custom-quantities-table-rate-shipping-pro-woocommerce-measurement-price-calculator-plugin/)

[ Next  WooCommerce Table Rate Shipping Pro plugin With WPML for Multilingual sites  ](https://www.pluginhive.com/knowledge-base/using-wpml-woocommerce-table-rate-shipping-pro-plugin-multilingual-sites/)
