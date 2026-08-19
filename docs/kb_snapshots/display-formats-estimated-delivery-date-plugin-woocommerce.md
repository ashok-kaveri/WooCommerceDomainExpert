# Display Estimated Delivery Date Formats in WooCommerce

**Source:** https://www.pluginhive.com/knowledge-base/display-formats-estimated-delivery-date-plugin-woocommerce/
**Platform:** WooCommerce (WordPress)
**Plugin:** estimated-delivery
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Display Estimated Delivery Date Formats in WooCommerce

Using the **[Estimated Delivery Date and Time plugin](https://www.pluginhive.com/product/estimated-delivery-date-plugin-woocommerce/)** , WooCommerce store owners can provide estimated or approximated delivery dates for the products to their customers. Store owners can easily display the dates on the Product page, Cart page, and Checkout page as well. They can even configure these display formats by choosing from a variety of options and defining various rules that are incorporated in the plugin.

This article has been curated in a way to help you understand these options and rules. Moreover, it will eventually help you create a better system in order to help your customers reciprocate and purchase the products accordingly. So, without any further delay let us quickly jump into the article.

* * *

## Display formats in the plugin

Now as soon as you install the plugin and set it up in your WooCommerce, you would be able to see the settings page of the plugin. It is located under the WooCommerce Settings page and if you click on the **Estimated Delivery** tab on the top right corner of the page, you would see the following option in front of you.

In the screenshot given above, you can see the three options under the Text Format drop-down menu. It contains the **Simple** , **Simple Range,** and **Date Range** options.

**Note** : The product’s estimated date of delivery can be shown in a pre-defined format. This format can be chosen by the store owner based on his or her choice. Following are the date format options available in the plugin.

Now, the **Simple** option in the drop-down menu shows the estimated delivery of the product in just one simple format. Have a look at the following sample.

The second option is the **Simple Range** which is used to show the basic delivery duration range. It looks something like the sample image below.

Now the third option is the **Date Range** and this format is a bit different when compared to the Simple Range. It shows the actual delivery date range within which the delivery would be attempted. You can refer to the following sample image.

* * *

## Specifying the Minimum Delivery Days

In this section of the plugin, you can specify the minimum delivery days required for your online store to deliver the shipment. You can refer to the following image shown below.

Thus, based on the number of days the shipment will start accordingly. This step is very necessary as it will determine the overall time taken during the shipment and delivery process. So, if a particular shipping zone has a value of 3 delivery days and the minimum delivery days are 2, then the overall delivery days would sum up to 5 (3+2).

* * *

## Configuring the delivery rules

This plugin also allows the WooCommerce store owners to apply certain rules to the display format. But before going into any specifications have a look at the rule settings section in the plugin.

As soon as a new order is placed in your store, the first option will enforce the calculation of the shipment and delivery process from the next working day. For instance, let the order date be 11/16/2017 (Thursday) and the next day is not a holiday. Moreover, the minimum number of delivery days defined by you is 3, then the delivery date will be 11/20/2017 (Monday). Thus, instead of starting the shipment calculation from the order date itself, the next working day is chosen.

However, you should note that this might not be always correct as it also depends on the delivery time zone.

Next up you have the **Calculation Mode**. Under this drop-down menu, you would be able to see two different options –

  1. Consider holiday for Shipper Only
  2. Consider a holiday for the Shipper and Recipient

If you choose the first option, the shipment calculation process will consider a holiday for you but not the customer. For example, if you receive an order today and tomorrow is a holiday, the shipment calculation will start the day after tomorrow. However, the shipment will be delivered to the customer in spite of the fact that the delivery day is a holiday/non-working day.

Now, if you choose the second option, the plugin will consider the holidays for both parties. Meaning, if the product or the item will be delivered to the customer only on working days. So, if the estimated delivery day is a Sunday or simply a holiday, the plugin will display the next possible working day as the estimated delivery day. However, the condition will remain the same for the shipper and will not change in both cases.

Let us take an example to understand the whole scenario in a better way.

Assume the following calendar,

Here, the order date is the 17th of November and the Minimum Delivery Day is 2. Now, if you select the first option (consider holiday for Shipper Only), then it will translate into the delivery date being the 19th of November (Sunday). Refer to the following image.

Now, if you select the second option which will consider a holiday for both sender and receiver, then the delivery date will be on the 20th of November (Monday). See the following screenshot below.

* * *

## Custom Estimated Date Formats

You can also set the date formats in additional formats based on your requirements, using the following plugins together.

  * [**WooCommerce Estimated Delivery Date plugin**](https://www.pluginhive.com/product/estimated-delivery-date-plugin-woocommerce/)
  * Custom Estimated Delivery Date Formats add-on plugin [contact PluginHive Support]

### Custom Estimated Delivery Date Formats add-on plugin

#### How does this plugin work?

The add-on plugin functions in the following ways,

  * **It replaces the Estimated Delivery Date with Today or Tomorrow**  
For example, if the **Current Date = 24th April and the Delivery Date = 25th April,** the plugin will display the delivery date as **Tomorrow**. The same will be the case with the Same Day Delivery. The plugin will display the delivery date as **Today**.
  * **It replaces the Estimated Delivery Date with the corresponding day of the week  
** For Example, if the delivery is after 3 days, the plugin will display the delivery date as Thursday.  
****Note – This functionality will revert back to the date after the first occurrence of the day (after the first week).**

Follow the steps below to set up the plugin.

  * Download and install WooCommerce Estimated Delivery Date plugin
  * Set up the delivery date formats to one of the following formats,  
****Note – This solution will work with the following formats only**

    * **YYYY/MM/DD**
    * **MM/DD/YYYY**
    * **DD-MM-YYYY**
    * **YYYY-MM-DD**
    * **DD.MM.YYYY**
    * **DD MON YYYY**
    * **MON DD**
    * **MON DD YYYY**
  * Download, Install and **Activate** the **Custom Estimated Delivery Date Format add-on plugin**
  * Visit the product page and check the delivery dates

* * *

We hope that this article was useful to you in some way. Let us know in the comment section below.

[ Previous  Estimated Shipping Date for WooCommerce Product Variations  ](https://www.pluginhive.com/knowledge-base/estimated-shipping-date-for-woocommerce-product-variations/)

[ Next  Display Delivery Estimates on your WooCommerce Store  ](https://www.pluginhive.com/knowledge-base/improve-customer-experience-showing-delivery-estimates/)
