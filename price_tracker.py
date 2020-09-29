#!/usr/bin/env python
import sys
import os
import logging
import smtplib
from scrapy.crawler import CrawlerProcess
from email.message import EmailMessage

from amazon_spider import AmazonSpider
from items import AmazonItem
from config import read_config, initialize
from logger import logger


def start_tracking():
    """
    Start tracking product price
    """
    data = read_config()
    if not data:
        return

    logger.info('Searching for product price')
    AmazonSpider.start_urls = [data['url']]
    item = AmazonItem()
    AmazonSpider.item = item
    process = CrawlerProcess(settings={'LOG_LEVEL': logging.ERROR})
    process.crawl(AmazonSpider)
    process.start()

    if float(item['product_price']) <= float(data['target_price']):
        logger.info(f"Price dropped to {item['product_price']}")
        send_email(data['gmail'], data['password'], item)
    else:
        logger.info(f"Current price is {item['product_price']}")


def send_email(gmail, password, itemObj):
    """
    Notify the user via email that the price has dropped

    Parameters
        gmail (str):
            User's gmail
        password (str):
            User's gmail password
        itemObj (items.AmazonItem):
            Data that contains product_url, product_price and product_name
    """
    msg = EmailMessage()
    msg['Subject'] = 'Price dropped!'
    msg['From'] = gmail
    msg['To'] = gmail
    body = f"The price of {itemObj['product_name']} has dropped to {itemObj['product_price']}!\n" \
           f"Please visit {itemObj['product_url']}"
    msg.set_content(body)

    try:
        logger.info(f'Sending a notification to {gmail}')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(gmail, password)
            smtp.send_message(msg)
    except Exception:
        logger.error('Sending failed')
    else:
        logger.info('A message was sent to your inbox. Please check it out.')


def print_help():
    """
    Print help message
    """
    script_name = os.path.basename(sys.argv[0])
    print(f"""
    Usage: {script_name} [command]

    commands:
        initialize  -   Initialize configuration file
        start       -   Start tracking product price
    """
          )
    sys.exit()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_help()
    command = sys.argv[1]
    if command == 'initialize':
        initialize()
    elif command == 'start':
        start_tracking()
    else:
        print(f"Error: Unknown command '{sys.argv[1]}'")
        print_help()
