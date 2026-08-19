# Set up Event Booking with WooCommerce Bookings Plugin

**Source:** https://www.pluginhive.com/knowledge-base/set-up-event-booking-using-woocommerce-bookings/
**Platform:** WooCommerce (WordPress)
**Plugin:** bookings
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Set up Event Booking with WooCommerce Bookings Plugin

In this guide, you’ll learn how to set up Event Booking for your website using **[Bookings And Appointments for WooCommerces plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** by PluginHive and WooCommerce Deposit Plugin by WooCommerce. We are going to take a special business case to help you understand the process better.

## Business Case: Event Booking

A WooCommerce Bookings user wanted to offer a ** _Fit-3D_ _Body Scanning_** event. This event is supposed to be a 3-day event held at the **Victoria University Footscray** campus from October 3rd to 5th, 2019. The bookings are available between 10 AM to 5 PM.

The user wants to have the ability to cancel events until 12 hours before the booking starts. And the number of seats is limited to 100 per hour. The booking cost for the event is $31.82 for each participant with a 50% deposit of the total booking cost to be paid at the time of booking.

* * *

Let’s see how the **[Bookings And Appointments for WooCommerce plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** solves this business case.

## **Bookings And Appointments for WooCommerce** **Plugin** features:

##### Booking Duration

This feature will help in setting up the booking duration of the event.

##### Booking Availability

Allows to set up the booking calendar only on the event days.

##### Booking Participant

The feature allows users to add a section along with the booking calendar where customers can enter a numerical value.

##### WooCommerce Deposit Plugin by WooCommerce:

**WooCommerce Deposits by WooCommerce** is a WordPress and WooCommerce plugin that handles partial payments for your products. Using this plugin your customers can pay a fixed amount or a percentage upfront and then pay the remaining amount later.

* * *

## Solution using **Bookings And Appointments for WooCommerce Plugin** :

Kindly follow the below steps to fulfill the complete business requirement:

  * Create a Bookable Product “Fit3D Body Scanning event”.
  * Set up the Booking Period under the Booking tab.
    * Enable the booking period **Fixed Blocks of 1 Hour(s).**
    * Set **Maximum Bookings per block as 100.**
    * Enable the **Remaining Bookings** option to display the number of tickets left for any given hour.  

    * Enable **Allow Cancellation until 12 Hours** before the booking starts.  

    * Provide the **Daily Booking Times** as event timings where the **First booking starts at** **10 AM and Last Booking starts at 4 PM.** Please note that we need to provide the last booking start time and not the end time (which is 5 PM).  

  * Under the Bookings Availability tab, provide the days of the event within the option **Set a fixed booking window.** This will automatically load the calendar to the month when the event is going to take place skipping the current month and all the months in between.  

  * Under the Booking Participants tab, set the **minimum and the maximum number of participants** and the **booking cost for each participant** (which is $31.82).
  * Enable the option **Consider each participant as a separate booking** as each participant will be provided with a different event ticket, and the same will be deducted from max bookings per block.For example, if a customer books for 5 participants, then 5 bookings will be considered and thus there will be 95 seats remaining.  

  * Under the Deposit tab provided by the WooCommerce Deposit plugin **Enable the Deposit option and set the Deposit Type as 50 percent.  
  
**

**Voila!** Now we have completely set up the 3 days event booking for Fit3D Body Scanning as illustrated below:  
  
Say, a customer wants to book at 3 PM on 4th October for 10 participants.  
  
All the payment details (Due today and the future payments) will also be displayed in the cart.  
  
Once the order is successfully placed for 10 participants, the 3 PM slot on 4th October will now have only 90 remaining seats for booking.  

* * *

## Conclusion:

There you go! That’s how easy to set up an event booking using Bookings And Appointments for WooCommerce from PluginHive and WooCommerce Deposit plugin by WooCommerce.

If you have any doubts or need help setting up Bookings on your WooCommerce-based website then feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**. Our support team should be able to help you out.

**Good Luck!**

[ Previous  Book Online Diving Adventure with Additional Services using Bookings And Appointments for WooCommerce  ](https://www.pluginhive.com/knowledge-base/online-diving-adventure-additional-services-using-woocommerce-bookings/)

[ Next  Farmhouse Accommodation Setup Using Bookings And Appointments for WooCommerce and Product Add-Ons  ](https://www.pluginhive.com/knowledge-base/farmhouse-accommodation-set-up-using-woocommerce-bookings-plugin-and-product-add-on/)
