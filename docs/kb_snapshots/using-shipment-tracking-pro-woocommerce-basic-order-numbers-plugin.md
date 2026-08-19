# WooCommerce Basic Order Numbers Plugin: Streamline Order Tracking

**Source:** https://www.pluginhive.com/knowledge-base/using-shipment-tracking-pro-woocommerce-basic-order-numbers-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** shipment-tracking
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce Basic Order Numbers Plugin: Streamline Order Tracking

WooCommerce has become a hub for many store owners who are looking forward to opening their first online store. However, there are some limitations to the features that it offers. To overcome these limitations, people install useful plugins that make their life easier and work more productive. For instance, if you want to have a payment gateway set up on your Checkout page then you need to install a payment gateway plugin. This type of plugin allows your customers to pay for their orders, which is indeed hassle-free.

As you might know, WooCommerce does not show the Order numbers in sequence. This happens because of the posts saving method of WordPress. You see, WordPress considers every new event like a blog post, media, etc, as a new post. And yes, WordPress also considers a new order as a new post. This has been done to make it easier for the developers to work with the WordPress database.

On contrary to the benefits, many store owners might find this system difficult. They sometimes make mistakes while preparing their orders for shipment or sharing the tracking information with the customers using tracking plugins like the [Shipment Tracking Pro from PluginHive](https://www.pluginhive.com/product/woocommerce-shipment-tracking-pro/).

But, this might be the end of your problems. The [WooCommerce Basic Order numbers ](https://wordpress.org/plugins/woocommerce-basic-ordernumbers/)plugin is designed to help store owners streamline their order numbers. This way you can manage and assign correct tracking data to the orders.

* * *

## Configure the order numbers

Once you have installed the plugin, you can find the plugin settings by following **WooCommerce > Settings > Checkout > Order Numbers**. Here you can set the order format once you have enabled the **Customize Order Numbers** option. This plugin automatically changes your next order number once you have defined the format.

It is quite easy to set up the sequence of the order sequence. So, if you want to display the order number along with a custom text then you can do that. For instance, in the above image, we have defined the format as Order_No#. The # is used to determine the order number and this format would translate into Order_No.121, Order_No.122, etc.

Once you are done configuring the plugin, you need to add a code snippet that will convert the Order ID to the Order Number. You need to paste the snippet in your WordPress > Appearance > Editor > Theme Functions**(functions.php)**. You can [copy the code snippet from here](https://gist.github.com/xadapter/611aee58bbc2322fcf6a62271c80c6d9).

* * *

## Importing bulk tracking data

When paired with the WooCommerce Basic Order numbers, the Shipment Tracking Pro plugin becomes quite a breeze to work with. For one, if you know the format of your orders then you can easily assign the correct tracking information. What the Shipment Tracking Pro plugin does best is importing multiple tracking data into their respective orders. For that, you just need to create a CSV file in a certain format and just upload it to the plugin directly or via FTP.

Below is the CSV file that needs to be uploaded to five orders that are under **Processing status**. The plugin uses this particular format with the columns, ID, Carrier, TrackingNumber and ShippingDate.

Please note that you need to enter the Order Number instead of the Order ID. Every order page would have an Order ID and Number as shown below. Just copy this Number and paste it into the Excel sheet under the ID column. And after creating this Excel sheet, you will have to convert it into a CSV file.

The file can be uploaded by going into the **WooCommerce > Shipment Tracking Import > Import > Choose file** and then clicking on Upload file and import. And once you complete the importing process, you will find that the orders have been automatically marked as completed. As mentioned before, the order completion emails are sent along with the tracking details.

In the image below, you can see that the shipment tracking details has been allotted to their respective Order Numbers.

The WooCommerce Sequential Numbers Pro is the way to go when it comes to simplifying your orders for shipment. And now with this compatibility, order completion with minimum effort doesn’t seem to be that difficult of a job. What’s surprising is that the overall process hardly takes any time, and it is convenient for you and your customers.

[ Previous  Choose The Best WooCommerce Shipment Tracking Plugin  ](https://www.pluginhive.com/knowledge-base/top-features-ideal-woocommerce-tracking-plugin/)

[ Next  WPML Compatibility with WooCommerce Shipment Tracking Pro  ](https://www.pluginhive.com/knowledge-base/wpml-compatibility-woocommerce-shipment-tracking-pro-plugin/)
