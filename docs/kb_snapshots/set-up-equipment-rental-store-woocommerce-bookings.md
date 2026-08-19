# Set up an Equipment Rental Website with WooCommerce Bookings

**Source:** https://www.pluginhive.com/knowledge-base/set-up-equipment-rental-store-woocommerce-bookings/
**Platform:** WooCommerce (WordPress)
**Plugin:** bookings
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Set up an Equipment Rental Website with WooCommerce Bookings

[**Bookings and Appointments for WooCommerce Plugin**](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/) allow the equipment rental companies to rent out many different items like sports-equipments, bicycles, furniture items or musical instruments, etc., But in this article, we will focus on setting up a sports equipment rental store, which will essentially allow users to rent out surfboards.

## Business Case:

Let’s first understand the framework of the business (surfboard-rental store) you’re going for and list up essential things which are required to do so.

Rent surfboard from a wide variety of surfboards:

  * **Soft Top surfboard**
  * **Soft Top Premium surfboard**
  * **Boogie board**

We have 10 surfboards each to rent every hour. Here are the tariffs for the same:

  * **Fixed charges – $50 per surfboard**
  * **Additional charges**
    * **For Adults (18 and above) – $10 per participant per hour**
    * **For Children (below 18) – $5 per participant per hour**

All the bookings have to be made between the specific time period

  * **From 5 AM to 4 PM**

#### Additional goal

**Limited period offer!!!**

Book for more than 5 tickets, and get your ticket price reduced to $5 for every additional ticket more than 5. Optionally, you can choose from accessories that are provided to you:

  * **Drinks bottle for $5**
  * **Sunglasses for $10**

* * *

### Solution:

