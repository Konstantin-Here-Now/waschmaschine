import bs4

from webpage_getter import get_soup, get_response


def create_machine_list_url(page_number_to_insert: int) -> str:
    base_url = "https://market.yandex.ru/catalog--stiralnye-mashiny/18031204/list?rs=eJwdUCurQkEY3KNJ_AWCwpoNos0XHE" \
               "3CRRAxXuEk8T9YDj7AICabZbMoaLD4wHODiE0QwwXBgyI2g3AV292ZMgwz3zfz7cYb3qKxMYSoZjRa5ZRG55bWaF4WGu1jUqPbg" \
               "-I84YoRdNMm_4EuOkAVXGK-wK07FHcCbs3pRuCqPpUjuPwCihJ6zTBzWnDllvMzoP2dQM6H90yB1h963foafAdXxrhbYeMQmWae" \
               "mW_qPnDZBKo0bzDoRtGlunxvm10v9h740jHdAXv3_IER-S8nT9iyrrxHUg-toOfY6GG-n5OKaQEmn_k_Nmey4M6DLbXUP1YoiHA" \
               "%2C&viewtype=list&hid=90566&allowCollapsing=1&local-offers-first=0&glfilter=7893318%3A152818"
    return base_url + f"&page={page_number_to_insert}"


def get_machines_list_from_page(soup_to_parse: bs4.BeautifulSoup) -> list[bs4.Tag]:
    machines_list_on_one_page = soup_to_parse.find_all('a', attrs={"class": "egKyN _2Fl2z"})
    return machines_list_on_one_page


def get_machines_list(pages_number) -> list[bs4.Tag]:
    machines_list_output = []
    for i in range(1, pages_number + 1):
        print(f"Processing page number {i}...")
        page_number = i
        url = create_machine_list_url(page_number)
        response = get_response(url)
        soup = get_soup(response)

        one_page_machines = get_machines_list_from_page(soup)
        print(f"Got {len(one_page_machines)} machines.")
        machines_list_output.extend(one_page_machines)

    return machines_list_output


def get_machines_endpoints(machines_list_to_parse: list[bs4.Tag]) -> list[str]:
    hrefs = []
    for machine in machines_list_to_parse:
        full_href = machine["href"]
        short_href = full_href.split("?")[0]
        hrefs.append(short_href)
    return list(set(hrefs))
