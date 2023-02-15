import webbrowser as web

class tony():
    
    print("hello")
    
    def AI():
        type = input()
        if 'search' == type:
            mysearch = input()
            search = web.open_new('https://www.google.com/search?q='+ mysearch)
            print(search)
        elif 'query' == type:
            url = input()
            query =web.open_new("www."+url+".com")
            print(query)
    def Heatmap():
        web.open('https://www.moneycontrol.com/stocksmarketsindia/360-degree-market-view-heat-map')


             
tony.Heatmap()
tony.AI()
