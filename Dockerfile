FROM php:7.0-apache
COPY php.ini /usr/local/etc/php/
COPY central/ /var/www/html/
