# Debug Error: FedEx ADDRESS VALIDATION RESPONSE

**Source:** https://www.pluginhive.com/knowledge-base/plugin-giving-error-debugged-fedex-address-validation-response-reveal/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Debug Error: FedEx ADDRESS VALIDATION RESPONSE

Here’s a small guide to help you solve the debug error when using the WooCommerce Shipping Plugin for FedEx with Print Label. With this, you can solve the [FedEx Address Validation](https://www.pluginhive.com/how-to-use-fedex-address-validation-on-your-online-store/) Response. Read along to know more.

**Customer** :

I am using the premium version of **WooCommerce Shipping Plugin for FedEx with Print Label**. When I enable _Debug Mode,_ it throws me the following error:

> FedEx ADDRESS VALIDATION RESPONSE: Reveal
> 
> stdClass Object  
> (  
> [HighestSeverity] => ERROR  
> [Notifications] => stdClass Object  
> (  
> [Severity] => ERROR  
> [Source] => prof  
> [Code] => 1000  
> [Message] => Authentication Failed  
> )
> 
> [TransactionDetail] => stdClass Object  
> (  
> [CustomerTransactionId] => *** Address Validation Request v2 from WooCommerce ***  
> )[Version] => stdClass Object  
> (  
> [ServiceId] => aval  
> [Major] => 2  
> [Intermediate] => 0  
> [Minor] => 0  
> )
> 
> )

Please help me in this issue.

* * *

**PluginHive Support** :

Address validation is an advance FedEx service that requires the authorization from FedEx. If you don’t have permission from FedEx, the response will show authentication failed for the address validation.

You need to contact FedEx support, they will help you through the entire process. Kindly check the following link for FedEx guidelines for advance services:

https://www.fedex.com/us/developer/downloads/pdf/CertificationGuidelines2016.pdf

[ Previous  WooCommerce FedEx Shipping Rates in Multiple Currencies  ](https://www.pluginhive.com/knowledge-base/provide-woocommerce-fedex-shipping-rates-in-multiple-currencies/)

[ Next  FedEx Hold At Location at WooCommerce Checkout  ](https://www.pluginhive.com/knowledge-base/fedex-hold-at-location-at-woocommerce-checkout/)
