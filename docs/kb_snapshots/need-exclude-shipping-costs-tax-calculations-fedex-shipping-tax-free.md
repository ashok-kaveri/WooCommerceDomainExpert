# Exclude WooCommerce Shipping Costs from Tax Calculations

**Source:** https://www.pluginhive.com/knowledge-base/need-exclude-shipping-costs-tax-calculations-fedex-shipping-tax-free/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Exclude WooCommerce Shipping Costs from Tax Calculations

With this guide, we’ll tell you about WooCommerce Shipping Tax and how to exclude WooCommerce shipping costs from tax calculation. We’ll take the example of the **[WooCommerce FedEx Shipping plugin](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** and show you the necessary steps.

* * *

## What is WooCommerce Shipping Tax?

WooCommerce shipping tax is the option provided by WooCommerce to include tax in the price calculation. WooCommerce also allows you to set the tax percentage and lets you enable tax based on the location.

Under the **Standard rates** , you get to enable or disable the tax option for locations and zones. In the image shown above, you can clearly see that the radio button has been disabled, meaning, the 14% tax is not applicable for the ZIP code 10017, New York.

* * *

* * *

## Why exclude WooCommerce shipping costs from tax calculation

You have the choice to apply taxes to either each product or the entire cart. You also get to choose if you want to have a tax on the shipping charges you offer.

However, most shipping carriers like FedEx have either taxes already included in the shipping costs or are tax-free. So there’s no need to add an additional tax to the shipping amount.

* * *

## How to exclude WooCommerce FedEx shipping cost from tax calculation

WooCommerce does not have built-in support for FedEx shipping. You require the **[WooCommerce FedEx Shipping plugin](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** to calculate and display real-time FedEx shipping rates on the WooCommerce cart and checkout page. FedEx shipping rates are inclusive of the necessary tax and thus, there’s no need to add another layer of tax.

To exclude tax from shipping cost calculation, you need to go to your WooCommerce settings and slide up to the Tax section. Once there, you can uncheck the Tax option under the **Shipping** column from the respective tax rule.

* * *

Now, let’s take an example and try to see its effects on the cart page.

* * *

In the above example, since the WooCommerce shipping tax calculation is turned on, the cart clearly says that the taxes are being calculated and the FedEx shipping rates are also inclusive of taxes.

Note that the **FedEx Ground** is **$11.90** which is a tad more than what FedEx usually charges.

Now, once you disable the WooCommerce tax option under the tax option, you should be able to see shipping rates exclusive of the tax. In the image below, you can see that the **FedEx Ground** is **$10.44** , which is the actual shipping cost without the additional tax as per WooCommerce tax settings.

* * *

## Conclusion

WooCommerce tax is one area where users often face difficulty in setting up a WooCommerce store. It may get even worse when you try calculating the WooCommerce shipping costs and managing taxes on shipping.

We hope this article would have helped you exclude tax from the shipping cost calculation. If you have any problem setting up the **[WooCommerce FedEx Shipping plugin](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** , then feel free to **[Contact PluginHive Customers Support](https://www.pluginhive.com/support/)**.

[ Previous  I need a WooCommerce Shipping Plugin so that my Vendors can Print their Labels with Postage Paid  ](https://www.pluginhive.com/knowledge-base/need-plugin-vendors-can-print-shipping-labels-postage-paid/)

[ Next  Where can I find the Web Services Password for FedEx?  ](https://www.pluginhive.com/knowledge-base/can-find-web-services-password/)
