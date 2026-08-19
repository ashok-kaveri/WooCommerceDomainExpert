# Weight-based Packing with WooCommerce FedEx Shipping Plugin

**Source:** https://www.pluginhive.com/knowledge-base/weight-based-packing-woocommerce-fedex-shipping-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Weight-based Packing with WooCommerce FedEx Shipping Plugin

In this article, we will discuss one of the most important features of the **[WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** , which is, the weight-based parcel packing method. Read below to know more about it.

Sometimes store owners come up with a special scenario that needs something different from the usual. Such was the case with one of our customers, who wanted the plugin to offer cheaper shipping rates for his items. Let’s see what he has to say.

> **Customer: Hello. I’m using your WooCommerce Shipping Plugin for FedEx with Print Label to ship jewellery. When a customer buys several pieces, I would like to save money on shipping by packing multiple items in one box. is there a way to set this up in your plugin?**

Before we get into solving the above query, let’s first see how weight-based parcel packing works.

* * *

## **Weight-based parcel packing**

The WooCommerce Shipping plugin for FedEx provides three options for parcel packing to store owners. With the help of these parcel packing methods, store owners can choose the one that suits their business case. The image below shows the three parcel packing methods:

In order to opt for the weight-based packing, you need to select the option **Weight based: Calculate shipping on the basis of the order’s total weight.** Now let’s see how it works.

The products that do not have dimensions or do not require it can be packed easily with this particular packing method. On selecting the weight-based packing, you would have to define the **Max Package Weight** and **Packing Process**.

* * *

Now let’s check out these parameters in detail.

### **Max Package Weight**

The plugin allows you to set up a Max Package Weight value. This allows store owners to pack up to that value in a single package. The image below shows the option to add a Max Package Weight value in the plugin settings.

As you can see the Max Package Weight set at 10 lbs and so, you can pack in one package for all the products weighing up to 10 lbs. And if the total weight of all the products crosses the 10 lbs mark, then any additional products will be automatically added to a new package.

* * *

### **Packing Process**

The WooCommerce Shipping Plugin for FedEx also supports some of the pre-defined packing processes that you can select from. The image below shows you the packing options that are available.

* * *

Now, let us discuss these processes in brief.

#### **Pack Heavier Items First**

Suppose there are three types of products in a shop- **Product A (3 lbs), Product B (2 lbs), Product C (6 lbs).** According to the rule, the Max Package Weight set as 10 lbs and thus, the above products will be packed in the following fashion.

  * **Box A – Product C (6 lbs) + Product A (3 lbs) = Total of 9 lbs**
  * **Box B – Product B (2 lbs) = Total of 2 lbs**

You can easily make out that this process first packs the heavy products in the box until the box is either filled or the remaining products can no longer fit into the box. And once the Max Weight is reached, it packs the remaining products into another box.

* * *

#### **Pack Lighter Item First**

This option allows the lighter products to be packed first till the Max Weight is reached or a product can no longer fit into the box. And once the Max Weight is reached, it takes another box to pack the remaining products. So the same scenario will be different while using this packing process. The image below shows the packages created using this process.

  * **Box A – Product B (2 lbs) + Product A (3 lbs) = Total of 5 lbs**
  * **Box B – Product C (6 lbs) = Total of 6 lbs**

* * *

#### **Purely Divided By Weight**

This packing process is different from the other two processes. Packing using this process involves separating and then packing different products having the same weight together. In simple words, all the products with the same weight will be packed in one box until the weight limit reaches.

For example, consider there are 3 of Product A (3 lbs), 2 of Product B (2 lbs), and 1 Product A (6 lbs) in one order. Using this process, all the products with similar weights will be packed in one box. The image shows the products packed based on their weight.

  * **Box A – 2 x Product A (2 lbs) = Total 4 lbs**

But since the package can still contain an additional 6 lbs, the other product with 6 lbs weight can be added to this box.

  * **Box A – 2 x Product A (2 lbs) + 1 x Product C (6 lbs) = Total 10 lbs**
  * **Box B – 3 x Product B (3 lbs) = Total 9 lbs**

* * *

### **Packing based on Volumetric Weight**

WooCommerce provides an option to add weight to the products based on the fact that the products will be shipped based on the weight of the products. However, this is not true in every scenario.

Products such as cotton balls, pillows, stuffed toys, etc., do not have much weight, to begin with. However, the packing space that they require is significant compared to their actual weight. In such cases, actual weight is not considered for calculating the shipping rates and that’s because the volumetric weight of the product exceeds the actual weight of the product.

Now, let us see how the plugin handles shipping for products that have a greater volumetric weight than the actual weight.

**Our Product – Stuffed Toy**

Here is a product that has a higher volumetric weight than the actual weight of the products. Now, let us see how you can compare the volumetric weight and the actual weight of the products.

* * *

### **How To Calculate the Volumetric Weight Of Your Products?**

So, now we have the actual weight and the dimensions of our product, let us see how you can calculate the volumetric weight of your products easily.

**Dimensions of the product –** 10 x 07 x 02 in = 25.4 x 17.78 x 5.08 cm

**The volume of the products –** 140 cu. in = 2294.18896 cu. cm = 2294.2 cu. cm

**Volumetric Weight – Volume / 5000 kg –** 2294.2 / 5000 kg = 0.45884 kg

**Volumetric Weight (in lbs) –** 1.015 lbs = 1.02 lbs

Now since we already had the actual weight of the product, we can easily compare and see which one is greater.

**Actual Weight of the Product –** 1 lbs  
**Volumetric Weight of the Product –** 1.02 lbs

Our product here is having more volumetric weight than the actual weight. Hence, this weight will be considered for calculating shipping rates. According to FedEx, the official shipping rates for FedEx Ground for our product will be based on the volumetric (dimensional) weight of the product. The image below shows the shipping rates based on the volumetric weight of the product.

* * *

Now, let us see the shipping rates as well as the weight that the plugin uses as the package weight.

### **Comparison**

The WooCommerce Shipping plugin for FedEx can provide real-time shipping rates for both domestic as well as international shipments. However, in our case, where the volumetric weight is greater than the actual weight, you need to enable the setting which will calculate and compare the two weights and check which to consider for shipping rate calculation and creating packages. the following image shows the plugin settings store owners need to enable.

Once we enable the setting and add the product to the cart, the following shipping rates were shown on the cart page.

You can easily see the shipping rates are similar to the shipping rates returned by the official FedEx shipping calculator. Now, once the order is placed, the plugin creates shipping packages based on the weight of the product. However, in our case, since the volumetric weight is greater than the actual product weight, the volumetric weight will be considered while creating packages. The image below shows the weight of the package generated to ship our product.

As you can clearly see, the package weight matches the volumetric weight that we calculated in the section before. Hence, the plugin is more than capable of handling shipping based on the volumetric weight of the products.

Selecting the right packaging method for your business shouldn’t be a pain. This is why you are always welcome to submit any query regarding the packaging method in the WooCommerce Shipping plugin for FedEx to our [customer support](https://www.pluginhive.com/support/).

[ Previous  Manage Return Shipments with FedEx Plugin for WooCommerce  ](https://www.pluginhive.com/knowledge-base/manage-return-shipments-woocommerce-fedex-shipping-plugin/)

[ Next  How to Generate Packages Automatically using WooCommerce Shipping Plugin for FedEx  ](https://www.pluginhive.com/knowledge-base/how-to-generate-packages-automatically-using-woocommerce-fedex-shipping-plugin/)
