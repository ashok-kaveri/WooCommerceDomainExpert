# Add the custom description during label printing

**Source:** https://www.pluginhive.com/knowledge-base/add-custom-description-label-printing/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Add the custom description during label printing

In order to add the custom description during creating the label for international as well as domestic shipping, you can use the [**custom solution**](https://gist.githubusercontent.com/WooForce/47d58092c89f51154c455050009a3edc/raw/1502f8fe5d1943b384cecfd68dba62f789f3985f/functions.php) developed by our development team. You can add the code to your functions.php or anywhere relevant.

In the above code, $request contains API request data which will be sent to Canada Post during label creation and $order parameter contains order data. This code is given for changing the description to ‘ My Product Description’ as an example.

**Note** : Custom description can be up to 35 characters, more than that will be truncated.

$xml contains API request. For international shipping, $ref_no as an order number( custom-ref-1 in code) is added with comma and $custom_product_description at end. And Custom Description with order number should not exceed more than 35 characters, more than that will be truncated. For reference, it appears on the label as highlighted below:

For Domestic shipping, $custom_product_description is added as custom-ref-2.

For reference, it appears on the label as highlighted below:

Function returns value of $xml.

[ Previous  Set up WooCommerce Shipping by Product Weight and Size  ](https://www.pluginhive.com/knowledge-base/setting-default-product-weight-dimensions-ship-products-using-woocommerce-shipping-plugins/?seq_no=3)

[ Next  How to Download, Install, Activate, and Update PluginHive WooCommerce Plugins  ](https://www.pluginhive.com/knowledge-base/how-to-download-install-update-woocommerce-plugin/)
