# Setting Up WooCommerce Shipment Tracking Pro Plugin

**Source:** https://www.pluginhive.com/knowledge-base/setting-woocommerce-shipment-tracking-pro-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** shipment-tracking
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Setting Up WooCommerce Shipment Tracking Pro Plugin

Use this quick guide to set up your **[PH Shipment Tracking Pro WooCommerce](https://www.pluginhive.com/product/woocommerce-shipment-tracking-pro/)** plugin by **PluginHive**. We’ve shown all the necessary settings, steps, and images along the way to help you configure the features available in the plugin.

* * *

## Table of Content

  1. Plugin download, installation & license activation
  2. Choose the shipping carrier(s) used for order fulfillment
  3. Display shipment tracking details to customers on My Account > Orders page
  4. Send shipment tracking details to customers via WooCommerce order completion email
  5. Create a tracking page on your WooCommerce store
  6. Send email notifications to customers on every shipment tracking status update
  7. Customize the shipment tracking message
  8. Add shipment tracking details to WooCommerce orders
  9. Automatically update the WooCommerce order status to “Delivered”
  10. A quick overview of the tracking number and live tracking status in the Admin Orders page
  11. Integrations of PH Shipment Tracking Pro for WooCommerce
  12. Enable Debug Mode for PH Shipment Tracking Pro for WooCommerce

* * *

### 1\. Plugin download, installation & license activation

After purchasing the plugin, log on to PluginHive.com and visit **My Account > API Downloads** and click on the **Download** option in front of the PH Shipment Tracking Pro for WooCommerce plugin, as shown below

* * *

* * *

** _Reference_**  
Please Refer For Installation & License Activation Details – [How to install and activate the license of a PluginHive WooCommerce Plugin?](https://www.pluginhive.com/knowledge-base/how-to-download-install-update-woocommerce-plugin/)  

* * *

### 2\. Choose the shipping carrier(s) used for order fulfillment

After installation, visit **WooCommerce Plugins > PH Shipment Tracking Pro for WooCommerce > Order Tracking**.

The plugin has 85+ shipping carriers built in for easy access. You can either choose from the list of carriers or set up your own shipping carrier. On adding a shipping carrier, you will be able to use the plugin’s shipment tracking functionalities, like

  * Display shipment tracking details to customers on the **My Account > Orders page**
  * Send shipment tracking IDs and the tracking link to the customers via **WooCommerce Order Completion Email**

You can add shipping carrier details within the plugin by clicking on **Add Carrier** , as shown below.

* * *

* * *

#### 2.1 Select from built-in 85+ shipping carriers

From the list of carriers, select your preferred carrier, let’s say FedEx.

* * *

* * *

You can change the carrier display name based on your preference by updating the **Display Name** field. Now, click on **Add Carrier** to successfully add the shipping carrier.

* * *

* * *

#### 2.2 Add a shipping carrier that’s not in the built-in carrier list

In case your preferred shipping carrier is not in the default shipping carrier list, and you have the shipment tracking link for that particular shipping carrier, you can add it to the plugin.

Select the **Add Custom Carrier** option from the drop-down list.

* * *

* * *

Enter the tracking URL of the shipping carrier in the **Tracking URL** field, as shown below, and click on **Add Carrier** to successfully add the custom shipping carrier.

* * *

* * *

**_Note_**  
Once you find the tracking URL for the carrier, you need to format the URL in such a way that,   
* The tracking number is replaced with [ID]  
* and similarly, if the carrier tracking URL requires a Zip Code value, you can replace it with [PIN]  
  
_For Example:_  
If the shipping carrier tracking URL is   
**‘https://www.tnt.com/express/en_in/site/shipping-tools/tracking.html?searchType=con &cons=152121130’**,  
where ‘152121130’ is the tracking ID, while adding the URL in the plugin, you can add the URL as  
**‘https://www.tnt.com/express/en_in/site/shipping-tools/tracking.html?searchType=con &cons=[ID]’**

* * *

#### 2.3 Add shipping carrier API credentials for live shipment tracking

Apart from the default shipment tracking functionality, PH Shipment Tracking Pro for WooCommerce also supports the live tracking feature. This feature provides the shipment tracking updates from the shipping carrier in real-time.

* * *

**_Note_**  
By default, PH Shipment Tracking Pro for WooCommerce supports Live Shipment Tracking for the following carriers only.  
  
* UPS   
* FedEx   
* USPS   
* DHL Express   
* Delhivery  
* Canada Post  
* Canpar Express  
* Colissimo   
* Australia Post  
* Blue Dart  
* Aramex   
* Chilexpress   
* Purolator   
* Sendle   
* TNT Consignment   
* TPC   
* Yanwen   
  
If you want us to provide WooCommerce live shipment tracking for your preferred shipping carrier as well, please contact [**PluginHive Support.**](https://www.pluginhive.com/support/)

* * *

If you want to make use of this functionality on your WooCommerce store, make sure you have a shipping carrier account and API credentials.

Add any supported shipping carrier to the plugin by clicking on the **Add Carrier** button.

Enter the **carrier API credentials** in the respective fields, as shown below.

* * *

* * *

Click on **Add Carrier** to add the shipping carrier successfully.

### 3\. Display shipment tracking details to customers on My Account > Orders page

PH Shipment Tracking Pro for WooCommerce allows you to display shipment tracking details to the customers on the **My Account > Orders** page

Enable the **Tracking Details To Customer** option in the plugin settings.

* * *

* * *

The customers will now be able to view the tracking details by logging in to the **My Accounts > Orders Page**, as shown below.

* * *

* * *

#### 3.1 Display live shipment tracking details to customers on My Account > Orders page

Once the shipping carrier is configured along with the API credentials, you can let customers view the real-time tracking status of the shipments on their My Account page.

Enable the **Display Live Tracking Status in My Account** option in the plugin settings and select from the options explained below.

* * *

* * *

##### Automatic Refresh – Enable

This option will automatically refresh the shipment tracking status on **My Account > Orders page**, in real-time

* * *

* * *

##### Automatic Refresh – Disable

This option will display a Refresh button on the **My Account > Orders page** that will refresh the tracking status manually

* * *

* * *

### 4\. Send shipment tracking details to customers in the WooCommerce order completion email

Another way the plugin gives you an option to send the tracking details to the customers is through the WooCommerce Order Completion Email.

Enable the **Send Tracking details via Email** option in the plugin settings, and the plugin will send the tracking ID along with the shipping carrier name, date of shipment, and order notes (if any) via email.

* * *

* * *

After enabling, once the orders are marked completed, the plugin will attach the shipment tracking details in the **WooCommerce Order Completion Email** , as shown below.

* * *

* * *

### 5\. Create a tracking page on your WooCommerce store

PH Shipment Tracking Pro for WooCommerce lets you create a custom tracking page on your WooCommerce store. You can use this page to display the tracking status to your customers as well as to increase customer engagement on your WooCommerce store.

To set this up, visit **Order Tracking > Tracking Lookup Page** in your WordPress dashboard.

Create a new page on your WooCommerce store and add the shortcode **[ph-shipment-tracking-page]** to that page, as shown below.

* * *

* * *

Once the page is published, copy the page URL and paste it in the **Tracking Page URL** field, as shown below.

* * *

Optionally, you can customize the placeholder text for the **Order Number Place Holder** and **Order Email Place Holder** fields on the tracking page.

Once configured, customers can access the tracking page, enter their order number and email ID to get the shipment tracking status

* * *

* * *

You can also enable the **Let Customers View Tracking Details on Carrier’s Page** option. Once enabled, customers can view the tracking details directly on the carrier’s page by clicking the Tracking URL.

* * *

### 6\. Notify customers on every shipment tracking status update via emails

Enable the **Live Shipment Tracking Alerts For Customers** option in the plugin settings. This will enable your customers to get live tracking updates as soon as the shipping carrier updates the tracking status of the shipment.

* * *

* * *

Here are the sample emails sent to the customers on the tracking status update from the shipping carrier.

##### When the tracking status is changed to ‘Delivered’ by the shipping carrier

* * *

* * *

##### When the tracking status is changed to ‘Item Processed’ by the shipping carrier

* * *

You can also define a custom tracking email template that will be sent to your customers by following the steps below.

Select your preferred email template from the **Choose Tracking Email Template** dropdown. You can choose between **Plugin Default** and **WooCommerce Emails**.

  * Fill in the **Sender Email Details** , i.e. **Name** and **Email ID** , that will be used in the email sent to the customers
  * Enter the email subject in the **Tracking Email Subject** field as per your preference
  * Create your personalized tracking email under the **Email Content** field

* * *

* * *

** _Note_**  
Use the following Tags to customize your Email Template.   
* [CUSTOMER_NAME] – will enter customer’ name in the email   
* [EMAIL_ID] – will enter customer’ email Id in the email   
* [ORDER_NUM] – will enter the order number in the email   
* [CARRIER_NAME] – will enter the carrier name in the email   
* [TRACKING_ID] – will enter the tracking Id in the email   
* [TRACKING_STATUS] – will enter the current tracking status in the email   
* [SHIPMENT_PROGRESS] – will display the tracking history in Table Format in the email   
* [TRACKING_LINK] – will display the Shipment Tracking Number with Link in the email  

* * *

#### 6.1 Choose the WooCommerce order statuses for which the live tracking emails will be sent to the customers

PH Shipment Tracking Pro for WooCommerce allows you to send tracking status notifications to the customers based on your business requirements. You can easily choose the order statuses for which the plugin will send the email notifications for every tracking status update.

By default, the plugin will check for the tracking status updates for the following orders,

  * Completed
  * Processing
  * Pending Payment

However, if your business requires it, you can visit the plugin settings and select your preferred orders under the **Check & update live tracking status for orders**, as shown below.

* * *

* * *

Also, to minimize the load and provide additional flexibility, you can prioritize the orders selected in the last couple of days by entering a value in the **In Last ___ Days** field.

* * *

**_Reference_**  
For Example, if all your orders delivered in 1-3 days, you can enter 3in this field and the plugin will check the shipment status of all the orders marked as Processing, Completed or Pending Payment, in the last 3 days.  
If the shipment status is changed by the shipping carrier, the plugin will also send the email notifications to the customers.  

* * *

#### 6.2 Choose the frequency of checking the live tracking status

PH Shipment Tracking Pro for WooCommerce also allows you to choose the frequency for checking the tracking status and sending email notifications to the customers.

Visit the plugin settings and enter a value in **Check Live Tracking Status after an Interval of every ___ Minutes** field.

* * *

* * *

Based on this value, the plugin will keep on checking the tracking status with the shipping carrier, and if the status is updated by the carrier, the plugin will automatically notify the customers via email.

### 7\. Customize the shipment tracking message

PH Shipment Tracking Pro for WooCommerce allows you to create a custom shipment tracking message that will be displayed to the customers.

* * *

**_Note_**  
This tracking message will be displayed at the following places if you have enabled these options the plugin settings,  
* WooCommerce Order Completion Email  
* Customer’s My Account > Orders page  

* * *

In the plugin settings, visit the **Custom Shipment Tracking Message** option and create your personalized tracking message, as shown below.

* * *

* * *

**_Note_**  
To define your own shipment message you can use the following tags,   
* [ID] to display the carrier tracking ID  
* [SERVICE] to display the shipping carrier  
* [DATE] to display the date of shipment   

* * *

### 8\. Add shipment tracking details to WooCommerce orders

PH Shipment Tracking Pro for WooCommerce allows you to add tracking details to WooCommerce orders in the following ways.

#### 8.1 Manually add shipment tracking details to individual orders

If your order volume is very low and you tend to update the tracking details for your orders manually, PH Shipment Tracking Pro for WooCommerce allows you to add shipment tracking details to each order, along with the carrier and shipment date.

To add shipment tracking details to individual orders, visit the WooCommerce orders page and select the order.

In the Order Edit page, select your preferred shipping carrier under the **Shipment Tracking Drop-down** , and add the tracking details like the **Shipment Tracking ID** , **Custom Description** , and the **Date of Shipment** , as shown below.

* * *

* * *

#### 8.2 Add shipment tracking details to multiple orders via CSV import

In case you require a more convenient and less time-consuming method to add shipment tracking details to your WooCommerce orders in one go, we recommend you opt for this method.

Create a CSV file containing the following fields,

  * Order ID
  * Shipping Carrier Name
  * Shipment Tracking Number
  * Date of Shipment
  * Custom Description
  * Order Status after adding the Tracking Details

* * *

** _Note_**  
* The columns in the CSV file are required to be in the specific order as shown above. Please make sure to mantain the order to avoid import failure.  
* A sample CSV is included inside the plugin ZIP file or you can visit the **Shipment Tracking > Import > Manual Import **and download the sample CSV file.   
* The desired encoding of CSV is UTF-8 ( Which most of the text editors will default ). In the Windows environment you can use Notepad++, using which you can check and even convert the CSV text encoding formats.   

* * *

The sample CSV file format is displayed in the image below.

* * *

* * *

Once you create the CSV properly, visit **Order Tracking > Import Tracking Details** and click on **Go to Import Page**.

* * *

Click on **Choose File** to upload the CSV file and then click on **Import CSV** to complete the import process.

* * *

* * *

**_Reference_**  
For more details, please refer – [How to Import WooCommerce Shipment Tracking Details via CSV Bulk Import?](https://www.pluginhive.com/knowledge-base/importing-tracking-data-csv-file-shipment-tracking-pro-woocommerce/)   

* * *

#### 8.3 Add shipment tracking details to multiple orders manually via FTP/SFTP import

One of the more secure methods to add tracking details to WooCommerce orders supported by the plugin is via FTP or SFTP.

Visit **Order Tracking > Import Tracking Details** and click on **Go to Import Page,** and fill in your FTP or SFTP details in the fields below.

  * **Enable FTP/SFTP Import** – Check this option to enable FTP or SFTP settings for PH Shipment Tracking Pro for WooCommerce
  * **Select FTP or SFTP** – Choose whether you want to use FTP or SFTP for import
  * **Server Host/IP** – Enter your FTP or SFTP Server hostname
  * **User Name** – Enter your FTP or SFTP username
  * **Password** – Enter your FTP or SFTP password
  * **Port** – Enter your FTP or SFTP port number
  * **Timeout** – Enter the timeout period for loading
  * **Path/CSV File Name** – Enter the CSV file path for importing
  * **Use FTPS** – Check this option to use FTPS. FTPS (File Transfer Protocol Secure) is a secured extension of FTP (File Transfer Protocol)
  * **Use Passive Mode** – Enable this option if you want to use a more secure FTP import

Once you have filled in the details, click on **Test your connection** to verify the FTP or SFTP connection.

* * *

**_Reference_**  
For more details, please refer – [How to Import WooCommerce Shipment Tracking Details via FTP or SFTP?](https://www.pluginhive.com/knowledge-base/woocommerce-tracking-now-import-tracking-details-automatically-via-ftp/)   

* * *

#### 8.4 Automatically add shipment tracking details to multiple orders via FTP/SFTP Scheduling

When it comes to importing tracking details to WooCommerce orders via FTP or SFTP, PH Shipment Tracking Pro for WooCommerce also allows you to schedule the import automatically.

Please refer to Section 8.3 to get more information on the FTP or SFTP fields.

* * *

* * *

**_Reference_**  
Please refer Section 8.3 to get more information on these fields.  

* * *

Now, enable the automatic import by setting the **Automatically Import CSV** to **Enabled**.

* * *

* * *

Enter the following details to successfully configure the import schedule.

  * **Import Start Time** – Enter the start time for import. You can enter a time value like 6:18 pm or 12:27 am.
  * **Start Import After an Interval of Every** – Enter the time interval in minutes after which you want to automatically re-run the shipment tracking import
  * **Skip if Already Imported** – Check this option to skip importing the tracking details of the orders that are already imported
  * **Delimiter** – Enter the delimiter used in your CSV file
  * **Combine Tracking Details while Importing** – Enable this option to combine the old tracking details with the new tracking details while importing. This is useful when a single order consists of multiple packages that are shipped at different times.

* * *

**_Note_**  
Please enter the**Import Start Time** carefully as the plugin shows the current server time, hence, you need to enter the import start time based on the server.   
* For example, if the current time shown on the plugin page is 8.21 pm, and you want to start the import half an hour after the current time, enter at 8.51 pm as the import start time.  

* * *

Once all settings are configured, click the **Save Settings** button

* * *

** _Reference_**  
For more details, please refer – [How to Automatically Import WooCommerce Shipment Tracking Details via FTP or SFTP using Scheduling?](https://www.pluginhive.com/knowledge-base/woocommerce-tracking-now-import-tracking-details-automatically-via-ftp/)   

* * *

### 9\. Automatically update WooCommerce order status to ‘Delivered’

PH Shipment Tracking Pro for WooCommerce makes it convenient to check the live tracking status of your shipments, and once the shipments are delivered, automatically mark the orders to Delivered.

‘Delivered’ is a custom WooCommerce Order Status that you can use to easily distinguish between the delivered orders. Visit the plugin settings page and select **Delivered (custom)** under the **After Delivery Change the Order Status To** field.

* * *

* * *

However, you can also use the conventional ‘Completed’ order status and select it within the same field.

### 10\. A quick overview of the shipment tracking number and live tracking status for WooCommerce Admin

* * *

** _Note_**  
This complete feature works parallel to the Live Shipment Tracking feature and is only available if the live tracking is configured for the supported shiping carrier(s).  

* * *

To enable live tracking, visit **Order Tracking > Live Shipment Tracking** and enable the **Enable Live Tracking** option, as shown below.

* * *

PH Shipment Tracking Pro for WooCommerce provides easy access to the shipment tracking details for the store owner, as well. WooCommerce store owners can visit the **WooCommerce Orders page** and view the following details for every WooCommerce order.

  * Shipment Tracking ID(s) of every WooCommerce order
  * Live Shipment Tracking Status updated by the shipping carrier

* * *

* * *

#### 10.1 Complete WooCommerce order tracking history available for the Admin

Apart from the WooCommerce Orders page, the store owners can also view the detailed shipment tracking history for each order.

Visit the **WooCommerce Orders** page and click on the order you want to view. Under the **Tracking History tab** , you can view the complete tracking history of all the packages within that particular order, as shown below.

* * *

* * *

### 11\. Integrations of PH Shipment Tracking Pro for WooCommerce

**PH Shipment Tracking Pro for WooCommerce** integrates seamlessly with popular shipping and fulfillment plugins to automatically sync tracking details to your WooCommerce orders. This helps reduce manual work and ensures customers receive accurate tracking updates.

To access these options, go to: **Order Tracking > Integrations**

* * *

Here, you’ll find a list of supported plugins and services that can be enabled with a simple toggle.

#### 11.1 PluginHive Shipping Plugins (UPS, FedEx, Canada Post, WooCommerce Shipping Services)

PH Shipment Tracking Pro for WooCommerce works smoothly with PluginHive’s shipping plugins, such as:

  * [WooCommerce UPS Shipping Plugin with Print Label](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/)
  * [FedEx Shipping Plugin for WooCommerce with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)
  * [Canada Post Shipping Plugin for WooCommerce with Print Label](https://www.pluginhive.com/product/woocommerce-canada-post-shipping-plugin-with-print-label/)
  * [WooCommerce Shipping Services  
](https://www.pluginhive.com/woocommerce-shipping-services/)

When any of these plugins generate tracking numbers for an order, the tracking details are automatically synced to the WooCommerce order. Customers will then receive tracking updates through emails and their My Account page (based on your settings).

To enable an integration, turn **on the toggle** for the required PluginHive shipping plugin under the **Integrations** tab and click **Save changes**.

* * *

**_Note_** To avoid duplicate tracking information, make sure tracking emails or customer-facing tracking options are not enabled in both plugins at the same time.

* * *

#### 11.2 Integration with Shipping Platforms (Shippo, ShipStation, ShippingEasy, Pirate Ship, Sendle)

The plugin also supports popular third-party shipping platforms, including:

  * Shippo
  * ShipStation
  * ShippingEasy
  * Pirate Ship
  * Sendle  

* * *

Once enabled, tracking details generated by these platforms are automatically imported into WooCommerce orders. This allows you to manage shipping externally while keeping order tracking centralized in WooCommerce.

Enable the required service using the toggle under the **Integrations** tab to start syncing tracking details.

* * *

#### 11.3 WooCommerce Shipment Tracking Integration

PH Shipment Tracking Pro for WooCommerce can sync tracking details from the default **WooCommerce Shipment Tracking** plugin.

After enabling this integration, you can control how often tracking details are synced by configuring:

  * Order statuses to sync
  * Number of recent days to check
  * Sync interval
  * Start time

* * *

This ensures tracking information stays up to date without manual intervention.

**_Reference_**  
For more details on how the two solutions work together, please refer – [How WooCommerce Shipment Tracking Pro & ShippingEasy work together?](https://www.pluginhive.com/knowledge-base/woocommerce-shipment-tracking-shipping-easy-integration/
)  

* * *

#### 11.4 PayPal Integration

The plugin also supports **PayPal** integration, allowing shipment tracking details to be shared with PayPal when orders are shipped.

To enable this:

  * Turn on the PayPal integration
  * Enter your **PayPal Client ID** and **Client Secret**

* * *

Once configured, tracking details will be synced with PayPal, helping improve payment protection and order visibility.

* * *

### 12\. Enable Debug Mode for PH Shipment Tracking Pro for WooCommerce

PH Shipment Tracking Pro for WooCommerce allows you to enable Debug Mode to log tracking data in WooCommerce Logs. This is useful when you want to troubleshoot any issues with the shipment tracking updates on your WooCommerce store.

To enable Debug Mode, visit WooCommerce Shipment Tracking Pro Settings and check the **Enable this option to log tracking data in WooCommerce Logs** option, as shown below.

Once enabled, the plugin will start logging the tracking data in WooCommerce Logs, which can be accessed under **WooCommerce > Status > Logs**.

* * *

[ Previous  How to Download, Install, Activate, and Update PluginHive WooCommerce Plugins  ](https://www.pluginhive.com/knowledge-base/how-to-download-install-update-woocommerce-plugin/)

[ Next  How Shipment Tracking Pro for WooCommerce improves customer experience?  ](https://www.pluginhive.com/knowledge-base/woocommerce-shipment-tracking-pro-improves-customer-experience/)
