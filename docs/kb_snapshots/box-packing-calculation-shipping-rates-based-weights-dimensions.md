# WooCommerce FedEx Plugin: Calculate Rates by Weight & Dimensions

**Source:** https://www.pluginhive.com/knowledge-base/box-packing-calculation-shipping-rates-based-weights-dimensions/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce FedEx Plugin: Calculate Rates by Weight & Dimensions

In this article, we will tell you how to calculate the shipping rates based on the weight and dimensions of the box when using the **[WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)**. Read more below.

## Business Case

Let us consider an example where we want to pack more than one product in a single box based on weights and dimensions, by using **[WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)**.

* * *

## Solution using WooCommerce Shipping Plugin for FedEx with Print Label

Consider we have two products:

Product A with weight 2, and dimensions = 3 x 2 x 1 (length x breadth x height)  
Product B with weight 3, and dimensions = 4 x 3 x 2 (length x breadth x height)  
C is the box in which we would like to pack Product A and B.

Open the product page of **Product A** , move to _Shipping_ section in the _Product Data_ meta box of the product. The first step is to configure the weight and dimensions of each product. Follow the similar procedure for **Product B**

The following screenshot shows above configuration:

_Product dimension of Product A_ _Product dimension of Product B_

Next, follow the below steps:

  * In **Parcel Packing Method** option, select “Pack into boxes with weights and dimensions”.

  * Next, add a custom box which can be used for packing **Product A** and **Product B** together. To create a custom box, click on the _Add Box_ button in the custom box dimensions.

  * Give dimensions and weight of the custom box, as shown in the screenshot below.

_Box Sizes_

  * _Verification_ : To check whether **Product A** and **Product B** are packaged in a single package, enable the debug option. Go to cart page and check package dimensions in FedEx request.

In the FedEx request, we can see the plugin has requested FedEx with a box of the requisite dimensions.

_FedEx Request_

FedEx has responded that it has custom box services for weight = 5 lbs. So billing amount will be charged for the package of total weight 5 lbs.

_FedEx Response_

The weight of Product A + Weight of Product B + Weight of package = 5 lbs ( package weight is Zero). Hence, as you can see that both **Product A** and **Product B** can fit easily in a single package.

_FedEx Response_

Therefore, box packing is quite easy if you pay attention to the dimensions of the boxes being packed.

If you need any help setting up FedEx shipping on your WooCommerce store, feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**. We would be more than happy to help.

_Good luck!_

[ Previous  Add FedEx WooCommerce Tracking Number to Order Completion Email  ](https://www.pluginhive.com/knowledge-base/woocommerce-tracking-number-for-fedex-shipments-in-order-completion-email/)

[ Next  Debug Error: Product # is missing weight. Aborting.  ](https://www.pluginhive.com/knowledge-base/installed-fedex-plugin-shipping-throwing-issues/)
