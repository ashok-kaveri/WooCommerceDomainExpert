# Set Up Discount for WooCommerce Bookings – An Ultimate Guide

**Source:** https://www.pluginhive.com/knowledge-base/discount-woocommerce-bookings-an-ultimate-guide/
**Platform:** WooCommerce (WordPress)
**Plugin:** bookings
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Set Up Discount for WooCommerce Bookings – An Ultimate Guide

In the competitive E-commerce environment, charging the right amount is a decisive factor to attract new customers. The best way to keep a check on your pricing is to provide regular discounts, loyalty offers or bulk prices to accommodate the cost with the sales. Based on your business, you can provide a discount based on factors like quantity, price, customer loyalty, etc.

In this article, we are going to check out some scenarios where you can provide a discount for your customers using the **[Bookings And Appointments for WooCommerce plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)**. Moreover, this article will cover different factors like the booking duration, the number of guests, booking a particular time of the day, etc. and help you set up booking discounts based on them.

## How to Provide Online Booking Discounts?

This section will cover the following scenarios and how you can set up Bookings And Appointments for WooCommerce plugin to provide booking discounts.

  * **Booking Discount based on Number of Guests**
  * **Discounts Based on Duration or number of blocks**
  * **Percentage Discount based on no of participants or for an additional participant**
  * **Seasonal Discounts for Tour Booking**
  * **Discounted Booking Rates on Weekends**
  * **Promotional Discount Coupons**
  * **Discounts Based on an Exact Match of Day(s)**

### Discount based on Number of Guests/People/Participants

#### Business case:

**_You provide online booking for the amusement park. However, you would like your customers to have a discount based on the number of guests. Basically, you offer the following discount packages:_**

  * _**Up to 4 Guests, provide a standard booking charge**_
    * _**$10 per adult and $5 per Child**_
  * _**You get a 25% discounted price if the number of guests is between 4 to 8**_
  *  _**You get a 30% discounted price if the number of guests is between 8 to 12**_
  *  _**You get a 40% discounted price if the number of guests is between 12 to 20**_

#### Required Configuration:

Follow the steps below to set up the above business scenario and provide the discount based on the number of guests.

##### Creating Rules for Cost Calculation

  * Visit **Participant Rule** section and set up rules for cost calculation.  
