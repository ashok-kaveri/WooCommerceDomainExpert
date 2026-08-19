# WooCommerce Shipping Pro- Chapter 7: Extend using Add-ons

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-shipping-pro-chapter-7-extend-using-add-ons/
**Platform:** WooCommerce (WordPress)
**Plugin:** table-rate
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce Shipping Pro- Chapter 7: Extend using Add-ons

**Business case: For shipping calculation, override/customize the item quantity using the product level shipping unit. Products will either count as multiple shipping units or fractional shipping units. We’ll see how WooCommerce Table Rate Shipping Pro can achieve that.**

### WooCommerce Per Product Shipping Addon For Shipping Pro

Assign shipping unit at product level based on the shipping complexity and configure shipping cost based on the total shipping units customer purchased.

The following table explains the shipping units for each product based on the size of the package.

  * Chair: 1 Quantity is 1 unit
  * Table: 1 Quantity is 5 unit 5
  * Cots: 1 Quantity is 20 unit 20
  * Wardrobes: 1 Quantity is 40 unit 40
  * Bedsheets: 10 Quantity is 1 unit

Total shipping unit will be calculated based on the shipping unit assigned for each product, and final shipping cost will be determined using the following Rate Matrix:

  * 1-4 Units $6.50/ea.
  * 5-14 Units $5.50/ea.
  * 15-24 Units $4.75/ea.
  * 25+ Units $3.00/ea.

Case1: If the customer purchase 1 Chair and 1 Table  
Total shipping units will be 6(1×1 + 1×5)  
Shipping cost will be 6unit X 5.5 which is $33

Case2: If the customer purchases 10 bedsheets and 1 wardrobe  
Total shipping units will be 41 (10X.1 + 1X40)  
Shipping cost will be 41unit X 3 which is $123/-

**Rate Matrix will be configured using Shipping pro and overriding item quantity using product shipping unit using Addon Per Product Shipping Plugin.**  
Download WooCommerce Per Product Shipping AddOn For Shipping Pro plugin from wordpress.org

**Check out[WooCommerce Shipping Pro with Table Rate Plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/) page.**

[ Previous  WooCommerce Shipping Pro – Chapter 8 : Business cases handled by WooCommerce Weight and Country based shipping  ](https://www.pluginhive.com/knowledge-base/woocommerce-shipping-pro-chapter-8-business-cases-handled-woocommerce-weight-country-based-shipping/)

[ Next  WooCommerce Shipping Pro- Chapter 6: Per Shipping Class  ](https://www.pluginhive.com/knowledge-base/woocommerce-shipping-pro-chapter-6-per-shipping-class/)
