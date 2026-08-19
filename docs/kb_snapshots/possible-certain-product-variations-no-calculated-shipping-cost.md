# How to exclude certain product variations from the FedEx shipping calculation

**Source:** https://www.pluginhive.com/knowledge-base/possible-certain-product-variations-no-calculated-shipping-cost/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# How to exclude certain product variations from the FedEx shipping calculation

In this article, we will guide you how to exclude certain product variation from the FedEx shipping calculation. This way you can mail them separately to your customer if you wanted to. Read along to know more.

**Customer:**

Is it possible to have certain product variations not to be calculated in the shipping cost? (they will be mailed by us, separately to the client). I would probably try to do this with a shipping class (“FedEx” and “No Cost”), with the “No Cost” shipping class not being added to the shipping calculation.

* * *

**PluginHive Support:**  
Yes, it is possible.

For each variation, you need to define a shipping class. Once you define a shipping class, you can hide the shipping services from the class by using the [**code snippet**](https://gist.githubusercontent.com/WooForce/3e8e65075e469e1e422d/raw/1b8f22e2ab0e3719f3b6ca7c04313171c651ba56/functions.php).

[ Previous  Fix the error message “There are no valid services available” for FedEx Mexico  ](https://www.pluginhive.com/knowledge-base/error-message-displayed-no-valid-services-available/)

[ Next  Create two FedEx Pak shipments, for two different FedEx Pak orders  ](https://www.pluginhive.com/knowledge-base/two-fedex-paks-order-create-two-shipments/)
