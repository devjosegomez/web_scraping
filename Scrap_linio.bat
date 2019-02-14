@echo off
IF EXIST "1.csv" (
	del "1.csv"
	start "Linio Scraper" scrapy runspider Linio.py -o 1.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Linio Scraper" scrapy runspider Linio.py -o 1.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "2.csv" (
	del "2.csv"
	start "Linio Scraper" scrapy runspider Linio2.py -o 2.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Linio Scraper" scrapy runspider Linio2.py -o 2.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "3.csv" (
	del "3.csv"
	start "Linio Scraper" scrapy runspider Linio3.py -o 3.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Linio Scraper" scrapy runspider Linio3.py -o 3.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "4.csv" (
	del "4.csv"
	start "Linio Scraper" scrapy runspider Linio4.py -o 4.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Linio Scraper" scrapy runspider Linio4.py -o 4.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "5.csv" (
	del "5.csv"
	start "Linio Scraper" scrapy runspider Linio5.py -o 5.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Linio Scraper" scrapy runspider Linio5.py -o 5.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "6.csv" (
	del "6.csv"
	start "Linio Scraper" scrapy runspider Linio6.py -o 6.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Linio Scraper" scrapy runspider Linio6.py -o 6.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "7.csv" (
	del "7.csv"
	start "Linio Scraper" scrapy runspider Linio7.py -o 7.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Linio Scraper" scrapy runspider Linio7.py -o 7.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "8.csv" (
	del "8.csv"
	start "Linio Scraper" scrapy runspider Linio8.py -o 8.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Linio Scraper" scrapy runspider Linio8.py -o 8.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "9.csv" (
	del "9.csv"
	start "Linio Scraper" scrapy runspider Linio9.py -o 9.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Linio Scraper" scrapy runspider Linio9.py -o 9.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "10.csv" (
	del "10.csv"
	start "Linio Scraper" scrapy runspider Linio10.py -o 10.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Linio Scraper" scrapy runspider Linio10.py -o 10.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "11.csv" (
	del "11.csv"
	start "Linio Scraper" scrapy runspider Linio11.py -o 11.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Linio Scraper" scrapy runspider Linio11.py -o 11.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
IF EXIST "12.csv" (
	del "12.csv"
	start "Linio Scraper" scrapy runspider Linio12.py -o 12.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
) else (
start "Linio Scraper" scrapy runspider Linio12.py -o 12.csv -s COOKIES_ENABLED=False --nolog -s CONCURRENT_REQUESTS=25 -s CONCURRENT_ITEMS=140 -s DNSCACHE_ENABLED=False -s REACTOR_THREADPOOL_MAXSIZE=20
)
