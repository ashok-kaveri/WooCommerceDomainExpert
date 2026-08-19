# Volumetric Weight-Based Shipping with WooCommerce FedEx Shipping Plugin

**Source:** https://www.pluginhive.com/knowledge-base/volumetric-weight-based-shipping-using-woocommerce-fedex-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Volumetric Weight-Based Shipping with WooCommerce FedEx Shipping Plugin

Both WooCommerce and Shopify allow you to add weight to products. This concept is based on the fact that each product is shipped by taking only weight into account. However, it does not apply everywhere and there’s another concept called volumetric weight.

Products such as cotton balls, pillows, etc., usually don’t have much weight to them. But they do require more space and thus, the overall weight turns out to be comparatively greater than the actual weight. In such a scenario, actual weight is not considered for calculating the shipping rates. That’s because of the reason that the volumetric weight of the product exceeds the actual weight.

In this guide, we will see how the **[WooCommerce Shipping plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/) **and **[Shopify Shipping App for FedEx](https://www.pluginhive.com/product/shopify-fedex-shipping-app-with-print-label-tracking/)** could help you ship your products based on volumetric weight. We have taken an example of a product with actual weight and dimensions to help you understand better.

* * *

## Setting up volumetric weight in WooCommerce shipping plugin for FedEx

**[WooCommerce Shipping plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** is the best shipping plugin when it comes to automating the entire shipping process. You could use this plugin to fetch real-time FedEx shipping estimates. You could even choose the packing method, automatically generate shipping labels, track your shipments, and much more.

Now let’s see how the plugin handles shipping for products that have a greater volumetric weight than the actual weight. Here’s a sample product that has a higher volumetric weight than its actual weight.

**Our Product – Cotton Balls (Pack of 100)**

* * *

## How to calculate the volumetric weight of your products?

Since we have the actual weight and the dimensions of our product, let us see how you can calculate the volumetric weight of your products easily.

**Dimensions of the product  
** 10 x 07 x 02 in = 25.4 x 17.78 x 5.08 cm

**The volume of the products  
** 140 cu. in = 2294.18896 cu. cm = 2294.2 cu. cm

**Volumetric Weight – Volume / 5000 kg  
** 2294.2 / 5000 kg = 0.45884 kg

**Volumetric Weight (in lbs)  
** 1.015 lbs = 1.02 lbs

Now, since we already had the actual weight of the product, we can easily compare and see which one is greater.

**The actual weight of the product: 1 Lb**  
**The volumetric weight of the product: 1.02 Lbs**

Our product here is having more volumetric weight than the actual weight. Hence, this weight will be considered for calculating shipping rates.

According to FedEx, the official shipping rates for **[FedEx Ground](https://www.pluginhive.com/fedex-ground-shipping-for-woocommerce-users/)** for our product will be based on the volumetric (dimensional) weight of the product. The image below shows the shipping rates based on the volumetric weight of the product.

Now, let us see the shipping rates as well as the weight that the plugin uses as the package weight.

### Comparing the shipping rates

As we know, the **[WooCommerce Shipping plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** can provide FedEx shipping rates for both domestic and international shipments. However, things change in our case as the volumetric weight is greater than the actual weight.

So you need to enable an option that will calculate and compare the two weights, and check which shipping service to choose for the final rate calculation. The following image shows you need to click on Enable Volumetric Weight.

Once you enable the option and you can add the sample item to the Cart. Here are the shipping rates returned by FedEx.

You can easily see the shipping rates are similar to the shipping rates returned by the official FedEx shipping calculator. Now, once the order is placed, the plugin creates shipping packages based on the weight of the product. However, in our case, since the volumetric weight is greater than the actual product weight, the volumetric weight will be considered while creating packages.

As you can see, the package weight matches the volumetric weight that we calculated in the section before. Hence, the plugin is more than capable of handling shipping based on the volumetric weight of the products.

* * *

## Setting up volumetric weight in Shopify Shipping App for FedEx

The **[Shopify Shipping App for FedEx](https://apps.shopify.com/fedex-shipping)** supports volumetric weight-based packing out of the box. You just need to select the ‘Weight Based’ option under the Packing Method. You should be able to see this option on the App page once you’ve installed the Shopify Shipping App for FedEx correctly.

Now let us take the same product and compare the shipping rates. To do that, you will again have to go to the FedEx official rate calculator page. We have now changed the location and the delivery is now from New York to Georgia.

When you pack the same item with the help of the Shopify Shipping App for FedEx, you will get the same shipping rates. For that, the App also allows you to define the weight and dimensions under its Products page.

Once everything is ready, you can move the product to the Cart page and see the shipping rates. Here is the **[FedEx shipping estimate](https://www.pluginhive.com/determine-fedex-shipping-estimate-for-your-woocommerce/)** obtained for the **[FedEx Ground service](https://www.pluginhive.com/fedex-ground-shipping-for-woocommerce-users/)** for the same shipment.

* * *

## Final thoughts…

**[Shipping carriers like UPS, FedEx, DHL](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/)** , etc. have a standard based on which they charge shipping rates. Mostly the shipping rates that we get are based on the weight of the product. However, there is a different aspect that needs to be considered.

This article covers how WooCommerce and Shopify store owners can handle the shipping of those products whose volumetric weight exceeds the actual weight. We also saw how the WooCommerce Shipping plugin for FedEx and Shopify Shipping App for FedEx help you in this particular case.

We hope this guide would have helped you. If you have any queries then feel free to reach out to our **[customer support](https://www.pluginhive.com/support/)**. They should be able to help you configure FedEx shipping on your online store.

_**Happy selling!**_

[ Previous  How to Ship WooCommerce Custom Product Boxes via FedEx  ](https://www.pluginhive.com/knowledge-base/create-ship-woocommerce-custom-product-assortments-via-fedex/)

[ Next  Handle FedEx Non-Standard Packages on WooCommerce  ](https://www.pluginhive.com/knowledge-base/handle-woocommerce-shipping-fedex-non-standard-packages/)
