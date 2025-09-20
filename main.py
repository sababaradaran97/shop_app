from data_base.data_base_manager import *
from view.view_program import main_view
from tools.mudals import *

# main_view --> 2 interence --> count_bottom , check_date from data_base.data_base_manager


total_number = count_bottom() 
list_of_expired_products = check_date()
list_of_names = choose_title()
# main_view( list_of_expired_products , total_number , list_of_names )

