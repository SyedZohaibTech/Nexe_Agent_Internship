import urllib.parse


def search_web(query):

    try:

        encoded_query = urllib.parse.quote(query)

        results = [
            {
                "title": f"Google Search for: {query}",
                "link": f"https://www.google.com/search?q={encoded_query}"
            },
            {
                "title": f"Wikipedia Search for: {query}",
                "link": f"https://en.wikipedia.org/wiki/{encoded_query}"
            },
            {
                "title": f"YouTube Search for: {query}",
                "link": f"https://www.youtube.com/results?search_query={encoded_query}"
            }
        ]

        return results

    except Exception as e:

        return str(e)