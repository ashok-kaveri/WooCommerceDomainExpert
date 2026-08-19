# How to Sync WooCommerce Bookings to Microsoft Outlook Calendar

**Source:** https://www.pluginhive.com/knowledge-base/sync-woocommerce-bookings-to-microsoft-outlook-calendar/
**Platform:** WooCommerce (WordPress)
**Plugin:** bookings
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# How to Sync WooCommerce Bookings to Microsoft Outlook Calendar

In this article, we will cover how to sync Bookings and Appointments for WooCommerce Plugin to your Microsoft Outlook Calendar as an event and let your customers join the events as attendees. This way you can offer your customers the ability to add bookings to their personal calendar as an event.

Before proceeding, you will require the following to access this feature:

  * **[Bookings And Appointments for WooCommerce v.5.0.0 or above](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)**

* * *

** _Reference_**  
  
If you are on the older versions, refer the following article to update the plugin to the latest version.  
  
* [How to update Bookings And Appointments for WooCommerce](https://www.pluginhive.com/knowledge-base/how-to-download-install-update-woocommerce-plugin/)

* * *

## Sync Bookings and Appointments WooCommerce to MS Outlook Calendar

After updating the Bookings and Appointments for WooCommerce Plugin to the latest version, visit the plugin settings.

* * *

On the plugin settings page visit the **MS Outlook Sync** tab and enable the **MS Outlook Event Sync** option.

* * *

To configure the MS Outlook Sync, you must find your Client ID and Client Secret. Firstly, go to the Azure portal and sign in to your work, school, or personal Microsoft account.

* * *

Once, you’ve done this, click on the View button under the Manage Microsoft Entra ID option as shown in the image below.

* * *

Click on the Add option and select the App Registration option from the drop-down as shown in the image below.

* * *

Fill in the “**Name** ” field as per your preference. For example, fill in the Display name as ‘PH Bookings Sync’. Then under “**Supported account types** ” choose the option “**Accounts in any organizational directory (Any Azure AD directory- Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)** “.

* * *

Once done, select “**Web** ” under the “**Select A Platform** ” option in the Redirect URI section. Enter the redirect URI from the bookings plugin settings as shown below and click on the **Register** button.

* * *

After registering, you will get the Client ID/Application ID you need to enter in the bookings plugin settings as shown below.

* * *

To get the Client Secret, click on the **Certificates & Secrets** option under the **Manage** section on the left panel of the screen, as shown below.

* * *

Click on the **New Client Secret** button to create a client secret and enter the **Description** and the number of days after the client secret expires under the **Expires** option, as shown below.

* * *

After adding the expiry days, you will get the client secret under the “Value” column, which you need to enter in the bookings plugin settings as shown below.

* * *

The next thing that you will need to do is go back to the left side panel and find the **API Permissions** option as shown below:

* * *

Under the Configured Permissions section, click on the Microsoft Graph option, and click on the Delegated Permissions option as shown below.

* * *

Next, search for the **Calendars.ReadWrite** in the search panel, select it once found, and then click on the **Update Permissions** button.

* * *

Go back to your WooCommerce store and make sure you have entered your Client ID and Client Secret in the respective fields. Save these settings first by clicking on **Save Settings**. Then click on the **Sign In to MS Outlook** button.

* * *

Once connected to your MS Outlook, the plugin will update the **Connection Status** as shown in the image below.

* * *

## **Complete the Microsoft Outlook Calendar Sync Setup**

After syncing successfully, follow these steps to finalize the setup:

  * Under the **Outlook Calendar for Bookings** section in the plugin settings, select the calendar you want to sync. It will display the calendars available in your Microsoft Outlook account. 
  * If your calendar is not reflected yet, click on the **Refresh Calendar List** button.

* * *

  * If you want to customize and display only particular bookings as events, you can do this under the **“Booking Status Filter”** as shown below

* * *

You can also email the customers an email notification of the event by enabling the **Add Customer as Event Attendee** option.

* * *

This way customers also get an option to add the bookings to their respective calendars.

Check your Microsoft Outlook Calendar to ensure that the bookings are now reflected as events.

* * *

## **Re-sync Outlook Calendar for Existing Bookings**

If your Outlook Calendar events are out of sync, for example, after a connection issue or a settings change, you can manually re-sync bookings directly from the All Bookings page.

To do this, go to WooCommerce → Bookings → All Bookings, select the bookings you want to re-sync, choose Re-sync Outlook Calendar from the Bulk Actions dropdown, and click Apply.

This will push the selected bookings back to your Outlook Calendar as events.

* * *

## **Troubleshoot MS Outlook Sync with Debug Logging**

To troubleshoot your MS Outlook Sync, visit **Bookings → Settings → Diagnostics** tab and enable the **MS Outlook Sync Debug Log** toggle. Logs are viewable at **WooCommerce → Status → Logs**.

* * *

## **Cross-Calendar Sync with Google Calendar**

If you have both MS Outlook Calendar Sync and Google Calendar Sync enabled on your store, the plugin automatically keeps both calendars in sync. When a booking order is created from an MS Outlook Calendar event, a corresponding Google Calendar event is also created automatically.

This ensures that store owners using both calendar integrations do not need to manually manage events across platforms.

**Note:** For details on setting up Google Calendar Sync, refer to:

  * [ How to Set up Google Calendar Sync ](https://www.pluginhive.com/knowledge-base/sync-woocommerce-bookings-with-your-google-calendar/)
  * [ How To Use 2-Way Google Calendar Sync ](https://www.pluginhive.com/knowledge-base/how-to-use-2-way-google-calendar-sync-with-woocommerce-bookings-and-appointments-plugin/)

* * *

## Modify Bookings and Appointments for WooCommerce Event Details

You can customize the booking details that get added to the calendar events by selecting from the following placeholders:

  * [ASSET]

Enter this in the event title or description to add asset details from bookings to the calendar event

  * [BOOKING_STATUS]

Enter this in the event title or description to add the booking status from bookings to the calendar event

  * [BOOKING_COST]

Enter this in the event title or description to add the total booking cost from bookings to the calendar event

  * [BILLING_ADDRESS]

Enter this in the event title or description to add the billing address from bookings to the calendar event

  * [BOOKING_NOTES]

Enter this in the event title or description to add the booking notes (if any) from bookings to the calendar event

  * [CUSTOMER_NAME]

Enter this in the event title or description to add the customer name from bookings to the calendar event

  * [CUSTOMER_PHONE]

Enter this in the event title or description to add the customer’s phone number from bookings to the calendar event

  * [CUSTOMER_EMAIL]

Enter this in the event title or description to add the customer’s phone number from bookings to the calendar event

  * [PARTICIPANT]

Enter this in the event title or description to add the participant details from bookings to the calendar event

  * [PRODUCT_NAME]

Enter this in the event title or description to add the bookable product’s name from bookings to the calendar event

  * [RESOURCE]

Enter this in the event title or description to add the booking notes (if any) from bookings to the calendar event

* * *

If you face any issues or need assistance exporting Bookings and Appointments for WooCommerce Plugin to the iCalendar, please contact our **[support team](https://www.pluginhive.com/support/)**.

[ Previous  How to Export WooCommerce Bookings to iCalendar  ](https://www.pluginhive.com/knowledge-base/export-woocommerce-bookings-to-icalendar/)

[ Next  How to Display WooCommerce Bookings Search Availability Widget on your store  ](https://www.pluginhive.com/knowledge-base/display-woocommerce-bookings-search-availability-widget/)
