# Set Booking Cost with WooCommerce Bookings and Appointments

**Source:** https://www.pluginhive.com/knowledge-base/how-to-set-booking-costs-using-woocommerce-bookings-and-appointments/
**Platform:** WooCommerce (WordPress)
**Plugin:** bookings
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Set Booking Cost with WooCommerce Bookings and Appointments

With this tutorial, we’ll help you set up WooCommerce bookings costs using the [Bookings and Appointments for WooCommerce Plugin ](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)by **PluginHive**.

It involves setting up the base cost and adding the block cost and all additional costs (resources, participants cost) to display the final cost on your website.

* * *

## Bookings and Appointments for WooCommerce Costs

You need to log in to your WordPress as admin and get into the **Edit product** page of your desired product. Click on **Booking Costs**.

Bookings Costs

* * *

## Bookings and Appointments Costs Configuration Options

The [Bookings and Appointments for WooCommerce Plugin ](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)comes with the following Booking costs setup. Read along to know more.

  * **Base Cost**  
The Base Cost is a one-time cost, which will be applied only once per booking.
  * **Cost Per Block**  
The Cost Per Block is based on the number of slots that the customers will select. This cost will be applied for every slot that the customer will book.
  * **Display Cost**  
By default, the Product price displayed on the product page is the sum of Base Cost + Cost per block. If you wish to display a cost that is different from this, you can use the display cost. By setting a value for the display cost, you will be overriding the product price that will be displayed on the product page. This price is for display purposes and won’t be added to the booking cost calculation.
  * **Add Pricing Rules**  
The plugin provides additional flexibility for cost calculation based on custom duration and time slots, which you can set up by creating dedicated price rules for your products.

* * *

### Set up a basic Booking with just the Base Cost, Cost Per Block, and Display Cost

Just like any normal WooCommerce product, you can set up a basic booking price for your bookable resource, product, or service. Here’s how you do it.

#### Provide a One-Time WooCommerce Bookings Costs

You can set up a flat rate/ base cost in the Edit product which will apply to your bookings. **Keep in mind that the prices will not** **change even if the customer selects more than one time slot.**

In other words, _**i**** _f_ you rent out a product for multiple days for a fixed price of $25**_, all you need to do is visit **Booking Costs** and then define the **Base Cost** as shown in the image below:

Set static booking cost

* * *

**The Result:**

Booking cost for one day of bookingBooking cost for six days

* * *

#### Provide Bookings Costs based on the Number of Slots Selected by the Customer

In the case of Hotel Bookings, the booking cost is based on the number of days the customers want to stay. A similar scenario can be set up using the Bookings and Appointments for WooCommerce Plugin  
using the**Cost Per Block** functionality.

Depending on the number of blocks or time slots selected by your customer, **the Cost Per Block will be multiplied by the number of total blocks selected.**

So, for example, if you charge $5 per day for a product, and a customer wants to rent the product for 4 days, then the total booking cost would be $5 x 4 = $20. All you need to do is visit Booking Costs and define **Cost Per Block** as shown in the image below:

Set up Cost per block

**The Result:**

Cost of booking for one dayCost of booking for four days

* * *

#### Provide One-Time WooCommerce Bookings Costs with an Additional Cost for Each Day (Hotel Booking)

In the case of Hotel Bookings, you can set up a one-time booking cost, and then a variable cost based on the number of slots selected by the customers.

In other words, you need to define both the **Base Cost** and **Cost Per** **B****lock**. Depending on the number of blocks or time slots selected by your customer, the Cost Per Block will be added to the Base Cost accordingly.

So, for example, if the one-time booking cost is $25 and you want to charge $5 per day, all you need to do is visit Booking Costs and define **Base Cost** and **Cost per block** as shown in the image below:

Set up Base cost and Cost per block

**The Result:**

Cost of booking for one dayCost of booking for three days

* * *

#### Set Display Cost for your WooCommerce Bookings

You can set display any booking costs and exclude them from the price calculation. So this cost will not be calculated and will only appear on the front end.

But if you have defined either **Base Cost** or **Cost per block** or both then the Display Cost will be excluded and will be not considered for price calculation.

Go to Booking Cost and enter the required cost in the **Display Cost** option as shown below in the image:

Set a display cost

**The Result:**

* * *

#### **How to Provide Special Booking Prices to the Customers?**

The [Bookings and Appointments for WooCommerce Plugin ](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)also lets you set up and offer special booking prices to your clients and customers. Let’s check out the possible scenarios.

