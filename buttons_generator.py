
def button_generater_func(new_sentences, InlineKeyboardButton,InlineKeyboardMarkup, msg):

    try:
            
        num_of_rows = len ( new_sentences )
        num_of_buttons = 1

        buttons = [ ]

        for i in range ( num_of_rows ) :
            row = [ ]
            for j in range ( num_of_buttons ) :
                button_text = new_sentences [ i ]
                button_callback = f"{new_sentences [ i ]}"
                row.append ( InlineKeyboardButton ( button_text, callback_data = button_callback ) )
            buttons.append ( row )

        keyboard = InlineKeyboardMarkup ( buttons )
        a =  msg.reply_text ( 'اختر البرنامج:', reply_markup = keyboard )

        return a

    except:
        
        return  msg.reply_text ('يوجد مشكله باظهار النتائج جرب سيرفر ثاني او اختر فلم ثاني')
