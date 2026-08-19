# WooCommerce Table Rate Shipping Pro – Chapter 3: Bundle Rate Shipping

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-shipping-pro-chapter-3-bundle-rate-shipping/
**Platform:** WooCommerce (WordPress)
**Plugin:** table-rate
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce Table Rate Shipping Pro – Chapter 3: Bundle Rate Shipping

In this guide, we will help you configure the **[Bundle Rate Addon for WooCommerce Table Rate Shipping Pro](https://www.pluginhive.com/bundle-rate-addon-for-woocommerce-table-rate-shipping-pro/)** by showing some common business cases.

## Set up incremental shipping rates for multiple products

If a customer buys say 3 books the first at $5 then $2 for the remaining and then buys 2 DVDs the first at $5 and $3 for remaining.

Let’s see how the **[WooCommerce Table Rate Shipping Pro Plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)** from PluginHive implements this business case.

**Calculating the shipping cost:**  
1st Book: $5  
2nd & 3rd Book : $2 x 2 = $4  
1st DVD: $5  
2nd DVD: $3  
Total Shipping Cost: $17

The plugin can help you implement the shipping scenario by setting up the following shipping rules in the plugin settings.

  * If the order item count is less than or equal to 1 then the shipping cost is $5.
  * If the order item count is more than 1 and less than or equal to 999 then shipping cost is $5 + per item $2 for the remaining item count above 1.
  * If the order item count is less than or equal to 1 then the shipping cost is $5.
  * If the order item count is more than 1 and less than or equal to 999 then shipping cost is $5 + per item $3 for the remaining item count above 1.

Following is a sample screenshot of the WooCommerce Cart page with 3 Books and 2 DVDs. Have a look.

## Set up WooCommerce Bundle rate shipping for multiple countries

Is it possible to combine the Bundle Rate Shipping Cost with a difference for countries? Say the first shipping cost is 5 in the US, 6 in Canada and 7 in the rest of the world?

Following the same, you can set up the shipping rules in the **[WooCommerce Table Rate Shipping Pro plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)** as shown below.

### Set up Free shipping only for one product category

Now let’s try to set up Free shipping for Books when purchased along with DVDs. Following are the conditions explored in detail.

  * If a customer takes accessories & furniture, Accessories & furniture shipped in the same truck. So shipping cost only for furniture.
  * This item ships free with another item.
  * If someone adds gift items & they are also purchasing a gift basket, then just charge the gift basket shipping (so free shipping for all of the gift items).
  * Shipping rate of a particular Category of the product can be set to “Free” or “Fixed Cost” when purchased along with other Category of products.
  * Shipping rate of a particular Shipping Class can be set to “Free” or “Fixed Cost”, when purchased along with other Shipping Class.

Along with the WooCommerce Table Rate Shipping Pro Plugin, [**Bundle Rate Add-on For WooCommerce Shipping Pro**](https://www.pluginhive.com/bundle-rate-addon-for-woocommerce-table-rate-shipping-pro/)plugin is also required to solve this business case.

This is a simple matrix to configure:

  * First Column ‘For this Shipping Class’: Shipping cost for ‘BOOK’ is going to changed.
  * Second Column ‘With these Shipping Class(s)’: When purchased along with ‘DVD’.
  * Last Column ‘New Cost’: Zero set as the new Shipping cost for ‘BOOK’.
  * Similarly For product category instead of shipping class you need to use Columns ‘For this product Category’ & ‘With these Product categories (s)’.

So now When BOOK is purchased along with DVD, Shipping Costs for BOOK is going to be Free. Remaining all the Shipping Cost will be calculated based on the WoOCommerce Table Rate Shipping Pro matrix.

## Set up shipping rates by dividing the total costs among products

Let’s see how you can charge your customers by dividing the total amount based on the number of items.

A store owner has devised their pricing scheme in the following way.

  * Item 1 is $4 for the first item and $1 for each additional. Likewise, for item 2 it is $5 for the first item and $1 for each additional.
  * If I have one of Item 1 and one of the Item 2, can I tell the plugin only to charge the customer $6 ($5 for Item 2 and $1 for Item 1)? I do not want the customer to have to pay $9 for shipping.

To achieve this shipping scenario, you have to configure the rates based on WooCommerce Shipping Classes. For example, if there are two items(Item 1 and Item 2), the rules will have to be framed based on shipping classes ‘Item 1’ and ‘Item 2’, as shown below.

After that, by using the **[Bundle Rate Addon](https://www.pluginhive.com/bundle-rate-addon-for-woocommerce-table-rate-shipping-pro/)** , you will able to change the shipping cost incase the products from shipping class Item 1 and item 2 are selected together by the customers in the cart page, as shown below.

Hence, the shipping cost displayed to the customers would be, as shown in the image below.

## Various business cases handled by Bundle Rate Addon for WooCommerce Table Rate Shipping Pro

  * Column ‘Product Category’ can be used instead of Shipping Class if products are grouped based on Product category and not based on the shipping class.
  * Use the column ‘Country’ to define different shipping costs for each country. Similarly, State & Post Code columns can also be used.
  * Shipping cost can be based on Weight/Price instead of Quantity.
  * Use Round column as 12 if the shipping cost is calculated by the box of 12 bottles. Calculate shipping cost for 12 bottles even if user shop 9 bottles, calculate for 24 even if user shop 21 etc.
  * Set Base Cost & Unit cost as 0 for Free shipping after a certain quantity of products.
  * Use column ‘Method Group’ to have multiple shipping service option to choose for customers.

## Conclusion

If you need any help setting up table rate shipping on your WooCommerce store then feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**. Our team would be more than happy to help you out.

**_Good luck!_** 🙂

[ Previous  WooCommerce Shipping Pro – Chapter 4: Usability Features  ](https://www.pluginhive.com/knowledge-base/woocommerce-shipping-pro-chapter-4-usability-features/)

[ Next  WooCommerce Shipping Pro Chapter-1: Setting Up  ](https://www.pluginhive.com/knowledge-base/woocommerce-shipping-pro-chapter-1-setting-plugin/)
