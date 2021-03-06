import logging

import requests

from tor import __version__
from tor.helpers.flair import flair
from tor.helpers.flair import flair_post
from tor.strings.responses import bot_footer


def set_meta_flair_on_other_posts(r, tor, config):
    """
    Loops through the 10 newest posts on ToR and sets the flair to
    'Meta' for any post that is not authored by the bot or any of
    the moderators.

    :param r: Active reddit object
    :param tor: The Subreddit object for ToR.
    :param config: the active config object.
    :return: None.
    """
    for post in tor.new(limit=10):

        if (
            post.author != r.redditor('transcribersofreddit') and
            post.author not in config.tor_mods and
            post.link_flair_text != flair.meta
        ):
            logging.info(
                'Flairing post {} by author {} with Meta.'.format(
                    post.fullname, post.author
                )
            )
            flair_post(post, flair.meta)


def _(message):
    """
    Message formatter. Returns the message and the disclaimer for the
    footer.

    :param message: string. The message to be displayed.
    :return: string. The original message plus the footer.
    """
    return bot_footer.format(message, version=__version__)


def log_header(message):
    logging.info('*' * 50)
    logging.info(message)
    logging.info('*' * 50)


def clean_list(items):
    """
    Takes a list and removes entries that are only newlines.

    :param items: List.
    :return: List, sans newlines
    """
    cleaned = []
    for item in items:
        if item.strip() != '':
            cleaned.append(item)

    return cleaned


def send_to_slack(message, config):
    """
    Sends a message to the ToR #general slack channel.

    :param message: String; the message that is to be encoded.
    :param config: the global config dict.
    :return: None.
    """
    # if we have the api url loaded, then fire off the message.
    # Otherwise, don't worry about it and just return.
    if config.slack_api_url:
        payload = {
            'username': 'Kierra',
            'icon_emoji': ':snoo:',
            'text': message
        }
        requests.post(config.slack_api_url, json=payload)

    return
