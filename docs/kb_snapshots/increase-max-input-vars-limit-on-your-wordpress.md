# Increase the Maximum Input Variables Limit(Max Input Vars) on your WordPress.

**Source:** https://www.pluginhive.com/knowledge-base/increase-max-input-vars-limit-on-your-wordpress/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Increase the Maximum Input Variables Limit(Max Input Vars) on your WordPress.

In this guide, we would help you solve the Maximum Input Variables(Max Input Vars) error by increasing the Maximum Input Variables Limit on your WordPress site. Read along to learn more.

## What is Input Variables in WordPress?

WordPress allows you to do many things. For that, it consumes many resources and requires input from the admin at specific steps. The Input Variables are used by WordPress to process functions. 

The PHP Maximum Input Variables/Vars is the maximum number of variables your server can use for a single function. So by definition, more the number of Max Input Vars, better the overall functioning of your website. 

## When do you see the Max Input Vars error?

For your website to work without a hitch, it’s essential to set the maximum value to a higher number. Most of the new/latest WordPress sites require a value of 3000 to work satisfactorily.

If the number is too low, you may face problems such as lost data and being unable to add more values/rules. 

## How to increase the PHP Maximum Input Variables?

Most shared hosting providers won’t grant you full access to modify the Max Input Vars value. You can contact your provider to gain access and then proceed further. 

There are necessarily two ways you can increase the PHP Max Input Vars. 

  1. Define the value in the PHP.ini file
  2. Define the value in the .htaccess file 

### Editing in the PHP.ini file

It’s a straightforward process to update the value of Max Input Vars in your WordPress. If you have direct access to your PHP.ini file, then you can search and find it somewhere in your WordPress root folder. 

If you don’t find it there, then you can always create a new PHP.ini file and put it back to your root folder. Once you’re in your PHP.ini file, you need to find the following line of code. 
    
    
    max_input_vars = xx; 

Here you need to enter the desired value instead of ‘xx’ (3000, in this example) and then save your changes. After saving the changes, you must reboot your server to see the effect. 

### Editing in the .htaccess file

Before going ahead, please note that this step is only required if you don’t have access to your PHP.ini file. 

First, make sure to back up your .htaccess file before making any changes. You need to locate your .htaccess file found in your WordPress root folder.

Now open the .htaccess file in any preferred editor software and insert the following line of code. 
    
    
    php_value max_input_vars 3000

Again, 3000 is the value we’ve considered to explain to you the process. You can add any other value based on your requirements. So once that is done, you can save the changes in your file and refresh your website. 

### What to do if you have access to neither PHP.ini or .htaccess file?

If you’re on shared hosting, you may not have access to the PHP.ini or .htaccess file. They tend to keep it low by default to save their resources. So it’s best to contact your hosting provider to have them change these values if you are not able to fix yourself.

## Conclusion

Increasing the PHP Maximum Input Variables is a simple process. It’s a simple setting that you can change without facing any problems. If you have any doubts regarding this or need help with any of PluginHive’s plugins, feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**. 

If you’re looking for the best **[WooCommerce Shipping Plugins](https://www.pluginhive.com/product-category/woocommerce-plugin/woocommerce-shipping/)** then check out **PluginHive Shipping plugins**. And if you’re on the look for the best Booking solution for your website, then check out **[Bookings And Appointments for WooCommerce](https://www.pluginhive.com/product/woocommerce-booking-and-appointments/)**.

**_Good luck!_**

[ Previous  How to Increase PHP WordPress Memory Limit?  ](https://www.pluginhive.com/knowledge-base/increase-php-wordpress-memory-limit/)

[ Next  WooCommerce Order Fulfilment Made Easy with Touchless Label Printing  ](https://www.pluginhive.com/knowledge-base/woocommerce-order-fulfilment-with-touchless-label-printing/)
