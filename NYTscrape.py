# LNDP

    if 'Sorry, your search returned no results.' in driver.page_source:
    	print 'no results'
    	driver.quit()
    	date += timedelta(days=1)
    	continue
    #print results
    results = results.split(' ')[(len(results.split(' '))-1)]
    print results
    if results>10:
    	r = int(results)/10
    	resultPages = math.ceil(r)
    if results<=10:
    	resultPages = 1