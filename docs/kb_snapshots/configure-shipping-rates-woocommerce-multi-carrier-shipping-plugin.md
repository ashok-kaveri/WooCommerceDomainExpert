# Set Shipping Rates in WooCommerce with Multi-Carrier Shipping Plugin

**Source:** https://www.pluginhive.com/knowledge-base/configure-shipping-rates-woocommerce-multi-carrier-shipping-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** multi-carrier
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Set Shipping Rates in WooCommerce with Multi-Carrier Shipping Plugin

With this guide, we’ll see how to set shipping rates in WooCommerce using the **[WooCommerce Multi-Carrier Shipping plugin](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/)**. We’ll also discuss how to display shipping methods like flat rate and free shipping on your cart/checkout page.

## What is WooCommerce Multi-Carrier Shipping Plugin?

The **[WooCommerce Multi-Carrier Shipping plugin](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/)** is the best solution for the store owners looking to offer multiple shipping methods to their customers.

It offers live shipping rates from carriers – USPS, UPS, FedEx, DHL, and USPS(Stamps.com) as well other methods like Flat rates, Free shipping, Local pickup, and more.

* * *

## How does the WooCommerce Multi-Carrier Shipping Plugin work?

The Multi-Carrier Shipping plugin for WooCommerce combines the power of table rate shipping and carriers like FedEx and UPS. It offers great control over the returned shipping rates and services from the respective shipping APIs.

It lets you configure the shipping rates by either increasing or decreasing the API returned shipping rates. Using this plugin, you can even decide how the products will be packed into the boxes, and if an order does not fall under any shipping rule then customers will have to pay the pre-defined fallback rate.

* * *

## How to Set Shipping Rates in WooCommerce?

Let’s begin with the most common business requirement, that is, how to increase or decrease the returned shipping rates.

### Adjusting the value of the WooCommerce Shipping Rates

Many times, store owners may not be happy with the rates returned by shipping carriers. Some may feel the rates are too costly while some feel they are cheaper than the assumed value.

If you too have the need to make slight adjustments in the returned rates, then you can do that under the plugin settings page.

As you can see in the screenshot given below, the **Rule table** contains a column called **Cost Shipping Option**.

In this column, you can add the amount by which the returned shipping rate should either increase or decrease. If you want to cut down the price of the shipping cost then you would have to write ‘-‘ followed by the amount value.

For example, if you wish to decrease the shipping cost by $10 then you need to write ‘-10’ in the column as shown in the image above. Have a look at the video displayed below.

You can notice that when the first item goes into the Cart, the returned shipping cost is $74.92. When we go to the plugin settings page and then define the discount the price goes down to $64.92. This is a great way to give any value in order to increase or decrease the shipping price.

In the latter part of the video, we added $20 to another product in order to increase the shipping cost. Then the shipping rate equals the sum of the shipping cost, the total discount, and the added value as well. After the above steps, the final shipping value turned out to be $166.38.

### Display WooCommerce Flat rate based on product category

Store owners can choose to charge their customer a fixed amount for the shipping, regardless of what he or they orders. It’s a proven way to attract new customers without offering free shipping. Displaying flat rates is also less complicated than calculating shipping rates based on product weight and dimensions.

For example, if you are selling something quite small like a letter or sticker, then offering a Flat rate would be an ideal choice over going with the other method.

With the WooCommerce Multi-Carrier Shipping plugin, you can easily set up a Flat-rate for certain products. You need to define the correct shipping class of the items in the **Rule Table**.

In the image shown below, you would find that you can define the Flat rate under the **Cost Shipping Section** column.

In our example, we have provided a flat rate of $30 for the products under the ‘T-Shirts’ category. When an item under this product category is selected then the Cart/Checkout page will show the pre-defined Flat Rate shipping method.

However, when there is a non-flat rate item along with the above item in the Cart then the scenario changes. Since both products belong to the same Method Group, the total shipping cost would come as the sum of both.

Consider the following image that shows the Cart page containing two different products.

As you can see, the product ‘Some Name’ is a Flat rate product while the other one has a FedEx returned rate. You can check the actual rate by enabling the Debug mode in the plugins settings page.

Refer the following snapshot of the FedEx Response containing the actual shipping rates, that is $61.71.

Thus, the total shipping cost of the multiple products is $91.71( $61.71+$30).

* * *

## What is a Fallback rate and how to set it up?

Defining a **Fallback shipping rate** is necessary in case a shipping rule does not apply to a certain product or the entire cart. This way the customer will have to pay a fallback amount instead of nothing.

You can define the Fallback shipping rate based on either per quantity or per weight. Let us take an example to understand this in a better way.

Consider that you have a product that does not belong to any shipping class and the Fallback Rate On is set as Per Unit Weight. You can refer to the following images.

As you can see that the Fallback rate is defined as $100. The Fallback Rate On option is set as Per Unit Weight, then the rate will be multiplied by the unit weight of the item.

Let us take the example of the product ‘Some Name’ and the Product data page is shown below. You can see that there is no shipping class assigned to this product.

Now, if this product comes into the Cart Page then the shipping rate will be displayed as $200.

You can check out the following image of the Cart page for your reference.

If you have not defined the Fallback rate then the Cart page will show the No shipping methods available error. This is a very important feature to have when you are defining the shipping rules only on certain products.

* * *

## Take away…

We hope this article would have helped you learn how to set shipping rates in WooCommerce using the [**WooCommerce Multi-Carrier Shipping plugin**](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/).

The above plugin is an excellent conditional shipping plugin that gives you quite a lot of control over the shipping methods and how they appear on the Cart page.

Let us know if have any queries regarding this article in the comment section below. If you need any further assistance then feel free to **[contact our customer support](https://www.pluginhive.com/support/)**.

_**Happy selling!**_

[ Previous  WooCommerce Conditional Shipping with Multi-Carrier Shipping Plugin  ](https://www.pluginhive.com/knowledge-base/woocommerce-conditional-shipping-with-multi-carrier-plugin/)

[ Next  Shipping Prohibited Items in WooCommerce  ](https://www.pluginhive.com/knowledge-base/hassle-free-shipping-flammable-goods-using-woocommerce/)
