import math
def make_pagination_range(page_range, qty_pages, current_page):
    middle_range = math.ceil(qty_pages / 2) 
    start_range = current_page - middle_range
    stop_range = current_page + middle_range
    return page_range[start_range:stop_range]