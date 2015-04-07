import LinkExplorer
import LinkSource
import RedditBot

class LinkManager(object):
    """LinkManager handles the creation and polling of the LinkExplorer"""

    def __init__(self):
        reddit = RedditBot.RedditBot()
        source = LinkSource.LinkSource([reddit])
        self._explorer = LinkExplorer.LinkExplorer(source)

    def get_links(self):
        """Returns a set of all new links found"""
        yield from self._explorer.explore()
