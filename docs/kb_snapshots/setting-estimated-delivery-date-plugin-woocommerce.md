# Setting Up Estimated Delivery Date Plugin for WooCommerce

**Source:** https://www.pluginhive.com/knowledge-base/setting-estimated-delivery-date-plugin-woocommerce/
**Platform:** WooCommerce (WordPress)
**Plugin:** estimated-delivery
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Setting Up Estimated Delivery Date Plugin for WooCommerce

The****[Estimated Delivery Date Plugin for WooCommerce](https://www.pluginhive.com/product/estimated-delivery-date-plugin-woocommerce/) calculates and displays the estimated delivery dates of the products. The Customer can see estimated delivery dates on the product page, cart page, checkout page, and through Email. It allows estimates for all products, specific shipping classes, shipping methods, or shipping zones with customizable combinations.

This tutorial provides a comprehensive guide to setting up and using the plugin, offering essential knowledge and step-by-step instructions to help you get started seamlessly.

* * *

## In This Guide

  1. **Install& Activate The Plugin**
  2. **Access the Plugin Settings**
  3. **Configure the General Settings**
     * Choose the text format
     * Set custom text for the product page
     * Customize display options
     * Set the time zone
     * Select the date format
     * Define minimum delivery days
     * Adjust delivery estimates for backordered products
     * Set shipping time
     * Configure store working days
     * Configure Carrier working days
     * Start From Next Working Day
     * Define the calculation mode 
     * Display delivery date on various pages
     * Enable plain text mode
     * Consider carrier holidays in the calculation
     * Enable estimated delivery per package
     * Enable and view log records for debugging

  4. **Setting Up Holidays& Non-Working Days**
  5. **Set additional delivery days for different shipping classes**
  6. **Adjust delivery estimates by shipping zones.**
  7. **Assign delivery estimates for various carriers through shipping methods**
  8. **Displaying Estimated Delivery Dates on Storefront**
  9. **Examples of Estimated Delivery Date Calculation**
     * Case 1: General settings without shipping class or zone rules
     * Case 2: Adding shipping class-specific delivery days
     * Case 3: Combining shipping class and shipping zone 
     * Case 4: Combining shipping class, shipping zone, and shipping methods

## **1\. Installation And Activation** of **the Plugin**

Visit the [Estimated Delivery Date Plugin for WooCommerce](https://www.pluginhive.com/product/estimated-delivery-date-plugin-woocommerce/) page and purchase the plugin. After a successful purchase, the plugin will be available to download at **My Accounts > API Downloads**. Download the plugin and install it on your WooCommerce store.

* * *

**Reference:**   
For more information on the installation and activation of the plugin, please refer – [ **How to install a PluginHive WooCommerce Plugin?** ](https://www.pluginhive.com/knowledge-base/how-to-download-install-update-woocommerce-plugin/).

* * *

## **2\. Access the Plugin Settings**

After installing the Estimated Delivery Date plugin, you can navigate to the Plugin in two ways as given below:

  * Navigate to Dashboard and then **WooCommerce > Settings > Estimated Delivery**

* * *

OR

  * Navigate to **Plugins > Installed Plugins > WooCommerce Estimated Delivery Plugin > Settings**

* * *

OR

  * Navigate to **Delivery Date > Settings**

* * *

You will be able to set up the plugin with four tabs: 

  * **General**
  * **Holiday**
  * **Shipping Class**
  * **Shipping Zone**
  * **Shipping Method**

Let’s start with General Settings.

* * *

## **3\. Configure General Settings**

The Settings are as given below:

  1. **Choose** **Text Format:** You can select a format for text display.   
There are three available choices:

  1. 

  * **Simple** – Allows you to set a simple text display as defined in the _Product Page Text_ field below the _Text Format_ option.
  * **Simple Range** – This allows you to set a simple date range within which the package is estimated to be delivered. The _Product Page Text (Range)_ field is enabled instead of the _Product Page Text_ field(for simple format), where you can set custom text for the date range.  
Once you select these options, the following two additional fields appear:
    * **Date Lower Range** – Allows you to set a numerical value for a lower range of the delivery date.  
For example, if the date lower range value is **2** and the delivery date is 3/1/2017, the start range for the delivery date will be 1/1/2017.
    * **Date Higher Range** – Allows you to set a numerical value for a higher range of the delivery date.  
For example, if the date higher range value is **2** and the delivery date is 3/1/2017, the end range for the delivery date will be 5/1/2017.
  * **Date Range** – Allows you to set a date range within which the package is estimated to be delivered.

* * *

2\. **Product Page Text** : Enter the custom text with the date. This text is visible on the product page just above the add-to-cart button.

  * **Product Page Text (Simple)** : Enter the custom text with the date delimiter. For Example, **estimated delivery by [date]**
  * **Product Page Text (Range)** : Enter the custom text with the date range delimiter. This text is visible on the product page just above the add-to-cart button.  
For Example, estimated delivery between [date_1] – [date_2]
  * **Date Lower Range[date_1]** : The plugin calculates a single date of delivery. So if you want to display a date range, specify the number of days in this setting and the delivery date range will start with that number of days before the actual delivery date. For example, if the plugin calculates the delivery date as 04/05/2018, and you have set this option to 2, then the delivery date range would start from 02/05/2018.
  * **Date Upper Range[date_2]:** Similar to the above setting, if you want to display a date range, specify the number of days in this setting, and the delivery date range will end that number of days after the actual delivery date. For example, if the plugin calculates the delivery date as of 04/05/2018, and you have set this option to 3, then the delivery date range would end at 07/05/2018.

Hence, the plugin will display the following message:  
Estimated Delivery Between 02/05/2018 – 07/05/2018

* * *

3\. **Display Text** : Enter text that gets displayed on Cart, Checkout, Admin Order, Order Received Page, and Email, beside which the estimated delivery date is shown.

* * *

4\. **Time Zone:** The plugin provides two time zones for calculating the delivery date.

  * **WP Time Zone** – This is the time zone set in the _General Settings_ section of your WordPress site. It reflects the site’s configured time zone, which may be a GMT offset or a city-based time zone.
  * **UTC** – This time zone is the time standard commonly used across the world.

* * *

5\. **Date Display** : Select the required date format from the drop-down list and available options as given below:

  * Custom (you can customize your own date format)
  * DD/MM/YYYY
  * YYYY/MM/DD
  * MM/DD/YYYY
  * DD-MM-YYYY
  * YYYY-MM-DD
  * MM-DD-YYYY
  * DD.MM.YYYY
  * YYYY.MM.DD
  * MM.DD.YYYY
  * DD MON YYYY

* * *

6\. **Minimum Delivery Days** : Enter the minimum number of days for the delivery of all the products.

* * *

7\. **Adjustment for Back-Ordered Products:** This setting adds extra days to the delivery estimate for backordered products, ensuring accurate timelines by factoring in restocking time.

* * *

8\. **Shipping Times** : Set the delivery time limit for the selected day of the week.

* * *

9\. **Working Days for Store** : Select the working days of your store, and according to these days, the date of delivery can be estimated.

* * *

10\. **Working Days for Carriers:** Choose the working days of the carrier, and the delivery date will be estimated based on their operational schedule.

* * *

11\. **Start From Next Working Day:** You can calculate the estimated date based on your preferences by enabling or disabling this option.

  * **Disable** – the plugin starts calculating the delivery from the same day the order is placed, only if the order is placed before the cut-off time.
  * **Enable** – The plugin starts calculating the estimated delivery from the next working day. This means the current day (order day) is not counted, even if the order is placed before the cut-off time.

* * *

12\. **Calculation Mode:** This option allows you to choose the holidays for the shipper and the customers. Based on your selection, the plugin will calculate delivery dates.

* * *

13\. **Display Estimated Delivery:**

  * **Display on Product Page:** Shows the estimated delivery date on individual product pages for in-stock products.
  * **For Every Item in Cart/Checkout:** Shows the estimated delivery date for each item in the cart and at checkout.
  * **Display on Shop:** Displays the estimated delivery date on the Shop page, Search page, and Suggested items.

* * *

14\. **Plain Text Mode:**

When enabled, this removes all HTML tags from the text field on the product page, ensuring that the estimated delivery message appears as plain text without any formatting.

* * *

15\. **Consider Carrier Holidays:**

If enabled, the plugin will factor in carrier holidays (such as public holidays when shipping services are unavailable) and automatically adjust the estimated delivery date accordingly.

* * *

16\. **Estimated Delivery Per Package:**

Instead of showing a general estimated delivery date for the entire order, this option displays a specific delivery estimate for each package based on the chosen shipping method. 

Use the **Per Package Delivery Date Text** field to modify how the estimated delivery date appears.

* * *

17\. **Record Log** : To debug the problem, select the checkbox to record log, which gets generated in the folder **wordpress\wp-content\uploads\wc-logs**. Here, you can check the estimation input and result pair.

* * *

Click **Save Changes** to save/update the General Settings.

* * *

## **4\. Setting Up Holidays & Non-Working Days**

Admins can set holidays using a date range, ensuring those days are excluded from delivery estimation.

To access the Holiday setting, go to **Estimated Delivery > Holidays**

  * **Mark Holidays with a Date Range**
    * Enter a start and end date to define the holiday period.
    * The plugin will exclude these days from delivery estimation.

  * **Set a Single-Day Holiday****  
**Use the same date for both the “From” and “To” fields to mark a single-day holiday.

  * **Add a New Holiday:** Click the **Add Holiday** button to include a new holiday in the list.

  * **Remove Holidays:** Select the holiday(s) and click the **Remove Holidays** button to delete them.

For example, Year year-end holiday:

Click **Save Changes** to save/update the settings.

* * *

## **5\. Shipping Class Settings**

Admins can configure shipping classes to define specific handling and delivery timeframes for different types of products. 

To set it up, go to **Estimated Delivery > Shipping Class**, 

  * **Add a Shipping Class:** Enter the name of the **Shipping Class** in the provided field. This helps categorize products that require similar shipping conditions.
  * **Set Additional Delivery Days:** Enter the number of extra days required for this shipping class. These additional days will be added to the estimated delivery time calculated based on the General Settings and shipping zone-specific days (if any).
  * **Define Cutoff Time:** Click on the **clock icon** to set a Cutoff Time for order processing. Orders placed after the cutoff time will be processed on the next working day.
  * **Specify No Delivery Days:** Select the specific days when **deliveries will not be available** (e.g., weekends or public holidays).

**_What is Cutoff Time?_**_  
The cutoff time is the deadline for processing orders on the same day. Orders placed after this time will be processed the following business day._

* * *

After configuring the days, click **Save Changes** to apply the settings.

* * *

**Reference:**   
To dive deeper into configuring shipping classes the right way, check out this [ **ultimate guide to setting up WooCommerce shipping classes** ](https://www.pluginhive.com/ultimate-guide-set-up-woocommerce-shipping-class/).

* * *

## **6\. Shipping Zones Settings**

Admins can configure shipping zones to define delivery timeframes for different geographical areas. By default, there is a zone for locations not covered by any specific shipping zone.

To set it up, go to **Estimated Delivery > Shipping Zones**,

  * **Select the Shipping Zone:** The list will display the WooCommerce Shipping Zones available in your store. Choose the appropriate zone for which you want to set delivery days.
  * **Set Additional Delivery Days:** Enter the number of extra days required for deliveries to this shipping zone. These additional days will be added to the estimated delivery time calculated based on General Settings and shipping class-specific days (if applicable).
  * **Define Cutoff Time:** Click on the **clock icon** to set a Cutoff Time for order processing in this zone. Orders placed after the cutoff time will be processed on the next working day.
  * **Specify No Delivery Days:** Enter the specific days when deliveries will not be available (e.g., Sundays or public holidays).

After configuring the settings, click **Save Changes** to apply the updates.

* * *

**Note:**   
If WooCommerce’s default customer location is set to “Geolocate”, the plugin will automatically detect the customer’s location and apply the relevant shipping zone settings.

* * *

**Reference:**   
Need help setting up your zones correctly? Check out this [ **step-by-step guide to configuring WooCommerce shipping zones** ](https://www.pluginhive.com/woocommerce-shipping-zones-ultimate-guide/).

* * *

## 7\. Shipping Method Settings

Admins can set the estimated delivery days for different shipping methods imported from WooCommerce. The final delivery estimate is calculated using the General Settings and shipping class specified days (if any). 

To set it up, go to **Estimated Delivery > Shipping Method**,

  * **Add** **Method:** Enter the shipping method(s) for which you want to set delivery estimates. You can find the shipping method value by inspecting it on the cart page.
  * **Enter No. of Days:** Define the additional number of days required for the selected shipping method.
  * **Define Cut-Off Time:** Set a specific time limit for processing orders. Orders placed after this time will be processed the next business day.
  * **Specify No Delivery On:** Mention days when deliveries are not available (e.g., Sundays, public holidays).
  * **Define Working Days:** Add which days are considered working days for this shipping method. (On non-working days, deliveries will not take place, but order pickup will be available.
  * **Remove Method(s):** You can remove specific shipping methods along with their associated delivery estimate settings if they are no longer required. 

* * *

Once the settings are updated, click **“Save Changes.”**

* * *

**How to Find the Shipping Method Value:**

  1. Go to the Cart page on your WooCommerce store and right-click on the shipping method you want to configure.
  2. Click **Inspect** to open the browser’s developer tools.

* * *

3\. Copy the shipping method value and paste it into the plugin settings.

* * *

## **8\. Product Page with Estimated Delivery Date**

After configuring the plugin, customers will see the estimated delivery date displayed on the product page.

* * *

## **9\. Cart Page: How Delivery Dates Are Calculated**

The estimated delivery date displayed at the cart page depends on various factors, including general settings, shipping class settings, and shipping zone settings. Below are three examples explaining how delivery dates are determined:

**If order processing starts on 4th April,**

**Example 1: No specific shipping class or zone days are set**

  * **General Settings:**
    * Enable start from next working day. 
    * Minimum of 2 days required for delivery.
    * Saturday and Sunday are non-working days. 

* * *

  * **Holidays Settings:** Monday (April 7th) 

* * *

  * **Final Estimated Delivery Date:** April 10th  
Since April 5th and 6th are non-working days and April 7th is a holiday, the 2-day delivery period starts from April 8th. So, the estimated delivery date is April 10th.

* * *

**Example 2: Shipping class-specific days are set, but no shipping zone-specific days**

  * **General Settings:**  
Same as Example 1

  * **Shipping Class Settings:**
    * Select the shipping class
    * Add the number of processing days. Here, 3 

* * *

  * **Final Estimated Delivery Date:** April 15th****  
As per general and holiday settings, Order processing begins on April 8th. With 2 processing days, it ends on April 10th. 3 more days (skipping weekend) for this particular shipping class. So, the final estimated delivery date is **April 15th**.

* * *

**Example 3: Both shipping class and shipping zone settings are configured**

  * **General Settings:** Same as example 1
  * **Shipping Class Settings:** Same as example 2
  * **Shipping Zone Settings:** Adds 2 more processing days to the US Zone.

* * *

  * **Final Estimated Delivery Date:** April 17th  
Previously, the delivery was estimated for April 15th. However, with 2 additional delivery days added in the US Zone, the new estimated delivery date shifts to **April 17th**.

* * *

**Example 4: Shipping class, shipping zone, and shipping method settings are configured**

**General Settings:** Same as example 1  
**Shipping Class Settings:** Same as example 2  
**Shipping Zone Settings:** Same as example 3  
**Shipping Method Settings:**

  * Select the free shipping method
  * Number of days: 2 
  * No delivery on Friday for free shipping
  * Working days: Tuesday, Wednesday, Thursday, Friday 

* * *

**Final Estimated Delivery Date** for free shipping**:** April 23rd

  * Based on General Settings, Holiday Settings, Shipping Class, and Shipping Zone Settings, the initial estimated delivery date was Thursday, April 17th.
  * The selected shipping method adds 2 more processing days. Friday (April 18th) is disabled as a delivery day. Since Saturday (April 19th) and Sunday (April 20th) are weekends, and Monday (April 21st) is a holiday, these days are skipped.
  * As a result, the final estimated delivery date becomes Wednesday, April 23rd.

* * *

Explore the [Estimated Delivery Date Plugin for WooCommerce](https://www.pluginhive.com/product/estimated-delivery-date-plugin-woocommerce/) and take your store to the next level!

If you need any further assistance, feel free to reach out to us anytime. Our [support team](https://www.pluginhive.com/support/) is always ready to help you with any queries or setup issues.

[ Previous  How to Download, Install, Activate, and Update PluginHive WooCommerce Plugins  ](https://www.pluginhive.com/knowledge-base/how-to-download-install-update-woocommerce-plugin/)

[ Next  Display or Hide Estimated Delivery Dates for Different Products based on WooCommerce Shipping Classes  ](https://www.pluginhive.com/knowledge-base/estimated-delivery-date-for-different-products-based-on-woocommerce-shipping-class/)
