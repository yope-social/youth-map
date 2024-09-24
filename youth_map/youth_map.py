"""youth_map"""

import reflex as rx

from youth_map.pages.data import data_page
from youth_map.pages.map import map_page

app = rx.App()
app.add_page(map_page(), route="/", title="yope.social - Youth Map")
app.add_page(map_page(area="lossatal"), route="/lossatal", title="Lossatal - yope.social")
app.add_page(map_page(area="colditz"), route="/colditz", title="Colditz - yope.social")
app.add_page(data_page(), route="/data", title="yope.social - Youth Map")
