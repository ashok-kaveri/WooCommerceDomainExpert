# Setup Guide for Bookings and Appointments for WooCommerce

**Source:** https://www.pluginhive.com/knowledge-base/setup-guide-woocommerce-bookings-and-appointments-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** bookings
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Setup Guide for Bookings and Appointments for WooCommerce

Use this quick guide to set up your **[Bookings and Appointments for WooCommerce](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** plugin by **PluginHive**. We’ve shown the necessary settings, steps, and images along the way to help you configure features available in the plugin.

* * *

## Table of Content

  1. **Booking Calendar****Appearance**
  2. **Create a Bookable Product**
  3. **Define the Booking Period**
  4. **Maximum Bookings per Block – How many bookings do you take for the same block?**
  5. **Daily Booking opening and closing times**
  6. **Booking Duration**
  7. **Booking Cancellation**
  8. **Bookings requiring Approvals**
  9. **Buffer Time: Do you need a Gap Time for Preparation or Travel between Bookings?**
  10. **Booking Costs, Discounts, and Special prices**
  11. **Booking Availability** – **Make calendar dates/times available/unavailable to book**
  12. **Add People to your Booking**s
  13. **Add Resources/Add-On options to your Bookings**
  14. **Set a language / WPML compatibility**
  15. **Booking Emails**
  16. **Manage your bookings** /**Booking Reports**
  17. **Centralized Booking Calendar View**
  18. **Booking Process – Frontend**
  19. **Staff Management**
  20. **Syncing bookings between 2 or more bookable products**
  21. **Bookings as Calendar Events**
     * **Google Calendar Sync**
     * **Export as iCalendar Event**
     * **MS Outlook Calendar Sync**
  22. **Create a WooCommerce Booking Form with additional fields or options**
  23. **Accept a deposit or partial payment for your bookings**
  24. **Dokan Multi-Vendor Integration**
  25. **Compatibility with Preview E-mails for WooCommerce**
  26. **Search Products based on availability**
  27. **FAQs**

* * *

## **1\. Booking Calendar Appearance**

The **[Bookings and Appointments for WooCommerce Plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** lets you create the booking calendar design of your choice. The following are available options in the plugin settings.

### 1.1 Choose a Design Template for your Booking Calendar

There are 3 calendar design templates provided within the Bookings and Appointments for WooCommerce Plugin.

  * Designs 1 and 2 have the calendar always displayed on the product page.
  * Design 3 displays the calendar on click.
  * Design 1 is selected as the default template by the plugin.

Visit**Bookings > Settings > Calendar Design**, select a preferred design and also customize the colors to suit your website.

* * *

Calendar Design 1 and 2

* * *

Calendar Design 3

### 1.2 Customize the Labels and Messages Displayed by the Plugin

Visit**Bookings > Settings > Calendar Display**

* * *

Calendar Display Options

### 1.3 Choose Calendar Display Options

Visit**Bookings > Settings > Calendar Display**

Use the below settings to:

  1. **Week Starts On:** Start the week on a Monday or Sunday
  2. **Month Picker:** Display a dropdown in the place of the month label for the user to select a month directly rather than scrolling through the months
  3. **Time Zone Conversion:** Have your customers see the time slots in their own time zone and not yours 
  4. **Booking Summary:** Display the end date and time in the calendar summary. 
  5. **Include End Date & Time in Cart, Order Details & Emails:** this option allows you to display or hide the end date/time of a booking on the cart page, order details, and the emails sent to the customers.

Calendar display Options 2

* * *

### 1.4 Choose the Date and Time Format for the Calendar

The plugin uses your WordPress date and time format. If you wish to use a specific format for your calendar, follow the instructions below.

Visit **Settings > General > Date and Time Format**

* * *

Date and Time Format

**Note:**  
This is a global setting and will be applied everywhere on your website.   

* * *

**Reference:**  
For more information related to Calendar Appearance queries, please refer – [WooCommerce Bookings – Calendar Appearance FAQs](https://www.pluginhive.com/knowledge-base/woocommerce-bookings-and-appointments-plugin-faqs/#CalendarAppearance)   

## **2\. Create a Bookable Product**

The **[Bookings and Appointments for WooCommerce Plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** lets you create bookable products/services or convert an existing WooCommerce Product into a Bookable Product

Edit the desired**** WooCommerce Product, and**change the Product Type to “Bookable Product”**. When you save and view the product in the front end, you will see a calendar available to book the product.

* * *

Create a Bookable Product

* * *

**Note:**  
Since “Bookable Product” is a product type, it cannot be used along with a variable product type. However you can achieve variation options for your booking calendar by using the plugin features like Assets and Resources or [The Product addons plugin](https://www.pluginhive.com/product/woocommerce-product-addons/)   

* * *

## **3\. Define the Booking Period: Decide how long your booking lasts (Booking Block)**

The **[Bookings and Appointments for WooCommerce Plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** offers multiple booking periods. You have the below options to choose from.

#### **3.1 Single-Day Booking**

If you need the user to choose a single day to book, you can use the “**Fixed Block of 1 Day(s)** ” option as shown below.

* * *

Set up a single day booking

* * *

Here is how the calendar will look on the front end.

* * *

Calendar – Fixed Block of 1 day

* * *

#### **3.2 Multiple Consecutive Days Booking**

If you need customers to **choose a booking start date and an end date** , then use the**“Enable Calendar Range with Blocks of 1 day(s)”** option.

* * *

Calendar – Enable Calendar Range with blocks of 1 Day

* * *

This is how the calendar looks on the front end.

* * *

Calendar view with a fixed block of 1 day

* * *

#### **3.3 Multiple consecutive days Booking – Check-in and Check-out**

**How to ensure the check-out date is available for other bookings and is not included in the cost calculation?**

When you need your customers to choose a start date (Check-in) and end date (check-out) and exclude the check-out date from the cost calculation, enable the “**Bookings per night** ” option. This option also ensures that the checkout date is available for other bookings.

* * *

* * *

In the below image, you will find that enabling this option shows the summary with check-in and check-out dates as May 28 and May 30. However, the cost is calculated for 2 nights- May 28 and May 29. 

* * *

* * *

After the booking is done, May 30th (The checkout date) is still available for other bookings as shown below. 

* * *

* * *

#### **3.4 Single Appointment**

If you need the user to **choose a date and a time** for an appointment, then use the “**Fixed Blocks of 1 Hour(s)”** option.

* * *

Fixed Block of 1 hour

* * *

Calendar view with fixed blocks

* * *

**Note:**  
Choose the block of time based on how long your appointment lasts. In this example, we have used a 1-hour block.   

* * *

#### **3.5 Multiple Consecutive Appointments**

If you need customers to **choose a Booking Date and a Start Time and an End time** covering multiple booking slots (on a single day) then use the “**Enable Calendar Range with Blocks of 1 Hour(s)** ” option.

* * *

Enable Calendar Range with Blocks of 1 hour

* * *

Calendar view with blocks of 1 hour

* * *

#### **3.6 Multiple Consecutive Appointments Across Days**

If you need your user to **choose a Booking Start Date & Time with the Booking End Date & Time which spans for more than one day**, use the **“Enable Calendar Range with Blocks of 1 Hour(s)”** option and enable the **“Allow Across Days Bookings”** option under the same Bookings tab. 

* * *

Allow Across Days Bookings

* * *

Calendar view of Across Days Booking

* * *

### Other Ways to Define a Booking Period

It’s likely that you have found the best option that suits your business from the above choices. If not, you can also take a look at the following options that can be achieved using Add-on plugins along with the **[Bookings and Appointments for WooCommerce Plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)**.

#### **3.7**PH Multiple Non-Adjacent Bookings for WooCommerce Plugin****

If you need the user to book **multiple dates that could be non-adjacent** , use the **[PH Multiple Non-Adjacent Bookings for WooCommerce Plugin](https://www.pluginhive.com/product/woocommerce-multiple-non-adjacent-bookings/)**.

* * *

**Note:**  
Note: This addon has limited cost rules or special prices options compared to the main Bookings plugin.   

* * *

#### **3.8****PH Recurring Bookings and Appointments for WooCommerce Plugin**.****

If you need the user to make a **recurring booking on a daily, weekly, or monthly basis** , use the **[PH Recurring Bookings and Appointments for WooCommerce Plugin](https://www.pluginhive.com/product/woocommerce-recurring-bookings-and-appointments/)**.

* * *

**Note:**  
* This addon plugin provides for recurring bookings with a one-time payment for all bookings.  
* It does not provide subscription payments.  
Please check out the available features on the product page link given above.  

* * *

#### **3.9 Custom Time Slots: Let the user choose from a set of time slots defined by you: For eg: 2, 4 or 9 hours or 2, 4 or 9 days**

If you need your user to be able to select only from a set of time slots that are defined by you, you can use this custom (paid) addon plugin – “<https://www.pluginhive.com/knowledge-base/woocommerce-bookings-custom-booking-interval/>“

* * *

## **4\. Maximum Bookings per Block – How many bookings do you take for the same block?**

Set the number of bookings allowed for the same day or time block by using the “**Max Bookings per Block** ” option under Bookings.

* * *

Max Bookings per Block

* * *

## **5\. Set the Daily Booking Opening and Closing Times**

You can set the time you start and end your bookings on a daily basis. In the booking settings page, you will find the ‘**Daily Booking Times** ‘ option.

* * *

Daily Booking Times

* * *

For 1-hour duration appointments starting at 9.00 AM and ending at 10.00 PM (Last appointment starts at 9.00 PM), the booking calendar looks like the following. 

* * *

Calendar view of daily booking times

***Please note that this option is only applicable to a time-based booking calendar.**

* * *

## **6\. Booking Duration: What are the Minimum and Maximum duration you allow your users to book in a single booking?**

Use the minimum and maximum duration fields to set the minimum and maximum booking durations you allow your users to select at a time. For example,

  * The customers can choose a minimum of 2 days and a maximum of 10 days to book a room. 
  * The customers can book a minimum of half an hour or a maximum of 3 hours of service in 1 booking. 

* * *

Minimum and maximum time duration

* * *

**Auto-Select Minimum Booking Slots** :  
When you give the minimum duration greater than 1, you get the option “Auto-Select Minimum Booking Slots”. This option when enabled ensures that the minimum number of bookings is auto-selected when the user clicks on any available date or time slot. When disabled, the user can select one slot but when the user clicks on “Book Now”, a message is displayed to select the minimum number.

* * *

**Reference:**  
By default, the minimum and maximum duration apply to all the blocks. However, if you need different min and max duration for different days or different blocks, refer to this custom (paid) addon: [WooCommerce Bookings Add-ons – Set Minimum/Maximum Booking Duration based on Date](https://www.pluginhive.com/knowledge-base/woocommerce-bookings-set-custom-duration-based-on-date/)   
Below given are examples where this addon could be useful :  
1\. Let Customers book minimum 2 days during Weekends,and 1 or more days during weekdays   
2\. Let customers book minimum 7 days during the Peak Season – April to July,

## **7\. Do you Allow Booking Cancellations?**

If you allow cancellations, you can use the **Product settings - >Bookings – > Allow Cancellation”** option. 

* * *

Booking cancellations options

* * *

**Reference:**  
For more details on Booking Cancellations, Refer: [Booking Cancellations](https://www.pluginhive.com/knowledge-base/woocommerce-bookings-cancellation/)   

* * *

## **8\. Does the Booking require Approval?**

If you want the users to request bookings and you would like to approve or reject, use the **Requires Confirmation** option. 

* * *

Requires booking confirmation

* * *

#### How to Approve or Reject the Bookings?

In order to approve/reject the bookings from within the plugin settings. Please follow the following steps.

  1. Go to -> **Bookings- > All Bookings **
  2. Select the desired booking -> **Bulk Actions - > Confirm Booking -> Apply**.

* * *

Approve or Reject the Bookings

* * *

**Reference:**  
For more details on Bookings requiring approvals, Refer: [WooCommerce Bookings Confirmation & Payment on Approval](https://www.pluginhive.com/knowledge-base/woocommerce-bookings-confirmation-payment-on-approval/)   

* * *

## **9\. Buffer Time: Do you need a Gap Time for Preparation or Travel between Bookings?**

Using the **Buffer Time** option, you can add a **before** and **after** buffer time. The plugin will ensure that the corresponding time is blocked when a booking happens.

Buffer Time

* * *

**Note:**  
If you need to provide a buffer in minutes(For Eg: 30 mins) when the booking period is in hours (For Eg: 4 hours), you just need to provide the booking period by converting the hours in minutes (ie 240 minutes) or else you will not see the buffer option in minutes.   

* * *

**Reference:**  
For more details Refer to [How to Set up Buffer Time in Bookings and Appointments for WooCommerce?](https://www.pluginhive.com/knowledge-base/how-to-set-up-buffer-time-in-woocommerce-bookings-and-appointments/)  

* * *

## **10\. Set up Booking Costs, Discounts, and Special Prices**

The **[**[Bookings and Appointments for WooCommerce](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** Plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** lets you set up the booking costs for your bookings. The following are the available options in the plugin settings.

### 10.1. Set up the Booking Costs

**Go to Bookings – > Booking Costs **

  * **Base Price**  
This is a one off cost for the booking. It is applied once irrespective of the no. of days/appointments booked in a booking.

  * **Block Cost**  
This is the cost that applies to every block. 

  * **Display Cost**  
Let’s say you wish to display a certain cost in the front end which is different from Base + block cost, or you need to have a suffix text displayed with the cost (For example, $50 / Day.), mention it in the Display Cost field. 

The **Total Price for the booking is Base Cost + Block Cost.** For eg; Base Cost $100 and Block Cost $50 result in,

1-day booking cost: $150 (100+50*1)  
7-day booking cost: $450 (100+50*7)

The display cost is used to display the amount in the front end and is not directly used for the total price calculation. 

* * *

Booking costs

* * *

Booking costs on the booking calendar

* * *

**Reference:**  
For more details, please refer: [How to Set Bookings Costs using Bookings and Appointments for WooCommerce](https://www.pluginhive.com/knowledge-base/how-to-set-booking-costs-using-woocommerce-bookings-and-appointments/)   

* * *

### 10.2. Do you Provide Discounts or Special Prices on your Bookings? 

**Use the Bookings Cost Rules option.**

There are different rules you can create to provide discounts and special prices based on your needs. You can easily do this by using one of the rules.

* * *

Booking costs rule

* * *

#### **Types of Discounts** **or Special Prices**

  1. **Block Count Rule** : Provide a special price based on **The number of days or appointments selected by the user.** This rule applies when the user selects any number of blocks that fall between the range specified in the rule.   
For example,   
1\. Discounted price for booking more than 10 days.  
2\. Discounted price for booking between 8 to 15 days.   
  

  2. **Custom Date Range** : Provide a special price **for a period/ seasons/months/date** **range** or a **specific date**. This rule applies when the user selects blocks that fall between the range of dates specified in the rule.   
For example,   
1\. Additional cost for high season (April 1st to May 31st).  
2\. Special Price for booking on May 5th.  
  

  3. **Range of months** : Provide a special price based on months. This rule applies when the user selects any block within the range of months specified in the rule.   
For example,  
1\. Discounted price for booking in the low season (June to August).  
  

  4. **Range of Days** : Provide a special price based on which day/days of the week it is. This rule applies when the user selects **any** day within the range of days specified in the rule.   
For example,  
1\. Discounted price for booking on a Monday  
2\. Special price for bookings between Friday and Sunday. Here the user gets the special price if he books for Friday, or Saturday or Friday and Saturday, or any combination that falls in the range.   
  

  5. **Exact Match (Days):** Provide a special price based on the day/days of the week. This rule applies when the user selects **all** the days from the range of days specified.   
For example,   
1\. Discounted price for booking Monday and Tuesday both  
2\. Special price for bookings on Friday, Saturday, and Sunday. Here the user gets a special price if he books for Friday, Saturday, and Saturday.   
  

  6. **Time Range(All Week):** Provide a special price based on what time of the day it is. This rule applies for all days of the week.   
For eg; a Special price for booking between 6.00 PM to 8.00 PM. The user gets a special price on all days of the week for booking between 6.00 pm and 8.00 pm.   
  

  7. **Weekday** **and** **Time** : Similarly, you can provide a special price for a specific time on a specific day using the Monday/Tuesday, etc rule.   
For eg; Special price for booking on Monday between 6.00 PM to 8.00 PM.   

* * *

**Note:**  
All the rules apply based on the priority. In the case of conflicting rules, the above rule takes preference.   

* * *

**Reference:**  
* For discounts based on people involved in the booking, please refer People/Participants in your Booking  
* For more information regarding discounts and special prices, please refer : [Discounts and Special Prices](https://www.pluginhive.com/knowledge-base/discount-woocommerce-bookings-an-ultimate-guide/)  

* * *

## 11\. Booking Availability 

Make the calendar dates/times available/unavailable to book based on your availability using the **[**[Bookings and Appointments for WooCommerce](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** Plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)**.

### 11.1. Set your Bookings Availability Window

Set booking availability

* * *

  1. If you have a fixed date when your bookings open/close, use the “**Set a fixed Booking Window** ” option and choose the start date and end date. 
  2. If you need your bookings to be**open for the next “X” number of days from today or from the first available date** use the “**Set a relative booking window** ”. 
  3. **Avoid last-minute bookings: Avoid last-minute bookings by setting a value for the “Allow customers to book until”** X minutes/hours/days before the booking starts.

### 11.2. Restrict Bookings to Start on Certain Days

Do you allow your customers to start bookings only on Mondays or Tuesdays or any other day? Use the option “**Restrict Bookings to start on certain days of the week** ”.

* * *

Restrict bookings on certain days

* * *

### 11.3. Booking Availability Rules

You can make the calendar dates/times available or unavailable to book based on your availability.

**Product Settings – > Bookings – > Booking availability – > Availability Rules.**

You can create availability rules in two ways.

  1. All dates are available by default, so you set only the rules for the dates you are unavailable by using ‘Bookable = No’. 
  2. Make all dates unavailable by checking this option ‘Make all dates unavailable’ and then create rules for the days you are available by using ‘Bookable = Yes’.

* * *

Set booking availability rules

* * *

  * **Custom Date Range Rule** : Define a date range by choosing a start date and an end date when you are available or not available to take bookings.   
For eg; Bookings are closed between April 1, 2020, to April 10, 2020, or Bookings are closed on May 05th.

  * **Range of Days** : Define the days or range of days when bookings are closed/open by choosing the start day and end day.   
For eg; Bookings are closed every Monday (choose Monday to Monday) or Bookings are closed from Saturday to Sunday.

  * **Range of Months** : Define the month or range of months when bookings are closed/open by choosing the start month and end month. For eg; Bookings are closed in December (choose December to December) or Bookings are closed from December to February. 

**Time Ranges: Below rules are applicable for the time-based calendar**.

  * **Time Range (All Week):** Define the time slots for which bookings are open or closed on all the days by selecting the start time and the end time.   
For eg; Bookings are closed on all days from 12:00 pm to 2.00 pm.

  * **Weekday** : Define the time slots for which bookings are open or closed on a specific weekday by selecting the start time and the end time.   
For example, Bookings are closed on all Sundays from 12:00 pm to 7.00 pm.

  * **Custom Date Range with time Rule** : Define a specific date and start time and end time or a start date and start time and end date and end time when you are available or not available to take bookings.   
For eg; Bookings are closed on May 1st, 2020 between 3.00 pm and 6.00 pm or Bookings are closed from May 1st, 2020 3.00 pm to May 10th, 2020 3.00 pm.  

* * *

**Note:**  
If you need to set availability for all your products across the site, visit   
**Bookings > Settings > Global Availability **   
You can also override these rules for certain products at the product level.  

* * *

### 11.4. Custom Message for Remaining slots and Fully booked Slots

You can display the number of slots left per block on the booking calendar and also show a custom message when all slots for a specific date or time are fully booked.

_Note: Before setting up these features, ensure that your maximum bookings per block are set to 2 or more, as this feature is only supported for such settings._

Follow the steps below,

#### Custom Message for Remaining Bookings:

  * **Product Settings – > Bookings – > **Enable**Remaining Bookings**
  * In the **“Remaining Bookings Text”** field, the text will default display as “left.”  
(e.g., if 4 slots are available, it will show “4 left”). If you wish to customize the message, you can type your preferred text. The message can have a maximum of 10 characters.

Now, customers will see the number of remaining bookings available per block on the calendar.

#### Custom Message for a Fully Booked Calendar Slot: 

  * Enable the **Fully Booked Indicator**.
  * In the **“Fully Booked Message”** field, the text will default display as “Sold out.” If you wish to customize the message, you can do so by typing your preferred text. The message can have a maximum of 10 characters.

Now, at checkout customers can see the custom message for fully booked calendar slots. 

* * *

**Note:**  
This custom message is applicable only for products that are fully booked with no more slots available. It does not apply to products that are unavailable due to predefined availability rules, such as blackout dates or manual unavailability settings.   

* * *

## 12\. Add People/Participants in your Booking

The **[**[Bookings and Appointments for WooCommerce](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** Plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** lets you add multiple fields to add participants to the booking. The following are the available options in the plugin settings.

### 12.1. If you have people involved in the booking, use the Booking Participants option

You can define **multiple types of persons** for booking. For Eg: Adults, Kids, etc. Every Participant can have an associated cost attached. 

* * *

Add participants and guests

* * *

Calendar view with participants and guests options

* * *

**Note:**  
Other than people, you can use the Participants option to add any field/option in the booking that needs a number input from the user.   
For example, Number of chairs for the party hall. Here you can create a participant as “No of chairs” and a user can input the number required.   

* * *

  * **Charge Per Block:** You can choose to charge the participants per block. For Eg: Every Adult is charged $100 per day. (where a day is a block)

  * **Multiply all costs by the number of participants:** Use this option when you want to multiply all the costs involved in the booking by the number of people chosen by the user.

  * **Consider Each Participant as a separate Booking:** Enable this option when you want the count of people to be the number of bookings. Enabling this option will deduct the “Max number of bookings allowed for a block” by the number of participants in a booking. For Eg: Booking for seats in a hall. The maximum seats available are 100. If a booking is done for 12 people, the remaining bookings are 88 (100 -12 )

  * **Minimum/Maximum number of participants allowed in a booking:** This option is applicable when you have multiple participant types and you allow only a minimum or maximum on the **combined** total number of participants.   
For Eg: Participants are Adults and Students in an adventure game. You need at least one participant per booking, it does not matter if it’s an adult or a student. Also, you have max 10 places combined.

### 12.2. Do you provide Discounts/Special Prices based on People? 

You have the option to provide special prices based on people by creating Participant Rules.

* * *

Set up Discounts or Special Prices

### **Participant Rules**

  * **Participant Total Count:** Use this rule to provide a special price based on **The number of people** in the booking.   
For example, a Special price on booking for 10 or more people. 

  * **Participant Total Count with Block Count:** Use this rule to provide a special price based on **The number of people and the number of days/blocks booked** in the booking.   
For example, a Special price on booking 7 or more days for 10 to 15 people. 

  * **Participant Total Count with Custom** **Date** : Use this rule to provide a special price based on **The number of people and for a certain period, season, or specific date.**  
For example,   
1\. Special price on booking for 10 to 15 people between May 1, 2020, to May 30, 2020.   
2\. Special price on booking for 10 to 15 people on May 1, 2020.

  * **Participant Total Count with Week Days** : Use this rule to provide a special price based on **The number of people and a** **weekday**.   
For example,   
1\. Special price on booking for 10 to 15 people on Sundays.  
2\. Special charge on booking for 10 to 15 people between Friday and Sunday.

* * *

**Note:**  
*If you have multiple types of participants (Eg: Adults, children) the total participant count rules work on the total number of people chosen(Eg: Adults+ Children) in the booking.   
*If you need rules to work on the specific participants (Eg: Adults only), please save the participant types first to view the participant-specific rule in the rule list.   

* * *

  * **Specific Participant:** Use this rule to provide a special price based on the number of specific participant types in the booking. For example,   
1\. Special price on booking for 2 to 5 Adults on Sundays.  
2\. Special charge on booking for 15 Students between Friday and Sunday. 

  * **Specific Participant with Block Count:** Use this rule to provide a special price based on specific participant numbers **and the number of days/blocks booked.** For example, a Special price on booking 7 or more days for 5 Adults. 

* * *

## 13\. Add Resources or Add-on Options to your Bookings 

If you need to provide extra options for the user to choose from (paid / free) along with your booking, you can do so by using the Resources Option. 

Go To **Bookings - > Booking Resources **

**Single Choice Resource type** – The plugin displays a drop-down with the options you specify and allows users to select only one option. 

**Multiple choices –** The plugin displays checkboxes with the options you specify in the table and allows users to choose multiple options.

**“Automatically Assigned/Let the customer choose” –** When an option is automatically assigned, the option is displayed as text in the front end with no option for the user to select. 

* * *

Add resources and addonsCalendar view with resources and addons

* * *

**Note:**  
With this plugin, you will be able to provide only 1 resource type with multiple options.  

  

* * *

**Reference:**  
If you need to provide multiple resource types and fields Refer –  
Create a WooCommerce Booking Form with additional fields or options for more details.  

* * *

## 14\. Change the Language & WPML Compatibility

The **[****](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)**[Bookings and Appointments for WooCommerce](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** Plugin** is language-ready and is available in all popular languages. All you need to do is set your WordPress Language to your preferred native language.

Change WordPress language

* * *

**Reference:**  
For more details on how to change the calendar language or create a multilingual booking site Refer   
[How To Set Up a Multilingual WooCommerce Bookings Store?](https://www.pluginhive.com/knowledge-base/multilingual-woocommerce-bookings-store/)  

* * *

## 15\. Booking Emails

The **[**[Bookings and Appointments for WooCommerce](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** Plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** automatically sends emails to the Admin and Customer when,

  1. The customer places a new booking
  2. The customer cancels an existing booking
  3. The admin requests, approves or rejects a booking (applies when booking requires approval)

Additionally, you can also configure,

  * [**Reminder and Follow-up/Thank you emails**](https://www.pluginhive.com/knowledge-base/woocommerce-bookings-email-notifications-reminders/)

Bookings – > Settings -> Reminder and Follow up Emails 

* * *

Set up booking emails

* * *

**Reference:**  
Refer to [WooCommerce Bookings Emails, Reminders and Follow up notifications](https://www.pluginhive.com/knowledge-base/woocommerce-bookings-email-notifications-reminders/#new) to learn more about the emails sent and the content included in the email.  

* * *

## 16\. Manage your Bookings 

Bookings and Appointments for WooCommerce Plugin lets you manage your bookings. Please go through the following available options.

### **16.1 Edit an Existing Booking**

The **Booking Modification** feature allows you to update an existing booking without cancelling and creating a new one. You can modify details such as the **booking date, time, participants, resources, assets, and payment details**.

To enable this feature, go to **Bookings → Advanced → Booking Modification (Beta)** and enable **Enable Booking Modification**.

**For detailed instructions, see How to Edit an Existing Booking in WooCommerce.**

* * *

### **16.2 Screen Options – Choose Which Columns to Display**

The All Bookings page uses WordPress’s native **Screen Options** panel, so you can hide the columns you don’t need and set how many bookings load per page.

Visit **Bookings → All Bookings** , then click the **Screen Options** tab at the top-right corner of the page. This opens a panel with two sections:

  * **Pagination** – Set the **Bookings Per Page** value to control how many bookings load at once, up to a maximum of **200 bookings per page**.
  * **Columns** – Check or uncheck which columns appear in the All Bookings table: Order, Product, Booking Status, From, To, No of Participants, Booked By, and Manage.

Once you’ve made your selections, click **Apply** to update the table.  

* * *

### 16.3. View and Filter your Bookings

In order to view all your bookings, go to**Bookings - > All Bookings.**

The All Bookings page displays a complete list of bookings along with key details like Order ID, Product, Booking Status, From and To dates, Assets, number of participants, and the customer who placed the booking.  

* * *

You can use the available filters at the top of the page to quickly locate specific bookings:

  * **Product Filter** : View bookings related to a specific bookable product.
  * **Booking Status Filter** : Filter bookings based on their status, such as Paid, Unpaid, Cancelled, Requires Confirmation, or Partially Paid.
  * **Date Filters** : Narrow down bookings using booking start and end date ranges.
  * **Asset Filter** : Filter bookings based on the assigned asset, allowing you to quickly track bookings linked to specific resources, staff, or equipment.

Manage your bookings

* * *

After selecting the required filters, click **Filter** to update the booking list. These filtering options help you quickly review booking activity and locate relevant bookings without manually scanning through the entire list.

* * *

### 16.4. Approve, Cancel or Delete Bookings

In order to perform actions on your bookings like **confirming a booking, canceling a booking or deleting a booking** , select the bookings and go to Bulk Actions and click on **Apply**. 

* * *

  
Approve, cancel or delete bookings

* * *

### **16.5 Create a Booking from the Backend**

If you had a customer call in and you would like to create a booking on the customer’s behalf. You can do it from,  
  
**Bookings – > Add Booking **

* * *

Add a custom booking

* * *

Choose the booking date and time

* * *

## **17\. Centralized Booking Calendar View**

The Admin Calendar provides a centralized overview of all bookings in a visual **monthly and daily layout** , helping you quickly track booking activity across your store. To access the calendar, navigate to: **Bookings → Calendar**

Each booking appears directly within the calendar based on its scheduled date, allowing you to easily view upcoming reservations without opening individual booking orders.

Admin Calendar View

* * *

You can use the available filters at the top of the calendar to narrow down the displayed bookings:

  * **Product Filter:** View bookings related to a specific bookable product.

* * *

  * **Booking Status Filter:** Display bookings based on their current status. The calendar uses color-coding to help you quickly identify the status of each booking:
    * **Blue:** Paid bookings
    * **Red:** Cancelled bookings
    * **Gray:** Unpaid bookings
    * **Yellow:** Requires Confirmation
    * **Green:** Partially Paid

* * *

  * **Asset Filter:** Filter calendar entries by assigned assets to track bookings linked to specific resources, staff, or equipment.

* * *

You can switch between **Month** and **Day** views depending on how you want to monitor your bookings. The **Month** view provides a broader overview of booking distribution across different dates. 

* * *

The **Day** view offers a more detailed look at individual scheduled reservations.

* * *

These calendar filters help you quickly monitor booking activity and understand availability trends without manually reviewing each booking from the list view.

* * *

## 18\. Customer Booking Process on the Frontend

Let’s check out the booking process of **[Bookings and Appointments for WooCommerce Plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** and how your customers can place a booking.

### **18.1. Booking Flow** for the Customer on the Frontend

  1. For placing a booking the user clicks on a date/time in the calendar and clicks on ‘**Book Now** ‘.

Select the booking dates

* * *

2\. Booking product has been added to the cart. Please check the cart for payment” message is displayed along with a link for ‘**View Cart** ‘.

Adding the product to the cart

* * *

3\. The user clicks on ‘View Cart’ and comes to the Cart Page.

WooCommerce cart page

4\. The user reviews the details and proceeds to checkout and payment.

Checkout page

* * *

5\. Once the payment is completed, the user sees the order received page as shown below.

Order details page

* * *

Booking details

* * *

6\. The user also receives a new booking order email.

Booking email

* * *

### **18.2. Bookings Requiring Approvals Flow for the Customer**

* * *

**Reference:**  
For Bookings Requiring approvals Refer to [WooCommerce Bookings Confirmation & Payment on Approval](https://www.pluginhive.com/knowledge-base/woocommerce-bookings-confirmation-payment-on-approval/)  

* * *

### 18.3. Booking Cancellation Flow for the Customers

* * *

**Reference:**  
For Bookings Requiring approvals Refer to [WooCommerce Bookings Cancellation](https://www.pluginhive.com/knowledge-base/woocommerce-bookings-cancellation/)  

* * *

## 19\. Staff Member Management

Do you have staff that handles the different services provided in your store? For eg; Masseuse, Dog Walkers, etc? They must have their own working schedule and holidays (availability). Also, each staff may have a different charge based on their experience and service. 

The **[Bookings and Appointments for WooCommerce Plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** allows you to define staff, their availability, and cost and attach them to the desired products/services. The bookings are assigned to the staff according to their availability ensuring there are no double bookings.

* * *

**Note:**  
This plugin does not provide for individual staff members to login and manage their bookings. The plugin provides you a way to define staff, their availability and the bookings are assigned by the plugin accordingly  
* For individual staff members to login and manage their own bookings dashboard, you will need a **Multi-vendor Solution**. This bookings plugin is compatible with Dokan Pro multi vendor solution.  
To know more refer : [Dokan Integration](https://www.pluginhive.com/product/dokan-woocommerce-bookings-integration/)

* * *

### 19.1. How to set up a Bookable service that is serviced by different staff members who have their own availability and price? 

To use the asset feature in order to set up the Staff, visit **Bookings** >**Settings > Global Assets**.

Create an asset each for staff members with quantity 1 and define the asset availability – **Bookings - > Settings -> Global Assets**.

Set up global assets

Define availability for each Staff – **Bookings - > Settings -> Global Assets** -> **Asset Availability**.

Setting up staff availability

Assign the staff asset to the desired product/service – **Product settings - > Booking assets -> Enable Assets**.

Assign products to your staff members

* * *

**Note:**  
* If you need the customer to choose the staff – select the “Let customer Choose” option and provide a label for the choice.  
* If you want the staff to be assigned internally but not to be chosen by the customer use the “Assign automatically” option.   

* * *

The product calendar is displayed based on staff availability and the price calculation considers the staff member price. 

Calendar view with staff selectionStaff availability

### 19.2. How to ensure there are no double bookings when the same staff handles 2 services?

You need to follow the below steps:

  1. Refer section 18.1 above to create an asset and assign it to a product 
  2. Create an asset with quantity 1 for the staff member
  3. Assign this staff member to the desired products/services
  4. The plugin ensures that when a service/product is booked for the staff member for a particular date/time, the same staff member is not available for any other services/products during that time. 

* * *

**Reference:**  
For more on assets refer: [How to Set Booking Assets](https://www.pluginhive.com/knowledge-base/how-to-set-booking-assets-using-woocommerce-bookings-and-appointments-plugin/)  

* * *

## **20\. Syncing Bookings Automatically between Two or more Bookable Products**

The **[Bookings and Appointments for WooCommerce](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** **[Plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** lets you share a resource or asset between two or more bookable products.

### 20.1. Synching Bookings between Two or more Bookable Products

Let’s say you need a particular product to be automatically booked when some other product is booked. For eg; when Product A is booked, Product B is automatically booked for that period and when Product B is booked, Product A is automatically booked. For Eg: You rent a product for the whole day or half-day (4 hours) and need to be sure that when the product is booked for the whole day, it is not available to book half-day on that date and vice-versa.

You need to follow the below steps:

  1. Create an asset – Refer section 18.1 to know how to create an asset and assign it to a product. (18.1 explains assets with the example of staff, however same steps can be followed to create any asset)
  2. Assign the quantity 1 to this asset. 
  3. Assign this asset using the “automatically assigned option” to Product A and B both. 

* * *

**Reference:**  
For more on assets refer: [How to Set Booking Assets](https://www.pluginhive.com/knowledge-base/how-to-set-booking-assets-using-woocommerce-bookings-and-appointments-plugin/)  

* * *

### 20.2. Using asset for providing the customer a choice between resources having a quantity

Let’s say you provide a service that uses two types of equipment each having different inventory/quantity. For eg; surfboard rentals that provide 3 types of surfboards that have different inventory/quantity of boards.

You need to follow the below steps:

  1. Refer section 18.1 to create an asset and assign it to a product.
  2. Create assets for each type of surfboard type with their available quantity. (Soft Top – 10, Soft Top Premium – 15 and Boogie Boards – 8)
  3. Assign these assets to the Surfboard rental product 
  4. The plugin ensures that the bookings are taken for the available quantity of each surfboard and calculates the cost based on the board cost. 

* * *

**Reference:**  
For more on assets refer: [How to Set Booking Assets](https://www.pluginhive.com/knowledge-base/how-to-set-booking-assets-using-woocommerce-bookings-and-appointments-plugin/)  

* * *

## **21\. Bookings as Calendar Events**

****Bookings and Appointments for WooCommerce Plugin** v.5.0.0** offers store owners and customers to save bookings to personal calendars including:

  * Google Calendar
  * Apple iCalendar
  * Microsoft Outlook Calendar

### **21.1 Google Calendar Sync**

The **[Bookings and Appointments for WooCommerce Plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** provides 2-way Google Calendar Sync to its users.

  1. When you create a booking on the WooCommerce online store, the booking automatically gets synced with your Google Calendar. 
  2. When you create a booking in the Google Calendar (using the product id and the format specified by this plugin), the booking automatically gets synced with your online store. 

* * *

**Note:**  
Bookings and Appointments for WooCommerce plugin will not sync all the older bookings that were present in your calendar before the plugin was installed and google calendar sync was enabled. The sync happens only for the new bookings that are created after the plugin is installed and sync is enabled.  

* * *

**Reference:**  
For more details, please refer,  
* [How to Set up Google Calendar Sync](https://www.pluginhive.com/knowledge-base/sync-woocommerce-bookings-with-your-google-calendar/)   
* [How To Use 2 Way Google Calendar Sync](https://www.pluginhive.com/knowledge-base/how-to-use-2-way-google-calendar-sync-with-woocommerce-bookings-and-appointments-plugin/)  

* * *

### **21.2 Export Bookings to Apple iCalendar**

The plugin offers flexibility to the store owners as well as the customers by offering an option to export bookings as a .ics file. This file can be used to import the bookings to iCalendar as an event by both the store owner and customers.

* * *

**Reference:**  
For more details, please refer,  
* [How to Export WooCommerce Bookings to iCalendar](https://www.pluginhive.com/knowledge-base/export-woocommerce-bookings-to-icalendar/)  

* * *

### **21.3 MS Outlook Calendar Sync**

The[ Bookings and Appointments for WooCommerce Plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/) provides 2-way MS Outlook Calendar Sync to its users.

  1. When you create a booking on your WooCommerce online store, the booking automatically gets synced with your MS Outlook Calendar.
  2. When an event exists in your Outlook Calendar, it can be imported into WooCommerce as a blocking booking, preventing customers from booking that time slot.

* * *

**Note:** Bookings and Appointments for WooCommerce will not sync older bookings that were already present in your calendar before the plugin was installed and Outlook calendar sync was enabled. The sync only applies to new bookings created after the plugin is installed and sync is enabled.

* * *

**Reference:**  
For more details, please refer to:

  * [ How to Sync WooCommerce Bookings to your Microsoft Outlook Calendar ](https://www.pluginhive.com/knowledge-base/sync-woocommerce-bookings-to-microsoft-outlook-calendar/)
  * [ How to Use 2-Way MS Outlook Calendar Sync ](https://www.pluginhive.com/knowledge-base/set-up-2-way-ms-outlook-calendar-sync-with-woocommerce-bookings/)

* * *

## **22\. Create WooCommerce Bookings Form with Additional Fields or Options**

The **[Bookings and Appointments for WooCommerce Plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** provides you with an option to create one additional form field (checkbox or dropdown) having multiple options and one text field.

* * *

**Reference:**  
Refer : Add Resources/Add-On options to your Bookings  

  

* * *

However, if you need to provide multiple fields or extra options with your Bookings calendar you can make use of the **[PH Product Add-ons for WooCommerce Plugin](https://www.pluginhive.com/product/woocommerce-product-addons/).** This plugin is compatible with the Bookings plugin and provides you the flexibility to create any number and type of fields with your booking calendar allowing you to create a complete booking form. 

The Booking cost calculation considers the additional options’ costs (set by you) and displays the total cost to the user. 

* * *

* * *

## **23\. Accept Deposit or Partial Payment for your Bookings**

If you need your users to book your product or service by making partial payments or paying a deposit, you could make use of the **[PH Deposits for WooCommerce plugin](https://www.pluginhive.com/product/woocommerce-deposits/)**. This plugin is compatible with the WooCommerce Bookings and Appointments plugin and ensures a seamless payment of deposits for the bookings. 

* * *

* * *

## **24\. Dokan Multi-Vendor Integration with WooCommerce Bookings**

The **[Bookings and Appointments for WooCommerce Plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** comes with an integration with the Dokan Multi-Vendor Solution(Dokan Pro Plugin).

If you need multiple sellers/staff members/teachers or service providers to be logged in and be able to manage their own bookings, the Dokan multi-vendor solution for Bookings could be a great choice.

* * *

**Reference:**  
Refer to the [Dokan WooCommerce Bookings Integration](https://www.pluginhive.com/product/dokan-woocommerce-bookings-integration/) for more details.  

* * *

* * *

## **25\. Compatibility with Preview E-mails for WooCommerce**

The [Bookings and Appointments for WooCommerce Plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/) is fully compatible with the **Preview E-mails for WooCommerce** plugin. This allows you to preview and test booking-related email templates before sending them to customers.

  * Install and activate the **Preview E-mails for WooCommerce plugin.**
  * Enter the email type you want to preview, provide the order number, and click on the **Preview** button to view the email.

### **Emails That Can Be Previewed:**

  * PH Booking Cancelled (for customers)
  * PH Booking Cancelled for Admin
  * PH Booking Confirmed
  * PH Booking Requires Confirmation
  * PH Booking Follow-Up
  * PH Booking Reminder
  * PH Manual Bookings
  * PH Waiting for Approval (for Admin)

  
For more details, please refer,  
* [Preview Emails for WooCommerce Plugin](https://wordpress.org/plugins/woo-preview-emails/)  

  

## **26\. Search Bookable Products on the shop page**

With the Bookings and Appointments for WooCommerce plugin, you will be able to search the products on the shop page based on their availability. The search feature is available to be created as a widget. The widget can be placed on the top bar or the sidebars based on your preference. Please refer to this article to know more about the search widget custom (paid) addon plugin: [Bookings Availability Search Widget](https://www.pluginhive.com/knowledge-base/display-woocommerce-bookings-search-availability-widget/)

* * *

## **27\. FAQs**

For additional queries related to the Bookings and appointment plugin, please refer

  * [Bookings and Appointments FAQs](https://www.pluginhive.com/knowledge-base/woocommerce-bookings-and-appointments-plugin-faqs/)

[ Previous  WooCommerce Bookings & Appointments v.3.0.0 – Database Update  ](https://www.pluginhive.com/knowledge-base/woocommerce-bookings-database-update/)

[ Next  Set Booking Cost with WooCommerce Bookings and Appointments  ](https://www.pluginhive.com/knowledge-base/how-to-set-booking-costs-using-woocommerce-bookings-and-appointments/)
