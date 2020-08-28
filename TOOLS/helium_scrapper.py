import json
from bs4 import BeautifulSoup
import requests


def helium_script(data):
    # print(data)
    headers = {

    "x-csrf-token": "QCeSXkF-cQJcA02Z60l5vZqTC8cIBHnVZtMp4ord5sQZUsQLGUoQTmRRKd2NHk3l0dRBjGMxEYFRqXCj5auXgQ==",
    "cookie": "__distillery=b1c4564_2aa5f5a3-cdb9-4d44-95c0-488a8db3991c-5be6dbb20-2e53b3a324b4-dabb; _csrf=c2a7d8649e34a76da9ed74b0d079b83d7e2687d755179d8d5eae7bf264445715a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22YuVUX4aL8RdDfW4XKGJKk5hT7zYAovqE%22%3B%7D; 7879928_viewed_6=3; cf:aff_sub=; cf:aff_sub2=; cf:aff_sub3=; cf:affiliate_id=; cf:cf_affiliate_id=; cf:content=; cf:medium=; cf:MzI1MDAyMzg=:visited=true; cf:name=; cf:source=; cf:term=; cf:visitor_id=c83857f0-992c-43c9-8e7c-97848fe39909; current-marketplace=5a7deede86e62213f2adae2c21dde37c8919c5317898e27c859a9080214c380fa%3A2%3A%7Bi%3A0%3Bs%3A19%3A%22current-marketplace%22%3Bi%3A1%3Bs%3A13%3A%22ATVPDKIKX0DER%22%3B%7D; GleamId=OQXWzZ89*GH6%20NAX_; sidebar=10e72d2c5fa6bd03252eaf0d9f87e2bc1020bb80d5d174d7a4a3ed09e7a80426a%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22sidebar%22%3Bi%3A1%3Bs%3A0%3A%22%22%3B%7D; zvtgmpc9mr382nb2=true; _identity=3c23f0d9df2188aa1595f78e60b7ddfb5f87465ba168c282f785f8e957d14b79a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A81%3A%22%5B1543613976%2C%22Gsm-Nxe-_FQ4WcGrt8cBxH05X8qEV4eX%22%2C2592000%2Cnull%2Cnull%2C%2239.53.254.174%22%5D%22%3B%7D; _gcl_au=1.1.1622150552.1597935794; ab.storage.userId.4d3ca359-c724-43de-9b97-cb9f1fee4769=%7B%22g%22%3A%221543613976%22%2C%22c%22%3A1597935794254%2C%22l%22%3A1597935794254%7D; _ga=GA1.3.355721092.1597935795; _gid=GA1.3.1156987563.1597935795; _fbp=fb.1.1597935794655.5047329; ajs_user_id=%221543613976%22; ajs_anonymous_id=%220cf4ecda-56ac-471c-9b6d-57d44c1d0c71%22; amplitude_idundefinedhelium10.com=eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==; sid=8t5vfiob5uk5itltilbm5090o8; ab.storage.sessionId.4d3ca359-c724-43de-9b97-cb9f1fee4769=%7B%22g%22%3A%228ddc50ac-6769-ed63-8218-ccd11197e7e9%22%2C%22e%22%3A1597942440662%2C%22c%22%3A1597940640664%2C%22l%22%3A1597940640664%7D; _dc_gtm_UA-75738827-2=1; _uetsid=53a3080b8bfad53742cc5e50e735407a; _uetvid=b76ad12c7103919583e4cbb7b6403cea; amplitude_id_95d3abbefaf19863dc230d5449736018helium10.com=eyJkZXZpY2VJZCI6ImM2YzkyYzQzLTY4ZDEtNGNmMy1hZGExLTg4ZjNiNzkzMWU5OVIiLCJ1c2VySWQiOiIxNTQzNjEzOTc2Iiwib3B0T3V0IjpmYWxzZSwic2Vzc2lvbklkIjoxNTk3OTQwNjQxODk0LCJsYXN0RXZlbnRUaW1lIjoxNTk3OTQwNjQxOTA5LCJldmVudElkIjoyLCJpZGVudGlmeUlkIjozLCJzZXF1ZW5jZU51bWJlciI6NX0=; AWSALB=ethHWN9rETs4uGvtIXaZlsCmUz0/40ytFgwPuD9zbexIZGkv9fKz5VeQvBA8/PUp0Fwebp+Y3aVpUJJfKM0rxjF0SJpKubaa6nW42znOXZHWspM4LogUE4XiPX+3; AWSALBCORS=ethHWN9rETs4uGvtIXaZlsCmUz0/40ytFgwPuD9zbexIZGkv9fKz5VeQvBA8/PUp0Fwebp+Y3aVpUJJfKM0rxjF0SJpKubaa6nW42znOXZHWspM4LogUE4XiPX+3; io=VeSNMxeiW0YzmUqrHe41; _gat_UA-75738827-2=1; intercom-session-yzizpoku=MTdWQ24yR2NWV3RIWU5ZQWtBb05ySlpLWHRQaUJjVEFxRk50ZGl2ei9QYnB3OUREbkpYamVRbnR4cHRhZXdnTi0tcmM0YWVrVkdZSlNmdEIzbFdEcGpoZz09--dd8030c4d814274b820967a2c4ba18b23599fb1a",
            }


    x=requests.post("https://members.helium10.com/black-box/set-filters",headers=headers,data=data)
    preview=x.text
    json_load=json.loads(preview)
    search_id=json_load['searchId']
    x=requests.post("https://members.helium10.com/black-box?searchId="+str(search_id)+"&marketplace=ATVPDKIKX0DER&page=1&_pjax=%23black-box-pjax&page=1",headers=headers)
    # print(x.text)
    dics_in_list=[]
    soup=BeautifulSoup(x.text,'lxml')
    for maindiv in soup.find_all('tbody'):
        for tr in maindiv.find_all('tr',{'class':'bb-product-row'}):
            td = tr.find_all('td')
            try:
                td_object_zero=td[0]
                media_body=td_object_zero.find('div',{'class':'media-body'})
                try:
                    amazon_link_parse =td_object_zero.find('a',{'target':'_blank'})
                    amazon_link=amazon_link_parse['href']
                    # print(amazon_link)
                except:
                    amazon_link=""
                try:
                    image_parse=td_object_zero.find('img',{'class':'media-object'})
                    image=image_parse['src']
                    # print(image)
                except:
                    image=""
                try:
                    title_parse=media_body.find('h5')
                    title=title_parse.text
                    # print(title)
                except:
                    title=""
                try:
                    category_div=media_body.find('div')
                    category=str(category_div.text).split('Category:')[1]
                    # print(category)
                except:
                    category=""
                try:
                    brand_div=category_div.find_next('div')
                    brand=str(brand_div.text).split('Brand:')[1]
                    # print(brand)
                except:
                    brand=""
                try:
                    seller_div = brand_div.find_next('div')
                    seller = str(seller_div.text).split('Seller:')[1]
                    # print(seller)
                except:
                    seller=""
                try:
                    fulfillment_div = seller_div.find_next('div')
                    fulfillment = str(fulfillment_div.text).split('Fulfillment:')[1]
                    # print(fulfillment)
                except:
                    fulfillment=""
                try:
                    tier_div = fulfillment_div.find_next('div')
                    size_tier = str(tier_div.text).split('Tier:')[1]
                    # print(size_tier)
                except:
                    size_tier=""

                try:
                    number_of_images_div = tier_div.find_next('div')
                    number_of_images = str(number_of_images_div.text).split('Images:')[1]
                    # print(number_of_images)
                except:
                    number_of_images=""

                try:
                    variation_count_div = number_of_images_div.find_next('div')
                    variation_count = str(variation_count_div.text).split('Count:')[1]
                    # print(variation_count)
                except:
                    variation_count

                try:
                    weight_div = variation_count_div.find_next('div')
                    weight = str(weight_div.text).split('Weight:')[1]
                    # print(weight)
                except:
                    weight=""
                try:
                    package_dimensions_div = weight_div.find_next('div')
                    package_dimensions = str(package_dimensions_div.text).split('Dimensions:')[1]
                    # print(package_dimensions)
                except:
                    package_dimensions=""

                try:
                    storage_fee_div = package_dimensions_div.find_next('div')
                    storage_fee = str(storage_fee_div.text).split(':')[1]
                    # print(storage_fee)
                except:
                    storage_fee=""

                try:
                    age_div = storage_fee_div.find_next('div')
                    age = str(age_div.text).split(':')[1]
                    # print(age)
                except:
                    age = ""
                    # print("===========================")
            except:pass

            try:
                td_object_one = td[1]
                sellers=td_object_one.text
                # print(sellers)
            except:
                sellers=""
            try:
                td_object_two = td[2]
                price=td_object_two.text
                # print(price)
            except:
                price=""
            try:
                td_object_three = td[3]
                monthly_sales=td_object_three.text
                # print(monthly_sales)
            except:
                monthly_sales=""
            try:
                td_object_four = td[4]
                monthly_revenue=td_object_four.text
                # print(monthly_revenue)
            except:
                monthly_revenue=""
            try:
                td_object_five = td[5]
                bsr=td_object_five.text
                # print(bsr)
            except:
                bsr=""
            try:
                td_object_six = td[6]
                reviews =td_object_six.text
                # print(reviews)
            except:
                reviews=""

            data={
                "amazon_link":amazon_link,
                "image":image,
                "title":title,
                "category":category,
                "brand":brand,
                "seller":seller,
                "fulfillment":fulfillment,
                "size_tier":size_tier,
                "number_of_images":number_of_images,
                "variation_count":variation_count,
                "weight":weight,
                "package_dimensions":package_dimensions,
                "storage_fee":storage_fee,
                "age":age,
                "sellers":sellers,
                "price":price,
                "monthly_sales":monthly_sales,
                "monthly_revenue":monthly_revenue,
                "bsr":bsr,
                "reviews":reviews
            }
            dics_in_list.append(data)
    return dics_in_list