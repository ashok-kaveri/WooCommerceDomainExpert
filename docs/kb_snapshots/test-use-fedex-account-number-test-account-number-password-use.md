# During the test mode, should I use my FedEx account number or test account number?

**Source:** https://www.pluginhive.com/knowledge-base/test-use-fedex-account-number-test-account-number-password-use/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# During the test mode, should I use my FedEx account number or test account number?

Which account number to use in test mode? The FedEx account or the Test account? Don’t worry, this article will help you figure it out. You can refer to the following conversation.

[](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)

[](https://www.pluginhive.com/product/shopify-fedex-shipping-app-with-print-label-tracking/)

[](https://www.pluginhive.com/magento-shipping-services/)

**Customer:**

During the test mode, should I use my FedEx account number or test account number?  
What password should I use?

When I enabled debug mode, a get the following error:

> stdClass Object  
> ([HighestSeverity] => ERROR[Notifications] => stdClass Object  
> ([Severity] => ERROR[Source] => prof[Code] => 1000[Message] => Authentication Failed  
> )
> 
> [TransactionDetail] => stdClass Object  
> ([CustomerTransactionId] => *** WooCommerce Rate Request ***  
> ) [Version] => stdClass Object  
> ([ServiceId] => crs[Major] => 16[Intermediate] => 0[Minor] => 0  
> )
> 
> )

* * *

**PluginHive Support:**

In the test mode, you only need to use a test account number.

You need to [register](http://www.fedex.com/us/developer/web-services/index.html) with FedEx for following test credentials:

  * FedEx account number
  * FedEx meter number
  * Web services key
  * Web services password

Kindly note the above credentials are different for test and live mode. If you are getting authorization error then the test credentials are incorrect, contact FedEx support.

* * *

**Customer:**

Is the web services password same as account password?

* * *

**PluginHive Support:**

Web services password is the password that you received via email when you have completed the registration for FedEx API. Account number and web services password are not the same.

* * *

**Customer:**

The system works with your test credentials, but not with the ones they gave us. I still wonder if we were supposed to get a separate password rather than the password we use to get into our FedEx account?

* * *

**PluginHive Support:**

Kindly provide us debug request and response in the text format. Also, send us the credentials email sent from FedEx as shown in the attached screenshots:

* * *

**Customer:**

Found the problem, thanks to your screenshots. We did not have the test password, only the account password.  
Got figured out, all is well.

[ Previous  Configure FedEx International Shipping with WooCommerce  ](https://www.pluginhive.com/knowledge-base/international-pricing-not-showing-website/)

[ Next  Manage Return Shipments with FedEx Plugin for WooCommerce  ](https://www.pluginhive.com/knowledge-base/manage-return-shipments-woocommerce-fedex-shipping-plugin/)
