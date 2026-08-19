# WooCommerce UPS Shipping Plugin Frequently Asked Questions

**Source:** https://www.pluginhive.com/knowledge-base/frequently-asked-questions-ups/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce UPS Shipping Plugin Frequently Asked Questions

With this article, we will be covering some of the most common frequently asked questions that people have for the **[WooCommerce UPS Shipping Plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)**. Read along to know more about it.

## WooCommerce UPS Shipping Plugin Frequently Asked Questions

**Q1:** Why am I getting an error as ‘ _No tracking information available [Error Code: 151044]’_ when clicking on **Print label** button? Also, I am not able to see tracking info on UPS site, while trying to test shipments.

**Ans:** The Tracking ID which is generated in the Test mode is not trackable and because of that, you are getting the error as ‘ _No tracking information available’_. You can get the tracking information in the Live/production mode.

* * *

**Q2:** Why am I getting an error as FATAL error: Cannot redeclare class UPS_WooCommerce_Shipping?

**Ans:** If you have already installed the **Free WooCommerce UPS Shipping Plugin** on your site, you must delete it and install the premium version to resolve **FATAL Error**.

* * *

**Q3:** What are the reasons for not getting correct API rates?

**Ans:** If you are getting incorrect UPS rates, recheck shipper address, recipient address, service code, product dimension, product weight, insured value, and negotiated UPS shipping rates.

* * *

**Q4:** Why am I getting an error as  _invalid license access number_ with Debug mode on? And how can I fix this error?

**Ans:** There can be two reasons for getting the above error as given below:

1\. You are getting this particular error because you may be using test credentials in the live mode. To fix this error, select Test option from API Mode field in the **[WooCommerce UPS Shipping Plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)** settings as shown below.

2\. If you are getting above error, recheck UPS User ID, UPS Password, UPS Access Keys and UPS Account Number.

* * *

**Q5:** Why am I getting Error as  _[UPS] No rate returned for service code 12, The requested service is invalid from the selected origin. (UPS code: 111100)_ in Debug Mode?

**Ans:** The above error is shown on the cart page if UPS does not have the particular service available for the specified address(Shipper and Recipient Address). You can see the service code in the **[WooCommerce UPS Shipping Plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)** settings as shown below.

* * *

**Q6:** Currently, I have not measured or weighed my products. Can I still print UPS labels?

**Ans:** Yes, you can use the print label in manual mode. In manual mode, you can mention package dimensions & weight manually while printing label.

* * *

**Q7:** Can I generate only single shipping label even if customer buy more than one item? Right now, it charges shipping individually.

**Ans:** Select the Parcel Packing mode as ‘pack into boxes’ & configure the package boxes also. Here is a documentation on **[FedEx parcel packing methods](https://www.pluginhive.com/knowledge-base/fedex-woocommerce-shipping-plugin-pack-items-boxes/)** to help to understand box packing better.

* * *

**Q8:** While updating the WooCommerce UPS Shipping Plugin, will it keep the settings?

**Ans:** Yes, it will keep settings. Please check our documentation explaining the procedure to [**install and update**](https://www.pluginhive.com/knowledge-base/how-to-download-install-update-woocommerce-plugin/) the **[WooCommerce UPS Shipping Plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)**.

* * *

**Q9:** Can I disable the tax calculated onto the total as I do not want to have the tax on the shipping?

**Ans:** You cannot disable the tax in the **[WooCommerce UPS Shipping Plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)** settings as the UPS API returns the rates with tax. Alternatively, you can navigate to **WooCommerce** > **Tax** > **Standard Rates**. Select the **Shipping** check-box for the required tax as shown below.

* * *

**Q10:** For an invalid zip code, why does the UPS response with a free shipping option?

**Ans** : If you are getting the response with a Free shipping option for an invalid ZIP code, make sure Fallback field is empty in WooCommerce UPS Shipping Plugin setting.

* * *

**Q11:** How can I adjust the box size to fit two products in the same box?

**Ans** : You select the **Parcel Packing Method** as **Pack into boxes**. Then, define the required box sizes in **Custom Box Dimensions** section. In this case, cart items get packed into one of those custom defined boxes. The best fit box gets auto chosen among the boxes defined.

* * *

**Q12:** Does the WooCommerce UPS Shipping Plugin automatically validate Residential/Commercial addresses?

**Ans** : If the residential checkbox is selected in **[WooCommerce UPS Shipping Plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)** settings for the rate request then the shipment will be classified as residential.

There is a second validation done at the back-end and if the address is really supposed to be commercial then the classification will be changed.

**Note:** UPS validates only US addresses as residential or commercial.

You can check out the **[WooCommerce UPS Shipping Plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)** to know more about its features. If you need help setting up UPS shipping on your WooCommerce store, feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**.

_**Happy selling!**_

[ Previous  UPS Insurance Policy with WooCommerce UPS Shipping plugin  ](https://www.pluginhive.com/knowledge-base/insurance-policy-ups/)

[ Next  A radical shift from physical invoices to paperless shipping!  ](https://www.pluginhive.com/knowledge-base/radical-shift-physical-invoices-paperless-shipping/)
