# Setup Google Calendar with WooCommerce Bookings and Appointments

**Source:** https://www.pluginhive.com/knowledge-base/sync-woocommerce-bookings-with-your-google-calendar/
**Platform:** WooCommerce (WordPress)
**Plugin:** bookings
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Setup Google Calendar with WooCommerce Bookings and Appointments

It’s a real struggle to streamline bookings with your daily work. Marking dates on the calendar, managing your staff, working late at night to prepare for the next booking, etc. But things start getting out of hand when you get more than 100 bookings per month. It isn’t easy to keep up.

What you might need here is an automated calendar system that will keep you updated with the bookings. With the Google Sync feature, no matter where you are, you can navigate through the bookings right up from your phone. The [**Bookings and Appointments for WooCommerce Plugin**](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)**** enables this feature and, in this article, we will explain to you everything you need to know about it. 

* * *

## How to set up Bookings on your WooCommerce Store?

First, you’d have to activate the**** Bookings and Appointments for WooCommerce Plugin. Once you have completed the setup process, you should see the following section under WordPress. 

Read more: [Installation and activation process of the Bookings and Appointments for WooCommerce Plugin](https://www.pluginhive.com/knowledge-base/installation-licence-activation-woocommerce-bookings-appointments-plugin/).

* * *

* * *

Once you’re inside **Bookings > Settings > Google Calendar Sync**, you should be able to see the following screen.

* * *

## How to integrate your bookings with the Google Calendar?

Proceed with the following steps to get Calendar credentials and integrate WooCommerce Bookings with Google Calendar.

### Get Google Calendar Credentials

  * Click on [**Google Developers Console**](https://console.developers.google.com/cloud-resource-manager)
  * Select **Create Project**

* * *

* * *

  * Enter the Project Name & Click **Create**

* * *

* * *

Note: _Creating a Project takes some time and you will be required to refresh the window once the project is created successfully_. You will see the project listed under **Manage Resources,** after refreshing

* * *

  * Search for **Google Calendar API** in the search bar at the top of the screen, as shown in the image below, and click on it

* * *

* * *

  * Click on **Enable** to enable Google Calendar API for your email

* * *

  * Click on **Create Credentials**

* * *

* * *

To create your credentials, follow the steps:

#Step 1: Credential Type

  1. Select **Google Calendar API** under **Which API are you using?**
  2. Select**User Data,** Click on**Next**

* * *

* * *

#Step 2: OAuth Consent Screen

  1. Under **App Information** , enter the **Application Name** (for example Test App)
  2. Enter **User support email**
  3. Under the **Developer Contact Information** , enter the **Email address**
  4. Click **Save and Continue**

* * *

* * *

#Step 3: Scopes (optional)

  1. Click**Save and Continue**

* * *

* * *

#Step 4: OAuth Client ID

  1. Under**OAuth Client ID** , Select **Web Application**
  2. Provide the name of the web application (eg: Web Client 1)

* * *

* * *

3\. Add Authorized JavaScript origins: Enter your website URL under **Authorized JavaScript** origins. 

**Note: Kindly do not remove the HTTP or HTTPS**

* * *

* * *

4\. Add Authorized redirect URIs: Enter your website URL under **Authorised Redirect URIs** while adding **/wc-api/phive_booking_google_calendar/** after the URL.  
For example – https://www.your_woo_store_url.com/wc-api/phive_booking_google_calendar/

* * *

* * *

**_Note:_**  
  
While using the Bookings and Appointments for WooCommerce Plugin in case of multiple vendors with Dokan:   
  
* Add /wc-api/phive_booking_google_calendar_dokan/ after the URL.   
  
For example: https://www.your_woo_store_url.com/wc-api/phive_booking_google_calendar_dokan/   

* * *

5\. Click on **Create**

#Step 5: Download your Credentials

  1. Click on Done
  2. The page returns to the updated API Project window

* * *

* * *

  * Now Click On **Credentials**
  * Click on the Name of the application, as shown in the image below to get OAuth 2.0 client IDs 
  * Click on your web application. Eg: Web client 1

* * *

* * *

  * You can see the details of**the Client ID** and**Client secret** of your Web Application as shown below. You will require these details in further steps.

* * *

* * *

  * Select**OAuth Consent Screen**
  * Under **Test Users,** click**Add Users**

* * *

* * *

  * Add your**Gmail Id** as **Test User** , Click**Save**

* * *

* * *

Your Credentials are updated. Now you have **Gmail ID, Client ID,** and**Client Secret**.

* * *

## **Connect and Integrate with the Bookings and Appointments for WooCommerce Plugin**

After completing the above steps, you can finally check if everything is working fine. Within the plugin, click the Connect option to integrate with the entered credentials.

  * Enter the credentials: **Client ID, Client Secret**
  * Enable **Google Calendar Sync**

* * *

* * *

  * Scroll to the bottom of the page. Click on**Save Changes** , in order to store the credentials
  * Click on **Connect**

* * *

* * *

  * To verify the credentials, click on **Continue**

* * *

* * *

  * Again Click on **Continue**

* * *

* * *

  * Your credentials are successfully authenticated, and Google Calendar is now connected.

* * *

## **Complete the Google Calendar Sync Setup**

After connecting successfully, follow these steps to finalize the setup:

  * Under the **Google Calendar for Bookings** section in the plugin settings, select the calendar you want to sync.
  * If your calendar is not reflected yet, click on the **Refresh Calendar List** button.

* * *

  * If you want to customize and display only particular bookings as events, you can do this under the **“Booking Status Filter”** as shown below

* * *

  * Check your Google Calendar to ensure that the bookings are now reflected as events.

* * *

## **Troubleshoot Google Calendar Sync with Debug Logging**

If you need to troubleshoot your Google Calendar Sync, visit **Bookings → Settings → Diagnostics** tab and enable the **Google Calendar Sync Debug Log** toggle. Logs are viewable at **WooCommerce → Status → Logs**.

* * *

## ****Cross-Calendar Sync with Microsoft Outlook Calendar****

If you have both Google Calendar Sync and MS Outlook Calendar Sync enabled on your store, the plugin automatically keeps both calendars in sync. When a booking order is created from a Google Calendar event, a corresponding MS Outlook Calendar event is also created automatically.

This ensures that store owners using both calendar integrations do not need to manually manage events across platforms.

For details on setting up MS Outlook Calendar Sync, refer to:

  * [How to Sync WooCommerce Bookings to your Microsoft Outlook Calendar](https://www.pluginhive.com/knowledge-base/sync-woocommerce-bookings-to-microsoft-outlook-calendar/)
  * [How to Use 2-Way MS Outlook Calendar Sync](https://www.pluginhive.com/knowledge-base/set-up-2-way-ms-outlook-calendar-sync-with-woocommerce-bookings/)

* * *

## **Final Thoughts!**

There you have it! Your ultimate Bookings and Appointment for WooCommerce and Google Calendar sync solution. Feel free to comment down below on how you feel about these solutions. And if you need any sort of help or have any queries, you can reach out to our customer support or check out the [FAQ ](https://www.pluginhive.com/knowledge-base/woocommerce-bookings-and-appointments-plugin-faqs/#GoogleSync)section.

* * *

[ Previous  Set Booking Participants with Bookings and Appointments for WooCommerce  ](https://www.pluginhive.com/knowledge-base/how-to-set-booking-participants-using-woocommerce-bookings-and-appointments/)

[ Next  Set up Buffer Time in WooCommerce Bookings and Appointments  ](https://www.pluginhive.com/knowledge-base/how-to-set-up-buffer-time-in-woocommerce-bookings-and-appointments/)
