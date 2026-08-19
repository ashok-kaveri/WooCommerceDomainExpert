# How to Share a Service with Multiple Bookable products using Bookings And Appointments for WooCommerce

**Source:** https://www.pluginhive.com/knowledge-base/share-service-with-multiple-bookable-products-using-woocommerce-bookings/
**Platform:** WooCommerce (WordPress)
**Plugin:** bookings
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# How to Share a Service with Multiple Bookable products using Bookings And Appointments for WooCommerce

In this guide, we will tell you how you can set up shared assets between two different products. We will use the **[Bookings And Appointments for WooCommerce](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** plugin and take a real-life example to help you understand how it’s done.

## Business Case:

Dave runs a rainforest tour containing both standard and private tours. However, he has only one vehicle which is shared among both the tours. Following are his challenges:

Attempting to assign a vehicle to a standard tour product so that other private tour product that uses the same vehicle does not allow bookings for the same time blocks while the standard tour is booked and vice-versa. That is, if the vehicle is already in use by one tour product, the other type of tour should close bookings for the same time period.

Also, since the vehicle contains 16 seats, in case if 10 seats are booked, the bookings for the same tour should be open for 6 more bookings while the other tour is blocked for that specific time period.

**In short, The goal is to restrict other products from allowing bookings when the vehicle is in use by another booked product at that time slot. Also, allow 16 bookings for the same tour while closing the other tour bookings for the same time.**

## Solution:

Usually, the **[Bookings And Appointments for WooCommerce](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** plugin will consider the asset quantity to identify the number of bookings left. The plugin considers the minimum value between Asset Quantity and Max booking number. The Booking Assets is a common feature used for many scenarios. For example, Saloon staff where it should work in this manner.

In order to achieve Dave’s complete requirement, we need to follow the steps given below:

  1. Contact our [support team](https://www.pluginhive.com/support/) to download and install the WooCommerce Bookings Asset Availability addon on your WordPress dashboard along with the plugin installed version 1.2.6 or later.
  2. Set the asset quantity, say “Vehicle” to the number of seats available, for example, 16 seats as shown in the screenshot below:
  3. Assign the asset automatically to both the products “Private Standard Tour” and “Standard Rainforest Tour” as shown in the screenshot below:

_**And voila!**_

Once done, the **[Bookings And Appointments for WooCommerce](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** plugin and the add-on will work combined to fulfill Dave’s complete business requirement as illustrated in the screenshots below:

A. Customer books for the Standard Rainforest Tour on July 25th for 10 people.

B. Standard Rainforest Tour for July 25th has still 6 seats left.

C. However, Private Rainforest Tour for July 25th gets blocked out as both the tour shares the same asset “vehicle” even though there are still 6 places left for standard rainforest tour, thus fulfilling Dave’s business case.

## Conclusion

There you go! That’s how you set up shared assets between different products using the **[Bookings And Appointments for WooCommerce](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/) **plugin by **PluginHive**.

If you have any doubts or need help setting up Bookings on your WooCommerce-based website then feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**. Our support team should be able to help you out.

[ Previous  How to Set up Weaving and Fibre Arts Studio using WooCommerce Bookings and Appointments  ](https://www.pluginhive.com/knowledge-base/set-up-weaving-and-fibre-arts-studio-using-woocommerce-bookings/)

[ Next  Indoor Arena Rentals — Set up using Bookings and Appointments for WooCommerce Plugin  ](https://www.pluginhive.com/knowledge-base/set-up-indoor-arena-rentals-with-woocommerce-bookings/)
