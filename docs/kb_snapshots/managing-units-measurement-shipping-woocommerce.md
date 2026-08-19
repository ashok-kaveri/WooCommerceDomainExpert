# WooCommerce Shipping – Managing Units of Measurement

**Source:** https://www.pluginhive.com/knowledge-base/managing-units-measurement-shipping-woocommerce/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce Shipping – Managing Units of Measurement

For businesses shipping internationally, it is sometimes a problem if Customs doesn’t recognize the unit of measurement of your goods. In those times, you don’t have any option but to take back your shipments. We will tell you how to do it properly when using the WooCommerce UPS Shipping Plugin with Print Label.

## UPS Commercial Invoice not accepting kilograms as the unit – Nancy’s facing a problem

Nancy runs a “dog care products” shop. She has a whole range of products like dog shampoo, dog fur freshener, and many other premium products. While shipping to international locations using ‘kg’ as the unit of measurement, it seems that her shipments are getting stuck. Upon inquiry, Nancy comes to know that UPS is not accepting an order that shows ‘kg’ as the unit of measurement in the Commercial Invoice. Even if they are accepting this, the shipment is getting delayed because of cross-checks. So she is finding it difficult to generate shipping invoices for fear of customs penalties or delays. Here is an existing label with “KG” as a unit:

## UPS Shipping API holds the key to the solution!

Our team found that UPS API has the option to change the unit of measurement. They have a varied set of choices depending upon the nature of the business. Now it was up to us how to implement this. The whole point was not to disturb the existing solution keeping in mind the problem of Nancy.  
The brainstorming session finally yielded the solution as a code snippet. This would not harm the existing customers in their routine shipping work, and Nancy can now just paste the code into the functions.php file of her theme and get her desired unit of measurement.

## Unit of Measurement in the Invoice Changes to Number of Units

Along with the [UPS plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/), Nancy had to just copy this code snippet into Appearance --> Editor --> functions.php :

Once done, the unit of measurement changed to ‘EA’.

**So what does “EA” mean?**  
It precisely stands for ‘Each’. That means ‘2 EA’ in the invoice shown below means that 2 units of “DOG SPRAY” are in the shipment. This becomes so easy to understand, doesn’t it?

All in all, it was just a small code that helped to fulfill a very relevant business case. Check out our [UPS Shipping plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) for a hassle-free shipping experience!

[ Previous  Adjust WooCommerce UPS Rates based on Destination Country  ](https://www.pluginhive.com/knowledge-base/ups-shipping-rate-adjustment-based-destination-country/)

[ Next  WPML WooCommerce Shipping Solutions for Multilingual Sites  ](https://www.pluginhive.com/knowledge-base/using-wpml-woocommerce-ups-shipping-plugin-multilingual-sites/?seq_no=2)
