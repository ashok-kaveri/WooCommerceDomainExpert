# Decoding Debug Data of WooCommerce UPS Plugin

**Source:** https://www.pluginhive.com/knowledge-base/decoding-debug-data-woocommerce-ups-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Decoding Debug Data of WooCommerce UPS Plugin

Debug data has information that is helpful to identify any advanced code-level issues with the plugin. UPS debug data provide useful insights into the functioning of the [**UPS Plugin for WooCommerce**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) in the following scenarios:

  1. Some/ All UPS services are not showing up on the cart page.
  2. Rates returned by the UPS plugin are not matching with the UPS calculator rates.

* * *

## **What information can be obtained from the WooCommerce UPS Plugin debug data?**

1\. UPS Account related information.

* * *

2\. Complete Origin Address.

* * *

3\. Complete Destination Address.  

* * *

4\. Requested and received services. The service code is sent through the request.  

* * *

5\. Availability of the Shipping services.  

* * *

6\. Actual returned rates and negotiated rates (if Negotiated Rate is enabled in the plugin settings).  

* * *

7\. Insurance rate, if insurance is enabled.

* * *

8\. Weights and Dimensions of the Package (Dimensions would be passed in the request only when box packing is selected in the settings page).

* * *

9\. Parcel Packing details.

In the above case, the Code “02” corresponds to the custom package described by the user.

* * *

10\. If Box packing is enabled, debug data would reveal which box has been selected.

* * *

## **What are errors easily revealed by the debug data?**

1\. Missing weights.

* * *

If the above error is showing up, you are required to check whether every product in the cart has weight defined (in the respective product settings).

* * *

2\. Invalid license number.

* * *

If the above error shows up, the “UPS Access Key” you have provided in the UPS settings page is wrong.

* * *

3\. Missing dimensions in case of box packing.

In the above case, you need to specify the dimensions for box packing.

* * *

4\. Wrong postal code for either origin or destination.

* * *

5\. Missing address fields.

* * *

6\. A service is not available for a particular origin-destination combination.

* * *

7\. Server-related issues. In such cases either the response from UPS is empty or the request is not sent.

8\. Authorization error. Invalid Service code.

* * *

In case of the above error, it is advisable to recheck the UPS Account related information entered in the settings page.

* * *

9\. Unpacked items. This happens when none of the defined boxes can fit the selected products.

* * *

10\. Reasons for rates mismatch in the WooCommerce UPS Plugin. There can be various reasons of rates not matching with the UPS rate calculator. These reasons are reflected well in the debug data.

  * If “Pack Items Individually” is selected, rates would be much higher than the UPS calculator.
  * “Weight-Based” packing too would give different rates based on the packaging type selected.
  * Different combinations of “Pickup Type ” and “Customer Classification” would give different rates. So, make sure that you select the right combination which is mentioned below.

* * *

## **Components of Debug Data**

The entire UPS debug data can be broadly classified into two parts:

  1. Request
  2. Response

Depending on our purpose of debugging, Request and Response provide different information. Let’s look into both.

### **Request**

UPS Request has the following information:

User’s **UPS Account related information** such as **Access License Number, User Id, and Password.**  
This part of the request is meant to determine the allowed UPS services to the user.

* * *

Next part contains **the actual request** made to the API **regarding rates and services**.

The separate request is sent for each service.

* * *

Along with the specific data from each service, the debug request will have information regarding the following parameters as well:

**Pickup Type:** To obtain correct rates, the Customer Classification should be set to ‘Daily Rates’, if the pickup type is ‘Daily Pickup’. If the pickup type is anything other than ‘Daily Pickup’, the Customer Classification should be set to ‘Retail Rates’.  
**Customer Classification:** If you are shipping from the United States, you can use the Customer Classification Code of UPS to retrieve rates. The available options in the drop-down are as follows:

  * Rates Associated with Shipper Number
  * Daily Rates
  * Retail Rates
  * Standard List Rates

* * *

**Shipment:** Shipment contains the **Shipper number** which is basically the UPS Account number, origin, and destination address.

**Service code:** This refers to the service requested.

**Package type:** This part of the request message would say whether “UPS packaging” is used or “My Packaging” is used. Code “02” is used to denote “My Packaging”. Then come the dimensions and weight of the package.

**Residential Address Indicator:** This would be displayed in the Request if the “**Residential** ” option is checked in the settings page.

* * *

**Insured Value:** The total insured value is shown in the request if “**Insurance** ” is enabled on the plugin settings.

**Negotiated Rates Indicator:** This tag comes in the request, if “**Negotiated Rates** ” is checked in the settings page.

* * *

### **Response**

UPS Response has the following information:

  1. **Response Status Code** and **Response Status Description** –**** The value of Response Status Code is either 1 or 0 (1 corresponds to ‘Success’ and 0 corresponds to ‘Failure’). The value of the Response Status Description is either ‘Success’ or ‘Failure’.
  2. Details of the **Shipping rate** –**** If there is more than one item, the shipping rate is calculated according to the set parcel packing option. When the user is not eligible for negotiated rates, the response will be as the below screenshot:

* * *

[ Previous  Configure WooCommerce UPS Shipping Methods by Country Code  ](https://www.pluginhive.com/knowledge-base/configure-woocommerce-ups-shipping-methods-based-country-codes/)

[ Next  WooCommerce UPS Shipping Plugin [Error Code 10001] -The XML document is not well formed  ](https://www.pluginhive.com/knowledge-base/woocommerce-ups-shipping-plugin-print-label-xml-document-not-well-formed-error-code-10001/)
