# I added 36 line and when I try to add more rows I’m faced with this error "action failed

**Source:** https://www.pluginhive.com/knowledge-base/added-36-line-try-add-rows-im-faced-error-action-failed/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# I added 36 line and when I try to add more rows I’m faced with this error "action failed

**Customer** :

I’m using the free version of your **[WooCommerce Table Rate Shipping Plugin](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/) **on my site and I’m planning to upgrade to the Pro version.

However, prior to preparing all of the shipping fees to set the transition on the demo version, finally I want to import my own site. So far, I added 36 line and when I try to add more rows I’m faced with this error “action failed. Please refresh the page and retry.”. Am I getting this error because I use the demo version or does the plugin allow to line up 36?

I’m really curious about this because I need to add more rows along with there may be hundreds of different shipping options.

In addition, I wanted to ask;

– during operation of A table with hundreds of rows, an extra load on the system, or a different problem?

– I’m sending you to a table in the Appendix. Is it possible to simplify the table in the Appendix, do you have support on this subject? I believe consist fewer lines of a table will be more stable, do you think so?

Details about the table;

0 – 250 grams between the packet transfer fee: $2.80  
250 – 500 grams between the packet transfer fee: $4.20  
500 – 1000 grams between the packet transfer fee: $8.40  
1000 – 2000 grams, between the packet transfer fee: $14

Economic/unregistered shipping option accepts packets with kilograms 2 . Therefore if the packages weight more than 2 kilograms they are sent in separate packages.

As an example; the shipping fee order 8250 grams for $5 and the order is sent as a separate packet 58.8 (2kg + 2kg + 2kg + 2kg + 0.25 kg)

* * *

**PluginHive Support** :

Regarding the “action failed” , this is due to the PHP Post length issue which can be increased by contacting the hosting provider.

As its very difficult to manage huge set of data in a web interface and it’s very easy to manage in excel sheet or google sheet our customers follow below practice:  
– Configure few rules.  
– Once the configuration is done, it can be verified by going to the shopping cart, adding few products and checkout.  
-the next step is to export the CSV file using the export feature of the plugin.  
-Once you are done with it, that means you now have a valid working CSV with you.  
-The prices for the remaining weight slab should be carefully configured.  
-Import the newly prepared CSV.  
-Then go to shopping cart and test again.  
-Whenever you need to modify the rules, you can modify the CSV and import again.

1000 of rows doesn’t impact the calculation during the checkout process, However, its recommended to limit the row for the maintainability. As per the analysis of the data provided by you, With the slight change in the shipping cost, you can represent the entire rules in one row.

I see a pattern of $1.4 for every 250 grams. If this is the case, you can configure the rule in single row like below:

Min-Max Weight: 0-20000  
Per Unit Cost: 1.4  
Round : 250

Alternative you can configure the Rounding as 2000 and define a Per Unit cost for every 2000 gram.

For more information and features, check out the **[WooCommerce Table Rate Shipping Pro](https://www.pluginhive.com/product/woocommerce-table-rate-shipping-pro-plugin/)** product page. If you need help setting up table rate shipping on your WooCommerce store, feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**.

[ Previous  Troubleshoot – Getting Multiple Shipping Options with No Price!  ](https://www.pluginhive.com/knowledge-base/troubleshoot-getting-multiple-shipping-options-no-price/)

[ Next  I need a Plugin that allows our store to Calculate WooCommerce Shipping based on Weight and Destination City  ](https://www.pluginhive.com/knowledge-base/need-plugin-allows-store-calculate-shipping-based-weight-destination-city/)
