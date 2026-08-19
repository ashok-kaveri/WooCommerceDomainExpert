# How to troubleshoot WooCommerce FedEx Shipping Plugin

**Source:** https://www.pluginhive.com/knowledge-base/troubleshooting-woocommerce-fedex-shipping-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# How to troubleshoot WooCommerce FedEx Shipping Plugin

With this guide, we are going to help you troubleshoot the **[WooCommerce Shipping Plugin for FedEx with Print Label](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/) **so you get the expected output for FedEx shipping rates, labels, and address validation. Read along to know more.

* * *

## Troubleshoot for not getting FedEx rates at all

If you are not getting the **FedEx shipping rates** at all, then there might be some reasons for not fetching real-time shipping rates from FedEx APIs. The list of reasons is as given below:

  * **Enable Shipping** : That sounds a bit trivial. But sometimes we forget to select **Enable shipping** checkbox. By default, Enable Shipping is disabled. So this should be your first check. You must enable shipping at two places:
    1. You should select the checkbox at WooCommerce Settings as shown below:  

* * *

Enable Shipping

* * *

* You should also select the checkbox at FedEx Plugin Settings as shown below:  

* * *

Enable FedEx

* * *

  * **Weight and Dimensions** : FedEx shipping carrier uses the weight and the dimensions of your product (Length, Width & Height) to calculate the shipping cost (besides using the origin and destination address). So make sure that you enter the Weight and the Dimension of your product in Product Settings as shown below:  

* * *

Product Dimensions

* * *

If you have done the above basic checks and still not getting rates, then you must enable debug mode to get the exact reason for not getting rates.

* * *

### Debug Mode

If you are not getting proper rates (lesser or higher than expected), not getting all the available shipping options, not getting rates at all, or not getting Print Labels, then you enable **Debug** option to find the error(s). You can also see the warning(s) by the WooCommerceFedEx Shipping Plugin.

By enabling debug mode, you can trace issues using a log. You can see information about debugging at the top of the Cart and Checkout page. Select the**Debug Mode** checkbox in FedEx Plugin Settings to enable debug mode as shown below:

* * *

Enable Debug Mode

* * *

After enabling debug mode, add a product to the cart. Go to the Cart/Checkout page to see the debugging information. Ensure that you have entered a proper shipping address. If you are not getting rates at all, then you need to check the response sent by FedEx to know the exact reason for not showing the rates. The cases are explained in the below section.

  * **Shipping address Error** : In case, the customer does not enter the correct postal code, then FedEx does not display the rates. The customer gets the message as shown below:

* * *

No Shipping Method is available

* * *

To know the reason, you need to check the response sent by FedEx as shown below:

* * *

FedEx Response

* * *

From the above response, you can clearly make out that the postal code is not correct. So correct it by clicking on **Calculate Shipping** in Cart/Checkout page as shown below:

* * *

Update Postal Code

* * *

  * **Authentication Error** : In Case, the credentials of FedEx are not correct, then FedEx does not display the rates. You get the message as shown below:

* * *

FedEx Response

* * *

From this response, you can clearly make out that authorization is a problem. So you can enter the correct credentials in the **[WooCommerce FedEx Plugin](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)** Settings page as shown below:

* * *

FedEx Plugin Settings

* * *

For Testing, you can use the FedEx credentials given below:

  * FedEx Account Number: 510087127
  * FedEx Meter Number: 118675423
  * Web Services Key: q8ncE6XYWCf4kPNx
  * Web Services Password: WwVzOMiam84RYDrn98nZL5Wo3

* * *

## Troubleshoot for correct FedEx rates

The Request is sent to FedEx by the plugin with Zipping code for the source, destination, and dimensions of the product, etc. The sample Request to FedEx is as shown below:

* * *

FedEx Response

* * *

  * Recheck the **Packaging Type** (at location **1** in the FedEx Request screenshot). According to your requirement, if it is not correct, you can Enable, Disable, and Add the required box dimension by navigating to FedEx Plugin Settings as shown below:

* * *

FedEx Box Sizes

* * *

  * Recheck the postal code and country code of the shipper. According to your requirement, if it is not correct, you can correct it as mentioned below:

* * *

  * For **POSTAL CODE** navigate to the shipping setting of FedEx and correct it as shown below:

Origin Post-Code

* * *

  * For **COUNTRY CODE** navigate to WooCommerce General settings and correct it as shown below:

Origin Country-Code

* * *

  * Recheck **Rate Request Type:** It indicates the setting of rates in the FedEx plugin settings. It can contain two values as shown below:
    * **None** : It indicates Account rates.
    * **List** : It indicates List rates.

According to your requirement, if it is not correct, you can correct it by navigating to WooCommerce FedEx Shipping Plugin Settings as shown below:

Request Rate Type

