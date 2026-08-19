# Troubleshooting Google Calendar Sync for WooCommerce Bookings and Appointments Plugin

**Source:** https://www.pluginhive.com/knowledge-base/troubleshooting-google-calendar-sync-woocommerce-bookings-and-appointments-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** bookings
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Troubleshooting Google Calendar Sync for WooCommerce Bookings and Appointments Plugin

The [Bookings and Appointments for WooCommerce Plugin](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/) is a simple, yet a robust solution to set up booking facility on your website. This document explains the common issues that might occur while setting up the Google Calendar Sync and how you can fix them. 

* * *

## On this page

  * **Error: redirect_uri_mismatch**
  * **Google API Authentication failed!**
  * **Warning message: “The app isn’t verified”**

* * *

## Error: redirect_uri_mismatch

**The possible reason for the error “** _**The redirect URI in the request does not match the ones authorized for the OAuth client**_**“, is because an incorrect “** _**Authorised redirect URI**_**” was provided at the time of setting up the Google Calendar sync, as shown in the image below.**

### Solution for redirect_uri_mismatch error

In order to resolve the issue, copy the redirect URI provided in the error message and update it under the “Authorised redirect URIs” in the link provided within the error message as shown below.

* * *

## Google API Authentication failed!

**There are two possible reasons for the error “** _**Google API authentication failed**_**“;  
  
1\. Incorrect or mismatching credentials (Client ID/Client Secret) was provided within the plugin settings.  
2\. The website opens up in both http and https.**

* * *

### Solution for Google API Authentication failed error

1\. In order to resolve the issue with incorrect or mismatching credentials provided within plugin settings, kindly update the same credentials within the plugin settings that was provided by Google. You can also re-check the credentials provided by Google from here: [https://console.developers.google.com/apis/credentials](https://console.developers.google.com/apis/credentials)

2\. In order to resolve the issue with the website opens up in both http and https, you need to ensure that your website should only open up in https.   
You can refer to the below link to try and force your website on https: [https://help.dreamhost.com/hc/en-us/articles/115003505112-How-to-force-your-site-to-redirect-to-https-SSL](https://help.dreamhost.com/hc/en-us/articles/115003505112-How-to-force-your-site-to-redirect-to-https-SSL-). Alternatively, you can also check the same with your hosting provider team.

* * *

## Warning message: “The app isn’t verified”

**The reason for the warning message “** _**The app isn’t verified**_**” is because of the privacy policy changes made by Google.**

* * *

### Solution for Google API Authentication failed error

In order to resolve it, click on “**Advanced** ” and then click on “**Go to** ” link, as shown below.

However, our plugin does not look or store any personal data and providing access to your Google Calendar via our plugin is safe and secure.

* * *

If you face any issues or have any queries regarding setting up Google Calendar Sync or the plugin, do **[contact our support](https://www.pluginhive.com/support/)**.

[ Previous  Customize Calendar Designs with Bookings and Appointments for WooCommerce  ](https://www.pluginhive.com/knowledge-base/customize-booking-calendar-on-woocommerce/)

[ Next  Book Online Diving Adventure with Additional Services using Bookings And Appointments for WooCommerce  ](https://www.pluginhive.com/knowledge-base/online-diving-adventure-additional-services-using-woocommerce-bookings/)
