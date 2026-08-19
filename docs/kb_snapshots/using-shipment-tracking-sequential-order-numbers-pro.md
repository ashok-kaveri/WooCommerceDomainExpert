# WooCommerce Shipment Tracking with Sequential Order Numbers Pro

**Source:** https://www.pluginhive.com/knowledge-base/using-shipment-tracking-sequential-order-numbers-pro/
**Platform:** WooCommerce (WordPress)
**Plugin:** shipment-tracking
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce Shipment Tracking with Sequential Order Numbers Pro

With this guide, we’ll tell you how to use the **[WooCommerce Shipment Tracking plugin](https://www.pluginhive.com/product/woocommerce-shipment-tracking-pro/)** along with the WooCommerce Sequential Order Numbers Pro plugin by SkyVerge to streamline WooCommerce orders.

## What is the purpose of WooCommerce Sequential Order Numbers Pro?

If you aren’t already aware, WooCommerce doesn’t maintain its order numbers in sequence. This happens because of the way WordPress saves its pages/posts.

WordPress considers every new addition like a blog post, media file, page, order as a new post. This was introduced as an effort to make it easier for the developers to work with the WordPress database. In a similar way, for every new order, WooCommerce creates order IDs that don’t always follow the same sequence or numbering as well.

On the contrary, most new users find this sequential system difficult to understand and cope up with. As a result, making mistakes while preparing orders or WooCommerce manifests for shipments or sharing the tracking information with the customers becomes a difficult affair.

The **[WooCommerce Sequential Order Numbers Pro](https://woocommerce.com/products/sequential-order-numbers-pro/)** is one of those plugins that solve this issue and is designed to streamline WooCommerce order numbers is a proper sequence.

* * *

## Compatibility between WooCommerce Shipment Tracking and WooCommerce Sequential Order Numbers Pro

For an online store owner like you, WooCommerce shipment tracking is the most important part of the WooCommerce order completion process. Even the slightest mistake can cause trouble for your orders and sales, in general.

The [**WooCommerce Shipment Tracking Plugin**](https://www.pluginhive.com/product/woocommerce-shipment-tracking-pro/) provides a wholesome way to manage and add tracking details to their respective orders. And with the use of WooCommerce Sequential Order Numbers Pro, you can easily assign tracking data to orders in the desired sequence.

Let’s have a look at how the two plugins work together. We’ll also cover the basic setting up steps involved throughout the complete process.

* * *

### How to correctly define the WooCommerce order sequence?

Once you have installed both the plugins, you can find the plugin settings by going into **WooCommerce > Settings > General**; and once you’re in, you can set the order sequence.

The WooCommerce Sequential Order Numbers Pro plugin automatically detects your current order number and shows the next order number under the Order Number Start option. Have a look at the image below.

It’s quite easy to set up the order sequence as the plugin displays the changes in real-time. So, if you want to display the order number along with the order date then you can do that in the two options – **Order Number Prefix** and **Order Number Suffix**.

For instance, in the first option(Order Number Prefix), you can set the date range by entering the date formats like **{DD}-{MM}**. This would translate into a date format like **06-11**. Similarly, based on your choice, you can further set up the Order Number Suffix option.

The plugin also lets you set timings in the Order number which could prove to be even more convenient for some orders. Also, you can exclude the free orders from your usual order sequence.

Once you are done configuring the plugin, you need to add a code snippet that will convert the Order ID to the Order Number. For that, you need to go to **WordPress > Appearance > Editor > Theme functions (functions.php)**. Here, you need to copy this [code snippet](https://gist.github.com/xadapter/53c0f79c3792d6712ce5b9646427d4f3) and paste it into **_functions.php_**.

* * *

### How to import and assign WooCommerce Shipment Tracking numbers in the correct order?

When WooCommerce Sequential Numbers Pro is used along with the WooCommerce Shipment Tracking plugin, it becomes quite easy to create and import the tracking details.

If you know the format of your orders then you can easily assign the correct tracking information. What the WooCommerce Shipment Tracking plugin does best is imported multiple tracking data into their respective orders. For that, you just need to create a CSV file in a certain format and just upload it to the plugin directly or via FTP. Let’s take an example.

Below is a sample CSV file that needs to be uploaded to five orders that are under Processing status. The plugin uses this particular format with the columns, ID, Carrier, TrackingNumber, and ShippingDate.

Please note that you need to enter the Order Number instead of the Order ID and every order page would have an Order ID and Number as shown below. Just copy this Number and paste it into the excel sheet under the ID column. And after creating this excel sheet, you will have to convert it into a CSV file.

The file can be uploaded by going into **WooCommerce > Shipment Tracking Import > Import > Choose file**, and then clicking on **Upload file** and import. Once you do that, you will find that the orders have been automatically marked as completed.

Furthermore, the order completion emails are sent to the customers along with the uploaded shipment tracking details. Have a look at the image below.

## 

## Conclusion

When it comes to simplifying orders, WooCommerce Sequential Numbers Pro is the way to go. This plugin works great with WooCommerce Shipment Tracking and makes the order completion process a breeze.

The WooCommerce Shipment Tracking plugin is also compatible with the **[WooCommerce Basic Ordernumbers](https://www.pluginhive.com/knowledge-base/using-shipment-tracking-pro-woocommerce-basic-order-numbers-plugin/), **another great order numbers sequence plugin. If you manage invoices online then you should definitely check it out.

**[WooCommerce Shipment Tracking plugin](https://www.pluginhive.com/product/woocommerce-shipment-tracking-pro/)** seems to be the right choice for business owners. You can check out the product page to know more about the features and facilities.

If you need any help setting up the plugin on your website then feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**.

**_Happy selling!_ **

[ Previous  Best WooCommerce Shipment Tracking Plugins-2023  ](https://www.pluginhive.com/knowledge-base/top-5-paid-woocommerce-shipment-tracking-plugins/)

[ Next  Translate WooCommerce Shipment Tracking Messages with Polylang Pro  ](https://www.pluginhive.com/knowledge-base/translate-shipment-tracking-message-polylang-pro-woocommerce-shipment-tracking-plugin/)
