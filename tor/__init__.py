import bugsnag
from addict import Dict

__version__ = '2.6.13'

config = Dict()

config.video_domains = []
config.audio_domains = []
config.image_domains = []

config.video_formatting = ''
config.audio_formatting = ''
config.image_formatting = ''
config.header = ''

config.subreddits_to_check = []
config.upvote_filter_subs = {}
config.no_link_header_subs = []

config.tor_mods = []

config.perform_header_check = True
config.debug_mode = False

# section for gifs
config.no_gifs = []

# global flag to enable / disable placing the triggers
# for the OCR bot
config.OCR = True

# configure bugsnag logging
try:
    config.bs_api_key = open('bugsnag.key').readline().strip()
except FileNotFoundError:
    config.bs_api_key = None

if config.bs_api_key:
    bugsnag.configure(
        api_key=config.bs_api_key,
        app_version=__version__
    )

# load slack API url
try:
    config.slack_api_url = open('slack.key').readline().strip()
except FileNotFoundError:
    config.slack_api_url = None
