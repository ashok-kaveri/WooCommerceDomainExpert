# WooCommerce Free Shipping only for Some of the Products

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-free-shipping-for-some-products/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce Free Shipping only for Some of the Products

With this guide, we’ll show you how to display **WooCommerce Free Shipping** for only some of your products and hide for others. We’ll consider a real-life example to show you how it’s done.

## Why offering WooCommerce Free Shipping is tricky?

Shipping a package from one place to another costs money. Either you or a third-party shipping courier service has to take the responsibility of delivering the package to its final destination. While that might sound effortless, the resulting situation could become a little tricky to handle. Consider the following case.

Most buyers expect free shipping option on the cart, especially when they purchase smaller and cheaper items. Managing **[WooCommerce shipping](https://www.pluginhive.com/woocommerce-shipping-a-complete-tutorial/)** costs while offering free shipping becomes rather problematic in such cases. To make it even worse, charging your customers with calculated shipping rates isn’t the ideal solution either. Nobody wants to pay $10 FedEx Ground shipping cost for an item worth $7.99.

So one thing is absolutely clear from above, you should have complete control over your shipping methods. In this specific example, you should know exactly how to offer WooCommerce [free shipping](https://www.pluginhive.com/knowledge-base/increase-sales-providing-free-shipping-beyond-certain-number-items-using-woocommerce-table-rate-shipping-pro/) for certain products and calculated rates for the others.

## WooCommerce Free Shipping along with Weight based Shipping rates

Along with its perks, preparing a calculated shipping rates table has its own loopholes, the biggest one being its implementation. You may choose to personalize the shipping rates on your store but whether it can be implemented or not, that’s the real question. So let’s dig into a simple business case of a WooCommerce store owner, Jason.

**Jason** , the owner of an online store based in the UK, came up with an interesting idea about providing customized shipping rates to his customers.

_We used to provide free shipping on all our products. But recently our store started selling quite bigger products so we thought of charging customers extra for shipping. But this had a negative impact on our sales for the past one month._

_As a result, we decided to provide our customers free shipping for some products and charge shipping for only those products that we added later to the store._

_But can it be achieved? We want weight based shipping rates for some of our products along with free shipping for the others. Is there any way for that?_

Luckily for Jason, this is a very simple yet most popular shipping requirement, so there’s a solution indeed.

### Setting up WooCommerce Shipping Classes

The first step is to create a separate shipping class for both types of products, i.e, the **Free Products** and **Chargeable Products.** The image below shows the two WooCommerce shipping classes.

Now once these shipping classes are created, you need to assign products to their respective WooCommerce shipping classes based on your business case. You can learn more about **[WooCommerce Shipping Classes](https://www.pluginhive.com/ultimate-guide-set-up-woocommerce-shipping-class/)** to know how it works.

### Preparing WooCommerce Shipping Rate Calculation Table

The most important part to achieve this business case is to configure shipping rules using the plugin. To configure the plugin, you need to have a clear idea of what shipping rates you want for a single product and for multiple products.

In Jason’s case, he wants [**WooCommerce weight based shipping rate calculation**](https://www.pluginhive.com/knowledge-base/woocommerce-shipping-pro-chapter-9-woocommerce-weight-based-shipping-simplified/) for all the products that are in the **Chargeable Products** shipping class. Here’s a rough table containing the details about his shipping rates and tabs.

So to implement these shipping rates within the plugin, you need to select the following **matrix columns** in the plugin settings.

Once these columns are selected, you can easily configure Jason’s shipping rates in the plugin. The following image shows Jason’s shipping rates configured in the plugin. You may notice both the shipping classes listed there separately.

  
One of the main things to keep in mind is that all the shipping rates are placed in a **Single Group – Group 1.** This is important when the store owner wants to display only single shipping options among all the shipping methods configured in the table. You can learn about learn more about **[WooCommerce Shipping Zones](https://www.pluginhive.com/calculate-shipping-rates-based-on-woocommerce-shipping-zone/)** if you’d want to configure shipping rates based on zones.

### Choosing the WooCommerce Rate Calculation Method

Also, before going ahead with the shipping, you might want to configure how the rates will be calculated if one or more conditions are satisfied among those in the above image. The following image shows the settings that you need to apply based on the shipping classes.

Since we are all done with the settings, let’s see what shipping options are visible to the customers on the cart page.

#### When Free Shipping Products are Selected

As soon as a customer adds one or more than one free products to the cart, the following shipping method is visible on the cart page.

* * *

You can clearly see the Free Shipping option selected for the customers.

#### When Calculated Shipping Product is Selected

Now let’s see which shipping option is visible to the customers selecting a product from the chargeable product shipping class.

Since the weight of the product selected is 2 lbs, you can see that the shipping method selected in the above image charges $6, based on the **second rule** in the plugin settings.

Here you can see the shipping option that returns $15 based on the**fourth rule** in the plugin settings. The total weight of the shipment is 5 x 2 lbs = 10 lbs, which falls under the 5 – 10 lbs rule.

#### When both Free and Calculated Shipping Products are Selected

Now for the final case, when a customer adds both the products, Free and Chargeable, together in the cart.

You can easily see that the shipping is only charged for the product that is under the Chargeable Shipping Class, based on the **second rule** in the plugin settings.

  
In the above image also, the shipping cost is charged for only those products that are in the Chargeable Products shipping class, but this time it is based on the **last rule** in the plugin settings.

The total weight of the chargeable products is **7 x 2 lbs = 14 lbs.** This means now the shipping charges will be calculated using the formula.

**Base Cost + (Total Weight – Minimum Weight in the rule) x per unit cost**

Hence, shipping cost this time is, **$15 + (14 lbs – 10 lbs) x $1 = $19.**

## Conclusion

So this is how you can provide shipping cost to your customers based on your business needs, just like Jason did. The **[WooCommerce Table Rates Shipping Pro](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/) **has proven to hundreds of online store owners in preparing the shipping charges table.

If you have any issues regarding this article or need help setting up WooCommerce shipping on your store then feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**. Our team would be more than happy to help you out.

_**Happy selling!**_**🙂**

[ Previous  Set up WooCommerce Table Rate Shipping with Divi Theme  ](https://www.pluginhive.com/knowledge-base/divi-theme-compatibility-woocommerce-table-rate-shipping-pro/)

[ Next  Setting up Weight Based Shipping Rates using Shipping Pro  ](https://www.pluginhive.com/knowledge-base/setting-weight-based-rates-using-shipping-pro/)
