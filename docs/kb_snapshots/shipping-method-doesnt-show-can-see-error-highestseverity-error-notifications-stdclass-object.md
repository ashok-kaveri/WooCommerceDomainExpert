# Debug Error: [HighestSeverity] => ERROR

**Source:** https://www.pluginhive.com/knowledge-base/shipping-method-doesnt-show-can-see-error-highestseverity-error-notifications-stdclass-object/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Debug Error: [HighestSeverity] => ERROR

Getting errors when using the WooCommerce FedEx Shipping Plugin? This guide will help you bring the FedEx shipping method and show them on your WooCommerce store. So read along to know more.

**Customer** :

I am trying to setup your FedEx plugin on my site, the shipping method doesn’t show up. I have tried enabling the debug mode and all I can see as an error is in the FedEx response:

> [HighestSeverity] => ERROR  
> [Notifications] => stdClass Object  
> (  
> [Severity] => ERROR  
> [Source] => prof  
> [Code] => 1000  
> [Message] => Authentication Failed

Could this be the reason why it doesn’t show?

* * *

**PluginHive Support** :

This is the exact reason shipping rates are not getting displayed on your cart page.

You are getting an **Authentication error**. This error comes when you have given the test or live credentials incorrectly. Please check the credentials at your end.

Kindly note that FedEx has different credentials for test and live environments.

_Getting live account details:_

  1. To get live access, please contact FedEx support.
  2. Enter the live account details in the plugin settings.
  3. Enable production key checkbox in the plugin settings.

Once you get the live account details, you need additional authorization to print labels. To do this:

  * Contact FedEx with the sample label generated using test account details.
  * Please follow [certification guidelines](https://www.fedex.com/us/developer/downloads/pdf/CertificationGuidelines.pdf) to get advanced services for printing the labels.

[ Previous  It always seems to overlook the FedEx Ground and not include it as an option at checkout  ](https://www.pluginhive.com/knowledge-base/always-seems-overlook-fedex-ground-not-include-option-checkout/)

[ Next  When I try to create a label for my orders, error message I get: FedEx Create Shipment Error: Severity: ERROR  ](https://www.pluginhive.com/knowledge-base/try-create-label-orders-error-message-get-fedex-create-shipment-error-severity-error/)
