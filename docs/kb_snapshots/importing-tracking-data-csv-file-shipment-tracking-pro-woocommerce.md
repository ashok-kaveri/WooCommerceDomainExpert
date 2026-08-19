# Bulk Import WooCommerce Shipment Tracking Details via CSV

**Source:** https://www.pluginhive.com/knowledge-base/importing-tracking-data-csv-file-shipment-tracking-pro-woocommerce/
**Platform:** WooCommerce (WordPress)
**Plugin:** shipment-tracking
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Bulk Import WooCommerce Shipment Tracking Details via CSV

With this article, we would explore the CSV file importing feature provided by the **[WooCommerce Shipment Tracking plugin](https://www.pluginhive.com/product/woocommerce-shipment-tracking-pro/)**. We will show you how this nifty feature could help you manage orders in bulk.

As the number of WooCommerce orders increases, it becomes quite a challenge to manage every order and assign the accurate shipment tracking IDs to each one of them. The **[WooCommerce Shipment Tracking Pro](https://www.pluginhive.com/product/woocommerce-shipment-tracking-pro/) **plugin plays a vital role in making the entire shipment tracking ID assignment process easier with the CSV file upload feature. Let’s explore to see how.

## How to Create a CSV file?

CSV file is a file type that stands for **Comma Separated Values**. This file type is used to store tabular data (numbers and text) in plain text. You can create the CSV files using the Note++ or any other supported softwares.

However, please keep in mind that the desired encoding of CSV is UTF-8 and is supported by most of the text editors out there. You can [refer to this article](https://www.computerhope.com/issues/ch001356.htm) to know how to create a CSV file.

## How to Prepare a WooCommerce Shipment Tracking CSV file?

The **[WooCommerce Shipping Tracking Pro plugin](https://www.pluginhive.com/product/woocommerce-shipment-tracking-pro/)** has a pre-defined CSV format where the columns are absolute and cannot be changed. You can refer to the following image below.

As you can see in the image above, we have created a table that has six columns:

  1. **ID**
  2. **Carrier**
  3. **TrackingNumber**
  4. **ShippingDate**
  5. **Description**
  6. **OrderStatus**

These six columns help the plugin attach the shipment detail with its correct WooCommerce order. A sample CSV file is already included inside the plugin but you can download this [sample CSV file](https://woocommerceshipmenttracking.pluginhive.com/wp-content/plugins/ph-woocommerce-shipment-tracking/sample-data/sample_shipment_tracking.csv) if you would like to check out the format.

Make sure to fill in the three columns first when preparing the CSV file – **Carrier** , **TrackingNumber** , **ShippingDate.** They are quite self-explanatory and you can get these details right from your shipping carrier(like UPS, FedEx, USPS, etc.,) since most of them let you download the details in a CSV or zip file.

If you’re using a shipping software like the **UPS Worldship** or **Royal Mail Click & Drop**, you can simply download the details and add them to the CSV file as explained before.

## Map Shipment Tracking details to their Respective WooCommerce Orders

The six columns mentioned above would help you prepare your CSV file and upload the tracking details to their respective WooCommerce orders.

The first column, **ID** , represents the **WooCommerce order number** you find under the column **Order** under the **Orders page.** You can refer to the sample image below.

Now, if you aren’t already aware, WooCommerce doesn’t maintain its order numbers in sequence. This happens because of the way WordPress saves its pages/posts. That’s the reason why many WooCommerce users use a sequential order numbers plugin along with this WooCommerce Shipment Tracking plugin to streamline their orders. You can read about **[WooCommerce Sequential Order Numbers](https://www.pluginhive.com/knowledge-base/using-shipment-tracking-sequential-order-numbers-pro/)** here.

### Automatically mark the WooCommerce Order Status as Completed post Fulfilment

The next one you have is the **Description** column that allows you to enter a brief description for the order scheduled to appear in the Order confirmation page. The final column is the **OrderStatus** that lets you specify the status of the WooCommerce Orders.

If you wish to automatically mark some of your orders as completed then you need to enter **Completed** under the **OrderStatus**. This way the Order details page would be updated with the new order status, i.e, Completed.

And if you want to change the order status to anything else, like **Processing** , then simply enter **Processing** under the **OrderStatus** column like before.

## Importing the CSV file into the WooCommerce Shipment Tracking plugin

Let’s assume we have three WooCommerce orders to update – 30, 31, 32; and we’ve prepared a CSV file accordingly. In order to import the prepared CSV file, you need to go to **WooCommerce** →**Shipment Tracking Pro-Import** →**Import Tracking Details**. Once you’re there, you need to choose the CSV file from your local folder as shown in the image below.

After importing, the tracking data for the selected orders would be updated and the order statuses are marked as **Completed.** After this, the order completion emails containing the tracking details are sent directly to the customers.

Now as soon as you have chosen the file, you have to click on the **Update file and import**. You would see the following message after this step.

* * *

* * *

We could go to the Order summary page and open any one of the three orders to check whether the import was successful or not. In this example, we will go and check the UPS order i.e, order number **32.**

As you can see the email contains the UPS tracking number with the link and shipping date.

### Manually update the Shipment Tracking details for certain WooCommerce Orders

Let’s say there are a few WooCommerce orders that you’re planning to update manually. In that case, you can simply go to the desired order page and update the section available on the right-hand side. Here’s how the interface looks like.

Here you can select from the list of carriers, enter the tracking number manually, add description, and select the shipment date. Once you’re done with the order, you can click on the **Save/Show Tracking Info** to save the changes and send the order completion email manually.

### Import and Schedule WooCommerce Shipment Tracking Details automatically via FTP upload

The **[WooCommerce Shipment Tracking plugin](https://www.pluginhive.com/product/woocommerce-shipment-tracking-pro/)** also lets you to automatically import from a remote server using FTP. With the help of this feature, WooCommerce store owners can easily upload a CSV file containing the shipment tracking data, stored on a remote server automatically.

The plugin also provides a mechanism to automatically schedule the import based on the server current time. You can read more about **[automatic FTP WooCommerce shipment tracking upload](https://www.pluginhive.com/knowledge-base/woocommerce-tracking-now-import-tracking-details-automatically-via-ftp/)** to know more about this feature.

## Benefits of Importing the WooCommerce Shipment Tracking details Automatically

Here are some ways the importing feature in the WooCommerce Shipment Tracking Pro plugin can benefit you.

### A real time-saver!

Automation is all about making things better and faster than their manual counterparts. WooCommerce store owners can have from 5 to 50 orders on a daily basis. Shipping the products for this many orders using single or multiple shipping carriers is itself a time-consuming task.

In such a scenario, automating the process of importing the tracking details of all your shipments in one go will save a lot of time. Also, since the customers will be getting the tracking numbers automatically, they will themselves be able to track their packages.

### Saves money

As we already discussed, the plugin serves the following purposes very well.

  * **Importing the tracking details for all the orders.**
  * **Scheduling the import periodically.**
  * **Sending the tracking details to the customers automatically.**

WooCommerce store owners may be using a number of plugins for either of these tasks. Or in case of manually assigning the tracking numbers to the orders, the above-mentioned tasks require multiple personnel.

Automating the whole process singlehandedly, the plugin provides a scope for the store owners to save their money on multiple solutions.

### Added convenience and ease

Handling a medium or a large scale WooCommerce store is itself a tedious task. Besides, with multiple orders and customers all across the world, WooCommerce store owners require business solutions that can provide the power of automation and can be reliable at the same time.

**[WooCommerce Shipment Tracking Pro plugin](https://www.pluginhive.com/product/woocommerce-shipment-tracking-pro/)** provides store owners the most convenient way to deal with the shipment tracking as well as communicating the tracking details to the customers.

### Boosts customer satisfaction

Improving customer experience and satisfaction is one field in which every online store has been working on for quite some time now. The unnecessary efforts to call or mail a customer support representative or even the store owner can be totally eliminated with the help of the plugin.

Not only that, but the plugin also provides an additional option to personalize the email that will be sent to the customers. With almost all the details regarding their orders as well as with a customized text for some special customers, there is nothing more a customer can ask from an online store.

## Conclusion

So that’s it! That’s how you use the seamless CSV file upload feature to improve your overall order-fulfilment process with the WooCommerce Shipment Tracking plugin.

We hope this guide would have helped you explore features like FTP upload, Scheduled upload, Manual shipment tracking update, and more. If you need any help setting up shipment tracking on your WooCommerce then feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**.

**_Happy selling!_ 🙂**

[ Previous  Import WooCommerce Order Tracking Details via FTP & CSV  ](https://www.pluginhive.com/knowledge-base/woocommerce-tracking-now-import-tracking-details-automatically-via-ftp/)

[ Next  WooCommerce Shipment Tracking: Send Shipping IDs via Email  ](https://www.pluginhive.com/knowledge-base/how-shipment-tracking-pro-sends-shipping-ids-via-email/)
