# How to Pack a Product into Multiple Packages on WooCommerce

**Source:** https://www.pluginhive.com/knowledge-base/pack-multiple-packages-using-woocommerce-fedex-shipping-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# How to Pack a Product into Multiple Packages on WooCommerce

This article will show you how to optimally sell products that have multiple parts. You will also see how a store owner can divide a single product into multiple packages. Moreover, they can further ship them using **[WooCommerce Shipping plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)**. Besides, this plugin will also help them show real-time shipping rates, directly from FedEx.

It is a fact that every store needs to implement different strategies in order to run a successful business. The foundation of these business strategies is based on the type of product sold in the store. For instance, selling multiple packages from other vendors requires different business strategies than selling self-produced products.

But somehow, it is proving to be more and more difficult for the shop owners to implement these business strategies. This is because there has been a sudden migration of local businesses to online platforms like WooCommerce. They find it difficult to ship their products because of the limitations such as packing methods, weight limits, and many others. But with simple techniques and appropriate digital solutions, they can find a way to achieve their business case.

* * *

So, without any further delay let us jump right into the article.

## Understanding the multiple packages business case

Have a look at the following product.

This is a pack of three separate items

You can see that the weight of the entire product is 5 lbs with dimensions, 9x10x11 inches. This product is a set of three items that come along with it – A poster, a T-shirt, and Wallpaper. Please note that each item has its own weight and dimensions.

In the FedEx Shipping plugin, we will define the Parcel Packing Method as Weight based and the Maximum weight limit as 2 lbs. You can refer to the following image for reference.

The maximum weight limit is 2lbs

* * *

As you can see in the above image, the Pack heavier items first have been selected as the Packing Process. In order to pack the items optimally, we have chosen this parcel packing method. Please note that this parcel packing method will not consider the dimensions of the items and will only calculate the shipping rates based on the weight.

* * *

## Add More Shipping Fields Add-on plugin

This custom solution will allow you to set up your product in such a way that you will be able to set more than one package weight and dimensions to the same product.

In our case, since there are three products sold together as a single product, we can set up three packages. The weight and dimensions of the packages will be the same as that of the products that you are selling. Hence, while generating packages and shipping labels, the shipping plugins will easily distinguish this single product and pack it into three different packages.

* * *

### Setting Up a WooCommerce Product that will be packed into Multiple Boxes using the Add-on

**Pre-Requisites:**

  * [**WooCommerce Shipping plugin for FedEx with Print Label**](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)
  * [**Add More Shipping Fields Add-on plugin**](https://www.pluginhive.com/tailor-made-woocommerce-shipping-solutions/#ship_modular_products_into_multiple_boxes)

**Other Plugins that support Add-More Shipping Fields Add-on plugin:**

  * [**WooCommerce UPS Shipping plugin with Print Label**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)  
**NOTE: The set up will be the same for all compatible plugins (UPS and FedEx)**

Follow the steps below to set up the product with multiple weights and dimensions.

  * Install the [**Add More Shipping Fields Add-on plugin**](https://www.pluginhive.com/tailor-made-woocommerce-shipping-solutions/#ship_modular_products_into_multiple_boxes) from here
  * Activate the plugin and visit the product page for which you require multiple packages
  * Click on **Edit Product**
  * Under the **Shipping** Tab, you can see the weight and dimensions of the product that you have entered
  * Click on **Add More Dimensions** and enter the weight and dimensions of the products that are going to ship together, as shown in the image below  

Add more dimensions and weight to the product
* Update the product

* * *

You can also refer to the video tutorial on how you can set this up and make sure your products are packed based on your requirements.

* * *

## How does Add More Shipping Field Add-on plugin work?

As you can see in the video, we have mentioned the weight of each product is not more than 2lbs. We have done this because if the weight of the package crosses the maximum weight limit of the packing method then the rule will break. This breakage will result in incorrect package quantity and thus, will show higher or lower rates than the actual rates.

In order to check out how this plugin works, just enable the debug mode. Once you set up the product using the add-on plugin, visit the Cart page and choose a shipping destination. In the debug request, you will be able to see the packages in the form of arrays, as shown in the image below.

The number of arrays will show the number of packages

In the video, you can see that there are three arrays, [0] => Array, [1] => Array, and [2] => Array, that shows that there are three parcels of weights 2lbs, 2lbs, and 1lbs respectively.

If you look at the FedEx Response, you will find that FedEx is calculating the shipping rates by taking the weight as 5 lbs. You can refer to the following image for that.

The total weight is shown as 5lbs

* * *

In the video shown above, we have enabled FedEx Ground as the only shipping service. If you compare the shipping rates to that of the FedEx Rate calculator then you would find that the rates are the same. Have a look at the following screenshot of the FedEx Rate Calculator.

* * *

Now, if we go ahead and place the order, the store owner can see the order something like shown in the screenshot below.

* * *

* * *

As you can see that there are three packages and if you click on the Create Shipment option, then the next page would something like this.

Three shipping labels are generated

* * *

The shipping labels for these packages would like the following set of images.

* * *

* * *

This way customers can pay the exact shipping charges and you will be able to optimally pack your products into multiple packages.

* * *

## Summary…

So this article covers advanced functionality which can help a lot of store owners to customize the way they pack and ship their products. The WooCommerce Shipping plugin for FedEx and the add-on plugin together serve as a complete WooCommerce shipping solution. The need to add multiple dimensions and weights to the products has haunted the store owners for quite some time now. With this add-on, the WooCommerce shipping plugin for FedEx is the best way for store owners to make sure their products are packed the way they want. At the same time, store owners can also enjoy other features of the WooCommerce shipping plugin for FedEx such as shipping labels, showing estimated delivery dates to the customers, shipment tracking, and much more.

* * *

If you have any queries regarding this article or the integration of the WooCommerce shipping plugin for FedEx with the add-on plugin, feel free to share your views in the comment section below. I will be more than happy to help you understand how these plugins can work together to fulfilling your shipping requirements.

Or in case you are wondering what the WooCommerce Shipping plugin for FedEx serves, I would request you to kindly check out the [**plugin**](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/). If you need assistance regarding our plugins, you can also [**contact our support team.**](https://www.pluginhive.com/support/) We are always happy to help.

[ Previous  Set Up WooCommerce FedEx Shipping Plugin  ](https://www.pluginhive.com/knowledge-base/setting-woocommerce-fedex-shipping-plugin/)

[ Next  Adjust WooCommerce FedEx Shipping Rates by Shipping Class  ](https://www.pluginhive.com/knowledge-base/woocommerce-shipping-fedex-live-rate-adjustment-based-on-shipping-classes/)