* * *

  * Recheck**PostalCode** ,**City** ,**State or Province Code** , and**Country Code**. According to your requirement, if it is not correct, you can correct it by navigating to the cart/checkout page as mentioned below:

* * *

  * Recheck**the** weight of the product with units. You can recheck the weight of the product by navigating to the **Admin** Product setting as shown below:

Product Weight

* * *

  * Recheck**the Dimensions** of the box with units. If box dimensions are not correct according to you, add the box with the required dimension by navigating to the WooCommerce FedEx Shipping Plugin setting as shown below:  

Box Sizes

* * *

* Recheck if the product is insured or not. In case it is not correct as per your requirement, change it by navigating to the FedEx Plugin Settings of the plugin as shown below:
Insurance Option

* * *

  * Recheck for special services like FedEx One. In case, it is not correct as per your requirement, check/uncheck it by navigating to WooCommerce FedEx Shipping Plugin Settings of the plugin as shown below:

FedEx One Rate

* * *

**Note** : If all the information sent to FedEx is valid, you can contact FedEx. Or you can go to the FedEx site and log in with your User ID. After login, enter the same information in FedEx Calculator to get the quote.

  * **FedEx Response** : You get the Response sent by FedEx with rates for different services. You can see the response to analyzing information sent from FedEx.

On the cart/checkout page, you get two sets of Requests and Responses if the FedEx Freight service is enabled. The first set is for either FedEx or FedEx One service, and the second set is for FedEx Freight services.

* * *

## Troubleshoot WooCommerce FedEx shipping plugin – FedEx Shipping Labels

If you are not able to **print labels** , then it could be because of a reason listed below:

  * **Product Existence** : Sometimes we try to print a label for the product which is removed from the shop. So check if the product still exists in your shop.
  * **Weight and Dimensions** : While printing labels, the weight and dimensions are needed to calculate shipping costs. So make sure that you have properly set the weight and dimensions of your products.
  * **Service Eligibility** : If the selected service in the Admin Order page(shown in the below screenshot) is not available for the particular location/product, you will get the error about service eligibility.

* * *

* * *

  * **Shipper address details:** To let FedEx process shipment requests and generate shipping labels, it’s necessary to enter a valid address in the shipper address fields. If you’re not able to print shipping labels, please check the following address fields and try again.  

To know details about the available services for the required location/product contact FedEx.

* * *

### Debug Mode

If you are facing issues with label printing, enable **Debug** option in WooCommerce FedEx Shipping Plugin Settings to find an error(s).

  * **Authentication Error** : If the authentication information like FedEx Account Number, FedEx Meter Number, Web Services Key, or password are not correct, you get the error as shown below:

Authentication Error

* * *

From this response, you can clearly make out that authorization is a problem. Correct it in the settings page as shown below:

Plugin Settings Page

* * *

  * **Service Eligibility** : If the preferred service with the selected box is not available for the particular location/product, you will get the error as shown below:

Service Eligibility Error

* * *

In case, you get the error message as highlighted above, the service and packaging type in Sample Fedex Request are as shown below:

FedEx Request

* * *

But the above Service and Package Type is available only for FedEx One option. If you want the same package, then you must enable FedEx One service option by navigating to FedEx Settings as shown below:

FedEx One Rate

* * *

Or you can customize the box by navigating to [WooCommerce FedEx Plugin](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/) Settings as shown below:

WooCommerce FedEx Plugin Settings

* * *

To know details about the available services for the required location/product contact FedEx. If it’s still not working, please contact the**[support team](https://www.pluginhive.com/support/)**. We will help you to troubleshoot any issue.

* * *

## Troubleshoot for FedEx Address Validation

FedEx has a special service for address validation called the ‘Address Validation API’. If this service is not activated for your FedEx account, you could get the following error in your FedEx Response.

> 
>     FedEx ADDRESS VALIDATION RESPONSE returns
>     [Message] => Authentication Failed

To solve this, please ensure you’re using the Production credentials and you’ve enabled the **Production Key** option in the plugin settings.

_**Note: Given that the FedEx Address Validation service works only under a live/production environment, you cannot use your test account.**_

If your account doesn’t support this service, then please contact FedEx with your account details and request them to activate this service for your account. Please refer to this article on **[WooCommerce FedEx Address Validation](https://www.pluginhive.com/how-to-use-fedex-address-validation-on-your-online-store/)** to know more about the topic. 

If you need any more help setting up the WooCommerce Shipping Plugin for FedEx with Print Label, feel free to contact our **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**. We will try our best to help you find a solution.

[ Previous  How to Pack Items Based on Weight?  ](https://www.pluginhive.com/knowledge-base/pack-items-based-weight/)

[ Next  WooCommerce: Configure Box Dimensions  ](https://www.pluginhive.com/knowledge-base/woocommerce-configure-box-dimensions/)
