# Bookings And Appointments for WooCommerce plugin FAQs

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-bookings-and-appointments-plugin-faqs/
**Platform:** WooCommerce (WordPress)
**Plugin:** bookings
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Bookings And Appointments for WooCommerce plugin FAQs

* * *

This article provides answers to frequently asked questions related to the Bookings and Appointments for WooCommerce plugin. If you are new to the plugin and need help in setting it up, please refer to [Getting Started with Bookings and Appointments for WooCommerce Plugin](https://www.pluginhive.com/knowledge-base/setup-guide-woocommerce-bookings-and-appointments-plugin/). For further questions on set-up and possibilities with the plugin, please go through the below list.

* * *

## WooCommerce Bookings Calendar Appearance and location

  1. Can I customize the booking calendar design?
  2. Can I change the calendar location/position on the Product Page? 
  3. Can I place the calendar on a custom page?
  4. I am placing the booking calendar on a custom page using the product shortcode – [[ph_bookings_calendar id=”3131″]]. I don’t need the product image or image placeholder and want the calendar to be aligned on the left.
  5. How do I change the date and time format of the Booking Calendar?
  6. How do I display the end time for every time slot in the calendar – For Eg: 10 am to 11.00 am instead of displaying only start as 10.00 am
  7. How can I allow the user to choose a month directly rather than navigating by clicking the arrows? 
  8. How can I change the “Book Now” button text 
  9. How can I hide the appointment end time in the booking summary, cart and checkout pages, and the order details?
  10. I use the Elementor Theme. My Calendar’s “Book now” button appears on the right side. How do I correct it to display below the calendar?

* * *

## Product Type

  1. Can this plugin be used with WooCommerce Variable Products?
  2. Can I use the calendar for bookings without associating it with a WooCommerce product?

* * *

## Cart and Check-Out

  1. I want my users to directly go to Check Out after clicking on “Book Now”. Is it possible to skip the “View Cart” message and go to checkout directly?
  2. I want to change the message – “Booking Done, View Cart for payment”. Is it possible?
  3. How long is the time slot blocked for other users when the booking is in the cart?
  4. After placing bookings in the cart, the booking slot is not unblocked even after 15 minutes?
  5. Can I change the time limit for which the booking is blocked while it is in the cart? How can I do it?

* * *

## Payment

  1. How are cancellations refunded?
  2. Can I charge a deposit amount for booking rather than charging the full amount?
  3. Can I apply discounts and special prices for the bookings?

* * *

## Google Calendar Sync

  1. Can external or direct appointments on my google calendar be synced by the plugin?
  2. I am getting “Error 403: access_denied” while authenticating the credentials for Google Calendar Sync.

* * *

## Booking Calendar Appearance and location

* * *

### Can I customize the booking calendar design?

Yes, you can customize the calendar design and its colors to suit your website.

* * *

* * *

**_Reference_**  
  
For more details please refer – [ **Customize Booking Calendar Appearance** ](https://www.pluginhive.com/knowledge-base/setup-guide-woocommerce-bookings-and-appointments-plugin/#BookingCalendarAppearance)   
  

  
If you need further customization apart from what’s available within the plugin settings, you can do it with the help of a **CSS expert**. However, please note, these design changes will not be supported by our team and you will need to ensure the changes are not lost after you update the plugin.

* * *

### Can I change the calendar location/position on the Product Page?

The plugin places the calendar in a default location(product summary) of the WooCommerce Product. The exact location depends on your Theme.  
If you need to change the location of the calendar on the product page you could do it with the help of your **developer or CSS expert**. Please note that these design changes will not be supported by our team and you will need to ensure the changes are not lost after you update the plugin.

* * *

### Can I place the Calendar on a custom page?

Yes. If you need to add the calendar on a custom page, you will need to use the shortcode to get the bookable product on the desired custom page. Please note that here “3131” is the bookable product’s ID and this will get the entire bookable product calendar within the custom page including the product image placeholder. The shortcode is listed below.
    
    
    [ph_bookings_calendar id="3131"]

* * *

**_Note:_**   
  
Please ensure that only one shortcode is added. Multiple shortcodes are not supported.   
  

* * *

* * *

If you need to hide the product image, please refer to the next question.

* * *

### I am placing the booking calendar on a custom page using the product shortcode: `[ph_bookings_calendar id="3131"]`I don’t need the product image or image placeholder and want the calendar to be aligned on the left. How can I do that?

Go to Appearance > Click Additional CSS.   
Add this CSS code in the text area:

* * *
    
    
    .woocommerce-product-gallery {
    display:none;
     }
    Inorder to align the short description to the left and not the right, add this css code:
    .woocommerce #content div.product div.summary, .woocommerce div.product div.summary, .woocommerce-page #content div.product div.summary, .woocommerce-page div.product div.summary {
    float: left;
    }

* * *

### How do I change the date and time format of the Booking Calendar? 

You can easily change the date and time format of the Booking calendar.

* * *

* * *

**_Reference_**  
For more details please refer Section 1.4 – [ **Customize Booking Calendar Appearance** ](https://www.pluginhive.com/knowledge-base/setup-guide-woocommerce-bookings-and-appointments-plugin/#BookingCalendarAppearance)   

* * *

### How do I display the end time for every time slot in the calendar? For Eg: 10 am to 11.00 am instead of displaying only the start time as 10.00 am 

It is possible to display an end time for every time slot in the calendar.

**_Reference_**  
For more details please refer Section 1.3 – [ **Customize Booking Calendar Appearance** ](https://www.pluginhive.com/knowledge-base/setup-guide-woocommerce-bookings-and-appointments-plugin/#BookingCalendarAppearance)   

* * *

### How can I allow the user to choose a month directly rather than navigating by clicking the arrows?

It is possible to allow the user to choose a month directly.

**_Reference_**  
For more details please refer Section 1.3 – [ **Customize Booking Calendar Appearance** ](https://www.pluginhive.com/knowledge-base/setup-guide-woocommerce-bookings-and-appointments-plugin/#BookingCalendarAppearance)   

* * *

### How can I change the “Book Now” button text?

You can easily change the “Book Now” button text?

**_Reference_**  
For more details please refer Section 1.2 – [ **Customize Booking Calendar Appearance** ](https://www.pluginhive.com/knowledge-base/setup-guide-woocommerce-bookings-and-appointments-plugin/#BookingCalendarAppearance)   

* * *

### How can I hide the booking/appointment end date/time in the booking summary, cart and checkout pages, and order details? 

1\. You can easily hide the end date and time from the Booking summary box of the calendar.

**_Reference_**  
For more details please refer Point 4 in Section 1.3 – [ **Customize Booking Calendar Appearance** ](https://www.pluginhive.com/knowledge-base/setup-guide-woocommerce-bookings-and-appointments-plugin/#BookingCalendarAppearance)   

  
2\. For hiding the Booking End Date/Time from the cart, checkout, and the emails, kindly visit the plugin settings -> Calendar Display -> Calendar Display Settings and disable the **Include End Date and Time in Cart, Order Details and Emails** option, as shown in the image below.

* * *

* * *

### I use the Elementor Theme. My Calendar’s “Book now” button appears on the right side. How can I correct it to display below the calendar?

In order to place the button under the calendar, kindly add the following code snippet to the style.css file by navigating to the WP Dashboard -> Appearance -> Theme Editor -> Theme Files -> style.css file :   
Note: Please clear the cache before testing the change.

* * *
    
    
    .woocommerce div.product.elementor form.cart:not(.grouped_form):not(.variations_form)
    {
       display: block !important;
    }

* * *

## Product Type

* * *

### Can this plugin be used with WooCommerce Variable Products?

Bookings and Appointments for WooCommerce plugin converts a product into a “bookable product” and “Bookable product” is a product type just like “Variation product”. So you will not be able to use these together. However, all the variations that are possible with the “Variable product” type can be achieved by the Bookable product type using the resources, assets, and addons features in the plugin.

Please contact us with your business case at – <https://www.pluginhive.com/support/> if you would like to clarify.

* * *

### Can I use the booking calendar for bookings without associating it with the WooCommerce product?

No. Bookings and Appointments for WooCommerce plugin is meant to provide a booking facility for WooCommerce products/services and therefore it is tightly associated with WooCommerce product attributes.

However, If you need to place the calendar on a custom page, you can use the shortcode to get the bookable product on the desired custom page.

**Note** that this will get the entire bookable product into the custom page including the product image placeholder. Here is the shortcode:
    
    
    [ ph_bookings_calendar id="3131" ]

* * *

(here 3130 is your product id and you can get the product id of a particular product from the Product URL).

* * *

## Cart and Check-Out

* * *

### Can I have my users go to the checkout page directly after clicking on “Book Now”? Is it possible to skip the “View Cart” message?

Yes, the default flow of the cart and then checkout can be changed via WooCommerce settings. You can skip the cart and have the user go to check out directly by making the below changes to your WooCommerce settings.

* * *

* * *

1\. WooCommerce -> Settings -> Products -> Add to cart behaviour -> Check the ->Redirect to Cart Page 

* * *

* * *

2\. WooCommerce -> Settings ->Advanced -> Change Cart Page -> Check Out 

* * *

* * *

### I want to customize the message – “Booking Done, View Cart for payment”.

Yes, you can customize the string -> “Booking Done. Please check cart for payment” by adding the following code snippet at the end of the functions.php file by navigating to the Appearance -> Theme Editor -> Theme Files -> functions.php

* * *
    
    
    add_filter('ph_booking_add_to_cart_message_html', 'change_message', 10, 2);
    function change_message($message, $products)
    {
    	$message = '<a href="'.wc_get_page_permalink( 'cart' ).'" class="button wc-forward">'.__('View cart','bookings-and-appointments-for-woocommerce').'</a> '.__('Change Text Here. Please check cart for payment.','bookings-and-appointments-for-woocommerce');
    
    return $message;
    } 

* * *

### How long is the time slot blocked for other users when the booking is in the cart?

Bookings and Appointments for WooCommerce plugin blocks a slot for 15 minutes as soon as a booking is placed in the cart to avoid any double-booking. So, in a scenario where there is only one slot left and a customer places a booking in the cart, no other customers will be able to block that slot for the next 15 minutes.

This way, the plugin avoids double-booking and the customer will be able to successfully complete the checkout process and complete the booking. If a customer leaves the booking in the cart without completing the checkout process, the plugin will automatically add the slot back to the booking product after 15 minutes in order to allow other customers to book for that particular slot once again.

* * *

### After placing bookings in the cart, the booking slot is not unblocked even after 15 minutes?

There is a cron job running which searches and unblocks if there exist any frozen blocks after 15 minutes are over. However, if this cron is not running on your site, kindly try deactivating and activating the Bookings Plugin.

**_Note_**  
To check if the cron job is running as expected, kindly ensure you have the **Free WP Crontrol Plugin** installed and activated in your WP Site.   

* * *

### Can I change the time limit for which the booking is blocked while it is in the cart? How can I do it?

Yes. You would be able to change the time from 15 mins to a shorter or longer time. However, do not change it to zero as it may cause double bookings. To change the blocking time you can follow the below steps:   
  
Add the below code snippet in the functions.php file of your theme or use an external plugin that helps to add code snippets.

* * *
    
    
    add_filter('ph_schedule_unfreez_time_in_minutes_for_bookings_in_cart', 'ph_schedule_unfreez_time_in_minutes_for_bookings_in_cart_function', 10, 2);
    function ph_schedule_unfreez_time_in_minutes_for_bookings_in_cart_function($freezing_time, $product_id)
    {
    // default is 15 minutes, changing it to 5 minutes
    $freezing_time = 5;
    return $freezing_time;
    }

* * *

## Payment

* * *

### How are cancellations refunded?

Booking Cancellations refund is not automatic. You need to use the default WooCommerce Order Refund feature. 

* * *

### Can I charge a deposit amount for booking rather than charging the full amount?

Yes – You will need the [PH WooCommerce Deposits Plugin](https://www.pluginhive.com/product/woocommerce-deposits/)

** _Reference_**  
For more details please refer – [ **Accept Deposits for your bookings** ](https://www.pluginhive.com/knowledge-base/setup-guide-woocommerce-bookings-and-appointments-plugin/#deposit)   

* * *

### Can I apply discounts and special prices for the bookings?

Yes Of course. You can apply various types of discounts and special prices

** _Reference_**  
For more details please refer – [ **Booking Cost** ](https://www.pluginhive.com/knowledge-base/setup-guide-woocommerce-bookings-and-appointments-plugin/#cost)   

* * *

## Google Calendar Sync

* * *

### 1\. Are external or direct appointments on my google calendar synced by the plugin?

No. The appointments created on the bookable products on your WooCommerce site sync to your Google calendar. Also, any appointment created on your google calendar **by giving the product id** of these bookable products syncs back to the online site. However, the external appointments do not sync as they are not in a format that the plugin recognizes.

* * *

### 2\. I am getting “Error 403: access_denied” while authenticating the credentials for Google Calendar Sync

If you are getting the “**Error 403: access_denied – The developer hasn’t given you access to this app. It’s currently being tested and it hasn’t been verified by Google. If you think you should have access, contact the developer** ” while authenticating the credentials for Google Calendar Sync, you need to add your store email ID (the email ID you are using for Google Calendar Sync) as a Test User under the OAuth Consent Screen option as shown in the image below.

* * *

**Reference article** : <https://stackoverflow.com/questions/65184355/error-403-access-denied-from-google-authentication-web-api-despite-google-acc>

* * *

### 3\. I am getting “Error:400” while authenticating the credentials for Google Calendar Sync

The possible reason for the error “ _The redirect URI in the request does not match the ones authorized for the OAuth client_ ” is because an incorrect “ _Authorised redirect URI_ ” was provided at the time of setting up the Google Calendar sync.

-> In order to resolve the issue, copy the redirect URI provided in the error message and update it under the “Authorised redirect URIs” in the link provided within the error message.

* * *

### 4\. We are regenerating refresh tokens after some time. Could you please let us know whether you are using the developer’s test account credentials or service account credentials?

If you are using the developer’s test account credentials, then there is a limit for generating refresh tokens.

Some of the reasons for expiring refresh tokens are:

  * The user has revoked your app’s access.
  * The refresh token has not been used for six months
  * The user changed passwords and the refresh token contains Gmail scopes.
  * The user account has exceeded the maximum number of granted (live) refresh tokens: There is currently a limit of 50 refresh tokens per user account per client. If the limit is reached, creating a new refresh token automatically invalidates the oldest refresh token without warning. This limit does not apply to service accounts.
  * There is also a larger limit on the total number of refresh tokens a user account or service account can have across all clients. Most normal users won’t exceed this limit but a developer’s test account might.

You can also refer to this document: <https://developers.google.com/identity/protocols/oauth2#expiration>

Also, documentation for creating a service account: <https://developers.google.com/identity/protocols/oauth2/service-account>  

* * *

### 5\. What to do next if your Google API authentication fails?

You will require to force your site to redirect to HTTPS if your Google API authentication fails. Refer to the article below: <https://help.dreamhost.com/hc/en-us/articles/115003505112-How-to-force-your-site-to-redirect-to-https-SSL->?  

* * *

6\. What to do if you are unable to see the Bookings/events under All Bookings section that are placed on your Google calendar (2-way sync)?

Please navigate to Google calendar -> Settings -> Bin as shown below

Check if there are any events under Trash. If so, select all events and delete them. This should help to resolve the issue

[ Previous  WooCommerce Bookings Cancellation  ](https://www.pluginhive.com/knowledge-base/woocommerce-bookings-cancellation/)

[ Next  Export WooCommerce Bookings and Appointments to a CSV File  ](https://www.pluginhive.com/knowledge-base/export-woocommerce-bookings-appointments-to-csv/)
