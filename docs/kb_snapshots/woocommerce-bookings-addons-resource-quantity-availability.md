# WooCommerce Bookings addons – Resource quantity & availability

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-bookings-addons-resource-quantity-availability/
**Platform:** WooCommerce (WordPress)
**Plugin:** bookings
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce Bookings addons – Resource quantity & availability

The **Booking Resource Quantity Addon** extends the[ Bookings and Appointments for WooCommerce](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/) plugin by letting you control how many units of a resource are available per booking slot. Once customers book a resource, its quantity depletes for that slot, preventing over-booking and keeping your availability accurate in real time.

* * *

## **Table of Contents**

  * Requirements
  * Setting Up the Bookable Product
  * Setting Up Booking Resources
  * Configuring Resource Quantity in the Addon
  * What the Customer Sees
  * Using Multiple Resources

* * *

## **Requirements**

  * Bookings and Appointments for WooCommerce must be installed and active.
  * The Booking Resource Quantity Addon (v1.1.0 or later) must be installed and active.

* * *

## **Setting Up the Bookable Product**

Go to **Products → Edit Product → Product Data**.

Under the **Bookings** tab, set the **Booking Period** to either **Fixed Blocks** or **Calendar Range with Blocks** , and choose the unit — Day(s), Minute(s), Hour(s), or Month(s).

* * *

Set a **Max Bookings per Block** to control how many simultaneous bookings are allowed per slot, and enable **Remaining Bookings** if you want the calendar to show customers how many places are left.

Under **Booking Costs** , set a **Base Cost** and a **Cost per Block** as needed.

* * *

Under **Booking Participants** , enable participants and configure the minimum, maximum, and per-participant cost.

* * *

## **Setting Up Booking Resources**

Under the **Booking Resources** tab on the product, enable resources by checking **Enable Resources** and setting the **Resource Type** to Multiple Choice (Check box). Ensure that the **Assign** option is set to Let customer choose so customers can select their preferred resources. 

* * *

Add a **Resource Label** that will be displayed on the product page. Then, in each resource row, enter the **Resource Name/Label** , optionally set a **Resource Cost** , and configure the pricing options like **Charge Per Participant** and **Charge Per Block** as required.

* * *

## **Configuring Resource Quantity in the Addon**

Once the product and resources are set up, go to **WordPress Admin → Bookings → Resource Quantity**.

Click **\+ Add** and fill in:

* * *

  * **Bookable Product ID/Name** : select the product from the dropdown.
  * **Resource Name** : Enter the resource name exactly as it appears on the product.
  * **Quantity** : Enter the total units available per booking slot, for example, **25**.

Click **Save Changes**.

**Note:** The Booking Period must be set to Fixed Blocks or Calendar Range with Blocks, and Resources must be set to “Let Customers Choose” for the addon to apply.

* * *

## **What the Customer Sees**

Here is what happens on the front end with the above setup.

Before selecting the resource, the customer sees the calendar with available dates and the remaining bookings count for each slot. The resource checkbox appears but is unchecked, and the booking cost shown reflects just the base and participant costs.

* * *

Once the customer selects a resource and enters a quantity, for example, 4, the booking cost updates to include the resource cost across the number of participants and blocks selected. The customer then clicks **Book Now** , adds to cart, and proceeds to checkout as usual.

* * *

If the customer tries to enter a quantity that exceeds what is available for that slot, for example, entering 30 when only 25 units of Meals remain, they see an alert:

_“Only 25 of the selected resource available for Bookings on [date].”_

* * *

They cannot proceed until they reduce the quantity to within the available limit. Once the booking is placed and paid for, the resource quantity for that slot is reduced for all future bookings on the same date.

* * *

## **Using Multiple Resources**

If your product has more than one resource, add a separate row in the addon settings panel for each one. Each resource tracks its own quantity independently; if one resource runs low, only that resource triggers the availability alert. Other resources on the same product are unaffected.

* * *

## **Related Articles**

  * [Set Booking Resources with WooCommerce Bookings and Appointments](https://www.pluginhive.com/knowledge-base/how-to-set-booking-resources-using-woocommerce-bookings-and-appointments/)
  * [Set Booking Participants with Bookings and Appointments for WooCommerce](https://www.pluginhive.com/knowledge-base/how-to-set-booking-participants-using-woocommerce-bookings-and-appointments/)
  * [Set Booking Cost with WooCommerce Bookings and Appointments](https://www.pluginhive.com/knowledge-base/how-to-set-booking-costs-using-woocommerce-bookings-and-appointments/)
  * [Advanced Add-ons to Extend Bookings And Appointments for WooCommerce Functionality](https://www.pluginhive.com/knowledge-base/extend-woocommerce-bookings-and-appointment-plugins-functionality-advanced-add-ons/)

  

[ Previous  WooCommerce Bookings Add-ons – Customise Maximum Bookings Per Slot  ](https://www.pluginhive.com/knowledge-base/woocommerce-bookings-add-ons-customise-maximum-bookings-per-slot/)

[ Next  WooCommerce Bookings for Custom Order Status  ](https://www.pluginhive.com/knowledge-base/woocommerce-bookings-for-custom-order-status/)
