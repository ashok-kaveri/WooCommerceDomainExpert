# WooCommerce Shipping for FedEx – Change Customs Duty Payer based on the Destination country

**Source:** https://www.pluginhive.com/knowledge-base/change-customs-duty-payer-based-destination-country/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce Shipping for FedEx – Change Customs Duty Payer based on the Destination country

In this article, we will tell you how to change the customs duty payer based on the destination country when using the [**WooCommerce Shipping Plugin for FedEx with Print Label**](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/).

Marijn has set up a prolific eCommerce store. He has all the products set up on the WooCommerce platform. As a shipping solution, he chooses FedEx. Now, Marijn wants predictability in his expenditure. He doesn’t like surprises when it comes to rates.

> _But, to his dismay, it is impossible to predict the shipping rates for every country he is shipping to. It seems like the rates change drastically on a regular basis. And that is adding some confusion to his regular business._

## Customs Duty Fluctuation in Some Countries is the Root Cause of the Problem

Now he could finally figure out that this issue is being caused by the fact that in some countries, the customs duty rates fluctuate. So, as a solution to bring some certainty to his business, he would somehow have to prevent himself from paying the customs duties of those countries and instead make the receiver pay for the customs duties.

As an example, he can choose to pay the customs duties for the U.S. Shipments, because the duties in the US are non-fluctuating. Thus he can estimate the price and prevent his customers from having to pay extra while the shipment is delivered.

> _In some countries like Israel, the customs duty rates fluctuate on a daily basis. Within a day it can vacillate between 6% to 20%. In this case, he would want his customer to pay directly to FedEx as they won’t be willing to makeup for the rate differences later. And it would end up creating further inconvenience for his customers._

## WooCommerce Shipping Solution for FedEx by PluginHive allows changing the Customs Duty Payee

Looking at the [**WooCommerce Shipping plugin** **for FedEx**](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/), this seems to be a one-time decision made in the plugin’s settings page itself. Fortunately, PluginHive could find a suitable solution for him by providing a code snippet.

The code snippet below can override the decision made on the settings page. It would set up different options based on countries. For some countries, it would make the sender pay for the customs duties, and for others, it would ask the recipient to pay customs duties.
    
    
    add_filter( 'xa_shipping_duties_payer', 'xa_alter_shipping_duties_payer', 10, 2 );
    
    function xa_alter_shipping_duties_payer($customs_duties_payer, $package){
    
         //Config this array with Country code and payer.
         $payor_for_country = array(
             'GB' => 'RECIPIENT', 
             'CA' => 'SENDER', 
         );
    
         if( array_key_exists( $package['destination']['country'], $payor_for_country) ){
             return $payor_for_country[ $package['destination']['country'] ];
         }
    
         return $customs_duties_payer;
     }

In the above snippet, for ‘GB’ (United Kingdom), the customer would pay the customs duty and for ‘CA’ (Canada), the shop owner would be paying the customs duty. And that’s how the big headache of setting up different custom duty payers for different countries got resolved.

Check out the [**WooCommerce Shipping Plugin for FedEx**](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/) to find out great solutions like these. If you need help setting up FedEx shipping on your WooCommerce store then feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**.

[ Previous  Code snippet to display the Shipping phone number on the WooCommerce Shipping label instead of the Billing phone number  ](https://www.pluginhive.com/knowledge-base/code-snippet-display-shipping-phone-number-label-place-billing-phone-number/)

[ Next  How to Add Custom Text in Delivery Estimates Format using PluginHive Plugin for FedEx Shipping?  ](https://www.pluginhive.com/knowledge-base/add-custom-text-delivery-estimates-format-fedex-shipping-plugin/)
