# Hide ‘FedEx Ground’ for specific zip code

**Source:** https://www.pluginhive.com/knowledge-base/hide-fedex-ground-specific-zip-code/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Hide ‘FedEx Ground’ for specific zip code

Are you looking to hide FedEx Ground when using our **[WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)**? The following [**code snippet**](https://gist.githubusercontent.com/WooForce/53363d90ca7105f99bcfa8184bae7cf5/raw/c5add3d5c3b61d545d0dfdfca69e82538cdcd388/functions.php) facilitates you to hide the shipping service – FedEx Ground. You can hide this shipping service in a cart/checkout page for specified zip code.

In the above code:

–  _$woocommerce- >customer->get_shipping_postcode()_ returns the zip code of destination.

– _$zip_array_ contains the zip codes for which you want to hide FedEx Ground shipping service.

If the destination zip code matches with the zip code in _$zip_array,_ unset the rate for FEDEX_GROUND and return $rates.

[ Previous  Add Purchase Order(PO), Invoice, Customer Reference, and Department numbers to your WooCommerce Shipping Labels  ](https://www.pluginhive.com/knowledge-base/add-purchase-order-po-invoice-customer-reference-department-numbers/)

[ Next  Code snippet to display the Shipping phone number on the WooCommerce Shipping label instead of the Billing phone number  ](https://www.pluginhive.com/knowledge-base/code-snippet-display-shipping-phone-number-label-place-billing-phone-number/)
