import os

import newspy.client as newspy
from newspy import rss
from newspy.models import Article, Category, Country, Language, Source
from newspy.rss.models import RssArticle, RssSource
from newspy.shared.exceptions import NewspyException

newsorg_api_key = os.getenv("NEWSORG_API_KEY")
newspy.configure(newsorg_api_key=newsorg_api_key)


def fetch_news_sources(
    category: Category | None = None,
    country: Country | None = None,
    language: Language = Language.EN,
) -> list[Source] | list[RssSource]:
    """
    Fetch available news outlets and platforms from verified RSS feeds and the Newsorg API.

    Call this tool whenever the user wants to find, list, discover, or query news channels,
    publications, or media sources filtering by a specific topic, language, or country.

    Args:
        category: The domain topic filter.
        language: The 2-letter language code of publication. Defaults to 'en'.
        country: The 2-letter country code of origin.

    Returns:
        A list of Source domain model objects matching the selected filters.
    """

    if isinstance(category, str):
        try:
            category = Category(category.lower())
        except ValueError:
            category = None

    if isinstance(country, str):
        try:
            country = Country(country.lower())
        except ValueError:
            country = None

    if isinstance(language, str):
        try:
            language = Language(language.lower())
        except ValueError:
            language = None
    try:
        return newspy.get_sources(category=category, country=country, language=language)
    except NewspyException as exc:
        if (
            exc.msg
            == "The Newsorg API key is not configured. Please configure it by calling the configure function."
        ):
            return rss.get_sources(category=category, language=language)

        raise


def fetch_news_articles(
    category: Category | None = None,
    country: Country | None = None,
    language: Language = Language.EN,
) -> list[Article] | list[RssArticle]:
    """
    Fetch news articles from verified RSS feeds and the Newsorg API.

    Call this tool whenever the user wants to find, list, discover, or query news articles,
    publications or media sources filtering by a specific topic, language, or country.

    Args:
        category: The domain topic filter.
        language: The 2-letter language code of publication. Defaults to 'en'.
        country: The 2-letter country code of origin.

    Returns:
        A list of Article model objects matching the selected filters.
    """

    if isinstance(category, str):
        try:
            category = Category(category.lower())
        except ValueError:
            category = None

    if isinstance(country, str):
        try:
            country = Country(country.lower())
        except ValueError:
            country = None

    if isinstance(language, str):
        try:
            language = Language(language.lower())
        except ValueError:
            language = None
    try:
        return newspy.get_articles(
            category=category, country=country, language=language
        )
    except NewspyException as exc:
        if (
            exc.msg
            == "The Newsorg API key is not configured. Please configure it by calling the configure function."
        ):
            return rss.get_articles(category=category, language=language)

        raise
