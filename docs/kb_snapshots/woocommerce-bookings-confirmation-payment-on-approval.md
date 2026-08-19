# WooCommerce Bookings Confirmation & Payment on Approval

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-bookings-confirmation-payment-on-approval/
**Platform:** WooCommerce (WordPress)
**Plugin:** bookings
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce Bookings Confirmation & Payment on Approval

Some businesses prefer to review bookings before accepting payment, for example, to check availability or approve special requests. In such cases, customers place a booking request, the admin approves or rejects it, and payment is collected only after approval. The **[Bookings and Appointments for WooCommerce](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)** plugin makes this approval-based booking process easy to manage.

In this guide, we’ll walk you through how to enable Payment on Confirmation in WooCommerce, set up booking approvals, and manage the process from start to finish.

* * *

## **Enable Payment on Confirmation in WooCommerce**

To allow customers to pay only after their booking is confirmed, enable the Payment on Confirmation option in your WooCommerce payment settings.

To enable it:

  1. Go to **WooCommerce > Settings > Payments**.
  2. Locate **Payment on Confirmation**.
  3. Click **Enable**.

* * *

## **Customize Payment on Confirmation Settings**

After enabling, click **Manage** to customize the checkout display:

* * *

  1. **Title** : The label shown at checkout (e.g., Payment on Confirmation).
  2. **Description** : Short explanation for customers (e.g., Pay after your booking is confirmed.).
  3. **Place Order Button Text** : Text for the order button (e.g., Request Confirmation).

Once you’ve made your changes, click **Save changes**.

* * *

## **Enable Confirmation for WooCommerce Bookable Products**

In order to set the desired booking product as requiring approval, visit **Product settings > Bookings** and enable the **Requires Confirmation** option, as shown below.

* * *

## **WooCommerce Bookings Confirmation Request by Customers**

For requesting a booking, the customers can select a date/time in the calendar and click on **Book Now**.

* * *

**Note:**

  * For changing the View Cart message that is displayed, refer to: FAQ.
  * To skip this step and allow the user to go directly to cart/checkout after clicking **Book Now** , refer to: FAQ.  

After clicking on **Book Now** , the booking product will be added to the cart. Depending on your theme settings, customers may see a confirmation message with a cart link, be redirected directly to the cart page, or need to click on **View Cart** to proceed.

* * *

They can review the booking details and proceed to checkout. 

* * *

On the checkout page, the **Payment on Confirmation** option will be selected by default. After filling in the required details, customers can click the **Request Confirmation** button (label may vary based on your settings ) to complete the booking request.

* * *

With this, the booking request is complete, and the customer is presented with an Order Received page. The order details are displayed with the Booking status as **Requires Confirmation** and the payment method as **Payment on Confirmation** , as shown below.

* * *

The plugin will also send an email to the customers, as shown below:

* * *

You will also receive an email notification for new bookings, similar to the one shown here, with all the booking details and the payment method selected as payment on confirmation.

* * *

## **Confirm WooCommerce Bookings from the Admin Dashboard**

The Admin can view and approve the desired bookings from the WooCommerce Dashboard.  
Go to **Bookings > All Bookings**.  
Confirm the desired bookings under **Bulk Actions > Confirm Booking > Apply**.

* * *

## **WooCommerce Bookings Payment**

After the admin approves the booking request, the customers will receive the following email with a payment link for the booking.

* * *

On clicking the payment link in the email, the customers will be taken to the **My Account > My Orders** page, where the payment method is displayed.

Once the payment is made, the slot is blocked for the customer, and the booking is completed.  

[ Previous  WooCommerce Bookings Email Notification  ](https://www.pluginhive.com/knowledge-base/woocommerce-bookings-email-notifications-reminders/)

[ Next  WooCommerce Bookings Cancellation  ](https://www.pluginhive.com/knowledge-base/woocommerce-bookings-cancellation/)
