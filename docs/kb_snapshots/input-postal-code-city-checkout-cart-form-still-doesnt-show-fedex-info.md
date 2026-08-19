# I have input the Postal code and City into the checkout cart form and it still doesn’t show the FedEx info

**Source:** https://www.pluginhive.com/knowledge-base/input-postal-code-city-checkout-cart-form-still-doesnt-show-fedex-info/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# I have input the Postal code and City into the checkout cart form and it still doesn’t show the FedEx info

You have entered the correct postcode and city info but you’re not able to see the FedEx shipping rates on the Cart/Checkout page. Don’t worry, this guide will help you solve the issue using the **[WooCommerce Shipping Plugin for FedEx](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)**.

**Customer:**

Array  
(  
[WebAuthenticationDetail] => Array  
(  
[UserCredential] => Array  
(  
[Key] => ###############  
[Password] => ######################  
)

)

[ClientDetail] => Array  
(  
[AccountNumber] => ###########  
[MeterNumber] => ############  
)

[TransactionDetail] => Array  
(  
[CustomerTransactionId] => *** WooCommerce Rate Request ***  
)

[Version] => Array  
(  
[ServiceId] => crs  
[Major] => 16  
[Intermediate] => 0  
[Minor] => 0  
)

[RequestedShipment] => Array  
(  
[PreferredCurrency] => USD  
[DropoffType] => REGULAR_PICKUP  
[ShipTimestamp] => 2016-03-31T00:00:00+00:00  
[PackagingType] => FEDEX_SMALL_BOX  
[Shipper] => Array  
(  
[Address] => Array  
(  
[PostalCode] => 97023  
[CountryCode] => US  
)

)

[ShippingChargesPayment] => Array  
(  
[PaymentType] => SENDER  
[Payor] => Array  
(  
[ResponsibleParty] => Array  
(  
[AccountNumber] => ######  
[CountryCode] => US  
)

)

)

[RateRequestTypes] => NONE  
[Recipient] => Array  
(  
[Address] => Array  
(  
[Residential] =>  
[PostalCode] =>  
[City] =>  
[StateOrProvinceCode] => OR  
[CountryCode] => US  
)

)

[RequestedPackageLineItems] => Array  
(  
[0] => Array  
(  
[SequenceNumber] => 1  
[GroupNumber] => 1  
[GroupPackageCount] => 1  
[Weight] => Array  
(  
[Value] => 0.33  
[Units] => LB  
)

[Dimensions] => Array  
(  
[Length] => 11.25  
[Width] => 8.75  
[Height] => 2.63  
[Units] => IN  
)

[InsuredValue] => Array  
(  
[Amount] => 10  
[Currency] => USD  
)

)

)

[SpecialServicesRequested] => Array  
(  
[SpecialServiceTypes] => FEDEX_ONE_RATE  
)

[PackageCount] => 1  
[TotalInsuredValue] => Array  
(  
[Amount] => 10  
[Currency] => USD  
)

)

)

stdClass Object  
(  
[HighestSeverity] => ERROR  
[Notifications] => stdClass Object  
(  
[Severity] => ERROR  
[Source] => crs  
[Code] => 521  
[Message] => Destination postal code missing or invalid.  
[LocalizedMessage] => Destination postal code missing or invalid.  
)

[TransactionDetail] => stdClass Object  
(  
[CustomerTransactionId] => *** WooCommerce Rate Request ***  
)

[Version] => stdClass Object  
(  
[ServiceId] => crs  
[Major] => 16  
[Intermediate] => 0  
[Minor] => 0  
)

)

* * *

**Support:**

From the request information, we can see that you have not provided the recipient’s Postal code and City values as shown below.

