# Offer Online Booking for Music Lessons With the WooCommerce Bookings and Appointments plugin

**Source:** https://www.pluginhive.com/knowledge-base/online-booking-music-lessons-woocommerce-bookings-and-appointments-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** bookings
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Offer Online Booking for Music Lessons With the WooCommerce Bookings and Appointments plugin

In this article, we will set up online music lesson bookings using [**WooCommerce Bookings and Appointments plugin**](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/). This article will cover important aspects like staff management based on the lessons and the lesson time-slot availability for the customers.

## Business Case

Ryan wants to offer music lesson bookings on his website, where the customers will be able to book the lessons and then choose the teacher based on their availability of the teacher. This way the customer will have an idea of which time slot is available for a particular lesson with a particular teacher on a particular date.

The cost of booking would be based on the time interval of the lesson.

  * **A 30-minute lesson would cost $35**
  * **A 45 minutes lesson would cost $50**
  * **A 60 minutes lesson would cost $65**

There will be the following music lessons for bookings:

  * **Piano Lessons**
  * **Guitar Lessons**
  * **Violin Lessons**

Also, the teacher’s availability would be based on the following rules:

  * **Bookings would only be available between 10.00 am to 5.00 pm**
  * **Lucy would not be available on weekends**
  * **Mark would not be available before 11.00 am every weekday and before 3.00 pm on weekends**
  * **Stacy would not be available during Tuesdays**

Based on his business case of Ryan, he can use the WooCommerce Bookings and Appointments plugin to fulfill his requirements in the following manner.

* * *

### Setting Up Different Teachers

Since Ryan’s business case have multiple teachers which may have a limited number of lessons per day available for the students, it can become difficult to handle different teacher’s appointment such that the bookings would not get overlapped.

In order to set up different teachers, you can easily use the **Bookings Assets** feature of the WooCommerce Bookings and Appointments plugin. Click here to read more about the [**Booking Assets and How To Create an Asset**](https://www.pluginhive.com/knowledge-base/how-to-set-booking-assets-using-woocommerce-bookings-and-appointments-plugin/).

* * *

### Different Types of Lessons

Similar to the teachers, Ryan also requires to list out all the lessons so that the students can easily distinguish and proceed with the booking for the required lesson only.

For listing out the lessons, you can use the **Booking Resources** feature of the WooCommerce Bookings and Appointments plugin. Click here to read more about the [**Bookings Resources and How To Set up Resources**](https://www.pluginhive.com/knowledge-base/how-to-set-booking-resources-using-woocommerce-bookings-and-appointments/).

* * *

### Lessons Availability and Duration

Based on Ryan’s case, he requires a minimum of 30 minutes of lesson booking for any lesson and teacher combination. Moreover, he doesn’t want any booking of more than 60 minutes.

This can be achieved using the **Booking Availability** feature of the WooCommerce Bookings and Appointments plugin. You can click here to read more about [**How To Set Bookings Availability**](https://www.pluginhive.com/knowledge-base/how-to-set-bookings-availability-using-woocommerce-bookings-and-appointments/).

* * *

## Setting Up Online Music Lessons Bookings using WooCommerce Bookings and Appointments plugin

Ryan’s case can be set up using the WooCommerce Bookings and Appointments plugin by following the steps below:

  * After [**installing and activating**](https://www.pluginhive.com/knowledge-base/installation-licence-activation-woocommerce-bookings-appointments-plugin/) the WooCommerce Bookings and Appointments plugin, create a new product and set it as a **Bookable Product** on the Products page.  

  * Now you need to set the **Booking settings** in order to set the time slot for the bookable product, as shown in the image below.  
  
You can clearly see the following things that we have set up in the above image.

    * **Booking Period is 15 minutes blocks**
    * **Minimum Duration is set to 2. This way a customer will be able to book at least 15×2 minutes = 30 minutes slot.**
    * **Maximum Duration is set to 4. This way a customer will be able to book at most 15×4 minutes = 60 minutes slot.**
    * **Booking Opening Time is set to 10.00 am**
    * **Booking Closing Time is set to 5.00 pm**
  * Now, you can set the **Booking Cost** as displayed in the image below.  
You can clearly see the following cost that we have set up in the image.

    * **Base Cost is set to 5**
    * **Cost per block is set to 15**
    * **The total booking cost would be Cost per Block x Number Of Blocks + Base Cost**
    * **For a 45 minutes booking the cost would be, 15 x 3 (blocks of 15 minutes each) + 5 = $50**
  * Now you would require to set up lessons using the **Booking Resources** , as displayed in the image below.  
  
You can clearly see the following resources that we have set up in the image.

    * **Resources for all the lessons**
    * **All the resources are optional and set to Let Customers Choose**
  * Now, you need to click on Update product to save the settings.
  * Now visit the **Booking Settings in order to create Booking Assets** , as shown in the image below.  
  
You can see the following availability rules for the teachers set up in the image.

    * **Lucy is not available for Weekends**
    * **Mark is not available till 11.00 am and till 3.00 pm on weekends**
    * **Stacy is not available on the Tuesdays**
  * Now you need to assign the assets to the bookable product that you have created. Visit the Order page and click on edit.
  * You need to Enable the **Booking Assets** and assign the assets to the product as shown in the image below.  
  
Just update the product to save the settings.

* * *

## Placing a Booking…

Once the setup is complete, you can just visit the product page and place a booking.

  * Select a teacher in order to update the calendar based on the availability of the teacher, as shown in the image below.
    * **Lucy’s Availability**  

    * **Mark’s Availability**  

    * **Stacy’s Availability**  

  * Based on the time slots, there will be a minimum of 30 minutes slots and a maximum of 60 minutes sots availability, as shown in the image below.  

  * Also, the option to choose the lessons would be provided, as shown in the image below. You can also see the total booking cost based on the time slot gets updated and shown to the customers before placing the booking.  

* * *

## Final Thoughts…

So, this article covered the **[WooCommerce Bookings](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** plugin and its features like the Booking Assets and Resources in order to set up an online music lessons bookings website. The plugin allows you to define custom booking periods and availability based on days, months, hours, and minutes. This way you can choose from a variety of options for the booking duration of the lessons.

The WooCommerce Bookings and Appointments plugin is a flexible plugin that can be used to set up a variety of online bookings or appointment systems based on WordPress. If you are also looking for a robust and reliable solution for your online learning store, you can read more about the [**WooCommerce Bookings and Appointments plugin**](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/) and the amazing features this plugin provides

We hope this guide would have helped you. Please **[contact our customer support](https://www.pluginhive.com/support/)** if you need to set up bookings on your WooCommerce website. Our team should be able to help you out.

[ Previous  Indoor Arena Rentals — Set up using Bookings and Appointments for WooCommerce Plugin  ](https://www.pluginhive.com/knowledge-base/set-up-indoor-arena-rentals-with-woocommerce-bookings/)

[ Next  Online Dog Walking & Overnight Pet Care with WooCommerce Bookings  ](https://www.pluginhive.com/knowledge-base/online-dog-walking-overnight-pet-care-with-woocommerce-bookings/)
