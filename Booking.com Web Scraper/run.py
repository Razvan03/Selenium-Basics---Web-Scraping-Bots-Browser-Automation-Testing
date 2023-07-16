from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.implicitly_wait(3)
        bot.accept_cookie()
        bot.change_currency(currency='Euro')
        bot.close_popUp()
        bot.select_place_to_go(input("Where do you want to go ? "))
        bot.select_dates(check_in_date=input("What is the check in date ? (Ex: 2023-07-14) "),
                         check_out_date=input("What is the check out date ? (Ex: 2023-07-14) "))
        bot.select_adults(int(input("How many people ? ")))
        bot.click_search()
        bot.apply_filtrations()  #Modify in booking.py
        bot.report_results()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise