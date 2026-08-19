# Shipping Pro – Case based on weight and price

**Source:** https://www.pluginhive.com/knowledge-base/shipping-pro-case-based-weight-price/
**Platform:** WooCommerce (WordPress)
**Plugin:** table-rate
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Shipping Pro – Case based on weight and price

In this article, we will tell you how to configure the WooCommerce Table Rate Shipping Pro Plugin based on the weight and price of the Cart. Read below to know more about it.

Business Case – Suppose we have a case in which shipping prices have to be defined for three scenarios :

  1. Total weight of the order is under 2.5 Kgs.
  2. Total Weight of the order is over 2.5 Kgs.
  3. Total Price of the Items exceeds $50.

Solution to do it in Shipping Pro:-  
We frame three rules as shown :

Rate Matrix

First Rule says that if the order weight is less than or equal to 2.5 kg then shipping cost is $3.5.  
The second rule says that if the order weight is more than 2.5 kg and less than 99 kg then the shipping cost is $5.5.  
The third Rule says that if the order weight is less than or equal to 99 kg and the price is more than $50 and less than or equal to $99, then shipping is free.

Now we may have a question,  
What if the total weight of the product is under 2.5Kg and the total price is above $50?  
In this case, both 2nd and 3rd rules are satisfied. So final decision rests with an option called “Calculation mode” as shown below :

Calculation Mode

Here we have selected “Per Order Min Cost:Calculate shipping cost per order. Choose minimum rate in case multiple rules.”  
Can you guess now, between the 1st and 3rd rules, which one will be selected?  
The third rule will be selected because it selects the minimum cost among the multiple rules.  
This can be verified by seeing the cart page:

Cart

What would happen if we had selected “Per Order Max Cost:Calculate shipping cost per order Choose maximum rate in case multiple rules.”?

Calculation Mode

The plugin would have chosen the 1st rule, as this is the case of maximum.

Cart

Here, in this case, the cart page shows the 1st rule selected.****  
****  
From this, we can have a basic understanding of the relation between rules framed in Shipping Pro and the field “Calculation Mode”.

[ Previous  La Poste Add-on: Weight-Based Shipping for La Poste Colissimo  ](https://www.pluginhive.com/knowledge-base/la-poste-addon-weight-based-shipping-la-poste-colissimo/)

[ Next  What are the default units of weight, dimensions, and price for Shipping Pro?  ](https://www.pluginhive.com/knowledge-base/default-units-weight-dimensions-price-shipping-pro/)
