# WooCommerce Shipping Pro- Chapter 6: Per Shipping Class

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-shipping-pro-chapter-6-per-shipping-class/
**Platform:** WooCommerce (WordPress)
**Plugin:** table-rate
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce Shipping Pro- Chapter 6: Per Shipping Class

In this article, we will tell you how you can set the shipping cost for each country and the shipping class present when using the **[WooCommerce Table Rate Shipping Pro Plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)**. Read below to know more.

### Would like to set the shipping cost for each country and the shipping class. Is this Possible?

Absolutely Yes.

**Prerequisite for Such Business Cases:**

The calculation Mode must be set to Calculate Shipping Per Shipping Class, as shown in the image below.

#### **Detailed business case:**

Shipping cost for Class “gaskets”:

  * Australia:$11.00
  * USA:$24.00
  * Europe:$28.00

Shipping cost for Class “Carb spacer”:

  * Australia:$22.00
  * USA:$41.00
  * Europe:$47.00

Shipping cost for Class “rocker cover small”:

  * Australia:$28.00
  * USA:$88.00
  * Europe:$94.00

Shipping cost for Class “intake”:

  * Australia:$44.00
  * USA:$92.00
  * Europe:$115.00

#### Pretty easy to set up with shipping pro. Here you go:

#### Cart with all products shipping to Australia:

#### Cart with all products shipping to the USA:

#### Cart with all products shipping to Europe:

#### Business case: I have a shop that sells both products that can be sent and products that must be picked up at the store.

**More info:** Create a shipping class “Pick up at the store”, and apply this shipping class to the products that cannot be sent – create a shipping class “DHL”, and apply this shipping class to the products that can be sent.

  * When a customer buys just “sendable” products, he will be able to choose between “Pick up at the store” (free) and “DHL”
  * When a customer buys both “sendable” products AND “not sendable”, the only shipping option will be “Pick up at the store”.
  * When a customer buys just “not sendable” products, the only shipping option will be “Pick up at the store”.

**Is this doable with your plugin?**  
**Absolutely possible see the Settings screen below:**

**When a customer buys just “sendable” products:**

**When a customer buys both “sendable” products AND “not sendable”:**

#### Business case: Different shipping costs for Products A and B and or C, Also shipping costs vary depending on the number or the costs of the product. Can this plugin handle these scenarios?

  * Product A: shipping for small = 30% of small total PLUS shipping for large = 25% of large total
  * Product B If total <= $67, then shipping = $12 else if shipping > 67 <= 900 then shipping = 18% of total else shipping is FREE (>$900)
  * Product C shipping is $300 per product plus a flat fee of $40

**Yes, it is possible to define shipping costs for product categories/shipping classes individually and sum all the costs to calculate the total cost. Check the settings below:**

**Check out[WooCommerce Shipping Pro with Table Rate Plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/) page**

[ Previous  WooCommerce Shipping Pro- Chapter 7: Extend using Add-ons  ](https://www.pluginhive.com/knowledge-base/woocommerce-shipping-pro-chapter-7-extend-using-add-ons/)

[ Next  WooCommerce Shipping Pro- Chapter 5: United Kingdom Counties/States  ](https://www.pluginhive.com/knowledge-base/woocommerce-shipping-pro-chapter-5-united-kingdom-countiesstates/)
