# Create a Motorbike Rental Website with Multiple Engine Capacities

**Source:** https://www.pluginhive.com/knowledge-base/online-motor-bike-rental-using-woocommerce-bookings/
**Platform:** WooCommerce (WordPress)
**Plugin:** bookings
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Create a Motorbike Rental Website with Multiple Engine Capacities

In this article, we will cover one of the popular online booking scenarios – Online Motorbike Rental. We will check out how you can set up an Online Motor Bike Rental scenario with the help of [**WooCommerce Bookings and Appointments**](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/) plugin.

* * *

## Online Motor Bike Rental

Steven’s is planning to provide online motorbike rentals with the following requirement. According to Steven,

> **_Hello. I am planning to provide an online guided motorbike rental. I have 5 motorbikes,_**
> 
>   * **_4 X 1200cc_**
>   * **_1 X 800cc_**
> 

> 
> ** _I want to provide the rental only on weekends. And it’s for only 1 – 5 people._**
> 
> **_We wanted the ability to select a “preferred” engine size during checkout. So while booking there would be an option to choose between 1200cc or 800cc engine. However, if a single person has already booked the 800cc, that shouldn’t be available to choose for others._**

* * *

## Plugin Features Used

It is clear from the scenario that Steven can easily set this up using WooCommerce Bookings and Appointments plugin. He can make use of the following features to set up his scenario:

##### Booking Slots & Availability

Based on Steven’s scenario, he can set up a product for Online MotorBike Rental. One Day slot every weekend, where customers can select a max of 4 bookings for 1200 cc and 1 booking for 800 cc at a time.

##### Booking Participants

Steven provides rentals for up to 5 bikes per booking. He can set up Booking Participants where his customers can easily enter the number of people they want to book Bikes for. He can also make sure to charge for each bike booking by enabling Consider Each Participant as Separate Booking.

##### Assets for Engine Types

When it comes to Online MotorBike Rental, Steven has two types of Engines – 1200 cc and 800 cc. Based on the customer choice they can select a particular Bike depending upon the Engine Capacity and set dedicated Booking assets for each one of them and make sure their bookings are separate from each other.

* * *

## Solution

Follow the steps below to set up Online Motor Bike Rental.

  * Create a Bookable Product
  * Set up Booking Period under Booking tab.
    * Choose **Enable Calendar Range with Blocks of 1 Day(s).**
    * Set **Maximum Bookings per block as 5** (5 Motor Bikes).
    * Enable the **Remaining Bookings** Setting to view the Remaining Available Blocks.

  * Visit Bookings Availability and enable **Make All Dates/Blocks Unavailable**
    * Set the **Availability Rule for Weekends** as shown in the image below.

  * Visit **Booking Assets** and click on Enable.
    * Click on **Create a New Asset**
    * Create 2 Assets and name them 1200 cc and 800 cc with Quantity set to 4 and 1 respectively
    * Click on **Save Changes**

  * Visit the product and click on **Update/Publish** to see the assets under Bookings Asset
    * Click on Add Assets and add both 1200 cc and 800 cc to the product as shown in the image below

  * Visit Booking Participants and click on Enable. Here you can set up a field where customers will enter the number of Participant(s) they have.
    * Create a Participant and name it **Number of People**
    * Set **Minimum value as 1 and Per Participant Cost as 100**
    * Enable **Consider each Participant as separate booking**

Once the setup is complete, your Motor Bike Tour Booking product will look similar to the image shown below.

  * Choose the Type of Bike from the drop-down asset list.

  * Once the Bike Type is selected, **Choose a Block Period and Enter the No. of People**
  * If you enter the No. of People more than the Maximum Quantity of Asset (800 cc), an Error Message is displayed since the **maximum quantity of 800 cc Bike Type is 1**

  * Enter No. Of People as 1 and Make a Booking.
  * You will Notice that the Particular Day is being Blocked and no more bookings will be accepted for 800cc Bike on that day.

## Other WooCommerce Booking Use Cases

Apart from the scenario discussed in this article, check out the following use cases fulfilled by WooCommerce Bookings and Appointment plugin.

  * [**Online Hotel Booking**](https://www.pluginhive.com/knowledge-base/set-up-online-hotel-booking-woocommerce-bookings-and-appointments-plugin/)
  * [**Online Equipment Rentals**](https://www.pluginhive.com/knowledge-base/set-up-equipment-rental-store-woocommerce-bookings/)
  * [**Community Hall Booking**](https://www.pluginhive.com/knowledge-base/set-up-community-hall-availabilities-and-pricing-with-woocommerce-bookings-and-appointments/)
  * [**Online Music Lesson Booking**](https://www.pluginhive.com/knowledge-base/online-booking-music-lessons-woocommerce-bookings-and-appointments-plugin/)
  * [**Wine Tasting Session Booking**](https://www.pluginhive.com/knowledge-base/set-up-bookings-for-wine-tasting-session-using-woocommerce-bookings/)
  * [**Online Meeting Room Booking**](https://www.pluginhive.com/knowledge-base/reserve-meeting-rooms-with-woocommerce-bookings-and-appointments-plugin/)
  * [**Online Bike Rental**](https://www.pluginhive.com/knowledge-base/set-up-bike-rental-using-woocommerce-bookings-plugin/)
  * [**Dog Walking & Overnight Pet Care Appointment**](https://www.pluginhive.com/knowledge-base/online-dog-walking-overnight-pet-care-with-woocommerce-bookings/)

[ Previous  Online Dog Walking & Overnight Pet Care with WooCommerce Bookings  ](https://www.pluginhive.com/knowledge-base/online-dog-walking-overnight-pet-care-with-woocommerce-bookings/)

[ Next  Online Tour Booking — Set up using Bookings and Appointments for WooCommerce Plugin  ](https://www.pluginhive.com/knowledge-base/set-up-online-tour-booking-with-woocommerce-bookings-plugin/)
