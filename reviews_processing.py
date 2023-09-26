import re

import bs4

from webpage_getter import get_soup, get_response

Review = dict[str, int | str]


def get_reviews_link(endpoint_to_insert: str) -> str:
    full_link = f"https://market.yandex.ru{endpoint_to_insert}/reviews"
    return full_link


def get_review_info_or_none(review: bs4.Tag, review_info_type: str) -> str | None:
    review_info = review.find("dl", attrs={"data-auto": review_info_type})
    if review_info is not None:
        review_text = review_info.find("dd").text
        review_text = re.sub('"', '""', review_text)
        return review_text
    else:
        return None


def get_reviews_for_one_machine(machine_soup: bs4.BeautifulSoup) -> list[Review]:
    reviews_list = machine_soup.find_all("div", attrs={"class": "_3K8Ed"})
    output_reviews = []

    for review in reviews_list:
        stars = int(review.find("div",
                                attrs={"class": "_3iy4z autotest-RatingStars _3DD8b cia-vs cia-cs"})["data-rate"])
        experience = get_review_info_or_none(review, "review-usage")
        pros = get_review_info_or_none(review, "review-pro")
        cons = get_review_info_or_none(review, "review-contra")
        comment = get_review_info_or_none(review, "review-comment")

        review_dict = {
            "stars": stars,
            "experience": experience,
            "pros": pros,
            "cons": cons,
            "comment": comment
        }

        output_reviews.append(review_dict)

    return output_reviews


def get_machine_name_from_review_soup(machine_soup: bs4.BeautifulSoup) -> str:
    name = machine_soup.find("h1", attrs={"class": "_3wtYw _2OAAC"})
    try:
        return name.text
    except AttributeError:
        return "No name"


def get_reviews(endpoints: list[str]) -> dict[str, list[Review]]:
    reviews_dict = dict()
    for endpoint in endpoints:
        reviews_link = get_reviews_link(endpoint)
        machine_response = get_response(reviews_link)
        machine_soup = get_soup(machine_response)

        machine_name = get_machine_name_from_review_soup(machine_soup)
        machine_reviews = get_reviews_for_one_machine(machine_soup)

        reviews_dict[machine_name] = machine_reviews

    return reviews_dict
