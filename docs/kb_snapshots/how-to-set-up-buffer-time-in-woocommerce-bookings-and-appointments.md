# Set up Buffer Time in WooCommerce Bookings and Appointments

**Source:** https://www.pluginhive.com/knowledge-base/how-to-set-up-buffer-time-in-woocommerce-bookings-and-appointments/
**Platform:** WooCommerce (WordPress)
**Plugin:** bookings
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Set up Buffer Time in WooCommerce Bookings and Appointments

In this article, we will show you how to easily set up a buffer time between consecutive bookings in [**Bookings and Appointments for WooCommerce Plugin**](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/). We will also see how the buffer works under different booking period conditions.

The Bookings and Appointments for WooCommerce Plugin blocks the buffer time and thus allows your customers to know that the booking will not be available for that time period. You can define the time period for this delay and set any buffer time before and after every booking. You can even use this feature to give yourself or the team preparation time after every booking.

Customers would be allowed to book a resource, service or time, only after this time gap. You can easily use this feature where you need some additional time to prepare for the next booking. You can choose to have the buffer before and after, just before, or after every booking. This feature can help you in many business cases and get the maximum out of it. Some of the common examples where this feature can be used.

  * **Therapy service business** – You can have a time window before each booking and after each booking to allow you the time to travel and set up for the next client or customer
  * **Party organizer business** – You can set the time window to prepare and decorate the place for the party

* * *

## On this Page

  * Setting up Buffer Time
  * Set Buffer Time Before Booking
  * Set Buffer Time After Booking
  * Set Buffer Time Before and After Booking
  * How does buffer work when the buffer time is less than the booking period or is not a multiple of the booking period
  * How does buffer work when the buffer time is greater than the booking period and a multiple of the booking period

* * *

## Setting up Buffer Time

You need to log in to your WordPress as an admin and get into the Edit product page of your desired product. Click on **Bookings** and then enable the **Buffer Time** option as shown in the image below.

* * *

Allow buffer time between bookings

* * *

### Buffer time configuration options:

  * **Before Booking** – Minute(s), Hour(s), Day(s)
  * **After Booking** – Minute(s), Hour(s), Day(s)

* * *

## **Set Buffer Time Before Booking**

Go to **Bookings** and define the Booking Period with any desired time duration. You can either choose **Fixed Blocks** or **Enable Calendar Range with Blocks of**. After that, enable the **Buffer Time** option as shown in the image above. You have to now define the time duration inside **Before Booking**.

Assume that you own a business where you need the preparation time of one hour before you can actually deliver the bookable item or resource to your customers. In this case, you need to choose the **Booking Period** in Hour(s) and then mention the value 1 under the option shown below.

* * *

Set the Buffer time before the booking

* * *

Assume that your customer needs to book between 11:00 AM – 12:00 PM. He or she comes to the calendar, selects the date, and then selects the time as shown in the image below.

Selecting the booking slot of 1 hour(11:00 AM to 12:00 PM)

#### The result:

So when the next customer goes to the same calendar, he or she would see something like the following.

What other customers would see

* * *

## **Set Buffer Time After Booking**

Go to the **Bookings** section and define any desired time duration under the Booking Period option. You can either choose **Fixed Blocks** or **Enable Calendar Range with Blocks of**. After that, enable the **Buffer Time** option as shown in the image above. You have to now define the time duration inside **After Booking**.

You may use this time to restock your inventory or start preparing for the next booking or simply take time off to relax. Let’s take an example where you need a time gap of one entire day after every booking.

* * *

Set Buffer time after every booking

* * *

Assume that a customer has to book for three days. He or she then has to come to your website and then select the days as shown in the image below.

3 days of booking

#### The result:

So when the next customer goes to the same calendar, he or she would see something like the following.

The next is not bookable

* * *

## **Set Buffer Time Before and After Booking**

Go to the **Bookings** section and define any desired time duration under the Booking Period option. You can either choose **Fixed Blocks** or **Enable Calendar Range with Blocks of**. After that, enable the **Buffer Time** option as shown in the image above. You have to now define the time duration inside **Before Booking** as well as inside **After Booking**.

With the combination of the two options, you can have any desired time gap between your bookings. So suppose your team takes a maximum of 40 mins to reach your client’s place to organize their birthday event. And they further take about 80 mins to prepare for the booking and reach to the next client’s place.

* * *