**Check out –[How to set up Booking Participants and set up Participant Cost Calculation Rules?](https://www.pluginhive.com/knowledge-base/how-to-set-booking-participants-using-woocommerce-bookings-and-appointments/)**
  * Enter the following details
    * **Range Type** – Select Participant Total Count since the discount is based on the total number of participants
    * **From** – Enter the lower value of the number of guests for which you need to provide a discount
    * **To** – Enter the upper value of the number of guests for which you need to provide a discount
    * **Per****Participant****Cost** – Enter the values in per participant cost as shown below
      * **25% Discount – Change the arithmetic sign to ‘x’ and enter 0.75**
      * **30% Discount – Change the arithmetic sign to ‘x’ and enter 0.70**
      * **40% Discount – Change the arithmetic sign to ‘x’ and enter 0.60**

Create the partcipants and participant rules as given below:

* * *

#### How It Looks on the Product Page

##### Scenario1: Booking Tickets for 3 Adults and 1 Child

As shown in the image below, the cost is calculated based on the following,

  * **One-Time Booking Cost** – $100
  * **Adult Cost** – $10
  * **Children Cost** – $5
  * **Total Cost** = $100 + $10 x 3 + $5 x 1 = $135 (**Without any discount**)

* * *

##### Scenario2: Booking Tickets for 3 Adults and 4 Children

As shown in the image below, the cost is calculated based on the following,

  * **Without Discount**
    * **One-Time Booking Cost** – $100
    * **Adult Cost** – $10
    * **Children Cost** – $5
    * **Total Cost** = $150
  * **With Discount**
    * **One-Time Booking Cost** – $100
    * **Adult Cost** – $7.5 (25% off)
    * **Children Cost** – $3.75 (25% off)
    * **Total Cost** = $137.50

* * *

##### Scenario3: Booking Tickets for 4 Adults and 10 Children

As shown in the image below, the cost is calculated based on the following,

  * **Without Discount**
    * **One-Time Booking Cost** – $100
    * **Adult Cost** – $10
    * **Children Cost** – $5
    * **Total Cost** = $190
  * **With Discount**
    * **One-Time Booking Cost** – $100
    * **Adult Cost** – $6 (40% off)
    * **Children Cost** – $3 (40% off)
    * **Total Cost** = $154

* * *

### Discount based on the Duration or number of blocks

#### Business case:

**_You provide online hotel booking. However, you would like your customers to have a discount based on the number of days._**

  * **_If the customer is booking only 1 day, then the booking cost is $40 per day_**
  * ** _If the customer is booking 2-4 days, then the booking cost is $33 per day_**
  * ** _If the customer is booking 5-10 days then the booking cost is $28 per day_**

#### Required Configuration:

Follow the steps below to set up the above business scenario and provide the discount based on the number of days.

##### Creating Rules for Cost Calculation

  * Visit **Booking Cost** section and set up rules for cost calculation.  
**Check out –[How to set up Booking Participants and set up Participant Cost Calculation Rules?](https://www.pluginhive.com/knowledge-base/how-to-set-booking-participants-using-woocommerce-bookings-and-appointments/)**
  * Enter the following details
    * **Rule Type** – Select **Block Count** since the discount is based on the total number of days selected by the customers
    * **From** – Enter the lower value of the number of guests for which you need to provide a discount
    * **To** – Enter the upper value of the number of guests for which you need to provide a discount
    * **Cost Per Block** – Enter the values in per participant cost as shown below
      * **Change the arithmetic sign to ‘+’ and enter 40**
      * **Change the arithmetic sign to ‘+’ and enter 33**
      * **Change the arithmetic sign to ‘+’ and enter 28**

* * *

#### How It Looks on the Product Page

##### Scenario1: Booking for 2 Days

As shown in the image below, the cost is calculated based on the following,

  * **Booking Cost Per Block (For 2 to 4 days)** – $33
  * **Total Cost** = $33 x 2 = $66

* * *

##### Scenario2: Booking for 7 Days

As shown in the image below, the cost is calculated based on the following,

  * **Booking Cost Per Block (For 5 to 10 days)** – $28
  * **Total Cost** = $28 x 7 = $196

* * *

### Percentage Discount based on number of guests or an additional guest

#### Business case:

_**You provide online booking for hotels. The hotels have a single occupancy rate card. Per guest costs $100. Ideally, you allow 2 guests to check-in for a single room. However, the guests can pay the following price in case the total number of guests falls under a single occupancy.**_

  * _**If there is a single guest, provide a 25% discount for the guest**_
  *  _**If there is an additional guest(more than 2), the booking cost would be 25% less for the additional guest**_
  *  _**One room would accommodate at max 3 guests**_

#### Required Configuration:

Follow the steps below to set up the above business scenario and provide a single occupancy discount.

  * Visit the **Product Page** and click on**Edit** to edit the product
  * Enable **Booking Participants** to add a Guests option
  * Since the discount is based on the number of guests, (both 1 and 3 guests), you can create **Participant Rules** based on the total number of participants
  * Set up participant rules as shown in the image below  

  * Since we require a discount based on the number of guests,
    * If the guest count is 1, provide a booking discount of 25%
    * If the guest count is 3, provide the 3rd guest with a discount of 25%. This can be done by giving 75% per guests and then adding the (25%)discounted price for 2 guests back to the base price (+50)

* * *

#### How It Looks on the Product Page

##### Scenario1: Booking for a Single Guest

As shown in the image below, the cost is calculated based on the following,

  * **Booking Cost Per Guest** = $100
  * **Booking Cost for Guest Count 1** = $100 x 0.75 = $75 **(Discounted Booking Cost)**

* * *

##### Scenario2: Booking for Two Guests

As shown in the image below, the cost is calculated based on the following,

  * **Booking Cost Per Guest** = $100
  * **Booking Cost for Guest Count 2** = $100 x 2 = $200 **(Booking Cost without Discount)**

* * *

##### Scenario3: Booking for Three Guests

As shown in the image below, the cost is calculated based on the following,

  * **Booking Cost Per Guest** = $100
  * **Booking Cost for Guest Count 3** = $100 x 2 + $100 x 0.75 = $275 **(Discounted Booking Cost)**

* * *

### Seasonal Discounts for Tour Bookings

#### Business case:

**_You provide online tour booking services and the packages that you have, vary from season to season. You need to set up the discount packages based on the following,_**

  * _**Off-Season Bookings at 40% Discounted Price**_
    * _**Peak Season – October to April – Standard Price of $1500 and $70 per day**_
    *  _**Off-Season – May to September – 40% discount on the booking charges**_

#### Required Configuration:

Follow the steps below to set up the above business scenario and provide the discount based on booking time.

##### Set Up Discount based on a Month Range

  * Click on **Edit Product** to edit the product booking settings
  * Click on **Booking Cost  
Check out – [How to set up Booking Cost using WooCommerce Bookings and Appointments plugin?](https://www.pluginhive.com/knowledge-base/how-to-set-booking-costs-using-woocommerce-bookings-and-appointments/)**
  * Set up cost calculation rules based on Custom Date Range  

  * Since we require discounted rates from May to September, enter the following details,
    * **Range Type** – Select **Range of Months** since the discount is based on the months which are off-season
    * **From** – Select the starting Month of the off-season, i.e. May
    * **To** – Select the ending month of the off-season, i.e. September
    * **Base Cost**
      * **40% Discount – Change the arithmetic sign to ‘x’ and enter 0.60**
    * **Cost Per Block**
      * **40% Discount – Change the arithmetic sign to ‘x’ and enter 0.60**

* * *

#### How It Looks on the Product Page

##### Scenario1: Booking A Weeks Tour for March

As shown in the image below, the cost is calculated based on the following,

  * **One-Time Booking Cost** – $1500
  * **Daily Booking Cost** – $70
  * **Total Cost** = $1500 + $70 x 7 = $1990 (**Without any discount**)

* * *

##### Scenario2: Booking A Weeks Tour for August (Off-Season)

As shown in the image below, the cost is calculated based on the following,

  * **One-Time Booking Cost** – $1500 x 0.60 = $900
  * **Daily Booking Cost** – $70 x 0.60 = $42
  * **Discounted Total Cost** = $900 + $42 x 7 = $1194

* * *

### Discounted Booking Rates for Weekdays

#### Business case:

**_You provide online booking for theatre shows where a single booking is for a duration of 3 hours._**

**_So basically the cost includes,_**

  * _**Per ticket cost of $50**_
  *  _**Special Discount of 10% per ticket on the weekdays**_

#### Required Configuration:

Follow the steps below to set up the above business scenario and provide the discount based on booking time.

##### Set Up Discount based on Days of the Week

  * Set up **Booking Participant** and enable the **Multiply All Cost By Number Of Participants** option
  * Click on **Booking Cost** and set up **Booking Cost Rule** to provide a discounted price based on the day of the week
  * Since we require discounted rates during the weekdays, i.e. Monday to Friday, enter the following details,
    * **Range Type** – Select **Range of Days**
    * **From** – Select the starting day as Monday
    * **To** – Select the ending day as Friday
    * **Base Cost**
      * **10% Discount – Change the arithmetic sign to ‘x’ and enter 0.90**

* * *

#### How It Looks on the Product Page

##### Scenario1: Booking 5 Tickets on a Saturday

As shown in the image below, the cost is calculated based on the following,

  * **Ticket Cost** – $50
  * **Total Cost** = $50 x 5 = $250 (**Without any discount**)

* * *

##### Scenario1: Booking 5 Tickets on Thursday (Weekday Discount)

As shown in the image below, the cost is calculated based on the following,

  * **Ticket Cost –** $50 x 0.9 = $45
  * **Discounted Total Cost** = $45 x 5= $225

* * *

### Promotional Discount Coupons

#### Business case:

**_You offer monthly 100 discount coupons for your customers. Is it possible to use the discount coupons with this plugin..?_**

#### Required Configuration:

The Bookings And Appointments for WooCommerce plugin is by-default compatible with the WooCommerce Coupons. You can set up a coupon and use it while checkout.

Follow the steps below to set up a coupon so that your customers can use it while bookings

  * Create a coupon based on your requirements
  * Visit the Product Page and place a booking
  * Visit the cart page and proceed to checkout
  * You can enter the coupon on the **Checkout Page** as shown in the image below

### Discounts Based on an Exact Match of Day(s)

#### **Business Case:**

Let’s say you want to offer a Yoga room for rent and set up the Booking pricing rules displayed below.

  * From Monday to Thursday, the cost of the single-day booking is $195
  * From Friday to Sunday, the cost of the single-day booking is $245 
  * 10% discount if exactly Friday to Sunday is booked
  * 15% discount if exactly Monday to Tuesday is booked
  * 20% discount if exactly Monday to Friday is booked 
  * 30 % discount if exactly Monday to Sunday is booked

#### **Required Configuration:**

The above requirements can be easily fulfilled with the Bookings And Appointments for WooCommerce plugin. You just need to follow the steps shown below to achieve it.

  * Click on **Booking Cost** and set up **Booking Cost Rule** for:
    * **Range of Days**
    * **Exact match (Days)**

You can use the above image as an example to set up the booking pricing rules. Please note that the discount numbers entered here are pre-calculated and you just need to enter the number you want to offer. 

Friday to Sunday: ($245 x 3 days) – 10% discount = $661.5 

For instance, the third selection starts from Friday to Sunday and the amount entered is $661.5. This amount is the result of the following calculation. Consider the below image as a reference to the previous example. 

Now let’s take another case. 

Suppose someone selects only Friday to Saturday, then he or she won’t get any discounts since the base cost is priced at $245/day, which means it will match the 6th rule, i.e, $245 x 2 days = $490. Have a look at the sample image below. 

## Final Thoughts

So there it is. Bookings And Appointments for WooCommerce plugin with its flexible booking cost calculation, allows you to provide discounts based on almost any business scenario. You can set up custom cost calculation rules and provide a discount based on various parameters like the time of the day, days of the week, months or number of guests for a booking.

If you are a WooCommerce store and looking for a complete solution to turn your online store to a Booking website, feel free to check out the [**Bookings And Appointments for WooCommerce plugin**](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/). If you have any complex business scenario that you want to discuss with us, contact our [**support team**](https://www.pluginhive.com/support/) and we will definitely help you.

[ Previous  How To Use 2 Way Google Calendar Sync with WooCommerce Bookings and Appointments plugin?  ](https://www.pluginhive.com/knowledge-base/how-to-use-2-way-google-calendar-sync-with-woocommerce-bookings-and-appointments-plugin/)

[ Next  Set Up Booking Costs Based on Different Seasons in WooCommerce  ](https://www.pluginhive.com/knowledge-base/woocommerce-bookings-for-different-seasons/)
