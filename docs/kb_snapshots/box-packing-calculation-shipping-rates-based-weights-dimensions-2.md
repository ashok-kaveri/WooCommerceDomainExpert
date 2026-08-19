# UPS Box Packing – Calculation of shipping rates based on weights and dimensions

**Source:** https://www.pluginhive.com/knowledge-base/box-packing-calculation-shipping-rates-based-weights-dimensions-2/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# UPS Box Packing – Calculation of shipping rates based on weights and dimensions

Suppose you want to pack more than one product in a single box, based on weights and dimensions by using the [**WooCommerce UPS plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/). Here’s how to do it:

Let’s say you have two products.

Product A with weight 2, and dimensions = 3 x 4 x 3 (length x breadth x height)

Product B with weight 3, and dimensions = 4 x 4 x 4 (length x breadth x height)

C is the box in which we would like to pack both products A and B 

**Simple Mathematics involved in packing 2 products into 1 box** :

How to gauge the dimensions of Box C?

Method:

Length: Take the largest length between the two products. In this case, Product B has 4, and A has 3. So we select 4.

Breadth: Take the largest breadth between the two products. In this case, both A and B have 4, so keep it as 4.

Height: Now, if we need to stack one product over another, then heights of the two products would have to be added. So we just add 3+4 = 7.

So our dimensions of the box C would be = 4 x 4 x 7 (in cm) = 1.57 x 1.57 x 2.75 (in inches).

Just to be on the safe side, we round up these values and keep a little more for height (just to your liking). So, finally, we come up with the final dimensions as 2 x 2 x 3.15 (in inches).

Now, we want to pack these two products in a single box!

The first step would be to configure the weight and dimensions of each product.

Go to the admin page – Products – Select the product – Go to Product data Tab – Select Shipping – give values for weight and dimensions.

**Note** : Unit of weight here is kg, and for dimensions, it is cm.

The screenshot below shows the above configuration.

**Product A**

**Product B**

Next, we follow the steps mentioned in the points below.

  1. In Parcel Packing option, we select “Pack into boxes with weights and dimensions.”
  2. Once this is selected, we can now add a custom box which can be used for packing Product A and Product B together. To create a custom box, we just click on the “Add Box” button in the Custom Box Dimensions.
  3. We give the dimensions and weight of the custom box.

**Note:**

  * Items are packed into these boxes based on item dimensions and volume.
  * Outer dimensions are passed to UPS.
  * Inner dimensions are used for packing. 
  * Items not fitting into boxes are packed individually.

Points 1,2, and 3 are shown in the screenshot below:

**Step 3** :  
Verification: To check whether Product A and Product B are packed into a single package.

Enable the debug option. Go to the cart page and check the Package dimensions, UPS request, and UPS Response as shown below:

Package Dimensions: 

  1. In the screenshot below, we can see the weight and dimensions of Product A calculated in lbs and inches shown by point 1.
  2. The weight and dimension of Product B are given by point 2.
  3. The net weight (including package weight) and the dimensions are given by point 3 in the screenshot.

In the UPS Request below, we can see that the plugin has requested UPS with a box of the necessary dimensions.

Response from UPS:

UPS has responded that it has custom box services for weight = 14 lbs. So, billing amount will be charged for the package of total weight 14 lbs.

Note: Weight of Product A + Weight of Product B + Weight of package = 13.22 lbs

Hence, we can see that both Product A and Product B can fit easily in a single package.

This can be verified by printing the label. We can see the dimensions of the packed boxes, weight, and content of the boxes on the label below:

Hence, we can see that Box Packing is quite easy if we pay attention to the dimensions of the boxes being packed. Hope that was helpful!

[ Previous  Efficient Parcel Packing with WooCommerce UPS Plugin  ](https://www.pluginhive.com/knowledge-base/packing-options-available-woocommerce-ups-shipping-plugin/)

[ Next  Add WooCommerce Tracking Number in the Order Completion Email  ](https://www.pluginhive.com/knowledge-base/woocommerce-tracking-number-order-completion-email/)
