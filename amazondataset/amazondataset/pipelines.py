# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# import pandas as pds

class AmazondatasetPipeline:
    def process_item(self, item, spider):
        adapter=ItemAdapter(item)


        feild_names=adapter.field_names()
        for field_name in feild_names:
            if field_name == 'product_name' and field_name!=None:
                value = adapter.get(field_name)
                adapter[field_name] = value[0].strip()


        # price_keys = ['product_price']
        # for price_key in price_keys:
        value = adapter.get('product_price')
        amount=value[0]
        formatted_value="₹" + amount
        adapter['product_price'] = formatted_value
        # if value!=None:
        #     value = value.replace('₹', '')
        #     adapter['product_price'] = float(value)


      
        value1 = adapter.get('orignal_price')
        amount1=value1[0]
        amount_string = amount1.replace('₹', '').replace(',', '')
        formatted_value1="₹" + amount_string
        adapter['orignal_price'] = formatted_value1
        # print(value1)
        # if value1!=None:
        #     old_currency_symbol = "â‚¹"
        #     new_currency_symbol = "₹"
        #     updated_string = value1[0].replace(old_currency_symbol, new_currency_symbol)
        #     # value1 = value1.replace('₹', 'â‚¹')
        #     adapter['orignal_price'] = updated_string


        return item
