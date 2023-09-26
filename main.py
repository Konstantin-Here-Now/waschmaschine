from db import insert_reviews
from machine_links_getter import get_machines_list, get_machines_endpoints
from reviews_processing import get_reviews


PAGES_NUMBER = 50

if __name__ == "__main__":
    machines_list = get_machines_list(PAGES_NUMBER)
    machines_links_endpoints = get_machines_endpoints(machines_list)
    reviews = get_reviews(machines_links_endpoints)
    insert_reviews(reviews)
