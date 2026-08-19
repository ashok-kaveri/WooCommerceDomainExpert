# I have downloaded this plugin and it seems to be working fine. The only thing that isn’t showing up is the letter mail option

**Source:** https://www.pluginhive.com/knowledge-base/downloaded-plugin-seems-working-fine-thing-isnt-showing-letter-mail-option/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# I have downloaded this plugin and it seems to be working fine. The only thing that isn’t showing up is the letter mail option

**Customer:**

I’ve downloaded this plugin and it seems to be working fine. The only thing that isn’t showing up is the letter mail option. I added it in the settings of the plugin but I can’t see where I set the price of letter mail?

* * *

**Support:**

The Sizes, Dimensions, and Weights of lettermails are inbuilt in our plugin since these are flat rates provided by Canada Post.

Kindly find the following information about lettermails :

*******************************************  
“Standard Lettermail”,  
“length” => “24.5”,  
“width” => “15.6”,  
“height” => “0.5”,  
“max-weight” => “0.05”,

Cost = For .03kg, price is .85  
For 0.05kg, price is 1.20  
******************************************

“Medium Lettermail”,  
“length” => “23.5”,  
“width” => “16.5”,  
“height” => “0.5”,  
“max-weight” => “0.05”,  
Costs = For 0.03kg, price is 0.85,  
For 0.05kg, price is 1.20

******************************************

“Non-standard Lettermail”,  
“length” => “38”,  
“width” => “27”,  
“height” => “2”,  
“max-weight” => “0.5”,  
Costs = For “0.1kg” => price is ‘1.80’  
For “0.2kg” => price is ‘2.95’,  
For “0.3kg” => price is ‘4.10’,  
For “0.4kg” => price is ‘4.70’,  
For “0.5kg” => price is ‘5.05’

********************************************

* * *

 **Customer:**

I figured out how to get it on there and it appears to be working except one item that is 2 cm isn’t being marked parcel even though it’s too thick to go lettermail?

Also one last bit of help. All of my packagings goes by weight etc and goes into a poly mailer which is super light. One of my items are hats and they go in boxes which adds about 300g which significantly increases the shipping cost especially with the increased dimensions of the box. My question is how can I set it to add 300g plus the dimensions of the box when shipping hats but not add it’s exponential if someone orders two hats? I don’t want to add 600 grams etc. Just if you order any hats add the extra

Is this doable?

* * *

**Support:**

For the question on a 2cm item not being a marked parcel, kindly check whether you are putting product dimensions correctly. You have to put product dimensions so that the plugin identifies the item. You can put in the dimensions by going to Products --> edit product --> Product data tab --> shipping.

Based on the business case you have provided us, we would like to tell that we have options to allow packing based on weight/packing individually / based on weight and dimensions. (**Parcel Packing field in plugin settings**).

Ideally, the best case for you would be to use our weight based packing. However, you can only use **weight-based packing** or **packing based on dimensions** at one single instance (**one-time setting setup**). **You cannot use both of them together.  
**  
One workaround may be by allowing weight based packing for hats also.

[ Previous  The only label that prints are a testing one even though I have switched to live  ](https://www.pluginhive.com/knowledge-base/label-prints-testing-one-even-though-switched-live/)

[ Next  Can I have shipments go out from my contractor’s factory but the shipping costs are charged on my commercial account?  ](https://www.pluginhive.com/knowledge-base/can-shipments-go-contractors-factory-shipping-costs-charged-commercial-account/)
