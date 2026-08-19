# Set up WooCommerce Shipping by Product Weight and  Size

**Source:** https://www.pluginhive.com/knowledge-base/setting-default-product-weight-dimensions-ship-products-using-woocommerce-shipping-plugins/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Set up WooCommerce Shipping by Product Weight and Size

With this guide, we’ll help you set up WooCommerce Shipping by the Weight and Size of your WooCommerce Products. You’ll also learn how to set a default weight and dimensions for your products when using a [WooCommerce Shipping plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/).

* * *

## Importance of Adding the WooCommerce Product Weight and Dimensions

If you’re looking to calculate [shipping rates](https://www.storeapps.org/woocommerce-shipping-by-weight/) for your products, it’s very important that you mention the weight and dimensions.

However, store owners new to WooCommerce often forget to define the weight and dimensions of their products. In some cases, the products that they sell have incorrect weights and the complete shipping costs come out to be inaccurate.

Another issue is that all [shipping carriers](https://www.pluginhive.com/carriers/) require product weight to calculate the shipping rates. If your products don’t have correct physical attributes then you won’t be able to ship via their services.

Clearly, having inaccurate WooCommerce product weight and dimensions can create problems and you should avoid it at all times. So let’s see how to correctly calculate the WooCommerce shipping costs for your products.

* * *

## Setting up WooCommerce Shipping by Weight and Size of Products

As stated above, you need to define the physical attributes of the WooCommerce products before shipping. That’s because both WooCommerce and shipping carriers require the weight and dimensions of your packages/products to calculate the final shipping cost.

To do that, you can enter the **Edit Product** page and move to the **Product data** section where you can see the **Shipping** tab on the left. Here you enter the weight and dimensions of the product. Here you can also select the **[WooCommerce Shipping class](https://www.pluginhive.com/ultimate-guide-set-up-woocommerce-shipping-class/)** and assign it to the product.

* * *

### How to set the Default WooCommerce Product Weight and Dimensions values?

Consider the product shown in the image below. The product is not having any weight as well as dimensions set up on the product page.

* * *

Now, if this product is added to the cart, the following message is shown on the cart page.

* * *

To set up default product weight and dimensions, all you need to do is use the code in [**this Github link**](https://gist.github.com/xadapter/4fb8dbfc6c025630558e43488775eb7d). Copy this code and paste it into the **functions.php** file. You can access this file by clicking,

**Appearance > Editor > _functions.php_**

* * *

#### How to define the default values?

Once you’re done with pasting the code, you need to provide your desired weight and dimensions for the products that you want to be applied by default.

All you need to change the value in the following code to enter the length, width, height, and weight, respectively.

$default_length = **13** ;  
$default_width = **13** ;  
$default_height = **13** ;  
$default_weight = **13** ;

After providing the default values, just save the changes. Now all of your products would have the same default weight and dimensions that you have provided using the code.

As for our product, once adding the code we changed the default weight and dimensions to,

Weight – 1 lbs  
Length – 2 in  
Width – 3 in  
Height – 2 in

And the result being shipping rates were displayed for the product. You can see the weight and dimensions of the products on the cart page by enabling the **Debug Mode**.

The image above shows the shipping rates on the cart page for the product with no weight or dimensions. As you can see, the available shipping rates are displayed on the cart page as a result of accurate shipping weight and dimensions.

* * *

## Conclusion

We hope this article would have helped you set up **WooCommerce shipping by weight and size**. If you have any queries regarding this article or have any difficulty implementing the shipping scenario, please let us know in the comment section below.

You can also **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**. Our support team will surely help you resolve your issues.

**_Happy selling!_ **

[ Previous  Set Minimum Shipping Cost for WooCommerce Shipping Methods  ](https://www.pluginhive.com/knowledge-base/setting-minimum-shipping-cost-various-woocommerce-shipping-methods/?seq_no=4)

[ Next  Add the custom description during label printing  ](https://www.pluginhive.com/knowledge-base/add-custom-description-label-printing/)