[RateRequestTypes] => NONE  
[Recipient] => Array  
(  
[Address] => Array  
(  
[Residential] =>  
**[PostalCode] = >  
[City] =>  
**[StateOrProvinceCode] => OR  
[CountryCode] => US  
)

Once you provide the same, you will be able to see the rates.

* * *

**Customer:**

I have input the Postal Code and City into the cart checkout form, and it still doesn’t show the FedEx info. Is there another location in the setup where I need to do this? Shouldn’t it at least show the one-rate boxes as the USPS does?

* * *

**Support:**

Kindly send us the **response** information after you have put the Postal Code and City on the Checkout page. Also, a snapshot of the **plugin settings page** would really help. We will check and let you know.

From the analysis of the error, we can make out that no rates will be fetched if the error persists. Once the error is resolved, you will get the rates displayed.

* * *

**Support:**

As mentioned before, it is difficult for us to analyze the issue if you do not provide us with the response information after inputting the postal code and City on the checkout page. Kindly provide us with the same.

Or, if it is very urgent, then we request you to provide us your admin credentials(with website link) so that we can quickly analyze them and let you know.

* * *

**Support:**

We checked the issue at your end. We got the real-time rates on the checkout page. However, your website has javascript issues.

The checkout page also does not refresh upon adding the zip code. We request you to get that corrected.

Solution: You can try reinstalling the theme or try some themes compatible with woocommerce like Store Front. You can also try in a different browser.

* * *

**Customer:**

That did not answer any of my questions. The real-time rate I got was the one I had before with the USPS plug-in. It works just fine. Is there a possible conflict between the FedEx one and the theme?

* * *

**Support:**

On giving postcode, we got the following FedEx rates as expected.

It also shows that there is javascript error on your website. This comes up either when the theme is not advanced enough to handle the plugins or there is a third party plugin interfering.

To check this problem, we recommend you to try installing basic woocommerce supported theme like Storefront. If the error persists then there may be a third party plugin causing this issue.

**The theme or third party plugin is preventing the rates from getting displayed.**

Hope that helped!

* * *

**Customer:**

Found the Javascript conflict, but it had nothing to do with the theme. It was a gallery plug-in that issues with you Fedex. The Fedex overnight works, but the ground and flat rates don’t show up. Any thoughts?

* * *

**Support:**

Currently, FedEx test servers are down as shown in the attached screenshot. Hence we are not getting any rates.

Once the server is up and running, we request you to enable all the services in FedEx from the settings page(not just FedEx_Ground and FedEx_Home_Delivery) and then see from the front end, which all services are coming up for a specific postcode.

To compare the services with the services returned from FedEx, kindly go to [FedEx Rate Calculator](https://www.fedex.com/ratefinder/home) and check the services returned.

If the services returned don’t match with those returned using our plugin, kindly contact us. We will help you.

For Flat rates, kindly go to [FedEx One Rate](https://www.fedex.com/us/onerate/) and provide us the rate quoted with the same address you are providing in the order.

Hope that’s clear!

* * *

**Customer:**

I enabled all the different FedEx options.

The Flate rates were for the small, medium and large boxes. They very on distance. Here are the boxes we have selected in the plug-in:

FedEx® Small Box  
10-7?8″ x 1-1?2″ x 12-3?8″,  
8-3?4″ x 2-5?8″ x 11-1?4″

$8.50

$9.75

$10.75

FedEx® Medium Box  
11-1?2″ x 2-3?8″ x 13-1?4″,  
8-3?4″ x 4-3?8″ x 11-1?4″

$10.50

$12.50

$14.00

FedEx® Large Box  
12-3?8 x 3″ x 17-1?2″  
8-3?4″ x 7-3?4″ x 11-1?4″

$16.25

$17.75

$18.75

* * *

**Support:**

Please upgrade the plugin to latest (1.7.5) and let us know if the issue persists.

* * *

**Customer:**

It doesn’t give me the option to upgrade the plugin. When I read the read me file it say the version is 2.6.8. The WooCommerce Shipping plugin for FedEx problem is still there. The ground and flat rates don’t show up.

* * *

**Support:**

The latest version of our plugin is 1.7.5.

We request you to check the version you are using by going to Plugins > Installed plugins

If it is less than 1.7.5 then, kindly login to PluginHive.com > My accounts and then install the plugin.

Let us know if you need any help!

* * *

**Customer:**

I went in and installed the latest version (Version 1.7.9) and the same problem is still there. The ground and flat rates don’t show up.

* * *

**Support:**

This is due to FedEx One being checked on the settings page which disables support for a number of services. Please uncheck FedEx One option and try again.

* * *

**Customer:**

Still nothing. The ground and FedEx flat rates still don’t show up.

* * *

**Support:**

Currently, we request FedEx explicitly for One Rates when One Rate option is enabled. Moreover, while requesting One X rate, your package qualifies for FEDEX_SMALL_BOX, which doesn’t support Ground rates. We are in communication with FedEx Tech support for a possible solution for this issue. We will keep you updated.

* * *

**Customer:**

I’m a bit confused by your statement. One rate is enabled. Are you saying that ground rate and flat (one)rate won’t work together? If that is the case I would prefer getting the flat rate working.

* * *

**Support:**

We are checking to make both one rate and ground rates work together. We recommend enabling FedEx One rate checkbox in settings so that Flat Rate will work seamlessly.

* * *

**Customer:**

As I said before. The FedEx One Rate checkbox is enabled in the setting. It just doesn’t work.

* * *

**Support:**

We have enabled one rate-eligible FedEx service ‘[FedEx Express Saver](https://www.pluginhive.com/fedex-express-saver-guide-for-woocommerce-users/)‘.  
Please look for a comparison for the Flat/One Rate service ‘FedEx Express Saver’ ($10.75) from FedEx One website and your website. We have set the source zip as 97023 (Estacada) and the destination as 90002 (CA).

Please use the site [FedEx One Rate](https://www.fedex.com/us/onerate/) and click on ‘Get Rate’ for getting the expected one rate amount.

* * *

**Customer:**

Great!! I see what you’re talking about now. The name fooled me on that. Any word on getting the ground shipping as well?

* * *

**Support:**

We checked that for you.

The Ground rate and one rate cannot work together. We confirm this with FedEx and get the following response:

**Discussion Thread**  
---  
**Response Via Email (Brandon Svatek)**|  01:36 PM  
Hello,Thank you for using FedEx Online Support. In answer to your question, this is correct. Due to the requirements for FedExOne Rate pricing, Ground will not be included in the results (or vice versa- ONE_RATE will not be included in a request for Ground shipping).Thank you for choosing FedEx.  
Sincerely,  
Brandon Svatek  
FedEx Technical Support  
  
* * *

[ Previous  Print Order number on the WooCommerce Shipping Label  ](https://www.pluginhive.com/knowledge-base/way-print-order-generated-woocommerce-printed-shipping-label/)

[ Next  Configure FedEx International Shipping with WooCommerce  ](https://www.pluginhive.com/knowledge-base/international-pricing-not-showing-website/)
