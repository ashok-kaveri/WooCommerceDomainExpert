# How to Set Up 2-Way MS Outlook Calendar Sync with WooCommerce Bookings

**Source:** https://www.pluginhive.com/knowledge-base/set-up-2-way-ms-outlook-calendar-sync-with-woocommerce-bookings/
**Platform:** WooCommerce (WordPress)
**Plugin:** bookings
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# How to Set Up 2-Way MS Outlook Calendar Sync with WooCommerce Bookings

In this article, we will cover how to use the 2-Way MS Outlook Calendar Sync feature with the [Bookings and Appointments for WooCommerce](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/) Plugin. This feature allows events from your connected Outlook Calendar to be imported into WooCommerce as blocking bookings, preventing customers from booking those time slots. It also allows you to modify or cancel bookings directly from Outlook.

Before proceeding, make sure you have already completed the basic MS Outlook Calendar Sync setup. If not, refer to the following article first: [How to Sync WooCommerce Bookings to your Microsoft Outlook Calendar](https://www.pluginhive.com/knowledge-base/sync-woocommerce-bookings-to-microsoft-outlook-calendar/)

* * *

## **In this article**

  * **Enable Two-Way Outlook Calendar Sync in WooCommerce Bookings**
  * **Sync Outlook Calendar Events as Blocking Bookings in WooCommerce**
  * **How WooCommerce Booking Events Appear in Outlook Calendar**
  * **Modify or Cancel WooCommerce Bookings Directly from Outlook**

* * *

## **Enable Two-Way Outlook Calendar Sync in WooCommerce Bookings**

Once your MS Outlook Calendar is connected, go to WooCommerce → Bookings → Settings → MS Outlook Sync. You will find the Two-Way Sync section below the standard sync settings.

* * *

Enable the Two-Way Sync option by checking the Enable Two-Way Sync checkbox. The section clearly describes the behaviour: when enabled, events in the connected Outlook calendar are imported, and the matching time slots are blocked from being booked.

You will also find the following settings here:

**Look-Ahead Window (days)** – Set how many days ahead the plugin should look to import Outlook events. For example, entering 60 means the plugin will import events within the next 60 days.

**Sync Interval (seconds)** – Set how often the background sync runs. The minimum is 60 seconds. Make sure to save your settings before using the Sync Now button.

**Enable Debug Mode** – Enable this if you need to troubleshoot sync issues.

* * *

Click Save Changes once done.

* * *

## **Sync Outlook Calendar Events as Blocking Bookings in WooCommerce**

To sync an Outlook event as a blocking booking on your website, you need to follow the steps below:

  * Provide the Bookable Product ID (recommended) or the exact Bookable Product Name as the Outlook Calendar Event Title
  * Set the booking date & time based on your product’s availability

* * *

For example, if your product ID is 3214, set the event title to 3214 and timings. Once the sync runs, the plugin will import this event and block that time slot for the corresponding bookable product on your WooCommerce store.

You can verify this on the All Bookings page – the imported Outlook event will appear as a booking with the blocked time slot.

* * *

This order will appear on the Orders page, with the product and booking details automatically populated based on the Outlook event.

* * *

The booking will also be reflected on the corresponding product page, where the synced time slot now appears as blocked and unavailable for customers to select.

* * *

## **How WooCommerce Booking Events Appear in Outlook Calendar**

When a booking is created on your WooCommerce store, the plugin pushes it to your Outlook Calendar as an event. The event title follows this format:

**Order: #[Order ID], Order Item: #[Item ID], [Product Name]([Payment Status])**

* * *

This makes it easy to identify and manage bookings directly from your Outlook Calendar.

* * *

## **Modify or Cancel WooCommerce Bookings Directly from Outlook**

The two-way sync also allows you to modify or cancel existing bookings directly from your Outlook Calendar, without logging into your WooCommerce store.

Booking events pushed by the plugin have a title starting with Order: #…, Order Item: #…. To trigger an action, edit the event title and append one of the following:

**Modify: update** – Appending this to the event title and updating the event’s start and end times will reschedule the booking in WooCommerce on the next sync.

* * *

Then update the event time to the new slot and save. 

* * *

On the next sync, the booking in WooCommerce will be updated to reflect the new time.

* * *

The previously blocked slot is released, and the new time slot is blocked instead – you can confirm this by checking the product page, where the older slot becomes available again, and the updated slot now shows as booked.

* * *

**Note:** This process does not check availability. The plugin will sync and update the booking based on the dates you input.

* * *

**Modify: cancel** – Appending this to the event title will cancel the booking in WooCommerce on the next sync.

* * *

Save the event. On the next sync, the booking status in WooCommerce will be updated to Cancelled.

* * *

The order will reflect this cancelled status, and the previously blocked time slot is released, making it available again for customers to book on the product page.

* * *

**Note:** The change takes effect on the next sync. Make sure to save changes in Outlook before the next sync interval runs.

* * *

**Reference:**  
For more details on setting up the base MS Outlook Calendar Sync, refer to: [ How to Sync WooCommerce Bookings to your Microsoft Outlook Calendar ](https://www.pluginhive.com/knowledge-base/sync-woocommerce-bookings-to-microsoft-outlook-calendar/).

* * *

If you face any issues or need assistance with the 2-Way MS Outlook Calendar Sync, please contact our [support team](https://www.pluginhive.com/support/).

[ Next  Install & Activate License for WooCommerce Bookings and Appointments  ](https://www.pluginhive.com/knowledge-base/installation-licence-activation-woocommerce-bookings-appointments-plugin/)
