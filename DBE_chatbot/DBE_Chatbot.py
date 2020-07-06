import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import yaml
import random
import string
import sqlite3
from sqlite3 import Error


db_file = r"C:\Users\saseendr\Desktop\DBE_chatbot\pythonsqlite.db"



def run(sq):
    
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    
    sub = ['road','peds','ped','bldg','lot','lots','feat','intg','ecroad','ecbldg','ecped','eclot','ecfeat','ecintg']
    res = []
    severity = ['CRITICAL','MAJOR','MINOR']
    error_type = ['WARNING','FLAG','BLOCKING','NONE']
    le_allowed = ['yes','no','YES','NO','le allowed','le not allowed','LE','le']
    column_names = ['rule_code','severity','error_type','le_allowed','document_owner','link','jira_issues','document_status','product']
     
 

    EXAMPLE_TEXT = sq

    stop_words = set(stopwords.words('english'))
    #add custom words
    new_stopwords = ['validation','validations','list','all']
    stop_words.update(new_stopwords)
    new_stopwords_list = set(stop_words)
    words = word_tokenize(EXAMPLE_TEXT)
    filtered_sentence = [w for w in words if not w in new_stopwords_list]

    filtered_sentence = []

    for w in words:
        if w not in stop_words:
            filtered_sentence.append(w)

    print(filtered_sentence)



    jVal = "|".join(filtered_sentence).lower()
    valid = [i for i in sub if i in jVal ]
    print(valid)
    print('ye wala')
    stringx = ''
    type1 = '%%'
    if len(valid)!=0:
        type = stringx.join(valid[0]).upper()
        type1 = '%'+type+'%'
        print(type1)


    jsever = "|".join(filtered_sentence).upper()
    sever = [i for i in severity if i in jsever ]
    print(sever)
    print('ye wala bhi')

    jerror = "|".join(filtered_sentence).upper()
    error = [i for i in error_type if i in jerror]
    print(error)
    print('ye wala bhi part 2')
    
    jcolumn = "|".join(filtered_sentence).lower()
    column = [i for i in column_names if i in jcolumn]
    print(column)
    print('ye wala bhi part 3')
    pos_column = ''.join(column)
    print(pos_column)
    
    jle = "|".join(filtered_sentence).lower()
    le = [i for i in le_allowed if i in jle]
    print(le)
    print('ye wala bhi part 4')
    pos_le = ''.join(le)
    print(pos_le)

    
    search = ' '.join(filtered_sentence)
    search1 = '%'+search+'%'
    print(search1)

    possible_val = [ x for x in filtered_sentence if any(c.isdigit() for c in x)]
    val1 = ''
    val = ' '.join(possible_val).upper()
    print(len(val))
    
    if len(val)!= 0:
        if 'EC' not in val:
            val1 = 'EC.'+val
            
        elif '.' not in val:
            val1 = val[:2] + '.' + val[2:]
            val1 = '%'+val1+'%'
        else:
            val1 = val[:2] + val[2:]
            val1 = '%'+val1+'%'
        print(len(val1))
        print(val1)
    
    
    
    
    
    

    if len(val1) == 0:
        
        with open('greetings.yml') as f:
    
            data = yaml.load(f, Loader=yaml.FullLoader)
            conversations = data["conversations"]
            conversations = [[w.lower() for w in pair] for pair in conversations]
            print(conversations)
        bot_response_arr = []
        for conv_pair in conversations:
            if EXAMPLE_TEXT.lower() in conv_pair:
                bot_response_arr.append(conv_pair[1].capitalize())
        
        if len(bot_response_arr)!=0:
            return random.choice(bot_response_arr)
        
        
        if len(sever)!= 0 or len(error)!= 0 or len(le)!=0:
            le_ans = ''
            le_status = '%%'
            stri = ' '
            stri1 = ''
            pos_sever = stri.join(sever)
            pos_sever = '%'+pos_sever+'%'
            print(pos_sever)
            print(type1)
            pos_error = stri1.join(error)
            pos_error = '%'+pos_error+'%'
            print(pos_error)
            print("*")
            if len(sever)!=0 and len(error)== 0 and len(le) == 0:
                field = 'severity'
                print(field)
            elif len(sever)==0 and len(error)!= 0 and len(le) == 0:
                field = 'error_type'
            elif len(sever)==0 and len(error)== 0 and len(le) != 0:
                field = 'le_allowed'
                print(field)
            elif len(sever)!=0 and len(error)== 0 and len(le) != 0:
                field = 'severity,le_allowed'
                print(field)
            elif len(sever)!=0 and len(error)!= 0 and len(le) == 0:
                field = 'severity,error_type'
                print(field)
            elif len(sever)==0 and len(error)!= 0 and len(le) != 0:
                field = 'error_type,le_allowed'
                print(field)
            else:
                field = 'severity,error_type,le_allowed'
                print(field)
            if 'le not allowed'in EXAMPLE_TEXT:
                le_status = 'NO'
                le_ans = 'LE NOT Allowed'
            elif 'le allowed'in EXAMPLE_TEXT or 'le'in EXAMPLE_TEXT:
                le_status = 'YES'
                le_ans = 'LE Allowed'

            
            if 'many' in filtered_sentence or 'count' in filtered_sentence or 'number' in filtered_sentence:
                mySql_insert_query = 'SELECT count(rule_code),'+field+' FROM rule_codes WHERE severity LIKE ? AND rule_code like ? AND error_type LIKE ? AND le_allowed LIKE ?'
                                   
                print(pos_sever)    
                print(type1) 
                print(pos_error)
                print(le_status)
                cursor = connection.cursor()
                cursor.execute(mySql_insert_query,(pos_sever,type1,pos_error,le_status,))
                myresult = cursor.fetchall()
                connection.commit()

                
                myres = [str(item) for t in myresult for item in t] 
                print(myres)
                bot_answer = 'There are '+myres[0]+' '+pos_sever.replace('%','')+' '+pos_error.replace('%','')+' '+type1.replace('%','')+' '+le_ans+' validations'
                return bot_answer
            
            else:
            
                mySql_insert_query = 'SELECT link, '+field+' FROM rule_codes WHERE severity LIKE ? AND rule_code like ? AND error_type LIKE ? AND le_allowed LIKE ?'
                                   

                cursor = connection.cursor()
                cursor.execute(mySql_insert_query,(pos_sever,type1,pos_error,le_status,))
                myresult = cursor.fetchall()
                connection.commit()

                
                print(myresult)
                myres = [t[0] for t in myresult]
                myres = ', '.join(myres)
                bot_answer = 'The list of '+pos_sever.replace('%','')+' '+pos_error.replace('%','')+' '+type1.replace('%','')+' '+le_ans+' validations are: '+'<br>'+myres
                return bot_answer
                
        else:
            
            search1 = search1.replace(' ', "%%")
            print(search1)
            mySql_insert_query = """SELECT link,rule_name
                                   FROM rule_codes
                                   WHERE rule_name LIKE (?)
                                   OR rule_description LIKE (?)
                                   OR rule_label LIKE (?)
                                   """
    
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query,(search1,search1,search1,))
            myresult = cursor.fetchall()
            connection.commit()

            
            print(myresult)
            return myresult
        
    elif len(sever)!= 0 or len(error)!=0:
        stri = ' '
        pos_sever = stri.join(sever)
        print(pos_sever)
        stri1 = ''
        pos_error1 = stri1.join(error)
        pos_error = '%'+pos_error1+'%'

        possible_val = [ x for x in filtered_sentence if any(c.isdigit() for c in x)]
        val = ''.join(possible_val).upper()
        if 'EC' not in val:
            val1 = 'EC.'+val
            val2 = '%'+val1+'%'
        elif '.' not in val:
            val1 = val[:2] + '.' + val[2:]
            val2 = '%'+val1+'%'
        else:
            val1 = val[:2] + val[2:]
            val2 = '%'+val1+'%'
        
        query_for_cm = """SELECT rule_code
                           FROM rule_codes
                           WHERE rule_code LIKE ?
                           """
        cursor = connection.cursor()
        cursor.execute(query_for_cm,(val2,))
        myresult = cursor.fetchall()
        connection.commit()
        label = ''.join(myresult[0])
        
        
        mySql_insert_query = """SELECT link,rule_name ,severity
                               FROM rule_codes
                               WHERE rule_code LIKE ?
                               AND severity LIKE ?
                               AND error_type LIKE ?
                               """

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query,(val2,pos_sever,pos_error,))
        myresult = cursor.fetchall()
        connection.commit()

        
        if len(myresult)== 0:
            print(val1+' is not '+pos_sever+" "+pos_error1)
            myresult = label+' is not '+pos_sever+" "+pos_error1
            return myresult
        else:
            print(val1+' is '+pos_sever+" "+pos_error1)
            myresult = label+' is '+pos_sever+" "+pos_error1
            return myresult
    

        
    
    elif len(pos_column)!=0:
        print('hey')
        if 'EC' not in val:
            val1 = 'EC.'+val
            val1 = '%'+val1+'%'
        elif '.' not in val:
            val1 = val[:2] + '.' + val[2:]
            val1 = '%'+val1+'%'
        else:
            val1 = val[:2] + val[2:]
            val1 = '%'+val1+'%' 
        print(pos_column)       
        print(val1)
        mySql_insert_query = 'SELECT rule_code,'+pos_column+' FROM rule_codes WHERE rule_code LIKE ? '

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query,(val1,))
        myresult = cursor.fetchall()
        connection.commit()

        
        print(myresult)
        myres = [' is '.join(i) for i in myresult]
        myres = 'The '+pos_column+' of '+''.join(myres)
        return myres
    
    elif len(pos_le)!=0:
        if 'EC' not in val:
            val1 = 'EC.'+val
        
        elif '.' not in val:
            val1 = val[:2] + '.' + val[2:]
            val1 = '%'+val1+'%'
        else:
            val1 = val[:2] + val[2:]
            val1 = '%'+val1+'%' 
            
        mySql_insert_query = 'SELECT rule_code,le_allowed FROM rule_codes WHERE rule_code LIKE ? '

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query,(val1,))
        myresult = cursor.fetchall()
        connection.commit()

        
        print(myresult)
        if 'YES' in myresult:
            val1 = val1.replace('%','')
            myres = val1+ ' is LE Allowed'
            return myres
        else:
            val1 = val1.replace('%','')
            myres = val1+' is LE NOT Allowed'
            return myres
    
    
    else:
        if 'EC' not in val:
            val1 = 'EC.'+val
            val1 = '%'+val1+'%' 
        
        elif '.' not in val:
            val1 = val[:2] + '.' + val[2:]
            val1 = '%'+val1+'%'
        else:
            val1 = val[:2] + val[2:]
            val1 = '%'+val1+'%'
        print('this is '+val1)
        mySql_insert_query = """SELECT link, rule_name
                               FROM rule_codes
                               WHERE rule_code LIKE ?
                               """

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query,(val1,))
        myresult = cursor.fetchall()
        connection.commit()
        
        print(myresult)
        myres = [': '.join(i) for i in myresult]
        myres = ''.join(myres)
        return myres

