# How to troubleshoot Multi-Carrier Shipping Plugin for WooCommerce?

**Source:** https://www.pluginhive.com/knowledge-base/troubleshoot-multi-carrier-shipping-plugin-woocommerce/
**Platform:** WooCommerce (WordPress)
**Plugin:** multi-carrier
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# How to troubleshoot Multi-Carrier Shipping Plugin for WooCommerce?

In this tutorial, we will show you how to troubleshoot [**WooCommerce Multi-Carrier Shipping Plugin**](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/) to get accurate and real-time shipping rates from UPS, USPS, Stamps, DHL, and FedEx. It will help you tackle other issues like your cart page is taking too long to load, you are not getting any rates at all, or are unable to save the plugin settings.

## Troubleshooting Multi-Carrier Shipping Plugin for WooCommerce

### Enable Debug Mode

The first step towards finding a solution is to enable the **Debug mode** in the plugin settings, as shown in the screenshot below.

Once you enable this setting, you can view the request and response information on cart and checkout page. If a customer has entered an invalid destination address, selected a service/package that is not available in that region, and other related issues can be viewed in these sections.

Following is a sample screenshot of request and response data, when debug mode is enabled.

**Request:**

**Response:**

### If the problem still persists…

If debugging shipping method doesn’t solve the problem, consider the below case.

The issues stated earlier can also occur when you have a shared hosting service, which makes difficult to understand the root cause of the problem.

In such cases, the solution is simple. In your MySQL configuration file, increase the value of **max_allowed_packet**. Usually, in a shared hosting service, this value is set less. You can increase this value accordingly. The recommended value is **max_allowed_packet=16M**.

* * *

To know more about the product, check out [**Multi-Carrier Shipping Plugin for WooCommerce**](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/).

[ Previous  WooCommerce Shipping – Configure Shipping Area Management for Multiple Carriers  ](https://www.pluginhive.com/knowledge-base/woocommerce-shipping-configure-shipping-area-management-multiple-carriers/)

[ Next  WooCommerce Shipping Plugins Comparison Chart – Multiple vs. Individual Carrier-Integration  ](https://www.pluginhive.com/knowledge-base/woocommerce-shipping-plugins-comparison-chart-multiple-vs-individual-carrier-integration/)
