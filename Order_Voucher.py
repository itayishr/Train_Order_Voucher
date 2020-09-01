from selenium import webdriver
import stations as st
from selenium.webdriver.common.action_chains import ActionChains
import datetime

opt = webdriver.FirefoxOptions()
opt.add_argument('--headless')
driver = webdriver.Chrome("/home/itaybm2/chromedriver")

def station_cleanup_name(station_name):
    station_name = station_name.lower().strip().replace('\'', '').replace('-', ' ')
    return ' '.join(station_name.split())

def station_to_index(station_name):
	clean_name = station_cleanup_name(station_name)
	return st.STATION_INDEX[clean_name]

def decode_station_name(station_input):
	station_lowercase = str(station_input).lower()
	if station_lowercase in st.STATIONS:
		return st.STATIONS[station_lowercase]

def present_trains():
	# print("Please input origin station:")
	# origin_station = input()
	# print("Please input destination station")
	# destination_station = input()
	# print("Please input the date")

	orig = "2800"
	dest = "2300"
	tomorrow_date = datetime.date.today() + datetime.timedelta(days=1) 
	tomorrow_str = tomorrow_date.strftime("%Y%m%d")
	hour = "1500"
	search_address = "https://www.rail.co.il/pages/trainsearchresultnew.aspx?FSID={}&TSID={}&Date={}&Hour={}&IOT=true&IBA=false&TSP=1598809293068".format(orig,dest,tomorrow_str,hour)
	driver.get(search_address)



def init_voucher(address):

	driver.get(address)

	MY_ID = "PUT_ID_HERE"	
	EMAIL = "ENTER_MAIL_HERE"
	MOBILE = "PHONE_NUMBER"																																																													

	time.sleep(2)
	try:
		popup_close = driver.find_element_by_xpath("//div[@id='ZA_CAMP_CONTAINER']/div[@id='ZA_CAMP_DIV_1']/div[@id='ZA_CAMP_DIV_2']/div[@id='ZA_CAMP_CANVAS']/div[@aria-label='close']").click()
	except:
		pass
	time.sleep(2)
	# driver.maximize_window()
	# popup_btn = driver.find_element_by_xpath("//button[contains(text())]")
	choose_train = driver.find_element_by_id("railRadio_425").click()
	time.sleep(2)
	voucher_order = driver.find_element_by_class_name("jerusalem-voucher.\\ng-scope").click()
	time.sleep(5)
	try:
		popup_close = driver.find_element_by_xpath("//div[@id='ZA_CAMP_CONTAINER']/div[@id='ZA_CAMP_DIV_1']/div[@id='ZA_CAMP_DIV_2']/div[@id='ZA_CAMP_CANVAS']/div[@aria-label='close']").click()
	except:
		pass	
	time.sleep(2)
	id_ = driver.find_element_by_id("card-number")
	email_address = driver.find_element_by_id("email-address")																											
	mobile = driver.find_element_by_name("mobile")
	checkbox = driver.find_element_by_class_name("checkmark")

	# popup_btn.click()
	id_.send_keys(MY_ID)
	email_address.send_keys(EMAIL)
	mobile.send_keys(MOBILE)
	checkbox.click()
	time.sleep(2)
	button = driver.find_element_by_class_name("btn-container.\\text-center")
	button.click()

	sms_input = driver.find_element_by_id("voucherTokenMessage")
	# button.click()
	print('Enter the code from the SMS message:')
	sms_code = input()
	finish_button = driver.find_element_by_id("BtnPopUup")
	sms_input.send_keys(sms_code)
	time.sleep(15)
	finish_button.click()
	time.sleep(20)																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																							
	print("Done!")


# train_address = "https://www.rail.co.il/pages/trainsearchresultnew.aspx?FSID=5800&TSID=2300&Date=20200901&Hour=2400&IOT=true&IBA=false&TSP=1598809293068"
# voucher_address = "https://www.rail.co.il/taarif/pages/ordervaucherallcountry.aspx?TNUM=952&FSID=5800&TSID=2300&DDATE=20200901&Hour=2400&CS=null&SSID=3600&TSP=1598808383282"
# init_voucher(train_address)	

present_trains()