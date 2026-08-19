# WooCommerce Shipping Pro – Chapter 2: Solving Business Case

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-shipping-pro-chapter-2-solving-business-case/
**Platform:** WooCommerce (WordPress)
**Plugin:** table-rate
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce Shipping Pro – Chapter 2: Solving Business Case

In this article, we will show you how to show different shipping rates based on multiple weight slabs when using the WooCommerce Table Rate Shipping Pro. Read below to know more.

### Business Case: Different rates based on weight slabs. Beyond the defined range, use rate per unit.

0 – 1 kg : 2 USD  
1 – 2 kg : 3.5 USD  
2 – 3 kg : 4.5 USD  
3 kg + : 4.5 USD + 0.5 USD per each additional kg

### Let’s begin.

Total order weight needs to be considered for calculating the shipping cost, So set the Calculation Mode as ‘Per Order Max Cost’. (Did you notice the ‘Max Cost’? This tells that choose the rule with Maximum shipping cost when multiple rules identified, similarly, you have ‘Min Cost’ to choose the rule with Minimum shipping cost when multiple rules identified.)  
Choose only the matrix columns which are relevant and hide the matrix columns like the Country list, State list, Postcode, Product category, Shipping class, Min-Max Price and Min-Max Item.

### Here you go:

**Let’s have a look at the text translation of the business rule printed just above each rule.**

  * If the order weight is less than or equal to 1kg then shipping cost is $2.
  * If the order weight is more than 1kg and less than or equal to 2kg then shipping cost is $3.5.
  * If the order weight is more than 2kg and less than or equal to 3kg then shipping cost is $4.5.
  * If the order weight is more than 3kg and less than or equal to 999kg then shipping cost is $4.5 + per kg $.5 for the remaining weight above 3kg. (Weight is rounded-up to the nearest 1kg).

Pretty simple. isn’t it? First, 3 rules have fixed shipping cost and the last one has per kg cost.  
Few points to note here:

  * Order weight should be **more than** Min weight and **less than or equal to** Max weight.
  * Per Unit cost is only calculated for the weight above the ‘Min Weight’. So please adjust the Base Cost accordingly.
  * Weight is rounded-up to the nearest 1kg. So the cost will be calculated for 5Kg even though the actual weight is 4.7KG. Set it as 0 if you want cost to be calculated for actual weight without rounding.

### Cart with .45kg total weight:

Enhanced Business Case: Provide Express Service option for the customer to choose with an additional cost of $5.  
Matrix column **Method group** can be used to group shipping rules. Group all the normal service rules to **group1** and all express service rule to **group2**.

### Try again with .45kg total weight:

### Further enhanced Business Case: Need to configure an additional $5 for Canada Shipping, and an additional $10 for all other countries.

Few points to note here:

  * Rest of the world option will match for the countries which are not configured in all other rules.

### Canada Shipping with .45kg total weight:

### International Shipping with .45kg total weight:

### Business Case: Client wants to calculate shipping with the percentage for the total price in the cart.

  * If the price is less than or equal to 300$ then shipping cost is $20
  * If the price is more than 300$ and less than or equal to 400$ then shipping cost is $30
  * If the price is more than 400$ and less than or equal to 2500$ then shipping cost is 10% of the total amount.

Shipping cost based on total price can be configured like as follows:

Few points to note:

  * Set ‘Based on’ column as Price.
  * 10% can be configured as .01
  * 10% of the 400 should be configured as the base cost $40, and the amount above $400 will be multiplied with .01.

### Business Case: Set up a solution with an item based setup. I have a base cost, then a per item cost.

Cart with all 3 products:

### Many more complex business scenarios can be handled with this plugin:

  * Configure shipping rule by Shipping class OR Product Category.
  * Configure shipping rule by Quantity OR Price.
  * Calculate shipping cost based on Weight OR Quantity OR Price.
  * The shipping calculation can happen on Entire order /Line Item wise/Category wise/Shipping classwise, and all the costs will be summed to find the final cost.

### Business case: My shop has 3 options for customers to choose: Local pick up (Afhalen), Delivery (Bezorgen) & Office delivery (Bezorgen Kantoor).

  * Local pick-up: Free
  * Delivery: Based on postcode & Free if the order value is above a certain amount
  * Office Delivery: Fixed Fee

**Settings Screen:**

**Cart with all 3 options:**

### Business case: Envelope or Parcel shipping. Within the shop, items for category A are small package and fit into an envelope. Items from the other categories are larger and required a parcel shipping.

There is 3 weight/cost range for the envelope and the parcel shipping method.

  * Envelope: 0-150g, 150-300g, 300-500g
  * Parcel shipping: 0-250g, 250-500g, 500-750g

**Case scenarios:**

  * One or more items of category A = Envelope shipping (with the total weight of the order)
  * One or more items of category A + at least one item of the other categories = Parcel shipping (with the total weight of the order)
  * One or more items of the other categories = Parcel shipping (with the total weight of the order)

**Shipping Pro can easily handle this scenario.** As the Parcel cost will be higher than Envelope cost, we can use calculation mode “Per Order Max Cost” along with the Category filter to solve this business case:

  * When category Books are ordered: “Envelope Shipping” rule will be used to calculate shipping.
  * When category other than Books are ordered: “Parcel Shipping” rule will be used to calculate shipping.
  * When both the above items ordered together: “Parcel Shipping” shipping rules will be used to calculate shipping. (Shipping Cost for “Parcel Shipping” is higher than “Envelope Shipping” and we have selected “Calculation Mode” as “Per Order Max” cost)

**Check out[WooCommerce Shipping Pro with Table Rate Plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/) page.**

[ Previous  How to Download, Install, Activate, and Update PluginHive WooCommerce Plugins  ](https://www.pluginhive.com/knowledge-base/how-to-download-install-update-woocommerce-plugin/)

[ Next  Setting Up WooCommerce Per Product Shipping Add-on  ](https://www.pluginhive.com/knowledge-base/setting-woocommerce-per-product-shipping-plugin/)
