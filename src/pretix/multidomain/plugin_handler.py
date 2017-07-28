from pretix.presale.utils import event_view


def plugin_event_urls(urllist, plugin):
    for entry in urllist:
        if hasattr(entry, 'url_patterns'):
            plugin_event_urls(entry.url_patterns, plugin)
        elif hasattr(entry, 'callback'):
            # TODO: Find a way to set require_live=False
            entry.callback = event_view(entry.callback, require_plugin=plugin)
    return urllist
