# WooCommerce UPS Shipping Plugin [Error Code 10001] -The XML document is not well formed

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-ups-shipping-plugin-print-label-xml-document-not-well-formed-error-code-10001/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce UPS Shipping Plugin [Error Code 10001] -The XML document is not well formed

In this small guide, we will help you solve the issue where you get the message, “[Error Code 10001] – The XML document is not well-formed” while using the WooCommerce UPS Shipping Plugin with Print Label. Read more below.

A couple of our customers have encountered this error and it has affected their business. Getting this error means the shipping request sent to the UPS server does not get delivered. Why do they get this error? First, here’s what you need to know about the premise of the error. There are special characters in XML coding that’s used for specific functionalities. Some of the special characters are: ‘(‘, ‘)’, ‘}’, ‘{‘, ‘&’, ‘$’, etc. If you have these characters in your UPS account name/password field, it’s going to throw that error message.

#### What to do when you see this message while using UPS plugin for your shipping purposes?

Here are a few things you can do:

  1. Turn on the debug mode, and click on confirm shipment.
  2. Check the debug data: UPS Request-> check if there is any special characters on the password field/account name field, or any other shipper/ship-to data etc.
  3. If you find one, you’ll have to go to the location where there’s special character and change those.

What to do when the UPS password field has a special character?

  1. Go to UPS Login page: https://www.ups.com/one-to-one/login.
  2. Click on “I forgot my User ID or Password.”
  3. Reset the password without special characters.

If these steps still don’t fix your issue, please contact our [Support Team](https://www.pluginhive.com/support/).

[ Previous  Decoding Debug Data of WooCommerce UPS Plugin  ](https://www.pluginhive.com/knowledge-base/decoding-debug-data-woocommerce-ups-plugin/)

[ Next  How to resolve differences between rates returned by the plugin and the UPS shipping calculator  ](https://www.pluginhive.com/knowledge-base/difference-rates-returned-plugin-ups-shipping-calculator/)
