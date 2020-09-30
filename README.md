# Amazon Price Tracker

***

### Description
A web scraper in Python 3 that tracks the price of a product on [Amazon](http://amazon.com) and sends a notification to user via email when the price dropped to a certain amount that meets the target price specified by the user. (Only supports Gmail).

***

### Requirements

* Do only one of the following:
   * [Allow Less Secure Apps on your Google Account](https://myaccount.google.com/lesssecureapps)
   * [Enable Two-Factor Authentication](https://www.google.com/landing/2step/), and [generate a new app password](https://myaccount.google.com/apppasswords) (**recommended**)
* A linux system with crond daemon enabled and running:
  * `$ systemctl enable --now crond.service`

* Python 3 is installed on the system
* Install pip (use your package manager)
* Install scrapy:
  * `sudo pip install scrapy` - for system wide installation, or
  * `pip install --user scrapy` - for user only installation

***

### Installation

```bash
$ git clone http://github.com/domenickmb/amazon-price-tracker.git
$ cd amazon-price-tracker
$ ./install.sh && source ~/.bashrc
```

***

### Running the program

```
$ price_tracker
    Usage: price_tracker [command]

    commands:
        initialize  -   Initialize configuration file
        start       -   Start tracking product price
        
```

Run the program with *initialize* command option before start tracking if you are running it for the first time.

```
$ price_tracker initialize
Enter your Gmail: 'Your Gmail'
Enter password: 'Your Gmail password or the generated app password if you enabled 2-factor authentication'
Enter Amazon product url: 'product url'
Enter your target price [should be greater than 0]: 
```

```
$ price_tracker start
```
### Adding the program to crontab  
The command above only checks the price once and sends you an email if the target price was met. To enable real-time tracking, you should schedule the program with crontab.  

Edit your crontab file: `$ crontab -e` and add the line below. This will make the price_tracker run every hour. See `man 5 crontab` for more information.

```
0 * * * *  ~/bin/price_tracker start
```