The Bookings and Appointments for WooCommerce Plugin can be used to create a surfboard rental store using the following features of the plugin:

  * [**Bookings**](https://www.pluginhive.com/knowledge-base/setup-guide-woocommerce-bookings-and-appointments-plugin/)

This option will help you provide the duration of the booking period, maximum bookings, and the booking timings and the maximum bookings allowed.

  * [**Bookings Assets**](https://www.pluginhive.com/knowledge-base/how-to-set-booking-assets-using-woocommerce-bookings-and-appointments-plugin/)

You need to create three assets for the three different varieties of surfboards—Soft Top, Soft Top Premium and Boogie Boards. That’s because of the fact that the surfboards (assets) quantities are limited, and thus, you need to maintain the availability for the same.

  * [**Bookings Cost**](https://www.pluginhive.com/knowledge-base/how-to-set-booking-costs-using-woocommerce-bookings-and-appointments/)

This option lets you define the rental cost for your surfboards.

  * [**Bookings Participants**](https://www.pluginhive.com/knowledge-base/how-to-set-booking-participants-using-woocommerce-bookings-and-appointments/)

By using the Booking Participants feature, one can assign different prices to different participants. Since the Adults and Children are two separate participants defined here, they will have different tariffs/rates.

  * [**Bookings Resources**](https://www.pluginhive.com/knowledge-base/how-to-set-booking-resources-using-woocommerce-bookings-and-appointments/)

The resources option can be used when you want to sell additional items along with the bookings. Drinks and sunglasses, for example, can be considered resources that can be sold to customers as optional items.

* * *

## Setting up Surfboard Rental store with Bookings and Appointments for WooCommerce

  * **General Booking Settings**

    * Create a booking for 11-hour slot and allow booking period for a calendar range with blocks of 1 hour.

    * Go to Product Page from WooCommerce Dashboard→Select Bookable Product

    * Set the **Maximum Bookings per Block** to 30 as there are 30 surfboards available (10 each)

    * As surfboard timings are from 5 AM to 5 PM and no one will be allowed to book for more than 12 hours, set the **Maximum duration** to 12.

    * Set the **First booking starts at** 5 AM and **Last booking starts at** 4 AM as the surf booking timing is from 5 AM to 5 PM  

  * **Booking Assets**

    * Create bookable assets for three different variety of surfboards – Soft Top, Soft Top Premium and Boogie Board.

    * To create an asset, go to **Bookings Settings** from WooCommerce dashboard and select the **Assets** tab as shown in the screenshots below. Assign quantity of 10 to each as we have only 10 surfboards for each.  

    * Go to the product settings and click on **Enable Assets**.
    * Add the assets for that particular product and leave the base cost and block cost as blank as there is no cost associated with each variety of surfboard.  

  * **Booking Participants**

    * Go to the Product Page from the WooCommerce dashboard and click on**Booking Participants**   

    * Click on **Enable Participants** to add participants like **Adults** and **Children**   

    * Enable the option “**Multiply all costs by the number of participants** ” as the cost will be multiplied by the number of participants. Say, for example, if there are 4 participants (2 adults and 2 children), then the cost of each surfboard (which is $50) will be multiplied by the number of participants. This is because for 4 participants you need 4 surfboards.   

    * Enable the option “**Consider each participant as a separate booking** ” as every participant will be considered as a separate booking. Say, if 4 participants book for one slot at the same time, it should be considered as 4 separate bookings since 4 surfboards are being used.   

    * Add Adults as participants and provide the per-participant cost of 10 dollars. Provide charge per block to “Yes” as prices are calculated for every hour/block.   

    * Add Children as participants and provide the per-participant

cost to 10 dollars. Provide charge per block to “Yes” as prices are calculated for every hour/block.  

  * **Booking Resource**

    * Resources are used when you want to sell additional items along with the bookings. Like, provide drinks bottles and sunglasses as resources here which are the optional items customers can buy.   

    * Go to the Product page from the WooCommerce dashboard and click on **Booking Resources**   

    * Select “**Enable Resources** ” to add resources like Drinks bottle and Sunglasses   

    * Provide the resource cost to each of the resources
    * Enable “Yes” to **Charge per Participant** and “No” to **Charge per Block** as the customers will be charged based on the number of participants and not based on the number of hours/blocks.

* * *

## Place a Booking…

Once the set up is complete, visit the product page and place a booking.

  * Select the type of surfboard from the drop-down :  

  * Select the date and the time to book the surfboard and set 1 hour or a maximum of 12 hours block. (As you can see from the below screenshot the time available is from 5 AM to 4 PM). 4 PM is the last slot as the surf timing is till 5 PM   

  * Once done, enter the number of adults and children in the boxes below the calendar  

  * Last, below the Participants box, select any resources which you wanted to buy (optional)   

  * So for example, if a customer David wants to book a

surfboard for the

7th for the whole day (from 5 AM to 5 PM) for 2 adults and 2 children along with sunglasses, then the cost for the booking will be as follows :

    * The surfboard charge for 4 participants (if the charge for each surfboard is 50 dollars) is : 50 * 4 = 200 dollars
    * Price for 2 adults for 12 hours (if cost of adult is 10 dollars per hour) is : 2 * 10 * 12 = 240 dollars
    * Price for 2 children for 12 hours (if cost per child is 5 dollars per hour) is : 2 * 5 * 12 = 120 dollars
    * Cost for sunglasses for 4 participants (if each sunglass cost 10 dollars) is : 10 * 4 = 40 dollars
    * Therefore, the total cost will be : 200 + 240 + 120 + 40 = 600 dollars (as shown in the screenshot below).  

* * *

We really hope this article would have helped in setting up an equipment rental store. Do let me know in the comments if you have any query. If you need any help setting up the plugin, then feel free to **[contact our customer support](https://www.pluginhive.com/support/)**. They should help you through and out.

**_Happy selling!_**

[ Previous  Set up Recurring Online Courses with WooCommerce Bookings  ](https://www.pluginhive.com/knowledge-base/recurring-online-courses-woocommerce-bookings/)

[ Next  Set Up Online Hotel Booking with WooCommerce Bookings  ](https://www.pluginhive.com/knowledge-base/set-up-online-hotel-booking-woocommerce-bookings-and-appointments-plugin/)
