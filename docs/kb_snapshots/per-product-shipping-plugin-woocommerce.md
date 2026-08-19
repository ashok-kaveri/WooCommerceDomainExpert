# Per Product Shipping Plugin for WooCommerce

**Source:** https://www.pluginhive.com/knowledge-base/per-product-shipping-plugin-woocommerce/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Per Product Shipping Plugin for WooCommerce

This tutorial explains the business case for per product shipping by using **[WooCommerce Table Rate Shipping Pro Plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)**. Please refer to the product page to know more about the plugin features.

### Per Product Shipping for WooCommerce

**Business case:****For shipping calculation, override/customize the item quantity using the product level shipping unit. Products will either count as multiple shipping units or fractional shipping units.**

Assign shipping unit at a product level based on the shipping complexity and configure shipping cost based on the total shipping units customer purchased. The following table explains the shipping units for each product based on the size of the package.

  * Chair: 1 Quantity is 1 unit
  * Table: 1 Quantity is 5 unit 5
  * Cots: 1 Quantity is 20 unit 20
  * Wardrobes: 1 Quantity is 40 unit 40
  * Bedsheets: 10 Quantity is 1 unit

Total shipping unit will be calculated based on the shipping unit assigned for each product, and the final shipping cost will be determined using the following Rate Matrix:

  * 1-4 Units $6.50/ea.
  * 5-14 Units $5.50/ea.
  * 15-24 Units $4.75/ea.
  * 25+ Units $3.00/ea.

Case1: If a customer purchases 1 Chair and 1 Table  
Total shipping units will be 6(1×1 + 1×5)  
Shipping cost will be 6unit X 5.5 which is $33

Case2: If a customer purchases 10 bedsheets and 1 wardrobe  
Total shipping units will be 41 (10X.1 + 1X40)  
Shipping cost will be 41unit X 3 which is $123/-

Rate Matrix will be configured using Shipping pro and overriding item quantity using product shipping unit using Addon Per Product Shipping Plugin.

**Check out our[WooCommerce Table Rate Shipping Pro Plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)**. If you need more help or have a query then feel free to **[contact our customer support](https://www.pluginhive.com/support/)**. Our support team should be able to help you configure shipping on your WooCommerce website.

_**Happy selling!**_

[ Previous  Kalium Theme Compatible with WooCommerce Table Rate Shipping  ](https://www.pluginhive.com/knowledge-base/kalium-theme-compatibility-woocommerce-table-rate-shipping-pro/)

[ Next  Recover Postage Expenses by including the UK Postal-Code Surcharges to your Shipping Rates using WooCommerce Table Rate Shipping Pro  ](https://www.pluginhive.com/knowledge-base/recover-postage-expenses-including-uk-postal-code-surcharges-shipping-rates-using-woocommerce-table-rate-shipping-pro/)
