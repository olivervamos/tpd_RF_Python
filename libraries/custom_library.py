from QWeb.keywords.element import get_element_count
from QWeb.keywords.text import get_text
from robot.libraries.String import String
import logging
from robot.libraries.BuiltIn import _Misc
from robot.libraries.BuiltIn import _Converter
from robot.libraries.BuiltIn import _Verify
from robot.api.deco import keyword


def price_sorting_control(): #Create List of prices
    elements_count = get_element_count("//div[contains(@class,'products__item')]")
    prices = []
    for i in range(elements_count):
        locator = "//div[contains(@class,'products__item')][{}]//span[contains(@class,'number left')]".format(i+1)
        price_txt = get_text(locator, between="???€")
        price_txt2 = price_txt.replace(' ','')
        price_txt3 = String.fetch_from_left(String, price_txt2, ',')
        price_num = float(price_txt3)
        prices.append(price_num)

    count_for_compare = int(elements_count)-1
    for i in range(count_for_compare):
        logging.info('toto je prvy index {} a toto je druhy index {}'.format(prices[i], prices[i+1]))
        if prices[i] < prices[i+1]:
            logging.warning('sorting of items is not corect form high to low')
            
        
        #price_num = _Converter.convert_to_number(_Converter, price_txt3)
        #price_num = String._convert_to_integer(String,price_txt3)
        #price_txt2 = String.remove_string(String,price_txt, ' ')
        #price_txt2 = String.replace_string(String, price_txt, ' ', '')
        #price_list = _Converter.create_list(_Converter)
        #item2 = list.__getitem__(price_list, i)
        #list_item1 = list.__getitem__(price_list, i)
        #list_item2 = list.__getitem__(price_list, i+1)
        #_Verify.should_be_true(_Verify, condition=prices[i] >= prices[i+1])
        #_Misc.log(_Misc, 'sorting of items is not corect form high to low', 'INFO', True, True, 'DEPRECATED', 'str')