import configparser
import mysql.connector
import os, sys
sys.path.append(os.path.join(sys.path[0], '../../'))
sys.path.append(os.path.join(sys.path[0], '../Client/Models'))
from volunteer import *

class VolunteerRepo:
    def __init__(self):
        config = configparser.ConfigParser()
        if os.environ['PythonEnvironment'] == 'dev':
            config.read('config-dev.ini')
        else:
            config.read('config.ini')
        self._server = config['csci0371dbserver']['Server']
        self._username = config['csci0371dbserver']['Username']
        self._password = config['csci0371dbserver']['Password']

    def __get_db_server_conn(self):
        db_server_conn = mysql.connector.connect(
            host=self._server,
            user=self._username,
            password=self._password,
            database='volunteer'
        )
        return db_server_conn
    
    def __get_db_cursor(self, db_server_conn):
        if db_server_conn == None:
            db_server_conn = self.__get_db_server_conn
        cursor = db_server_conn.cursor()
        return cursor
    
    def get_volunteers(self):
        cursor = self.__get_db_cursor(None)
        cursor.execute("SELECT * FROM volunteer")
        results = cursor.fetchall()
        for result in results:
            print(result)

        return results

    def get_volunteer_by_phone_number(self, phone_number:int):
        cursor = self.__get_db_cursor(None)
        cursor.execute(f"SELECT * FROM volunteer WHERE PhoneNumber = {phone_number}")
        result = cursor.fetchall()
        if(len(result)) == 0:
            return None
        else:
            return result
        
    def save_volunteer(self, volunteer:Volunteer):
        existing_volunteer = self.get_volunteer_by_phone_number(volunteer.phone_number)
        if existing_volunteer == None:
            self.__insert_volunteer(volunteer)
        else:
            self.__update_volunteer(volunteer)

    def __insert_volunteer(self, volunteer:Volunteer):
        db_server_conn = self.__get_db_server_conn()
        cursor = self.__get_db_cursor(db_server_conn)
        sql = "INSERT INTO volunteer (FirstName, LastName, PhoneNumber, Email) VALUES (%s, %s, %s, %s)"
        val = (volunteer.first_name, volunteer.last_name, volunteer.phone_number, volunteer.email)
        cursor.execute(sql, val)
        db_server_conn.commit()

    def __update_volunteer(self, volunteer:Volunteer):
        db_server_conn = self.__get_db_server_conn()
        cursor = self.__get_db_cursor(db_server_conn)
        sql = f"UPDATE volunteer SET FirstName = '{volunteer.first_name}', LastName = '{volunteer.last_name}' Email = '{volunteer.email}' WHERE PhoneNumber = {volunteer.phone_number}"
        cursor.execute(sql)
        db_server_conn.commit()

    def __delete_volunteer(self, phone_number:int):
        db_server_conn = self.__get_db_server_conn()
        cursor = self.__get_db_cursor(db_server_conn)
        sql = f"DELETE FROM volunteer WHERE PhoneNumber = {phone_number}"
        cursor.execute(sql)
        db_server_conn.commit()