Set Buffer time before and after every booking

* * *

Now suppose that a customer has to book between 10:00 AM to 12:00 PM. Here is how they can book those two hours.

Buffer time of 40 mins before and 1 hour 20 mins after every booking

#### The result:

So when the next customer goes to the same calendar, he or she would see something like the following.

* * *

#### Additional information:

Since the buffer time after the booking is 1 hour and 20 mins(80 mins), the buffer time for the next booking(40 mins) will be included in it. Meaning, if another client tries to book at 2:00 PM then the 40 mins buffer time will be included in the previous buffer time. So in this example, the booking will start at 2:00 PM and the buffer time after the booking will be restricted to 4:00 PM. Refer to the following image to understand this better.

The next consequent booking at 2:00 PM

* * *

## How does buffer work when the buffer time is less than the booking period or is not a multiple of the booking period

When the buffer time is lesser than the Booking period, For Eg : Buffer is 1 hour and Booking period is 2 hours, the plugin pre-calculates the booking time slots taking into consideration the buffer times. The calendar displays the time slots by adding the buffer time before/after each slot. 

**Example 1** : Let us consider the Booking period is 2 hours, and a buffer of 1 hour is required after every booking slot. 

**Booking Period – 2 hours  
After Buffer – 1 hour**

* * *

* * *

**The front end Calendar:**

This is how the calendar displays the time slots. Please note the first time slot starts at 9.00 am and the second time slot starts at 12.00 pm. The first slot starts at 9.00 am continues till 11.00 am (2 hours) , then an after buffer of 1 hour is added, so the next slot starts at 12.00 pm.

The booking slots are : 9:00 – 11:00, 12:00 – 2:00, 3:00 – 5:00 and 6:00 – 8:00.  
Pre blocked After Buffer times : 11:00 – 12:00, 2:00 – 3:00, 5:00 – 6:00 and 8:00 – 9:00.

* * *

**Example 2** : Let us consider the Booking period is 30 minutes and a buffer of 10 minutes is required before and after every booking slot. 

**Booking Period – 30 minutes**

**Buffer:  
Before – 10 minutes  
After – 10 minutes**

* * *

* * *

**The front end Calendar:**

This is how the calendar displays the time slots. Please note the first time slot starts at 9.10 am and the second time slot starts at 10.00 am. Since the start time is 9.00 am and the before the buffer is 10 minutes, the first slot starts at 9.10 am and continues till 9.40 am (30 minutes) , then an after buffer of 10 minutes and a before buffering of next slot of 10 mins is added, so the next slot starts at 10.00 am 

* * *

**Example 3** : Let us consider a buffer time that is not a multiple of the booking period. 

**Booking Period** : 20 minutes   
After Buffer**: 30 minutes**

Here, the buffer is greater than the booking period but is not a multiple of it. 

* * *

## How does buffer work when the buffer time is greater than the booking period and a multiple of the booking period?

In cases, where the buffer times are greater than or equal to or multiples of the Booking period, the buffer times are blocked after the booking slots to the cart and not before.

**Example: 1**

**Booking Period – 30 minutes  
After Buffer – 60 minutes**

* * *

* * *

**The front-end Calendar:**

**Post-booking scenario:**

Here the Booking Period is 9:00 – 9:30 and the buffer is 9:30 – 10:30.

**Example: 2**

**Booking Period – 1 Hour  
After Buffer – 2 Hour(s)**

* * *

* * *

**The front end Calendar:**

**Post-booking scenario** : 

Here the Booking Period is 9:00 – 10:00 and the buffer is 10:00 – 12:00.

* * *

Let us know if you find this article useful. And if you have any queries regarding the Booking Availability setup then feel free to [**contact our support**](https://www.pluginhive.com/support/).

You can also [**check out this article**](https://www.pluginhive.com/woocommerce-bookings-and-appointments-plugin-ultimate-booking-solution/) to know more about the Bookings and Appointments for WooCommerce Plugin.

[ Previous  Setup Google Calendar with WooCommerce Bookings and Appointments  ](https://www.pluginhive.com/knowledge-base/sync-woocommerce-bookings-with-your-google-calendar/)

[ Next  Set Booking Availability with Bookings and Appointments for WooCommerce  ](https://www.pluginhive.com/knowledge-base/how-to-set-bookings-availability-using-woocommerce-bookings-and-appointments/)
