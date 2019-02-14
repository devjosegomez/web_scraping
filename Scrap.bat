@echo off
IF EXIST "walmart.csv" (
	del "walmart.csv"
	start "walmart Scraper" python walmart0.py
) else (
start "walmart Scraper" python walmart0.py
)
IF EXIST "R.csv" (
	del "R.csv"
	start "RadioShack Scraper" scrapy runspider Radio.py -o R.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "RadioShack Scraper" scrapy runspider Radio.py -o R.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)

IF EXIST "C.csv" (
	del "C.csv"
	start "Chedraui Scraper" scrapy runspider Chedraui.py -o C.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Chedraui Scraper" scrapy runspider Chedraui.py -o C.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "C2.csv" (
	del "C2.csv"
	start "Chedraui2 Scraper" scrapy runspider Chedraui2.py -o C2.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Chedraui2 Scraper" scrapy runspider Chedraui2.py -o C2.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "C3.csv" (
	del "C3.csv"
	start "Chedraui3 Scraper" scrapy runspider Chedraui3.py -o C3.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Chedraui3 Scraper" scrapy runspider Chedraui3.py -o C3.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "C4.csv" (
	del "C4.csv"
	start "Chedraui4 Scraper" scrapy runspider Chedraui4.py -o C4.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Chedraui4 Scraper" scrapy runspider Chedraui4.py -o C4.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "C5.csv" (
	del "C5.csv"
	start "Chedraui5 Scraper" scrapy runspider Chedraui5.py -o C5.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Chedraui5 Scraper" scrapy runspider Chedraui5.py -o C5.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "C6.csv" (
	del "C6.csv"
	start "Chedraui6 Scraper" scrapy runspider Chedraui6.py -o C6.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Chedraui6 Scraper" scrapy runspider Chedraui6.py -o C6.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "C7.csv" (
	del "C7.csv"
	start "Chedraui7 Scraper" scrapy runspider Chedraui7.py -o C7.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Chedraui7 Scraper" scrapy runspider Chedraui7.py -o C7.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "C8.csv" (
	del "C8.csv"
	start "Chedraui8 Scraper" scrapy runspider Chedraui8.py -o C8.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Chedraui8 Scraper" scrapy runspider Chedraui8.py -o C8.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "C9.csv" (
	del "C9.csv"
	start "Chedraui9 Scraper" scrapy runspider Chedraui9.py -o C9.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Chedraui9 Scraper" scrapy runspider Chedraui9.py -o C9.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "C10.csv" (
	del "C10.csv"
	start "Chedraui10 Scraper" scrapy runspider Chedraui10.py -o C10.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Chedraui10 Scraper" scrapy runspider Chedraui10.py -o C10.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "C11.csv" (
	del "C11.csv"
	start "Chedraui11 Scraper" scrapy runspider Chedraui11.py -o C11.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Chedraui11 Scraper" scrapy runspider Chedraui11.py -o C11.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "C12.csv" (
	del "C12.csv"
	start "Chedraui12 Scraper" scrapy runspider Chedraui12.py -o C12.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Chedraui12 Scraper" scrapy runspider Chedraui12.py -o C12.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "C13.csv" (
	del "C13.csv"
	start "Chedraui13 Scraper" scrapy runspider Chedraui13.py -o C13.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Chedraui13 Scraper" scrapy runspider Chedraui13.py -o C13.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "B.csv" (
	del "B.csv"
	start "BestBuy Scraper" scrapy runspider BestBuy.py -o B.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "BestBuy Scraper" scrapy runspider BestBuy.py -o B.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "A.csv" (
	del "A.csv"
	start "Amazon Scraper" scrapy runspider AmazonMX.py -o A.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Amazon Scraper" scrapy runspider AmazonMX.py -o A.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "A2.csv" (
	del "A2.csv"
	start "Amazon Scraper" scrapy runspider AmazonMX2.py -o A2.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Amazon Scraper" scrapy runspider AmazonMX2.py -o A2.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "O.csv" (
	del "O.csv"
	start "Office Depot Scraper" scrapy runspider OfficeDepot.py -o O.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Office Depot" scrapy runspider OfficeDepot.py -o O.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "S1.csv" (
	del "S1.csv"
	start "Soriana Scraper" scrapy runspider Soriana.py -o S1.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Soriana" scrapy runspider Soriana.py -o S1.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "S2.csv" (
	del "S2.csv"
	start "Soriana2 Scraper" scrapy runspider Soriana2.py -o S2.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Soriana2" scrapy runspider Soriana2.py -o S2.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
start "Linio todo" Scrap_linio.bat