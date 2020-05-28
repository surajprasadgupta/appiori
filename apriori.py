from efficient_apriori import apriori
def cotenants(request):
    retail_obj=RetailerLocation.objects.filter(category__icontains="General Merchandise",brand_name__icontains='Shopko')
    print([i.brand_name for i in retail_obj])
    db_record=RetailerLocation.objects.all()
   
    temp_list=[]
    for retail in retail_obj:
        cordinates=geodesic_point_buffer(retail.latitude, retail.longitude, 1)
        brand_area_point=[tuple(reversed(point)) for point in cordinates]
        # print(brand_area_point)
        records_in_area=polygonRecord(brand_area_point,db_record)
        temp_list.append(tuple(records_in_area[1]))
    print(temp_list)
    #transactions have all record that occur togather like [(milk,bread,butter),(bread,egg,butter),(bear,butter,egg)....]
    transactions=temp_list
    #acording your accuracy you can set min_support(current time its 10%) and nin_confidence
    itemsets, rules = apriori(transactions, min_support=0.1, min_confidence=0.5)    
    print(itemsets)
