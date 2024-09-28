"""youth_map"""

import reflex as rx

from youth_map.pages.data import data_page
from youth_map.pages.map import test_page

app = rx.App(
    stylesheets=[
        "/styles.css",  # This path is relative to assets/
    ],
)
app.add_page(test_page(), route="/", title="yope.social - Youth Map")
app.add_page(test_page(area="lossatal"), route="/lossatal", title="Lossatal - yope.social")
app.add_page(test_page(area="colditz"), route="/colditz", title="Colditz - yope.social")
app.add_page(data_page(), route="/data", title="Data - yope.social")
