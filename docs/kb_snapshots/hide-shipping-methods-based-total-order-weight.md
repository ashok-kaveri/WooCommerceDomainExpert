# Hide UPS Services for Shipments Weighing more than 10lbs and Show only FedEx

**Source:** https://www.pluginhive.com/knowledge-base/hide-shipping-methods-based-total-order-weight/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Hide UPS Services for Shipments Weighing more than 10lbs and Show only FedEx

With some good **[WooCommerce shipping plugins](https://www.pluginhive.com/product-category/woocommerce-plugin/woocommerce-shipping/)** , store owners like you can easily show various shipping services on the checkout page. The **[WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** , for example, can allow the users to show the desired shipping services on the Cart/Checkout page.

However, there are many business scenarios where the user wants to implement a certain condition. This condition can be based on the shipping zone, shipping class, item quantity, etc. The power to control the display of the shipping services is a highly requested feature.

In this article, we will show you how to hide certain shipping methods based on the total weight of the shipment. This way, store owners can set a weight limit beyond which the selected shipping services will be automatically hidden on the Cart or Checkout page. So, let us quickly get on with the article.

Initially, you need to [refer the following code snippet](https://gist.githubusercontent.com/anonymous/65b8bfcb98af6e70ba3ed1bb2c52ea7b/raw/14abfbe3383908ba98e79972b3c48dd9b3fd0be5/gistfile1.txt) and paste the code snippet in, **Appearance– > Editor–> Theme functions(functions.php) **and then click on Update File**.**

We are going to hide the UPS shipping service whenever the total weight of the shipment is more than 10 lbs. This way only FedEx services will be visible on the Cart page. Here, you would need to define the shipping methods that you need to hide. In the following line of code, you can see many shipping methods.

$shipping_services_to_hide = array(  
‘wf_shipping_ups:13’,  
‘wf_shipping_ups:14’,  
‘wf_shipping_ups:01’,  
‘wf_shipping_ups:59’,  
‘wf_shipping_ups:03’,  
‘wf_shipping_ups:02’,  
‘wf_shipping_ups:12’,  
);

These shipping service names are termed as value. They can be obtained by selecting the respective services on the cart page. Thereafter, you need to **Inspect** that service and you would obtain the service value. You can refer the following video for the same.

Inspecting the page

By following these steps, you can choose the choice of services and then paste it in the code snippet. After doing the above steps you have to set the weight limit. You can do that in the following line of code.

if($weight_oz > 10)

Here, you can choose to set the greater than or lesser than sign as well. Following are the valid signs – **<** , **>** , **< =** and **> =. **In the above case, we are going to define the weight limit of 10lbs. So, whenever the order weight crosses the threshold of this weight, only FedEx services will be visible. You can refer the following video that shows that working of this code snippet.

<https://www.pluginhive.com/wp-content/uploads/2018/02/hide_shipping_pluginhive.mp4>

* * *

If you have any query regarding this article or the integration of **[WooCommerce WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** with your WooCommerce then feel free to share your views in the comment section below. We will be more than happy to help you understand how this plugin can work together in fulfilling your shipping requirements.

Or in case you are wondering what more does the WooCommerce WooCommerce Shipping Plugin for FedEx with Print Label serve, I would request you to kindly [**visit the official product page here**](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)**.**

[ Previous  Set up WooCommerce Shipping by Product Weight and Size  ](https://www.pluginhive.com/knowledge-base/setting-default-product-weight-dimensions-ship-products-using-woocommerce-shipping-plugins/)

[ Next  Customize Delivery Date formats in WooCommerce FedEx plugin  ](https://www.pluginhive.com/knowledge-base/woocommerce-fedex-plugin-customize-estimated-delivery-date-formats/)