##### Provide Different Booking Costs for Different Numbers of Slots (Range) selected by the Customers

**Business Case:**

  * **Guitar Lessons Booking for a single slot of 2 hours**
  * **Booking Cost for up to 4 hours (either 1 or 2 slots of 2 hours each) – $39**
  * **Booking Cost for 6 hours (3 slots of 2 hours each) – $79**
  * **Booking Cost from 8 to 14 hours (from 3 to 7 slots of 2 hours each) – $229**

Go to the **Bookings Costs** section and click on**+Add.** The plugin will display a drop-down menu where you need to select **Block Count**. Here you can define the number of blocks/days/time-period for the bookable product.

Set up booking cost based on block count

**The result:**

Cost of booking for 4 hoursCost of booking for 8 hours

* * *

##### Provide a Seasonal Booking based on the Different Month Range

**Business Case:**

  * **Resort Booking with a One-Time cost of $250**
  * **A booking charge of $80 per day**
  * **Seasonal Booking Rate**
    * **From March to August – An additional $50 as a One-Time cost and an additional $10 per day**
  * **Seasonal Booking Discount**
    * **From September to December – $50 Discount on the One-time cost and $20 discount per day**

Go to the **Bookings Costs** section and click on**+Add.** The plugin will display the following drop-down menu where you need to select the **Range of months**.

Now you can define the range of months when you want to offer the bookings for a defined price. You need to select the starting and ending months in the **From** and **To** sections, respectively.

You have the choice to define the One-Time cost under the **Base Cost** and the per-day cost under the **Cost Per Block,** as shown in the image below**.**

Setting up bookings based on months

**The Result:**

Booking price in MarchBooking price in October

* * *

##### Provide Booking Cost Discounts on Weekdays

**Business Case:**

  * **Online Course with a $50 Registration Fee**
  * **Daily Classes on Weekdays and Weekends**
  * **$15 Per Day Cost during Weekends**
  * **$10 Per Day Cost during Weekdays**

Go to the **Bookings Costs** section and click on**+Add.** The plugin will display the drop-down and you have the option to choose either the **Range of Days** or individual days of the week like **Monday, Tuesday,…., or Sunday**.

Decrease the price on weekdays

**The Result:**

Booking costs on WeekendsBooking costs on Weekdays

* * *

##### Provide Christmas Discount for your Bookings

**Business Case:**

  * **Hotel Booking with a One-Time Booking Cost of $250**
  * **Booking is charged $30 per day**
  * **Special Christmas Offer – 50 percent discount on the one-time cost**

Select the **Custom Date Range** option from the list and set the To and From date based on your requirements. In this case, the date range would be from 24th December to 1st January. Set the value of **Base Cost** and **Cost per block** and save the settings****.**** Christmas discount

****The Result:  
****

Before Christmas   
  
Christmas Bookings

* * *

##### Provide Different Booking Costs based on the Time of the Day

**Business Case:**

  * **Doctor’s Appointment charge – $100 Registration Fee**
  * **Day-time Appointment charge – $20 per hour**
  * **Night-time Appointment charge – $25 per hour**

Go to the **Bookings Costs** section and click on**+Add.** The plugin will display the drop-down menu where you can use the **Time Ranges** section that includes **Time Range(all week)** and individual days of the week – **Monday, Tuesday, Wednesday, Thursday, Friday, Sunday,** and **Sunday**. This can help you set up the booking costs based on the time of day or week.

You can implement a fixed booking cost for your time slots which will be applicable for every day of the week. So, for instance, you can have a lower booking cost from 10:00 AM to 06:00 PM and have a comparatively higher cost starting from 07:00 PM to 11:00 PM, as shown in the image below.

Vary booking costs based on the time of the day

**The Result:**

Lower booking prices between 10:00 AM to 06:00 PMHigher booking prices between 07:00 PM to 11:00 PM

* * *

Let us know if you find this article useful. You can visit [Bookings and Appointments for WooCommerce Plugin ](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)to know other cool features and integrations with other plugins.

If you have doubts or need help setting up Bookings on your WooCommerce store, then feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**.

**_Good luck!_**

[ Previous  Setup Guide for Bookings and Appointments for WooCommerce  ](https://www.pluginhive.com/knowledge-base/setup-guide-woocommerce-bookings-and-appointments-plugin/)

[ Next  Set Booking Participants with Bookings and Appointments for WooCommerce  ](https://www.pluginhive.com/knowledge-base/how-to-set-booking-participants-using-woocommerce-bookings-and-appointments/)
