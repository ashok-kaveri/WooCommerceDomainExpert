# Can I allow the pickup items to remain in the order, while charging for the dump truck items?

**Source:** https://www.pluginhive.com/knowledge-base/can-allow-pickup-items-remain-order-charging-dump-truck-items/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Can I allow the pickup items to remain in the order, while charging for the dump truck items?

In this small guide, we will tell you how to allow pickup items to remain within the order and charge for the dump truck items when using the WooCommerce Table Rate Shipping Pro Plugin.

**Customer:**

If there are “pick up items” and “dump truck” items together, can I allow the pickup items to remain in the order while charging for the dump truck items? Also, occasionally there are two line items that are each dump truck deliveries, each with their own charge. It seems like this is all possible within the user areas of your app, but my logic is on a break.

* * *

**Support:**

You can configure the rate for pickup items by using the shipping class concept. For example, you can configure two shipping classes, one for pickup items, another one for dump trucks. Then create a rule for the dump truck with the rate you want. Create a separate rule for pickup items with cost 0. This way you will be able to achieve your first objective.

For two items in the cart with different charges (both dump truck deliveries) first, create two separate shipping classes. Let us say dump1 and dump2. So now if you frame two sets of rules for these two shipping classes and select calculation mode: Per Shipping class, It should do the job for you.

* * *

[ Previous  My concern is that it’s going to take 1,500 rules since it goes off per pound up to 150#  ](https://www.pluginhive.com/knowledge-base/concern-going-take-1500-rules-since-goes-off-per-pound-150/)

[ Next  How can I set “All the World” instead of typing all the countries names?  ](https://www.pluginhive.com/knowledge-base/can-set-world-instead-typing-countries-names/)
