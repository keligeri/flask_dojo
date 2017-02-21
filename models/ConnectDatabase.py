from peewee import *


class ConnectDatabase:

    def __init__(self, config_file="models/connect_str.txt"):
        self.config_file = config_file
        self.db_name = False
        self.db_username = False
        self.db = False

    def __init_connection(self):
        self.db_name, self.db_username = self.__get_connect_string()

    def connect(self):
        if self.db is False:
            self.__init_connection()
            self.db = PostgresqlDatabase(self.db_name, self.db_username)
        return self.db

    def __get_connect_string(self):
        try:
            with open(self.config_file, "r") as f:
                details = f.readline().split(";")
                return details[0], details[1]
        except:
            print("You need to create a database and store its name in a file named "+self.config_file+". \
                  For more info, head over to the README")