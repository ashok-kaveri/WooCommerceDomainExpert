# Troubleshooting WooCommerce Canada Post Plugin

**Source:** https://www.pluginhive.com/knowledge-base/troubleshooting-woocommerce-canada-post-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** canada-post
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Troubleshooting WooCommerce Canada Post Plugin

In this tutorial, we will show you how to troubleshoot **[WooCommerce Canada Post Shipping Plugin with Print Label](https://www.pluginhive.com/product/woocommerce-canada-post-shipping-plugin-with-print-label/)** in case you are having trouble with getting real-time Canada Post Shipping Rates, print shipping labels and track your orders from your WooCommerce store. It is a complete guide to solving all the issues you face while using the plugin.

* * *

## Troubleshooting for not Getting Rates at all

If you are not getting **rates** at all, then there might be some reasons for not fetching real-time shipping rates from Canada Post APIs. The list of reasons is as given below:

  * **Enable Shipping** : That sounds a bit trivial. But sometimes we forget to select **Enable shipping** checkbox. By default, Enable Shipping is disabled. So this should be your first check. You must enable shipping at two places.
    1. You should select the checkbox at WooCommerce Settings as shown below:
    2. You should also select the checkbox at Canada Post Plugin Settings as shown below:

  * **Weight and Dimensions** : Canada Post shipping carrier use the weight and the dimensions of your product (Length, Width & Height) to calculate the shipping cost (besides using the origin and destination address). So make sure that you enter the Weight and the Dimension of your product in Admin Product Settings as shown below:

If you have done the above basic checks and still not getting rates, then you must enable debug mode to get the exact reason for not getting rates.

* * *

### **Debug Mode**

If you are not getting proper rates( lesser or higher than expected), not getting all the available shipping options, not getting rates at all, or not getting Print Labels, then you enable **Debug** option to find the error(s). You can also see the warning(s) by **[WooCommerce Canada Post Shipping plugin](https://www.pluginhive.com/product/woocommerce-canada-post-shipping-plugin-with-print-label/)**.

By enabling debug mode, you can trace issues using a log. You can see information about debugging at the top of the Cart and Checkout page. Select the **Debug** checkbox in Canada Post Plugin Settings to enable debug mode as shown below:

**Note** : To enable debug mode, first you need to enable **Shipping Debug Mode** by navigating to **WooCommerce** > **System Status** as shown below:

After enabling debug mode, add a product to cart. Go to the checkout page to see the debugging information. Ensure that you have entered a proper shipping address. If you are not getting rates at all, then you need to check the response sent by Canada Post to know the exact reason for not showing the rates. Two cases are explained in the below section.

  1. **Shipping address Error** : In case, the customer does not enter the correct postal code, then Canada Post does not display the rates. The customer is shown the message as shown below: To know the reason, you need to check the response sent by Canda Post as shown below: From the above response, you need to check the recipient, shipper address. So correct recipient address by clicking on **Calculate Shipping** in Cart/Checkout page as shown below:
  2. **Authentication Error** : In Case, the credentials of Canada Post are not correct, then Canada Post does not display the rates. You are shown the message as shown below: From this response, you can clearly make out that authorization is a problem. So you can enter the correct credentials in the Canada Post Settings page as shown below:
  3. **Weight Error** : In Case, the weight of the product is not correct, then Canada Post does not display the rates. You are shown the message as shown below:

* * *

## Troubleshooting for Correct Rates

The Request is sent to Canada Post by the plugin with a Zip code for the source, destination, and dimensions of the product. The sample Request to Canada Post is as shown below:

  1.      1.         1. Recheck**** weight of the product with units (at location **1** in the Formatted Canada Post Request screenshot). Product Weight gets converted to Kilogram and passed to Canada Post API. In the above request, the weight is in Kilogram. You can recheck the weight of the product by navigating to **admin** Product setting as shown below:
        2. Recheck**Dimensions** of the product with units. Product Dimensions gets converted to the centimeter and passed to Canada Post API. In the above request, the dimensions are in Centimeter. If box dimensions are not correct according to you, add the box with the required dimension by navigating to Admin Product settings as shown below:

        3. Recheck if the product is insured or not. In case it is not correct as per your requirement, change it by navigating to Canada Post Plugin Settings as shown below:

        4. Recheck if the signature is needed at the time of delivery. In case it is not correct as per your requirement, change it by navigating to Canada Post Plugin Settings as shown below:

        5. Recheck **origin-postal-code** value. According to your requirement, if it is not correct, you can correct it by navigating to Canada Post Plugin Settings as mentioned below:
        6. Recheck **customer-number** and **contract-id** value. According to your requirement, if it is not correct, you can correct it by navigating to Canada Post Plugin Settings as mentioned below:

        7. Recheck for **zip-code** value under **Destination** node. According to your requirement, if it is not correct, you can correct it by navigating to cart/checkout page as mentioned below:

**Note** : If all the information sent to Canada Post is valid, you can contact Canada Post. Or you can go to the Canada Post site and log in with your UserID. After login, enter the same information in Canada Post Calculator to get the quote.

  * **Canada Post Response** : You get the Response sent by Canada Post with rates for different services. You can see the response(XML code) in a formatted way so that you can easily analyze information sent from Canada Post.

* * *

## Troubleshooting for Print Labels

If you are not able to **print labels** , then it could be because of a reason listed below:

  *     * **Product Existence** : Sometimes we try to print the label for the product which is removed from the shop. So check if the product still exists in your shop.
    * **Weight and Dimensions** : While printing labels, the weight and dimensions are needed to calculate shipping costs. So make sure that you have properly set the Weight and Dimensions of your products.
    * **Service Eligibility** : Select a valid service for your shipment from the**Preferred Service** drop-down list (shown in the below screenshot). If the selected service is not available for the particular location/product, you will get the error about service eligibility at the top of the page.To know details about the available services for required location/product contact Canada Post.
    * **Authentication Error** : If the authentication information like Merchant username, Merchant password, Customer number, or Contract number is not correct, you get the error as shown below:

From the above message, you can clearly make out that authorization is a problem. Correct it in the Canada Post plugin settings page as shown below:

### **Debug Mode**

If you are facing issues with label printing, enable **Debug** option in Canada Post Plugin Settings to find the error(s).

  * **Authentication Error** : If the authentication information like Merchant username, Merchant password, Customer number, or Contract number is not correct, you get the error as shown below: From this response, you can clearly make out that authorization is a problem. Correct it in the settings page as shown below:

If you are unable to troubleshoot or have any queries regarding the **[WooCommerce Canada Post Shipping plugin](https://www.pluginhive.com/product/woocommerce-canada-post-shipping-plugin-with-print-label/)** then reach out to our **[customer support](https://www.pluginhive.com/support/)**. Our support team will help you set up Canada Post shipping on your WooCommerce store in no time.

[ Previous  Find Pickup Point ID for Canada Post Deposits on WooCommerce  ](https://www.pluginhive.com/knowledge-base/find-pickup-point-id-canada-post-deposit-location/)

[ Next  Set Minimum Shipping Cost for WooCommerce Shipping Methods  ](https://www.pluginhive.com/knowledge-base/setting-minimum-shipping-cost-various-woocommerce-shipping-methods/)
