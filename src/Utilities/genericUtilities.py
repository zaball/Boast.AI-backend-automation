import logging as logger
import random
import string


def generate_random_user_email(domain=None, email_prefix=None):
    logger.debug("Generating random user email: ")

    if not domain:
        domain = 'boastcapital.com'
    if not email_prefix:
        email_prefix = 'testuser'

    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))

    email = email_prefix + '_' + random_string + '@' + domain

    random_info = {'email': email}
    logger.debug(f"Randomly generated email: {random_info}")

    return random_info


def generate_random_string(length=10, prefix=None, suffix=None):
    logger.debug("Generating random... : ")

    random_string = ''.join(random.choices(string.ascii_lowercase, k=length))

    if not prefix:
        prefix = 'test'
        random_string = prefix + random_string
    if suffix:
        random_string = random_string + suffix

    return random_string








