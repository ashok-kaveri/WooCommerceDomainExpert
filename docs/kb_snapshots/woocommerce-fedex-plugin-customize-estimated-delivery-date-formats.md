# Customize Delivery Date formats in WooCommerce FedEx plugin

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-fedex-plugin-customize-estimated-delivery-date-formats/
**Platform:** WooCommerce (WordPress)
**Plugin:** estimated-delivery
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Customize Delivery Date formats in WooCommerce FedEx plugin

This guide will help you to choose from various delivery date formats supported by our **[WooCommerce shipping plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)**. We will tell you how to customize the date formats to let your customers easily figure out the delivery estimates.

**[WooCommerce Shipping plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** offers other outstanding features like print shipping labels, order tracking, choosing parcel packing methods, and many more. However, many store owners do not know that they can show the estimated delivery dates and configure their format as well.

Based on your region or country you can either choose to show the delivery date in the default format or go for a format that is preferred by most of your customers. Moreover, by using this plugin you can easily display the dates on both the Cart and Checkout pages which is quite helpful.

## How to change the Delivery Date formats in the WooCommerce Shipping plugin for FedEx

If you go to the FedEx settings page you would be able to find the option to enable the **Show Delivery Time** feature. Enabling this option will show the estimated delivery date along with the different FedEx Shipping rates on both Cart and Checkout pages.

After doing the above step you would have to introduce another function that allows you to change the delivery date formats. This can be done by adding a code snippet to the plugin which can be further modified. To do that you would have to copy the code provided here and then **paste it into Appearance -- > Editor --> Theme Functions(function.php)**. You can refer to the following video that shows the necessary steps.

### Modifying the Estimated Delivery Date format

As you saw in the above video, the code snippet contains the following lines of code.

If you look carefully at the **3rd line of code** , there are letters(variables) **‘l, F jS Y’.** These variables represent the delivery date format. If you replace the letter F with js and then the format would change. So, for the letter arrangement **‘l, jS F Y’** the delivery date would look something like the format as shown in the following screenshot.

Now, let us see the various types of variables or letters that can be used together to show a custom delivery date.

### List of formatting variables that can be used in the Code Snippet

Here is a list of various format letters(variables) that you can make use of:

  * d – The day of the month (from 01 to 31)
  * D – Textual representation of a day (three letters)
  * j – The day of the month without leading zeros (1 to 31)
  * l (lowercase ‘L’) – Full textual representation of a day
  * N – The ISO-8601 numeric representation of a day (1 for Monday, 7 for Sunday)
  * S – The English ordinal suffix for the day of the month (2 characters st, nd, rd or th. Works well with j)
  * w – Numeric representation of the day (0 for Sunday, 6 for Saturday)
  * z – The day of the year (from 0 through 365)
  * W – The ISO-8601 week number of the year (weeks starting on Monday)
  * F – Full textual representation of a month (January through December)
  * m – Numeric representation of a month (from 01 to 12)
  * M – Short textual representation of a month (three letters)
  * n – Numeric representation of a month, without leading zeros (1 to 12)
  * t – The number of days in the given month
  * L – Whether it’s a leap year (1 if it is a leap year, 0 otherwise)
  * o – The ISO-8601 year number
  * Y – Four digit representation of a year
  * y – Two digit representation of a year

Let us look at some good examples and try to show various custom delivery dates on the Cart/Checkout page:

1\. Let us try to implement the following arrangement (d – jS – D – M – y). Please note that this is not a regular date format. We have used this format to show the possibilities of using multiple variables.

2\. Let us try to implement the official Slovakian date format**(dd.mm.yyyy)** by writing the term **‘d.m.Y’** in the code snippet. And as you can see in the following image, the necessary date format is displayed on the Cart page.

3\. Now we will try to implement the United States date format**(mm/dd/yyyy)**. For this, we would have to write the following term **‘m/d/Y’**.

And as you can see, the plugin displays the official date format. Please note that the variable **‘Y’** represents **‘yyyy’** and this is the reason why the year is displayed as 2018 on the Cart page.

4\. Now let us implement the following format**(dd/mm/yy)**. This is the official Indian date format and it can be represented by the term **‘d/m/y’** in the code snippet.

Sometimes it is better to display the month’s name instead of its numerical value in the estimated delivery date. This type of date format is helpful in cases where a store has both domestic and international customers. For example, the date format in the United States is (mm/dd/yyyy) but in some other country like India, the date format is (dd/mm/yyyy). If a customer from India visits an online store that is in the US then he or she might get confused with the estimated delivery date format. Especially if the date is something like 10/12/2017.

So, let us try some of the most common date formats that include the month’s name in them.

5\. Here, we will try to implement the following date format**(dd mmm yy)**. For this, we will write **‘d M y’** in the code snippet and the final result would display the format as shown in the following image.

Please note that the name of the months will be displayed in three letters only. So, for the month October, the estimated delivery date will show Oct. However for the months **June and July** , it will be displayed as June and July because they contain just four letters.

6\. Another way to show the delivery date that contains the month name would be in the format of **(dd-mmm-yyyy)**. This format is quite common and we will have to write the following term in the code snippet **‘d-M-Y’**.

7\. **(mmm dd yyyy)** is also preferred and used by many WooCommerce store owners. For this format, you will have to add the following term in the code snippet **‘M d Y’.**

8\. If you wish to show the complete information including the weekday and the name of the month, then you can choose the following format **(Weekday, dd of Month yyyy)**. Please copy the following line in the code snippet **‘l, dS F Y’.**

By making use of the list given above, you can try other display delivery formats as well.

### Try WooCommerce Estimated Delivery Date plugin for more control

The [**WooCommerce Estimated Delivery Date plugin**](https://www.pluginhive.com/product/estimated-delivery-date-plugin-woocommerce/) is a powerful and robust plugin that will allow you to control the delivery estimates by a greater factor. You will be able to show the estimated dates on the Product page as well as on both the Cart and Checkout pages.

You will also be able to further define holidays or days when you won’t be able to ship the packages. And if you are looking for some predefined delivery formats then here is the list of format options that is available in the plugin.

## In conclusion

The **[WooCommerce Shipping plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** is an amazing plugin that offers a whole bunch of features. And if you want to customize the plugin based on your business requirement then you can do that with a Code Snippet, just like we showed you in this article. You can check out other code snippets for the FedEx Shipping Plugin.

We hope this article was of help to you. Do let us know in the comment section below how you feel about this. If you have any further clarifications then feel free to **[contact our customer support](https://www.pluginhive.com/support/)**.

[ Previous  Will the WooCommerce Estimated Delivery Date plugin work with Shipping Classes and Shipping Zones, both at a time?  ](https://www.pluginhive.com/knowledge-base/will-woocommerce-estimated-delivery-date-plugin-work-shipping-classes-shipping-zones-time/)

[ Next  Installation and License Activation(Video)  ](https://www.pluginhive.com/knowledge-base/installation-license-activation-woocommerce-royal-mail-shipping-tracking-plugin/)
